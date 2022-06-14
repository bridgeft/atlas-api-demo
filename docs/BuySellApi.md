# swagger_client.BuySellApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_buy_sell**](BuySellApi.md#filter_buy_sell) | **POST** /data/luca/buy-sell/filter | Filter all Buy Sell records
[**get_buy_sell**](BuySellApi.md#get_buy_sell) | **GET** /data/luca/buy-sell/{id} | Retrieve a Buy Sell record
[**get_buy_sells**](BuySellApi.md#get_buy_sells) | **GET** /data/luca/buy-sell | List all Buy Sells records

# **filter_buy_sell**
> InlineResponse20058 filter_buy_sell(body=body, limit=limit, page=page)

Filter all Buy Sell records

Returns a filtered list of Buy Sell records

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuySellApi()
body = swagger_client.BuysellFilterBody() # BuysellFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Buy Sell records
    api_response = api_instance.filter_buy_sell(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuySellApi->filter_buy_sell: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BuysellFilterBody**](BuysellFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_buy_sell**
> InlineResponse20057 get_buy_sell(id, limit=limit, page=page)

Retrieve a Buy Sell record

Returns a Buy Sell record based on its ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuySellApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Buy Sell record
    api_response = api_instance.get_buy_sell(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuySellApi->get_buy_sell: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_buy_sells**
> InlineResponse20056 get_buy_sells(limit=limit, page=page)

List all Buy Sells records

Returns a list of Buy Sells

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuySellApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Buy Sells records
    api_response = api_instance.get_buy_sells(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuySellApi->get_buy_sells: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

