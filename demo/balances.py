from __future__ import print_function
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
    # this yields an error
    resp = api.get_account_balances()

    # produces no meaningful content
    # resp = api.get_account_current_balances()
    print('response:')
    print(resp)



def main():
    """
    Entry point for api key demonstration

    :return:
    """
    list_balances()


if __name__ == '__main__':
    main()
