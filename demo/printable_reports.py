from __future__ import print_function
import swagger_client
import websocket
from demo import authed_client, get_id_token
import json
import wget

auth_token = get_id_token()
pdf_api = swagger_client.PrintableReportsApi(authed_client())

object_ids = []


def on_message(ws, message):
    """
    Handles messages as they are received.

    :param ws: The websocket-client
    :param message: The received websocket message
    :return:
    """
    handle_message(ws, message)


def on_open(ws):
    """
    When the websocket connection is initiated, start the printable report job.

    :param ws: websocket-client
    :return:
    """
    start_pdf_process()


def handle_message(ws, message):
    """
    Called when a new websocket message has been received.
    Logs the websocket message and processes accordingly.

    :param message:
    :return:
    """

    msg_obj = json.loads(message)

    num_steps = msg_obj.get('total')
    current_step = num_steps - msg_obj.get('remaining')

    print(f"### Message received: Step {current_step} of {num_steps}\n\n")
    print(msg_obj)
    print("\n")

    # keep record of completed report ids
    if msg_obj.get('object_id') is not None:
        object_ids.append(msg_obj.get('object_id'))

    # when the printable report job completes, a bulk download is initiated
    if msg_obj.get('job_type') == 'pdfrp' and msg_obj.get('state') == "complete" and msg_obj.get('object_id') is None:
        print("### PDF Report Generation Completed ### \n")
        print("### Starting a bulk download ### \n")

        bulk_download_reports(object_ids)

    # when the bulk download is complete, download the reports
    if msg_obj.get('job_type') == 'bd' and msg_obj.get('state') == "complete":
        print("### Bulk Download Completed ### \n")
        print("Download Link: " + msg_obj.get('download_link') + "\n")

        download_reports(msg_obj.get('download_link'))

        # the bulk download is complete, terminate the websocket connection
        ws.close()


def start_pdf_process():
    """
    Starts a printable reporting job by using the sdk client.

    Endpoint: /reporting/printable-reports/create [POST]

    The printable report jobs takes a list of account IDs and reporting specific parameters to generate PDFs.

    :return:
    """
    # when the connection is opened, start your billing report job
    _ = pdf_api.filter_printable_report_start_pdf(body={
        # note: these are hard-coded to the eng-demo@bridgeft.com account
        'account_ids': [
            263329,
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


def bulk_download_reports(report_ids):
    """
    Initiates a bulk download job using the report ids that were generated.

    Endpoint: /reporting/printable-reports/download

    :param report_ids: Generated printable report IDs used
    :return:
    """

    _ = pdf_api.filter_printable_report_bulk_download(body={
        "ids": report_ids
    })

    print("### Bulk Download Started ### \n")


def download_reports(url):
    """
    Uses wget to download the zipped files from the provided url

    :param url: Link to the zipped printable reports
    :return:
    """
    print("### Downloading Reports as a zip of PDF ### \n")
    wget.download(url, out='../out/pdf-reports.zip')
    print("### Download Completed ### \n")


def main():
    """
    Initializes the websocket connection and receives registers callbacks.
    Messages are processed and handled by the callbacks when new websocket messages are received.

    :return:
    """

    ws = websocket.WebSocketApp(f'wss://websocket.bridgeft.com/?queryauth={auth_token}',
                                on_open=on_open,
                                on_message=on_message)

    ws.run_forever()


if __name__ == '__main__':
    main()
