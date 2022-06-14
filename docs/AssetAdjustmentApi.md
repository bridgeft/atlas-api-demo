# swagger_client.AssetAdjustmentApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset_adjustments**](AssetAdjustmentApi.md#create_asset_adjustments) | **POST** /billing/asset-adjustments | Create an Asset Adjustment
[**create_many_asset_adjustments**](AssetAdjustmentApi.md#create_many_asset_adjustments) | **POST** /billing/asset-adjustments/create-many | Create Asset Adjustments
[**detele_asset_adjustment**](AssetAdjustmentApi.md#detele_asset_adjustment) | **DELETE** /billing/asset-adjustments/{id} | Delete an Asset Adjustment
[**detele_many_asset_adjustments**](AssetAdjustmentApi.md#detele_many_asset_adjustments) | **POST** /billing/asset-adjustments/delete-many | Delete many Asset Adjustments
[**filter_billing_asset_adjustment**](AssetAdjustmentApi.md#filter_billing_asset_adjustment) | **POST** /billing/asset-adjustments/filter | Filter all Asset Adjustment
[**get_asset_adjustment**](AssetAdjustmentApi.md#get_asset_adjustment) | **GET** /billing/asset-adjustments/{id} | Retrieve an Asset Adjustment
[**get_asset_adjustments**](AssetAdjustmentApi.md#get_asset_adjustments) | **GET** /billing/asset-adjustments | List all Asset Adjustments
[**update_asset_adjustment**](AssetAdjustmentApi.md#update_asset_adjustment) | **PUT** /billing/asset-adjustments/{id} | Update an Asset Adjustment
[**update_asset_adjustments**](AssetAdjustmentApi.md#update_asset_adjustments) | **PUT** /billing/asset-adjustments | Bulk Update Asset Adjustments

# **create_asset_adjustments**
> InlineResponse20017 create_asset_adjustments(body, limit=limit, page=page)

Create an Asset Adjustment

Returns a created Asset Adjustment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdjustmentApi()
body = swagger_client.BillingAssetadjustmentsBody() # BillingAssetadjustmentsBody | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create an Asset Adjustment
    api_response = api_instance.create_asset_adjustments(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdjustmentApi->create_asset_adjustments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillingAssetadjustmentsBody**](BillingAssetadjustmentsBody.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_many_asset_adjustments**
> InlineResponse20016 create_many_asset_adjustments(limit=limit, page=page)

Create Asset Adjustments

Returns the created Asset Adjustment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdjustmentApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create Asset Adjustments
    api_response = api_instance.create_many_asset_adjustments(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdjustmentApi->create_many_asset_adjustments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detele_asset_adjustment**
> detele_asset_adjustment(id, limit=limit, page=page)

Delete an Asset Adjustment

Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdjustmentApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete an Asset Adjustment
    api_instance.detele_asset_adjustment(id, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling AssetAdjustmentApi->detele_asset_adjustment: %s\n" % e)
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

# **detele_many_asset_adjustments**
> detele_many_asset_adjustments(body, limit=limit, page=page)

Delete many Asset Adjustments

Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdjustmentApi()
body = NULL # object | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete many Asset Adjustments
    api_instance.detele_many_asset_adjustments(body, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling AssetAdjustmentApi->detele_many_asset_adjustments: %s\n" % e)
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

# **filter_billing_asset_adjustment**
> InlineResponse20016 filter_billing_asset_adjustment(body=body, limit=limit, page=page)

Filter all Asset Adjustment

Returns a filtered list of Asset Adjustment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdjustmentApi()
body = swagger_client.AssetadjustmentsFilterBody() # AssetadjustmentsFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Asset Adjustment
    api_response = api_instance.filter_billing_asset_adjustment(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdjustmentApi->filter_billing_asset_adjustment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssetadjustmentsFilterBody**](AssetadjustmentsFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_adjustment**
> InlineResponse20017 get_asset_adjustment(id, limit=limit, page=page)

Retrieve an Asset Adjustment

Returns an Asset Adjustment based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdjustmentApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve an Asset Adjustment
    api_response = api_instance.get_asset_adjustment(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdjustmentApi->get_asset_adjustment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_adjustments**
> InlineResponse20016 get_asset_adjustments(limit=limit, page=page)

List all Asset Adjustments

Returns a list of Asset Adjustments within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdjustmentApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Asset Adjustments
    api_response = api_instance.get_asset_adjustments(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdjustmentApi->get_asset_adjustments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_adjustment**
> InlineResponse20017 update_asset_adjustment(id, limit=limit, page=page)

Update an Asset Adjustment

Returns the updated Asset Adjustment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdjustmentApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update an Asset Adjustment
    api_response = api_instance.update_asset_adjustment(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdjustmentApi->update_asset_adjustment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_adjustments**
> InlineResponse20016 update_asset_adjustments(limit=limit, page=page)

Bulk Update Asset Adjustments

Returns the updated Asset Adjustments

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdjustmentApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Bulk Update Asset Adjustments
    api_response = api_instance.update_asset_adjustments(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdjustmentApi->update_asset_adjustments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

