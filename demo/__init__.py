import swagger_client
import os
import json

configuration = swagger_client.Configuration()
header_name = "Authorization"


def authed_client():
    """
    Obtain an authenticated client using the API_KEY environment var as the api key

    :return:
    """
    apikey = os.environ['API_KEY']
    return swagger_client.ApiClient(
        configuration=configuration,
        header_name=header_name,
        header_value=f"Bearer {apikey}"
    )


def token_authed_client(token):
    """
    Obtain an authenticated client using the provided token as the Bearer token

    :param token:
    :return:
    """
    return swagger_client.ApiClient(
        configuration=configuration,
        header_name=header_name,
        header_value=f"Bearer {token}"
    )


def get_id_token():
    """
    Use password grant type to retrieve and receive auth tokens.

    :return:
    """

    client = swagger_client.ApiClient(
        configuration=configuration,
        header_name="Content-Type",
        header_value="application/x-www-form-urlencoded"
    )

    p = {
        'username': os.environ['USERNAME'],
        'password': os.environ['PASSWORD'],
        'grant_type': 'password'
    }
    auth_endpoint = 'https://api.bridgeft.com/v2/oauth2/token'
    resp = client.request('POST', auth_endpoint, query_params=p)
    data = json.loads(resp.data)
    id_token = data['IdToken']
    print(f'using id token as a Bearer token: {id_token}')

    return id_token
