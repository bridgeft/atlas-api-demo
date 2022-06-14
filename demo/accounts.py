from __future__ import print_function
import swagger_client
from swagger_client.rest import ApiException
from demo import api_client
import csv

# declare an instance of the api for interacting with the accounts resource
api = swagger_client.AccountsApi(api_client())

# fields that we care about for this demonstration
fields = [
    'id',
    'number',
    'acct_type',
    'custodian',
    'display_name',
    'status',
    'payment_source',
    'address_1',
    'address_2',
    'city',
    'state',
    'zip_code',
]


def accounts_to_csv(path='accounts.csv'):
    """
    Outputs select fields (above) to a CSV file

    :param path:
    :return:
    """

    accounts = []
    has_next = True
    while has_next:
        resp = api.get_accounts()
        has_next = resp.has_next
        print(f'Page: {resp.current_page} of {resp.total_pages} has {resp.total_items} total results and {len(resp.data)} results on this page')
        for acct in resp.data:
            acct_row = []
            for f in fields:
                acct_row.append(acct[f])
            accounts.append(acct_row)

    # output the accounts to a csv
    with open(path, 'w', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(fields)

        for row in accounts:
            writer.writerow(row)



def filter_example():
    """
    Filters and prints all Schwab accounts located in Hawaii
    Illustrates simple filtering, using key-value pairs as exact matching
    See more: https://docs.bridgeft.com/docs/filtering-v26

    :return:
    """
    # find all schwab accounts in Hawaii
    resp = api.filter_accounts(body={
        'custodian': 'SWB',
        'state': 'Hawaii',
    })
    accounts = resp.data

    print(f'Found {len(accounts)} accounts. The first two are:')
    for acct in accounts[:2]:
        print(acct)


def complex_filter_example():
    """
    Finds and filters all TDA and Schwab IRA accounts located in Hawaii
    Illustrates complex filtering, which allows applying a number of range operations and join conditions
    See more: https://docs.bridgeft.com/docs/filtering-v26

    :return:
    """
    # find all schwab and TDA IRA accounts in Hawaii
    resp = api.filter_accounts(body={
        'custodian': {
            'any_or_all': 'any',
            'conditions': [{
                'value': 'SWB',
                'op': 'eq',
            }, {
                'value': 'TDA',
                'op': 'eq',
            }]
        },
        'acct_type': {
            'conditions': [{
                'value': 'IRA',
                'op': 'contains',
            }]
        },
        'state': 'Hawaii',
    })
    accounts = resp.data

    print(f'Found {len(accounts)} accounts. The first two are:')
    for acct in accounts[:2]:
        print(acct)



def get_single_account():
    """
    Fetches details for a single account from the API.
    In this case the API client will represent the data as an object with dot-referenceable fields
    rather than a dictionary

    :return:
    """
    print('Fetching single account')
    acct = api.get_account(id=217057)
    print(f'Details for account id {acct.id} ({acct.name}, {acct.number}):')
    values = []
    for f in fields:
        values.append(f'{f}: {getattr(acct, f)}')
    print(' '.join(values))


def main():
    """
    Entry point for demos with the accounts resource

    :return:
    """
    accounts_to_csv()

    # get a single account
    get_single_account()

    # filter out some accounts
    filter_example()

    # apply complex filtering to accounts
    complex_filter_example()


if __name__ == '__main__':
    main()

