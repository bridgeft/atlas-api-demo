# swagger_client.MinimumsApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_many_minimums**](MinimumsApi.md#create_many_minimums) | **POST** /billing/minimums/create-many | Create Minimums
[**create_minimums**](MinimumsApi.md#create_minimums) | **POST** /billing/minimums | Create a Minimum
[**detele_many_minimums_many**](MinimumsApi.md#detele_many_minimums_many) | **POST** /billing/minimums/delete-many | Delete many Minimums
[**detele_minimums**](MinimumsApi.md#detele_minimums) | **DELETE** /billing/minimums/{id} | Delete a Minimum
[**filter_minimums**](MinimumsApi.md#filter_minimums) | **POST** /billing/minimums/filter | Filter Minimums
[**get_minimums**](MinimumsApi.md#get_minimums) | **GET** /billing/minimums/{id} | Retrieve a Minimum
[**get_minimums_many**](MinimumsApi.md#get_minimums_many) | **GET** /billing/minimums | List all Minimums
[**update_minimums**](MinimumsApi.md#update_minimums) | **PUT** /billing/minimums/{id} | Update a Minimum
[**update_minimums_many**](MinimumsApi.md#update_minimums_many) | **PUT** /billing/minimums | Bulk Update Minimums

# **create_many_minimums**
> InlineResponse20031 create_many_minimums(limit=limit, page=page)

Create Minimums

Returns a list of created Minimums

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MinimumsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create Minimums
    api_response = api_instance.create_many_minimums(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MinimumsApi->create_many_minimums: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_minimums**
> InlineResponse20032 create_minimums(body, limit=limit, page=page)

Create a Minimum

Returns the created Minimums

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MinimumsApi()
body = swagger_client.BillingMinimumsBody() # BillingMinimumsBody | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create a Minimum
    api_response = api_instance.create_minimums(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MinimumsApi->create_minimums: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillingMinimumsBody**](BillingMinimumsBody.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detele_many_minimums_many**
> detele_many_minimums_many(body, limit=limit, page=page)

Delete many Minimums

Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MinimumsApi()
body = NULL # object | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete many Minimums
    api_instance.detele_many_minimums_many(body, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling MinimumsApi->detele_many_minimums_many: %s\n" % e)
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

# **detele_minimums**
> detele_minimums(id, limit=limit, page=page)

Delete a Minimum

Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MinimumsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete a Minimum
    api_instance.detele_minimums(id, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling MinimumsApi->detele_minimums: %s\n" % e)
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

# **filter_minimums**
> InlineResponse20031 filter_minimums(body=body, limit=limit, page=page)

Filter Minimums

Returns a filtered list of Minimums

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MinimumsApi()
body = swagger_client.MinimumsFilterBody() # MinimumsFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter Minimums
    api_response = api_instance.filter_minimums(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MinimumsApi->filter_minimums: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MinimumsFilterBody**](MinimumsFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_minimums**
> InlineResponse20032 get_minimums(id, limit=limit, page=page)

Retrieve a Minimum

Returns a Minimums based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MinimumsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Minimum
    api_response = api_instance.get_minimums(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MinimumsApi->get_minimums: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_minimums_many**
> InlineResponse20031 get_minimums_many(limit=limit, page=page)

List all Minimums

Returns a list of Minimumss within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MinimumsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Minimums
    api_response = api_instance.get_minimums_many(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MinimumsApi->get_minimums_many: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_minimums**
> InlineResponse20032 update_minimums(id, limit=limit, page=page)

Update a Minimum

Returns a list of updated Minimums

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MinimumsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update a Minimum
    api_response = api_instance.update_minimums(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MinimumsApi->update_minimums: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_minimums_many**
> InlineResponse20031 update_minimums_many(limit=limit, page=page)

Bulk Update Minimums

Returns the updated Minimumss

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MinimumsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Bulk Update Minimums
    api_response = api_instance.update_minimums_many(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MinimumsApi->update_minimums_many: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

