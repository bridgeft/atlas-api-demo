# swagger_client.PositionsApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_positions**](PositionsApi.md#filter_positions) | **POST** /data/luca/positions/filter | Filter all Positions records
[**get_position**](PositionsApi.md#get_position) | **GET** /data/luca/positions/{id} | Retrieve a Position record
[**get_positions**](PositionsApi.md#get_positions) | **GET** /data/luca/positions | List all Positions records

# **filter_positions**
> InlineResponse20078 filter_positions(body=body, limit=limit, page=page)

Filter all Positions records

Returns a filtered list of Positions records

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
body = swagger_client.PositionsFilterBody() # PositionsFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Positions records
    api_response = api_instance.filter_positions(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->filter_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PositionsFilterBody**](PositionsFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20078**](InlineResponse20078.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_position**
> InlineResponse20077 get_position(id, limit=limit, page=page)

Retrieve a Position record

Returns a Position record based on its ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Position record
    api_response = api_instance.get_position(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->get_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20077**](InlineResponse20077.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_positions**
> InlineResponse20076 get_positions(limit=limit, page=page)

List all Positions records

Returns a list of Positions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Positions records
    api_response = api_instance.get_positions(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->get_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20076**](InlineResponse20076.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

