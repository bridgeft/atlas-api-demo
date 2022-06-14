# swagger_client.HouseholdsApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_households**](HouseholdsApi.md#filter_households) | **POST** /reporting/households/filter | Filter all Households
[**get_household**](HouseholdsApi.md#get_household) | **GET** /reporting/households/{id} | Retrieve a Household
[**get_households**](HouseholdsApi.md#get_households) | **GET** /reporting/households | List all Households
[**read_updated_household**](HouseholdsApi.md#read_updated_household) | **PUT** /reporting/households/{id} | Update a Household
[**read_updated_households**](HouseholdsApi.md#read_updated_households) | **PUT** /reporting/households | Update Households

# **filter_households**
> InlineResponse20036 filter_households(body=body, limit=limit, page=page)

Filter all Households

Return a filtered list of all Households

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HouseholdsApi()
body = swagger_client.HouseholdsFilterBody() # HouseholdsFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Households
    api_response = api_instance.filter_households(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HouseholdsApi->filter_households: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HouseholdsFilterBody**](HouseholdsFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_household**
> InlineResponse20037 get_household(id, limit=limit, page=page)

Retrieve a Household

Returns a household based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HouseholdsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Household
    api_response = api_instance.get_household(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HouseholdsApi->get_household: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_households**
> InlineResponse20036 get_households(limit=limit, page=page)

List all Households

Returns a list of households within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HouseholdsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Households
    api_response = api_instance.get_households(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HouseholdsApi->get_households: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_updated_household**
> InlineResponse20037 read_updated_household(id, limit=limit, page=page)

Update a Household

Returns an updated household

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HouseholdsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update a Household
    api_response = api_instance.read_updated_household(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HouseholdsApi->read_updated_household: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_updated_households**
> InlineResponse20036 read_updated_households(limit=limit, page=page)

Update Households

Returns a list of updated households

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HouseholdsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update Households
    api_response = api_instance.read_updated_households(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HouseholdsApi->read_updated_households: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

