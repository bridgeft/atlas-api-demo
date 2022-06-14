# swagger_client.StrategiesApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_many_strategies**](StrategiesApi.md#create_many_strategies) | **POST** /investment-management/strategies/create-many | Create strategies
[**create_strategies**](StrategiesApi.md#create_strategies) | **POST** /investment-management/strategies | Create a Strategy
[**detele_many_strategies**](StrategiesApi.md#detele_many_strategies) | **POST** /investment-management/strategies/delete-many | Delete many Strategies
[**detele_strategy**](StrategiesApi.md#detele_strategy) | **DELETE** /investment-management/strategies/{id} | Delete a Strategy
[**filter_strategies**](StrategiesApi.md#filter_strategies) | **POST** /investment-management/strategies/filter | Filter all Strategies
[**get_strategies**](StrategiesApi.md#get_strategies) | **GET** /investment-management/strategies | List all Strategies
[**get_strategy**](StrategiesApi.md#get_strategy) | **GET** /investment-management/strategies/{id} | Retrieve a Strategy
[**update_strategies**](StrategiesApi.md#update_strategies) | **PUT** /investment-management/strategies | Bulk Update Strategies
[**update_strategy**](StrategiesApi.md#update_strategy) | **PUT** /investment-management/strategies/{id} | Update a Strategy

# **create_many_strategies**
> InlineResponse200126 create_many_strategies(body, limit=limit, page=page)

Create strategies

Returns a list of created strategies

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StrategiesApi()
body = [swagger_client.Paths1investmentManagement1strategiespostrequestBodycontentapplication1jsonschema()] # list[Paths1investmentManagement1strategiespostrequestBodycontentapplication1jsonschema] | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create strategies
    api_response = api_instance.create_many_strategies(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategiesApi->create_many_strategies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Paths1investmentManagement1strategiespostrequestBodycontentapplication1jsonschema]**](Paths1investmentManagement1strategiespostrequestBodycontentapplication1jsonschema.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200126**](InlineResponse200126.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_strategies**
> InlineResponse200127 create_strategies(body, limit=limit, page=page)

Create a Strategy

Returns the created strategy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StrategiesApi()
body = swagger_client.InvestmentmanagementStrategiesBody() # InvestmentmanagementStrategiesBody | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create a Strategy
    api_response = api_instance.create_strategies(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategiesApi->create_strategies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvestmentmanagementStrategiesBody**](InvestmentmanagementStrategiesBody.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200127**](InlineResponse200127.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detele_many_strategies**
> detele_many_strategies(body, limit=limit, page=page)

Delete many Strategies

Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StrategiesApi()
body = NULL # object | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete many Strategies
    api_instance.detele_many_strategies(body, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling StrategiesApi->detele_many_strategies: %s\n" % e)
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

# **detele_strategy**
> detele_strategy(id, limit=limit, page=page)

Delete a Strategy

Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StrategiesApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete a Strategy
    api_instance.detele_strategy(id, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling StrategiesApi->detele_strategy: %s\n" % e)
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

# **filter_strategies**
> InlineResponse200126 filter_strategies(body=body, limit=limit, page=page)

Filter all Strategies

Returns a filtered list of Strategy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StrategiesApi()
body = swagger_client.StrategiesFilterBody() # StrategiesFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Strategies
    api_response = api_instance.filter_strategies(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategiesApi->filter_strategies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StrategiesFilterBody**](StrategiesFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200126**](InlineResponse200126.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_strategies**
> InlineResponse200125 get_strategies(limit=limit, page=page)

List all Strategies

Returns a list of strategies within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StrategiesApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Strategies
    api_response = api_instance.get_strategies(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategiesApi->get_strategies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200125**](InlineResponse200125.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_strategy**
> InlineResponse200128 get_strategy(id, limit=limit, page=page)

Retrieve a Strategy

Returns a strategy based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StrategiesApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Strategy
    api_response = api_instance.get_strategy(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategiesApi->get_strategy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200128**](InlineResponse200128.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_strategies**
> InlineResponse200126 update_strategies(limit=limit, page=page)

Bulk Update Strategies

Returns the updated strategies

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StrategiesApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Bulk Update Strategies
    api_response = api_instance.update_strategies(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategiesApi->update_strategies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200126**](InlineResponse200126.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_strategy**
> InlineResponse200128 update_strategy(id, limit=limit, page=page)

Update a Strategy

Returns the updated strategy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StrategiesApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update a Strategy
    api_response = api_instance.update_strategy(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategiesApi->update_strategy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200128**](InlineResponse200128.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

