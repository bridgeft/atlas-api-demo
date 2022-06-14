# swagger_client.GainLossApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_gain_loss**](GainLossApi.md#filter_gain_loss) | **POST** /data/luca/gain-loss/filter | Filter all Gain Loss records
[**get_gain_loss**](GainLossApi.md#get_gain_loss) | **GET** /data/luca/gain-loss/{id} | Retrieve a Gain Loss record
[**get_gain_losses**](GainLossApi.md#get_gain_losses) | **GET** /data/luca/gain-loss | List all Gain Loss records

# **filter_gain_loss**
> InlineResponse20064 filter_gain_loss(body=body, limit=limit, page=page)

Filter all Gain Loss records

Returns a filtered list of Gain Loss records

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GainLossApi()
body = swagger_client.GainlossFilterBody() # GainlossFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Gain Loss records
    api_response = api_instance.filter_gain_loss(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GainLossApi->filter_gain_loss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GainlossFilterBody**](GainlossFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20064**](InlineResponse20064.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gain_loss**
> InlineResponse20063 get_gain_loss(id, limit=limit, page=page)

Retrieve a Gain Loss record

Returns a Gain Loss record based on its ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GainLossApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Gain Loss record
    api_response = api_instance.get_gain_loss(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GainLossApi->get_gain_loss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20063**](InlineResponse20063.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gain_losses**
> InlineResponse20062 get_gain_losses(limit=limit, page=page)

List all Gain Loss records

Returns a list of Gain Loss

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GainLossApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Gain Loss records
    api_response = api_instance.get_gain_losses(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GainLossApi->get_gain_losses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

