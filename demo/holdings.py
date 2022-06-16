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
    Demonstrates listing API keys
    API keys can be managed (created, read, deleted) by creating a temporary oauth2 id token
    from the /v2/oauth2/token endpoint, which can be used as a bearer token until expiration

    It's recommended to create and manage API keys for machine-to-machine backend applications
    for use cases where expiration and key management isn't necessary

    :return:
    """

    # get the latest date, this could be yesterday's date or the last market date.
    latest_date = (datetime.datetime.now() - timedelta(1)).date()

    # to fetch the latest holdings for each account filter body is set with as of date as yesterday's date
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

    resp = api.filter_account_holdings(body=filter_body)

    # Opening a CSV file for writing in write mode
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


def main():
    """
    Entry point for api key demonstration

    :return:
    """
    list_latest_holdings()

    holdings_to_csv()


if __name__ == '__main__':
    main()
