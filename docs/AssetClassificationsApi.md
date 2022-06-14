# swagger_client.AssetClassificationsApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset_classifications**](AssetClassificationsApi.md#create_asset_classifications) | **POST** /reporting/asset-classifications | Create an Asset Classification
[**create_many_asset_classifications**](AssetClassificationsApi.md#create_many_asset_classifications) | **POST** /reporting/asset-classifications/create-many | Create Asset Classifications
[**detele_asset_classification**](AssetClassificationsApi.md#detele_asset_classification) | **DELETE** /reporting/asset-classifications/{id} | Delete an Asset Classification
[**detele_many_asset_classifications**](AssetClassificationsApi.md#detele_many_asset_classifications) | **POST** /reporting/asset-classifications/delete-many | Delete many Asset Classifications
[**filter_asset_classifications**](AssetClassificationsApi.md#filter_asset_classifications) | **POST** /reporting/asset-classifications/filter | Filter all Asset Classifications
[**get_asset_classification**](AssetClassificationsApi.md#get_asset_classification) | **GET** /reporting/asset-classifications/{id} | Retrieve an Asset Classification
[**get_asset_classifications**](AssetClassificationsApi.md#get_asset_classifications) | **GET** /reporting/asset-classifications | List all Asset Classifications
[**update_asset_classification**](AssetClassificationsApi.md#update_asset_classification) | **PUT** /reporting/asset-classifications/{id} | Update an Asset Classification
[**update_asset_classifications**](AssetClassificationsApi.md#update_asset_classifications) | **PUT** /reporting/asset-classifications | Bulk Update Asset Classifications

# **create_asset_classifications**
> InlineResponse20039 create_asset_classifications(body, limit=limit, page=page)

Create an Asset Classification

Returns the created asset classification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetClassificationsApi()
body = swagger_client.ReportingAssetclassificationsBody() # ReportingAssetclassificationsBody | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create an Asset Classification
    api_response = api_instance.create_asset_classifications(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetClassificationsApi->create_asset_classifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportingAssetclassificationsBody**](ReportingAssetclassificationsBody.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_many_asset_classifications**
> InlineResponse20038 create_many_asset_classifications(limit=limit, page=page)

Create Asset Classifications

Returns a list of created Asset Classifications

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetClassificationsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create Asset Classifications
    api_response = api_instance.create_many_asset_classifications(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetClassificationsApi->create_many_asset_classifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detele_asset_classification**
> detele_asset_classification(id, limit=limit, page=page)

Delete an Asset Classification

Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetClassificationsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete an Asset Classification
    api_instance.detele_asset_classification(id, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling AssetClassificationsApi->detele_asset_classification: %s\n" % e)
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

# **detele_many_asset_classifications**
> detele_many_asset_classifications(body, limit=limit, page=page)

Delete many Asset Classifications

Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetClassificationsApi()
body = NULL # object | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete many Asset Classifications
    api_instance.detele_many_asset_classifications(body, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling AssetClassificationsApi->detele_many_asset_classifications: %s\n" % e)
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

# **filter_asset_classifications**
> InlineResponse20038 filter_asset_classifications(body=body, limit=limit, page=page)

Filter all Asset Classifications

Returns a filtered list of Asset Classifications

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetClassificationsApi()
body = swagger_client.AssetclassificationsFilterBody() # AssetclassificationsFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Asset Classifications
    api_response = api_instance.filter_asset_classifications(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetClassificationsApi->filter_asset_classifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssetclassificationsFilterBody**](AssetclassificationsFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_classification**
> InlineResponse20039 get_asset_classification(id, limit=limit, page=page)

Retrieve an Asset Classification

Returns an asset classification based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetClassificationsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve an Asset Classification
    api_response = api_instance.get_asset_classification(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetClassificationsApi->get_asset_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_classifications**
> InlineResponse20038 get_asset_classifications(limit=limit, page=page)

List all Asset Classifications

Returns a list of asset classifications within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetClassificationsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Asset Classifications
    api_response = api_instance.get_asset_classifications(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetClassificationsApi->get_asset_classifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_classification**
> InlineResponse20039 update_asset_classification(id, limit=limit, page=page)

Update an Asset Classification

Returns the updated asset classification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetClassificationsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update an Asset Classification
    api_response = api_instance.update_asset_classification(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetClassificationsApi->update_asset_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_classifications**
> InlineResponse20039 update_asset_classifications(limit=limit, page=page)

Bulk Update Asset Classifications

Returns the updated asset classifications

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetClassificationsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Bulk Update Asset Classifications
    api_response = api_instance.update_asset_classifications(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetClassificationsApi->update_asset_classifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

