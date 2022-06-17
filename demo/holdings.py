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


def holdings_to_csv(path='holdings.csv'):
    """
    Outputs all the holdings fields to a CSV file

    :param path:
    :return:
    """
    latest_date = (datetime.datetime.now() - timedelta(1)).date()

    filter_body = {
        'as_of_date': latest_date,
    }

    print("fetch account holdings for as_of_date = yesterday")
    resp = api.filter_account_holdings(body=filter_body)

    print("start writing holdings to a csv file")
    # Writing to a csv file
    data_file = open(path, 'w')
    csv_writer = csv.writer(data_file)

    count = 0
    for holding in resp.data:
        if count == 0:
            header = holding.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(holding.values())

    data_file.close()

    print("csv file generation complete!!")

def main():
    """
    Entry point for account holding api demonstration

    :return:
    """
    list_latest_holdings()

    holdings_to_csv()


if __name__ == '__main__':
    main()
