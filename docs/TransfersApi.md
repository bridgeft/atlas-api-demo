# swagger_client.TransfersApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_transfers**](TransfersApi.md#filter_transfers) | **POST** /data/luca/transfers/filter | Filter all Transfers records
[**get_transfer**](TransfersApi.md#get_transfer) | **GET** /data/luca/transfers/{id} | Retrieve a Transfer record
[**get_transfers**](TransfersApi.md#get_transfers) | **GET** /data/luca/transfers | List all Transfers records

# **filter_transfers**
> InlineResponse20075 filter_transfers(body=body, limit=limit, page=page)

Filter all Transfers records

Returns a filtered list of Transfers records

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransfersApi()
body = swagger_client.TransfersFilterBody() # TransfersFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Transfers records
    api_response = api_instance.filter_transfers(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->filter_transfers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransfersFilterBody**](TransfersFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20075**](InlineResponse20075.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transfer**
> InlineResponse20074 get_transfer(id, limit=limit, page=page)

Retrieve a Transfer record

Returns a Transfer record based on its ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransfersApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Transfer record
    api_response = api_instance.get_transfer(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->get_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20074**](InlineResponse20074.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transfers**
> InlineResponse20073 get_transfers(limit=limit, page=page)

List all Transfers records

Returns a list of Transfers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransfersApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Transfers records
    api_response = api_instance.get_transfers(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->get_transfers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20073**](InlineResponse20073.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

