import swagger_client
import os

configuration = swagger_client.Configuration()

def api_client():
    header_name = "Authorization"

    apikey = os.environ['API_KEY']
    header_value = f"Bearer {apikey}"

    return swagger_client.ApiClient(
        configuration=configuration,
        header_name=header_name,
        header_value=header_value
    )
