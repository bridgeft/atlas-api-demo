from __future__ import print_function
import csv

import swagger_client
from demo import authed_client

# declare an instance of the api for interacting with the account balance resource
api = swagger_client.AccountBalancesApi(authed_client())


def generate_aum_balance_to_csv():
    """
    Demonstrates fetching account balance and generating aum balance time series csv file
    :return:
    """

    # fetch all balances for all accounts
    resp = api.get_account_balances()
    balances = resp.data

    # balance_value_by_date, a dictionary set to keep a track of total balance by date
    balance_value_by_date = {}
    for balance in balances:
        date = balance['as_of_date']
        value = balance['cash_value'] + balance['security_holdings_value']
        if date not in balance_value_by_date:
            balance_value_by_date[date] = value

        balance_value_by_date[date] += value

    # write the dictionary set to a csv
    csv_path = 'aum.csv'

    data_to_file = open(csv_path, 'w', newline='')  # need to close at the end
    csv_writer = csv.writer(data_to_file, delimiter=",")
    csv_writer.writerow(["Date", "Balance"])

    print('generating aum csv')
    for key, value in balance_value_by_date.items():
        date = key,
        balance = value

        csv_writer.writerow([date, balance])
    data_to_file.close()

    print('aum csv generation complete!!')


def main():
    """
    Entry point for aum balance demonstration

    :return:
    """
    generate_aum_balance_to_csv()


if __name__ == '__main__':
    main()
