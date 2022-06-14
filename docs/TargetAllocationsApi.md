# swagger_client.TargetAllocationsApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_many_target_allocations**](TargetAllocationsApi.md#create_many_target_allocations) | **POST** /reporting/target-allocations/create-many | Create Target Allocations
[**create_target_allocations**](TargetAllocationsApi.md#create_target_allocations) | **POST** /reporting/target-allocations | Create a Target Allocation
[**detele_many_target_allocations**](TargetAllocationsApi.md#detele_many_target_allocations) | **POST** /reporting/target-allocations/delete-many | Delete many Target Allocations
[**detele_target_allocation**](TargetAllocationsApi.md#detele_target_allocation) | **DELETE** /reporting/target-allocations/{id} | Delete a Target Allocation
[**filter_target_allocations**](TargetAllocationsApi.md#filter_target_allocations) | **POST** /reporting/target-allocations/filter | Filter all Target Allocations
[**get_target_allocation**](TargetAllocationsApi.md#get_target_allocation) | **GET** /reporting/target-allocations/{id} | Retrieve a Target Allocation
[**get_target_allocations**](TargetAllocationsApi.md#get_target_allocations) | **GET** /reporting/target-allocations | List all Target Allocations
[**update_target_allocation**](TargetAllocationsApi.md#update_target_allocation) | **PUT** /reporting/target-allocations/{id} | Update a Target Allocation
[**update_target_allocations**](TargetAllocationsApi.md#update_target_allocations) | **PUT** /reporting/target-allocations | Bulk Update Target Allocations

# **create_many_target_allocations**
> InlineResponse20044 create_many_target_allocations(body, limit=limit, page=page)

Create Target Allocations

Returns a list of created Target Allocations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetAllocationsApi()
body = [swagger_client.Paths1reporting1targetAllocationspostrequestBodycontentapplication1jsonschema()] # list[Paths1reporting1targetAllocationspostrequestBodycontentapplication1jsonschema] | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create Target Allocations
    api_response = api_instance.create_many_target_allocations(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetAllocationsApi->create_many_target_allocations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Paths1reporting1targetAllocationspostrequestBodycontentapplication1jsonschema]**](Paths1reporting1targetAllocationspostrequestBodycontentapplication1jsonschema.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_target_allocations**
> InlineResponse20045 create_target_allocations(body, limit=limit, page=page)

Create a Target Allocation

Returns the created Target Allocation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetAllocationsApi()
body = swagger_client.ReportingTargetallocationsBody() # ReportingTargetallocationsBody | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create a Target Allocation
    api_response = api_instance.create_target_allocations(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetAllocationsApi->create_target_allocations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportingTargetallocationsBody**](ReportingTargetallocationsBody.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detele_many_target_allocations**
> detele_many_target_allocations(body, limit=limit, page=page)

Delete many Target Allocations

Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetAllocationsApi()
body = NULL # object | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete many Target Allocations
    api_instance.detele_many_target_allocations(body, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling TargetAllocationsApi->detele_many_target_allocations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detele_target_allocation**
> detele_target_allocation(id, limit=limit, page=page)

Delete a Target Allocation

Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetAllocationsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete a Target Allocation
    api_instance.detele_target_allocation(id, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling TargetAllocationsApi->detele_target_allocation: %s\n" % e)
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

# **filter_target_allocations**
> InlineResponse20046 filter_target_allocations(body=body, limit=limit, page=page)

Filter all Target Allocations

Returns a filtered list of Target Allocations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetAllocationsApi()
body = swagger_client.TargetallocationsFilterBody() # TargetallocationsFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Target Allocations
    api_response = api_instance.filter_target_allocations(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetAllocationsApi->filter_target_allocations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TargetallocationsFilterBody**](TargetallocationsFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target_allocation**
> InlineResponse20046 get_target_allocation(id, limit=limit, page=page)

Retrieve a Target Allocation

Returns a Target Allocation based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetAllocationsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Target Allocation
    api_response = api_instance.get_target_allocation(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetAllocationsApi->get_target_allocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target_allocations**
> InlineResponse20043 get_target_allocations(limit=limit, page=page)

List all Target Allocations

Returns a list of Target Allocations within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetAllocationsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Target Allocations
    api_response = api_instance.get_target_allocations(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetAllocationsApi->get_target_allocations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_target_allocation**
> InlineResponse20046 update_target_allocation(id, limit=limit, page=page)

Update a Target Allocation

Returns the updated Target Allocation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetAllocationsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update a Target Allocation
    api_response = api_instance.update_target_allocation(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetAllocationsApi->update_target_allocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_target_allocations**
> InlineResponse20044 update_target_allocations(limit=limit, page=page)

Bulk Update Target Allocations

Returns the updated Target Allocations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetAllocationsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Bulk Update Target Allocations
    api_response = api_instance.update_target_allocations(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetAllocationsApi->update_target_allocations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

