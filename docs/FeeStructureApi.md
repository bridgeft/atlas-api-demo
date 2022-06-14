# swagger_client.FeeStructureApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fee_structures**](FeeStructureApi.md#create_fee_structures) | **POST** /billing/fee-structures | Create a Fee Structure
[**create_many_fee_structures**](FeeStructureApi.md#create_many_fee_structures) | **POST** /billing/fee-structures/create-many | Create Fee Structures
[**detele_fee_structure**](FeeStructureApi.md#detele_fee_structure) | **DELETE** /billing/fee-structures/{id} | Delete a Fee Structure
[**detele_many_fee_structures**](FeeStructureApi.md#detele_many_fee_structures) | **POST** /billing/fee-structures/delete-many | Delete many Fee Structures
[**filter_fee_structures**](FeeStructureApi.md#filter_fee_structures) | **POST** /billing/fee-structures/filter | Filter all Fee Structures
[**get_fee_structure**](FeeStructureApi.md#get_fee_structure) | **GET** /billing/fee-structures/{id} | Retrieve a Fee Structure
[**get_fee_structures**](FeeStructureApi.md#get_fee_structures) | **GET** /billing/fee-structures | List all Fee Structures
[**update_fee_structure**](FeeStructureApi.md#update_fee_structure) | **PUT** /billing/fee-structures/{id} | Update a Fee Structure
[**update_fee_structures**](FeeStructureApi.md#update_fee_structures) | **PUT** /billing/fee-structures | Bulk Update Fee Structures

# **create_fee_structures**
> InlineResponse20023 create_fee_structures(body, limit=limit, page=page)

Create a Fee Structure

Returns the created  Fee Structure

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeeStructureApi()
body = swagger_client.BillingFeestructuresBody() # BillingFeestructuresBody | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create a Fee Structure
    api_response = api_instance.create_fee_structures(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeeStructureApi->create_fee_structures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillingFeestructuresBody**](BillingFeestructuresBody.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_many_fee_structures**
> InlineResponse20022 create_many_fee_structures(limit=limit, page=page)

Create Fee Structures

Returns a list of created Fee Structures

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeeStructureApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create Fee Structures
    api_response = api_instance.create_many_fee_structures(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeeStructureApi->create_many_fee_structures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detele_fee_structure**
> detele_fee_structure(id, limit=limit, page=page)

Delete a Fee Structure

Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeeStructureApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete a Fee Structure
    api_instance.detele_fee_structure(id, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling FeeStructureApi->detele_fee_structure: %s\n" % e)
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

# **detele_many_fee_structures**
> detele_many_fee_structures(body, limit=limit, page=page)

Delete many Fee Structures

Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeeStructureApi()
body = NULL # object | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete many Fee Structures
    api_instance.detele_many_fee_structures(body, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling FeeStructureApi->detele_many_fee_structures: %s\n" % e)
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

# **filter_fee_structures**
> InlineResponse20022 filter_fee_structures(body=body, limit=limit, page=page)

Filter all Fee Structures

Returns a filtered list of Fee Structure

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeeStructureApi()
body = swagger_client.FeestructuresFilterBody() # FeestructuresFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Fee Structures
    api_response = api_instance.filter_fee_structures(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeeStructureApi->filter_fee_structures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeestructuresFilterBody**](FeestructuresFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fee_structure**
> InlineResponse20023 get_fee_structure(id, limit=limit, page=page)

Retrieve a Fee Structure

Returns a Fee Structure based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeeStructureApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Fee Structure
    api_response = api_instance.get_fee_structure(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeeStructureApi->get_fee_structure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fee_structures**
> InlineResponse20022 get_fee_structures(limit=limit, page=page)

List all Fee Structures

Returns a list of Fee Structures within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeeStructureApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Fee Structures
    api_response = api_instance.get_fee_structures(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeeStructureApi->get_fee_structures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fee_structure**
> InlineResponse20023 update_fee_structure(id, limit=limit, page=page)

Update a Fee Structure

Returns the updated Fee Structure

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeeStructureApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update a Fee Structure
    api_response = api_instance.update_fee_structure(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeeStructureApi->update_fee_structure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fee_structures**
> InlineResponse20022 update_fee_structures(limit=limit, page=page)

Bulk Update Fee Structures

Returns the updated Fee Structures

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeeStructureApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Bulk Update Fee Structures
    api_response = api_instance.update_fee_structures(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeeStructureApi->update_fee_structures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

