# swagger_client.FirmsApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_firms**](FirmsApi.md#filter_firms) | **POST** /org/firms/filter | Filter all Firms
[**get_firm**](FirmsApi.md#get_firm) | **GET** /org/firms/{id} | Retrieve a Firm
[**get_firms**](FirmsApi.md#get_firms) | **GET** /org/firms | List all Firms
[**read_updated_firm**](FirmsApi.md#read_updated_firm) | **PUT** /org/firms/{id} | Update a Firm
[**read_updated_firms**](FirmsApi.md#read_updated_firms) | **PUT** /org/firms | Update Firms

# **filter_firms**
> InlineResponse2007 filter_firms(body=body, limit=limit, page=page)

Filter all Firms

Return a filtered list of all Firms

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirmsApi()
body = swagger_client.FirmsFilterBody() # FirmsFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Firms
    api_response = api_instance.filter_firms(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmsApi->filter_firms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirmsFilterBody**](FirmsFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firm**
> InlineResponse2008 get_firm(id, limit=limit, page=page)

Retrieve a Firm

Returns a firm based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirmsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Firm
    api_response = api_instance.get_firm(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmsApi->get_firm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firms**
> InlineResponse2007 get_firms(limit=limit, page=page)

List all Firms

Returns a list of firms within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirmsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Firms
    api_response = api_instance.get_firms(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmsApi->get_firms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_updated_firm**
> InlineResponse2008 read_updated_firm(id, limit=limit, page=page)

Update a Firm

Returns the updated firm

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirmsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update a Firm
    api_response = api_instance.read_updated_firm(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmsApi->read_updated_firm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_updated_firms**
> InlineResponse2007 read_updated_firms(limit=limit, page=page)

Update Firms

Returns a list of updated firms

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirmsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update Firms
    api_response = api_instance.read_updated_firms(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmsApi->read_updated_firms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

