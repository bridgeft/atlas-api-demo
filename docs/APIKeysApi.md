# swagger_client.APIKeysApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api**](APIKeysApi.md#create_api) | **POST** /auth-management/api-keys | Create an API Key
[**detele_api**](APIKeysApi.md#detele_api) | **DELETE** /auth-management/api-keys/{id} | Delete an API Key
[**get_api**](APIKeysApi.md#get_api) | **GET** /auth-management/api-keys/{id} | Retrieve an API key
[**get_apis**](APIKeysApi.md#get_apis) | **GET** /auth-management/api-keys | Retrieve all API keys

# **create_api**
> InlineResponse20089 create_api(body, limit=limit, page=page)

Create an API Key

Returns the updated API key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIKeysApi()
body = swagger_client.AuthmanagementApikeysBody() # AuthmanagementApikeysBody | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create an API Key
    api_response = api_instance.create_api(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->create_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthmanagementApikeysBody**](AuthmanagementApikeysBody.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20089**](InlineResponse20089.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detele_api**
> detele_api(id, limit=limit, page=page)

Delete an API Key

Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIKeysApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete an API Key
    api_instance.detele_api(id, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling APIKeysApi->detele_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api**
> InlineResponse20089 get_api(id, limit=limit, page=page)

Retrieve an API key

Returns an API key based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIKeysApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve an API key
    api_response = api_instance.get_api(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->get_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20089**](InlineResponse20089.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apis**
> InlineResponse20088 get_apis(limit=limit, page=page)

Retrieve all API keys

Returns a list of api keys within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIKeysApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve all API keys
    api_response = api_instance.get_apis(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->get_apis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20088**](InlineResponse20088.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

