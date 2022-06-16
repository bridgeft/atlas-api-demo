from __future__ import print_function

import csv

import swagger_client
from demo import configuration, authed_client
import json

# declare an instance of the api for interacting with the accounts resource
api = swagger_client.AccountBalancesApi(authed_client())


def list_balances():
    """
    Demonstrates listing API keys
    API keys can be managed (created, read, deleted) by creating a temporary oauth2 id token
    from the /v2/oauth2/token endpoint, which can be used as a bearer token until expiration

    It's recommended to create and manage API keys for machine-to-machine backend applications
    for use cases where expiration and key management isn't necessary

    :return:
    """
    # get all balances
    print("get balances")
    resp = api.get_account_balances()

    # first two balances from the response
    print('first two balance response:')
    print(resp.data[:2])


def list_current_balances():

    # get all current balances
    print("get current balances")
    resp = api.get_account_current_balances()

    print('first two current balance response:')
    print(resp[:2])


def balances_to_csv():

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
        csv_writer.writerow(["Date", "Account ID"])

        for balance in balances:
            date = balance["as_of_date"],
            account_id = balance["account_id"]

            csv_writer.writerow([date, account_id])
        data_to_file.close()
        break

    print("writing balance to csv complete!!")


def main():
    """
    Entry point for api key demonstration

    :return:
    """
    list_balances()

    list_current_balances()

    balances_to_csv()


if __name__ == '__main__':
    main()
