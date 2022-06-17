from __future__ import print_function

import csv

import swagger_client
from demo import configuration, authed_client
import json

# declare an instance of the api for interacting with the accounts resource
api = swagger_client.AccountBalancesApi(authed_client())


def list_balances():
    """
    Demonstrates listing all account balances.

    :return:
    """
    # get all balances
    print("get balances")
    resp = api.get_account_balances()

    # first two balances from the response
    print('first two balance response:')
    print(resp.data[:2])


def list_current_balances():

    """
    Demonstrate listing account current balances

    """

    # get all current balances
    print("get current balances")
    resp = api.get_account_current_balances()

    print('first two current balance response:')
    print(resp[:2])


def balances_by_account_to_csv():
    """
    Demonstrates
    1. Fetching all balances through pagination
    2. Copying time series balances for each account to csv files

    """

    # fetch all balances
    print("fetch balances for all accounts")

    balances_by_account = {}
    has_next = True
    page = 1
    while has_next:
        query_params = {'pager_page': str(page)}
        resp = api.get_account_balances(**query_params)
        has_next = resp.has_next
        page += 1
        print(f'Page: {resp.current_page} of {resp.total_pages} has {resp.total_items} total results and {len(resp.data)} results on this page')
        for balance in resp.data:
            account_id = balance["account_id"]
            if account_id not in balances_by_account:
                balances_by_account[account_id] = []
                balances_by_account[account_id].append(balance)

            balances_by_account[account_id].append(balance)

    print("write balance to csv")

    for accountId, balances in balances_by_account.items():
        print(f'Account ID: {accountId} \nBalance length: {len(balances)}')

        csv_path = f'./balance_csv_files/{accountId}_balance.csv'
        data_to_file = open(csv_path, 'w', newline='')  # need to close at the end
        csv_writer = csv.writer(data_to_file, delimiter=",")
        csv_writer.writerow(["Date", "Account ID", "Beginning Period Value", "Cash Value", "Security Holding Value",
                             "Net Return Percent"])

        for balance in balances:
            date = balance["as_of_date"],
            account_id = balance["account_id"],
            beginning_value = balance["beginning_period_value"],
            cash_value = balance["cash_value"],
            sec_holding_value = balance["security_holdings_value"],
            return_percent = balance["percentage_period_net_return"]

            csv_writer.writerow([date, account_id, beginning_value, cash_value, sec_holding_value, return_percent])
        data_to_file.close()
        break

    print("copying balances to csv complete!!")


def main():
    """
    Entry point for balance api demonstration

    :return:
    """
    list_balances()

    list_current_balances()

    balances_by_account_to_csv()


if __name__ == '__main__':
    main()
