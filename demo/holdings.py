from __future__ import print_function
from datetime import datetime, timedelta
import datetime
import csv
import swagger_client
from demo import configuration, authed_client

# declare an instance of the api for interacting with the account holdings resource
api = swagger_client.AccountHoldingsApi(authed_client())


def list_latest_holdings():
    """
    Demonstrates listing latest holdings

    :return:
    """

    # get the latest date, this could be yesterday's date or the last market date.
    latest_date = (datetime.datetime.now() - timedelta(1)).date()

    # the latest holdings is filtered by as_of_date = yesterday's date
    filter_body = {
        'as_of_date': latest_date,
    }

    # fetch holdings with the filter condition
    resp = api.filter_account_holdings(body=filter_body)

    # first two items from the response
    print('response:')
    print(resp.data[:2])


def holdings_to_csv(path='out/holdings.csv'):
    """
    Outputs all the holdings fields to a CSV file

    :param path:
    :return:
    """
    latest_date = (datetime.datetime.now() - timedelta(4)).date()

    filter_body = {
        'as_of_date': latest_date,
    }

    print("Fetching account holdings")
    resp = api.filter_account_holdings(body=filter_body)

    print(f"Writing {len(resp.data)} holdings to {path}")
    # Writing to a csv file
    csv_file = open(path, 'w+')
    csv_writer = csv.writer(csv_file)

    count = 0
    for holding in resp.data:
        if count == 0:
            header = holding.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(holding.values())

    csv_file.close()

    print("Done")

def main():
    """
    Entry point for account holding api demonstration

    :return:
    """
    list_latest_holdings()

    holdings_to_csv()


if __name__ == '__main__':
    main()
