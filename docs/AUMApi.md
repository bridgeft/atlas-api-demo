# swagger_client.AUMApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_au_ms**](AUMApi.md#filter_au_ms) | **POST** /analytics/aum/filter | Filter all AUM
[**get_au_ms**](AUMApi.md#get_au_ms) | **GET** /analytics/aum | List all AUM
[**get_aum**](AUMApi.md#get_aum) | **GET** /analytics/aum/{id} | Retrieve an AUM
[**get_filtered_au_ms**](AUMApi.md#get_filtered_au_ms) | **POST** /analytics/aum/get-aum | Get filtered AUM

# **filter_au_ms**
> InlineResponse20052 filter_au_ms(body=body, limit=limit, page=page)

Filter all AUM

Return a filtered list of all AUMs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AUMApi()
body = swagger_client.AumFilterBody() # AumFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all AUM
    api_response = api_instance.filter_au_ms(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AUMApi->filter_au_ms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AumFilterBody**](AumFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_au_ms**
> InlineResponse20052 get_au_ms(limit=limit, page=page)

List all AUM

Returns a list of AUMs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AUMApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all AUM
    api_response = api_instance.get_au_ms(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AUMApi->get_au_ms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aum**
> InlineResponse20053 get_aum(id, limit=limit, page=page)

Retrieve an AUM

Returns an AUM based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AUMApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve an AUM
    api_response = api_instance.get_aum(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AUMApi->get_aum: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filtered_au_ms**
> InlineResponse20052 get_filtered_au_ms(limit=limit, page=page)

Get filtered AUM

Returns a list of AUM, filtered by frequency and ordered by as_of_date

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AUMApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Get filtered AUM
    api_response = api_instance.get_filtered_au_ms(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AUMApi->get_filtered_au_ms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

