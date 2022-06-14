# swagger_client.HeldawayHoldingsApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_heldaway_holdings**](HeldawayHoldingsApi.md#filter_heldaway_holdings) | **POST** /heldaway/holdings/filter | Filter all Heldaway Holdings
[**get_heldaway_holding**](HeldawayHoldingsApi.md#get_heldaway_holding) | **GET** /heldaway/holdings/{id} | Retrieve a Heldaway Holding
[**get_heldaway_holdings**](HeldawayHoldingsApi.md#get_heldaway_holdings) | **GET** /heldaway/holdings | List all Heldaway Holdings

# **filter_heldaway_holdings**
> InlineResponse200109 filter_heldaway_holdings(body=body, limit=limit, page=page)

Filter all Heldaway Holdings

Returns a filtered list of Heldaway Holdings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HeldawayHoldingsApi()
body = swagger_client.HoldingsFilterBody() # HoldingsFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Heldaway Holdings
    api_response = api_instance.filter_heldaway_holdings(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeldawayHoldingsApi->filter_heldaway_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HoldingsFilterBody**](HoldingsFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200109**](InlineResponse200109.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heldaway_holding**
> InlineResponse200108 get_heldaway_holding(id, limit=limit, page=page)

Retrieve a Heldaway Holding

Returns a heldaway holding based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HeldawayHoldingsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Heldaway Holding
    api_response = api_instance.get_heldaway_holding(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeldawayHoldingsApi->get_heldaway_holding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200108**](InlineResponse200108.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heldaway_holdings**
> InlineResponse200107 get_heldaway_holdings(limit=limit, page=page)

List all Heldaway Holdings

Returns a list of all heldaway holdings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HeldawayHoldingsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Heldaway Holdings
    api_response = api_instance.get_heldaway_holdings(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeldawayHoldingsApi->get_heldaway_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200107**](InlineResponse200107.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

