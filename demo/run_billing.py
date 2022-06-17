from __future__ import print_function
import swagger_client
import websocket
from demo import authed_client, get_id_token
import json
import wget

auth_token = get_id_token()
billing_api = swagger_client.BillingReportsApi(authed_client())
invoice_api = swagger_client.InvoicesApi(authed_client())


def on_message(ws, message):
    """
    Called when a new websocket message has been received.
    Logs the websocket message and processes accordingly

    :param ws: The websocket-client
    :param message: The received websocket message
    :return:
    """
    msg_obj = json.loads(message)

    num_steps = msg_obj.get('total')
    current_step = num_steps - msg_obj.get('remaining')

    print(f"### Message received: Billing Group {current_step} of {num_steps} have processed.\n")
    print(msg_obj)
    print("")

    # handle completed billing message
    if msg_obj.get('job_type') == "b" and msg_obj.get('state') == 'complete' and msg_obj.get('object_id') is not None:
        print("### Billing Completed ###\n")

        billing_report_id = msg_obj.get('object_id')
        process_invoices(billing_report_id)

    # handle completed bulk download
    if msg_obj.get('job_type') == "bd" and msg_obj.get('state') == 'complete':

        # the websocket message returns a download link for the zipped invoices
        invoice_url = msg_obj.get('download_link')

        download(invoice_url)

        # process is completed, the websocket should be closed
        ws.close()


def on_open(ws):
    """
    Called when the websocket connection has been established.
    Starts the billing report.

    :param ws: The websocket-client
    :return:
    """
    start_billing_report()


def start_billing_report():
    """
    Starts a billing job using the API Client

    Endpoint: /billing/reports [POST]

    :return:
    """
    _ = billing_api.start_billing_report_start_pdf(body={
        'firm_id': 39,
        'create_invoices': True,
        'billing_date': '2022-04-01',
        'period_type': 'standard',
    })

    print("### Billing Started ### \n")


def process_invoices(billing_report_id):
    """
    Fetches invoices and initiates a bulk download for the completed billing report.

    :param billing_report_id:
    :return:
    """
    print("### Fetching Invoices ###\n")

    invoice_ids = fetch_invoices(billing_report_id)

    print("### Invoices Fetched ###\n")

    print("### Initiating Bulk Download ###\n")

    initiate_bulk_download_of_invoices(invoice_ids)


#
def fetch_invoices(billing_report_id):
    """
    Fetches the ids completed billing report's invoices

    Endpoint: /billing/invoices/filter

    :param billing_report_id:
    :return: List of invoice IDs
    """

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
    """
    Starts a bulk download job.
    Status updates for this job will be received in the on_message callback and handled accordingly.

    Endpoint: /billing/invoices/download

    :param invoice_ids: Generated invoice IDs
    :return:
    """

    print("### Starting Bulk Download ###\n")
    _ = invoice_api.filter_invoice_bulk_download(body={
        'ids': invoice_ids
    })


def download(url):
    """
    Uses wget to download the zip files from the provided url

    :param url: Url for the zipped invoices.
    :return:
    """
    # download
    print("### Downloading Invoices ###\n")

    wget.download(url)

    print("\n### Invoices downloaded ###\n")


def main():
    """
    Initializes the websocket connection and receives registers callbacks.
    Messages are processed and handled by the callbacks when new websocket messages are received.

    :return:
    """

    ws = websocket.WebSocketApp(f'wss://4s7vk7rtwc.execute-api.us-east-1.amazonaws.com/prod/?queryauth={auth_token}',
                                on_open=on_open,
                                on_message=on_message)

    ws.run_forever()


if __name__ == '__main__':
    main()
