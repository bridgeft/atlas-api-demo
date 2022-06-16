from __future__ import print_function
import swagger_client
import websocket
from demo import authed_client
import json
import wget

# TODO: Use code to get this
auth_token = ''
billing_api = swagger_client.BillingReportsApi(authed_client())
invoice_api = swagger_client.InvoicesApi(authed_client())

# Logs the message and processes accordingly
def on_message(ws, message):
    msg_obj = json.loads(message)

    num_steps = msg_obj.get('total')
    current_step = num_steps - msg_obj.get('remaining')

    print(f"### Message received: Billing Group {current_step} of {num_steps} have processed.\n")
    print(msg_obj)
    print("")

    if msg_obj.get('job_type') == "b" and msg_obj.get('state') == 'complete' and msg_obj.get('object_id') is not None:
        # get the billing report and log the response
        print("### Billing Completed ###\n")

        billing_report_id = msg_obj.get('object_id')
        process_invoices(billing_report_id)

    if msg_obj.get('job_type') == "bd" and msg_obj.get('state') == 'complete':
        # download
        invoice_url = msg_obj.get('download_link')

        download(invoice_url)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    # when the connection is opened, start your billing report job
    resp = billing_api.start_billing_report_start_pdf(body={
        'firm_id': 39,
        'create_invoices': True,
        'billing_date': '2022-04-01',
        'period_type': 'standard',
    })

    print("### Billing Started ### ")


def start_billing_report():
    # when the connection is opened, start your billing report job
    _ = billing_api.start_billing_report_start_pdf(body={
        'firm_id': 39,
        'billing_date': '2022-04-01',
        'period_type': 'standard',
    })

    print("### Billing Started ### \n")


def process_invoices(billing_report_id):
    print("### Fetching Invoices ###\n")

    invoice_ids = fetch_invoices(billing_report_id)

    print("### Invoices Fetched ###\n")

    print("### Initiating Bulk Download ###\n")

    initiate_bulk_download_of_invoices(invoice_ids)


def fetch_invoices(billing_report_id):
    # get invoices and return array of ids
    resp = invoice_api.filter_invoices(body = {
        'billing_report_id': billing_report_id
    })

    invoices = resp.data

    invoice_ids = []

    for i in invoices:
        invoice_ids.append(i.get('id'))

    print(f"### {len(invoice_ids)} Invoices were generated ###\n")

    return invoice_ids


def initiate_bulk_download_of_invoices(invoice_ids):
    # bulk download
    print("### Starting Bulk Download ###\n")
    _ = invoice_api.filter_invoice_bulk_download(body={
        'ids': invoice_ids
    })


def download(url):
    # download
    print("### Downloading Invoices ###\n")

    wget.download(url)

    print("\n### Invoices downloaded ###\n")

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
