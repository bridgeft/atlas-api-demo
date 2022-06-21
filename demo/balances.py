from __future__ import print_function

import csv

import swagger_client
from demo import configuration, authed_client
import json

# declare an instance of the api for interacting with the accounts resource
api = swagger_client.AccountBalancesApi(authed_client())



def list_current_balances():
    """
    Demonstrate listing account current balances

    """
    # get all current balances
    print("Getting all current balances")
    bals = api.get_account_current_balances()

    print(f'Received {len(bals)} records. The first two are:')
    print(bals[:2])


def balances_by_account_to_csv():
    """
    Demonstrates
    1. Fetching all balances through pagination
    2. Copying time series balances for each account to csv files

    """
    # fetch all balances
    print("Fetching balances by account")

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

        # limit the pagination...
        if page > 2:
            break

    print("Writing to csv...")

    ctr = 0
    for accountId, balances in balances_by_account.items():
        csv_path = f'out/account-balances/{accountId}.csv'
        print(f'Account ID: {accountId} \nBalance length: {len(balances)}. Writing to {csv_path}')

        csv_file = open(csv_path, 'w', newline='\n')  # need to close at the end
        csv_writer = csv.writer(csv_file, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["Date", "Account ID", "Beginning Period Value", "Cash Value", "Security Holding Value",
                             "Net Return Percent"])

        for balance in balances:
            date = balance["as_of_date"]
            account_id = balance["account_id"]
            beginning_value = balance["beginning_period_value"]
            cash_value = balance["cash_value"]
            sec_holding_value = balance["security_holdings_value"]
            return_percent = balance["percentage_period_net_return"]

            csv_writer.writerow([date, account_id, beginning_value, cash_value, sec_holding_value, return_percent])
        csv_file.close()

        # limit to 3 accounts
        if ctr > 3:
            break
        ctr += 1



def main():
    """
    Entry point for balance api demonstration

    :return:
    """
    list_current_balances()

    balances_by_account_to_csv()


if __name__ == '__main__':
    main()
