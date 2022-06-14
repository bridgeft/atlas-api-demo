# swagger_client.IndexDataApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_index**](IndexDataApi.md#filter_index) | **POST** /data/idc/indexes/filter | Filter all IDC Indexes
[**get_index**](IndexDataApi.md#get_index) | **GET** /data/idc/indexes/{id} | Retrieve an IDC Index
[**get_indexes**](IndexDataApi.md#get_indexes) | **GET** /data/idc/indexes | List all List all IDC Indexes

# **filter_index**
> InlineResponse200116 filter_index(body=body, limit=limit, page=page)

Filter all IDC Indexes

Return a filtered list of all IDC indexes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndexDataApi()
body = swagger_client.IndexesFilterBody() # IndexesFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all IDC Indexes
    api_response = api_instance.filter_index(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexDataApi->filter_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IndexesFilterBody**](IndexesFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200116**](InlineResponse200116.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_index**
> InlineResponse200115 get_index(id, limit=limit, page=page)

Retrieve an IDC Index

Returns an idc index based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndexDataApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve an IDC Index
    api_response = api_instance.get_index(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexDataApi->get_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200115**](InlineResponse200115.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indexes**
> InlineResponse200114 get_indexes(limit=limit, page=page)

List all List all IDC Indexes

Returns a list of List all IDC Indexes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndexDataApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all List all IDC Indexes
    api_response = api_instance.get_indexes(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexDataApi->get_indexes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200114**](InlineResponse200114.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

