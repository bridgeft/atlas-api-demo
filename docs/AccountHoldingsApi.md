# swagger_client.AccountHoldingsApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_account_holdings**](AccountHoldingsApi.md#filter_account_holdings) | **POST** /data/luca/account-holdings/filter | Filter all Account Holdings records
[**get_account_holding**](AccountHoldingsApi.md#get_account_holding) | **GET** /data/luca/account-holdings/{id} | Retrieve a Account Holding record
[**get_account_holdings**](AccountHoldingsApi.md#get_account_holdings) | **GET** /data/luca/account-holdings | List all Account Holdings records

# **filter_account_holdings**
> InlineResponse20071 filter_account_holdings(body=body, limit=limit, page=page)

Filter all Account Holdings records

Returns a filtered list of Account Holdings records

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountHoldingsApi()
body = swagger_client.AccountholdingsFilterBody() # AccountholdingsFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Account Holdings records
    api_response = api_instance.filter_account_holdings(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountHoldingsApi->filter_account_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountholdingsFilterBody**](AccountholdingsFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20071**](InlineResponse20071.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_holding**
> InlineResponse20070 get_account_holding(id, limit=limit, page=page)

Retrieve a Account Holding record

Returns a Account Holding record based on its ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountHoldingsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Account Holding record
    api_response = api_instance.get_account_holding(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountHoldingsApi->get_account_holding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20070**](InlineResponse20070.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_holdings**
> InlineResponse20069 get_account_holdings(limit=limit, page=page)

List all Account Holdings records

Returns a list of Account Holdings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountHoldingsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Account Holdings records
    api_response = api_instance.get_account_holdings(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountHoldingsApi->get_account_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20069**](InlineResponse20069.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

