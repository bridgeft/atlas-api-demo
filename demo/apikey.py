from __future__ import print_function
import swagger_client
from demo import configuration, token_authed_client
import json

def list_api_keys():
    """
    Demonstrates listing API keys
    API keys can be managed (created, read, deleted) by creating a temporary oauth2 id token
    from the /v2/oauth2/token endpoint, which can be used as a bearer token until expiration

    It's recommended to create and manage API keys for machine-to-machine backend applications
    for use cases where expiration and key management isn't necessary

    :return:
    """
    client = swagger_client.ApiClient(
        configuration=configuration,
        header_name="Content-Type",
        header_value="application/x-www-form-urlencoded"
    )

    p = {
        'username': 'demo@bridgeft.com',
        'password': 'demouser',
        'grant_type': 'password'
    }
    auth_endpoint = 'https://api.bridgeft.com/v2/oauth2/token'
    resp = client.request('POST', auth_endpoint, query_params=p)
    data = json.loads(resp.data)
    id_token = data['IdToken']
    print(f'using id token as a Bearer token: {id_token}')

    # use the id token as a bearer token to view api keys
    api = swagger_client.APIKeysApi(token_authed_client(id_token))
    resp = api.get_api_keys()
    for obj in resp.data:
        print(f'key: {obj["key"]}')



def main():
    """
    Entry point for api key demonstration

    :return:
    """
    list_api_keys()


if __name__ == '__main__':
    main()
