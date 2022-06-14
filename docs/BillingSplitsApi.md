# swagger_client.BillingSplitsApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_billing_splits**](BillingSplitsApi.md#create_billing_splits) | **POST** /billing/splits | Creat a Billing Split
[**create_many_billing_splits**](BillingSplitsApi.md#create_many_billing_splits) | **POST** /billing/splits/create-many | Create Billing Split
[**detele_billing_split**](BillingSplitsApi.md#detele_billing_split) | **DELETE** /billing/splits/{id} | Delete a Billing Splits
[**detele_many_billing_splits**](BillingSplitsApi.md#detele_many_billing_splits) | **POST** /billing/splits/delete-many | Delete many Billing Splits
[**filter_billing_splits**](BillingSplitsApi.md#filter_billing_splits) | **POST** /billing/splits/filter | Filter Billing Splits
[**get_billing_split**](BillingSplitsApi.md#get_billing_split) | **GET** /billing/splits/{id} | Retrieve a Billing Splits
[**get_billing_splits**](BillingSplitsApi.md#get_billing_splits) | **GET** /billing/splits | List all Billing Splits
[**update_billing_split**](BillingSplitsApi.md#update_billing_split) | **PUT** /billing/splits/{id} | Update a Billing Splits
[**update_billing_splits**](BillingSplitsApi.md#update_billing_splits) | **PUT** /billing/splits | Bulk Update Billing Splits

# **create_billing_splits**
> InlineResponse20034 create_billing_splits(body, limit=limit, page=page)

Creat a Billing Split

Returns the created Billing Split

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingSplitsApi()
body = swagger_client.BillingSplitsBody() # BillingSplitsBody | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Creat a Billing Split
    api_response = api_instance.create_billing_splits(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingSplitsApi->create_billing_splits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillingSplitsBody**](BillingSplitsBody.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_many_billing_splits**
> InlineResponse20033 create_many_billing_splits(limit=limit, page=page)

Create Billing Split

Returns a list of created Billing Splits

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingSplitsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create Billing Split
    api_response = api_instance.create_many_billing_splits(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingSplitsApi->create_many_billing_splits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detele_billing_split**
> detele_billing_split(id, limit=limit, page=page)

Delete a Billing Splits

Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingSplitsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete a Billing Splits
    api_instance.detele_billing_split(id, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling BillingSplitsApi->detele_billing_split: %s\n" % e)
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

# **detele_many_billing_splits**
> detele_many_billing_splits(body, limit=limit, page=page)

Delete many Billing Splits

Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingSplitsApi()
body = NULL # object | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete many Billing Splits
    api_instance.detele_many_billing_splits(body, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling BillingSplitsApi->detele_many_billing_splits: %s\n" % e)
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

# **filter_billing_splits**
> InlineResponse20033 filter_billing_splits(body=body, limit=limit, page=page)

Filter Billing Splits

Returns a filtered list of Billing Splits

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingSplitsApi()
body = swagger_client.SplitsFilterBody() # SplitsFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter Billing Splits
    api_response = api_instance.filter_billing_splits(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingSplitsApi->filter_billing_splits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SplitsFilterBody**](SplitsFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_split**
> InlineResponse20035 get_billing_split(id, limit=limit, page=page)

Retrieve a Billing Splits

Returns a Billing Splits based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingSplitsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Billing Splits
    api_response = api_instance.get_billing_split(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingSplitsApi->get_billing_split: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_splits**
> InlineResponse20033 get_billing_splits(limit=limit, page=page)

List all Billing Splits

Returns a list of Billing Splits within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingSplitsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Billing Splits
    api_response = api_instance.get_billing_splits(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingSplitsApi->get_billing_splits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_split**
> InlineResponse20035 update_billing_split(id, limit=limit, page=page)

Update a Billing Splits

Returns the updated Billing Splits

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingSplitsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update a Billing Splits
    api_response = api_instance.update_billing_split(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingSplitsApi->update_billing_split: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_splits**
> InlineResponse20033 update_billing_splits(limit=limit, page=page)

Bulk Update Billing Splits

Returns a list of updated Billing Splits

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingSplitsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Bulk Update Billing Splits
    api_response = api_instance.update_billing_splits(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingSplitsApi->update_billing_splits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

