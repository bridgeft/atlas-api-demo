from __future__ import print_function
import swagger_client
import websocket
from demo import authed_client
import csv
import json
import wget

# TODO: use code to get this
auth_token = ''
pdf_api = swagger_client.PrintableReportsApi(authed_client())

object_ids = []


# handle messages as they are received
def on_message(ws, message):
    handle_message(message)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### Websocket Closed ### \n")


def on_open(ws):
    start_pdf_process()


def handle_message(message):

    msg_obj = json.loads(message)

    num_steps = msg_obj.get('total')
    current_step = num_steps - msg_obj.get('remaining')

    print(f"### Message received: Step {current_step} of {num_steps}\n\n")
    print(msg_obj)
    print("\n")

    if msg_obj.get('object_id') is not None:
        object_ids.append(msg_obj.get('object_id'))

    if msg_obj.get('job_type') == 'pdfrp' and msg_obj.get('state') == "complete" and msg_obj.get('object_id') is None:
        print("### PDF Report Generation Completed ### \n")
        print("### Starting a bulk download ### \n")

        bulk_download_reports()

    if msg_obj.get('job_type') == 'bd' and msg_obj.get('state') == "complete":
        print("### Bulk Download Completed ### \n")
        print("Download Link: " + msg_obj.get('download_link') + "\n")

        download_reports(msg_obj.get('download_link'))


def start_pdf_process():
    # when the connection is opened, start your billing report job
    _ = pdf_api.filter_printable_report_start_pdf(body={
        'account_ids': [
            263328,
            263329,
            263330,
            263331,
            263332
        ],
        'frequency': "m",
        'start_date': "2022-01-01",
        'end_date': "2022-03-31",
        'sub_reports': [
            'account_summary',
            'consolidated_summary',
            'performance_summary',
            'performance_chart',
            'net_investment_chart'
        ],
    })

    print("### PDF Report Generation Started ### \n")


def bulk_download_reports():
    resp = pdf_api.filter_printable_report_bulk_download(body={
        "ids": object_ids
    })

    print("### Bulk Download Started ### \n")


def download_reports(url):
    print("### Downloading Reports ### \n")
    wget.download(url)
    print("### Download Completed ### \n")

    # Terminate the program
    exit()


def main():

    # Connect to a websocket to receive messages on your job status.
    # Provided callbacks handle messages as they are received.
    ws = websocket.WebSocketApp(f'wss://4s7vk7rtwc.execute-api.us-east-1.amazonaws.com/prod/?queryauth={auth_token}',
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()


if __name__ == '__main__':
    main()
