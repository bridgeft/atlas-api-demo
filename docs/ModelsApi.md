# swagger_client.ModelsApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_many_models**](ModelsApi.md#create_many_models) | **POST** /investment-management/models/create-many | Create Models
[**create_models**](ModelsApi.md#create_models) | **POST** /investment-management/models | Create a Model
[**detele_many_models**](ModelsApi.md#detele_many_models) | **POST** /investment-management/models/delete-many | Delete many Models
[**detele_model**](ModelsApi.md#detele_model) | **DELETE** /investment-management/models/{id} | Delete a Model
[**filter_models**](ModelsApi.md#filter_models) | **POST** /investment-management/models/filter | Filter all Models
[**get_model**](ModelsApi.md#get_model) | **GET** /investment-management/models/{id} | Retrieve a Model
[**get_models**](ModelsApi.md#get_models) | **GET** /investment-management/models | List all Models
[**update_model**](ModelsApi.md#update_model) | **PUT** /investment-management/models/{id} | Update a Model
[**update_models**](ModelsApi.md#update_models) | **PUT** /investment-management/models | Bulk Update Models

# **create_many_models**
> InlineResponse200122 create_many_models(body, limit=limit, page=page)

Create Models

Returns a list of created Models

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ModelsApi()
body = [swagger_client.Paths1investmentManagement1modelspostrequestBodycontentapplication1jsonschema()] # list[Paths1investmentManagement1modelspostrequestBodycontentapplication1jsonschema] | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create Models
    api_response = api_instance.create_many_models(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->create_many_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Paths1investmentManagement1modelspostrequestBodycontentapplication1jsonschema]**](Paths1investmentManagement1modelspostrequestBodycontentapplication1jsonschema.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200122**](InlineResponse200122.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_models**
> InlineResponse200123 create_models(body, limit=limit, page=page)

Create a Model

Returns the created model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ModelsApi()
body = swagger_client.InvestmentmanagementModelsBody() # InvestmentmanagementModelsBody | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create a Model
    api_response = api_instance.create_models(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->create_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvestmentmanagementModelsBody**](InvestmentmanagementModelsBody.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200123**](InlineResponse200123.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detele_many_models**
> detele_many_models(body, limit=limit, page=page)

Delete many Models

Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ModelsApi()
body = NULL # object | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete many Models
    api_instance.detele_many_models(body, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling ModelsApi->detele_many_models: %s\n" % e)
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

# **detele_model**
> detele_model(id, limit=limit, page=page)

Delete a Model

Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ModelsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete a Model
    api_instance.detele_model(id, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling ModelsApi->detele_model: %s\n" % e)
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

# **filter_models**
> InlineResponse200122 filter_models(body=body, limit=limit, page=page)

Filter all Models

Returns a filtered list of Model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ModelsApi()
body = swagger_client.ModelsFilterBody() # ModelsFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Models
    api_response = api_instance.filter_models(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->filter_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelsFilterBody**](ModelsFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200122**](InlineResponse200122.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> InlineResponse200124 get_model(id, limit=limit, page=page)

Retrieve a Model

Returns a model based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ModelsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Model
    api_response = api_instance.get_model(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->get_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200124**](InlineResponse200124.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_models**
> InlineResponse200121 get_models(limit=limit, page=page)

List all Models

Returns a list of models within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ModelsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Models
    api_response = api_instance.get_models(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->get_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200121**](InlineResponse200121.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model**
> InlineResponse200124 update_model(id, limit=limit, page=page)

Update a Model

Returns the updated model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ModelsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update a Model
    api_response = api_instance.update_model(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->update_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200124**](InlineResponse200124.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_models**
> InlineResponse200122 update_models(limit=limit, page=page)

Bulk Update Models

Returns the updated models

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ModelsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Bulk Update Models
    api_response = api_instance.update_models(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->update_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200122**](InlineResponse200122.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

