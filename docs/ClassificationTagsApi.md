# swagger_client.ClassificationTagsApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_classification_tags**](ClassificationTagsApi.md#create_classification_tags) | **POST** /reporting/class-tags | Create a Classification Tag
[**create_many_classification_tags**](ClassificationTagsApi.md#create_many_classification_tags) | **POST** /reporting/class-tags/create-many | Create Classification Tags
[**detele_classification_tag**](ClassificationTagsApi.md#detele_classification_tag) | **DELETE** /reporting/class-tags/{id} | Delete a classification Tag
[**detele_many_classification_tags**](ClassificationTagsApi.md#detele_many_classification_tags) | **POST** /reporting/class-tags/delete-many | Delete many Classification Tags
[**filter_classification_tags**](ClassificationTagsApi.md#filter_classification_tags) | **POST** /reporting/class-tags/filter | Filter all Classification Tags
[**get_classification_tag**](ClassificationTagsApi.md#get_classification_tag) | **GET** /reporting/class-tags/{id} | Retrieve a Classification Tag
[**get_classification_tags**](ClassificationTagsApi.md#get_classification_tags) | **GET** /reporting/class-tags | List all Classification Tags
[**update_classification_tag**](ClassificationTagsApi.md#update_classification_tag) | **PUT** /reporting/class-tags/{id} | Update a Classification Tag
[**update_classification_tags**](ClassificationTagsApi.md#update_classification_tags) | **PUT** /reporting/class-tags | Bulk Update Classification Tags

# **create_classification_tags**
> InlineResponse20041 create_classification_tags(body, limit=limit, page=page)

Create a Classification Tag

Returns the created classification tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClassificationTagsApi()
body = swagger_client.ReportingClasstagsBody() # ReportingClasstagsBody | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create a Classification Tag
    api_response = api_instance.create_classification_tags(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationTagsApi->create_classification_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportingClasstagsBody**](ReportingClasstagsBody.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_many_classification_tags**
> InlineResponse20040 create_many_classification_tags(limit=limit, page=page)

Create Classification Tags

Returns a list of created Classification Tags

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClassificationTagsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create Classification Tags
    api_response = api_instance.create_many_classification_tags(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationTagsApi->create_many_classification_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detele_classification_tag**
> detele_classification_tag(id, limit=limit, page=page)

Delete a classification Tag

Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClassificationTagsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete a classification Tag
    api_instance.detele_classification_tag(id, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling ClassificationTagsApi->detele_classification_tag: %s\n" % e)
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

# **detele_many_classification_tags**
> detele_many_classification_tags(body, limit=limit, page=page)

Delete many Classification Tags

Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClassificationTagsApi()
body = NULL # object | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete many Classification Tags
    api_instance.detele_many_classification_tags(body, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling ClassificationTagsApi->detele_many_classification_tags: %s\n" % e)
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

# **filter_classification_tags**
> InlineResponse20040 filter_classification_tags(body=body, limit=limit, page=page)

Filter all Classification Tags

Returns a filtered list of classification tags

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClassificationTagsApi()
body = swagger_client.ClasstagsFilterBody() # ClasstagsFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Classification Tags
    api_response = api_instance.filter_classification_tags(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationTagsApi->filter_classification_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClasstagsFilterBody**](ClasstagsFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classification_tag**
> InlineResponse20041 get_classification_tag(id, limit=limit, page=page)

Retrieve a Classification Tag

Returns a classification tag based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClassificationTagsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Classification Tag
    api_response = api_instance.get_classification_tag(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationTagsApi->get_classification_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classification_tags**
> InlineResponse20040 get_classification_tags(limit=limit, page=page)

List all Classification Tags

Returns a list of Classification Tags within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClassificationTagsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Classification Tags
    api_response = api_instance.get_classification_tags(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationTagsApi->get_classification_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_classification_tag**
> InlineResponse20041 update_classification_tag(id, limit=limit, page=page)

Update a Classification Tag

Returns the updated classification tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClassificationTagsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update a Classification Tag
    api_response = api_instance.update_classification_tag(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationTagsApi->update_classification_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_classification_tags**
> InlineResponse20040 update_classification_tags(limit=limit, page=page)

Bulk Update Classification Tags

Returns the updated classification tags

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClassificationTagsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Bulk Update Classification Tags
    api_response = api_instance.update_classification_tags(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationTagsApi->update_classification_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

