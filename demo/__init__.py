import swagger_client
import os

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
