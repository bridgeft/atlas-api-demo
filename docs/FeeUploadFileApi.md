# swagger_client.FeeUploadFileApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_fee_upload**](FeeUploadFileApi.md#filter_fee_upload) | **POST** /billing/fee-upload-files/filter | Filter all Fee Upload Files
[**get_fee_upload**](FeeUploadFileApi.md#get_fee_upload) | **GET** /billing/fee-upload-files/{id} | Retrieve a Fee Upload File
[**get_fee_upload_download**](FeeUploadFileApi.md#get_fee_upload_download) | **POST** /billing/fee-upload-files/download/{id} | Retrieve a Fee Upload File download
[**get_fee_uploads**](FeeUploadFileApi.md#get_fee_uploads) | **GET** /billing/fee-upload-files | List all Fee Upload Files

# **filter_fee_upload**
> InlineResponse20020 filter_fee_upload(body=body, limit=limit, page=page)

Filter all Fee Upload Files

Returns a filtered list of Fee Upload Files

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeeUploadFileApi()
body = swagger_client.FeeuploadfilesFilterBody() # FeeuploadfilesFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Fee Upload Files
    api_response = api_instance.filter_fee_upload(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeeUploadFileApi->filter_fee_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeeuploadfilesFilterBody**](FeeuploadfilesFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fee_upload**
> InlineResponse20019 get_fee_upload(id, limit=limit, page=page)

Retrieve a Fee Upload File

Returns a fee upload file based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeeUploadFileApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Fee Upload File
    api_response = api_instance.get_fee_upload(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeeUploadFileApi->get_fee_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fee_upload_download**
> InlineResponse20021 get_fee_upload_download(id, limit=limit, page=page)

Retrieve a Fee Upload File download

Returns a fee upload file based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeeUploadFileApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Fee Upload File download
    api_response = api_instance.get_fee_upload_download(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeeUploadFileApi->get_fee_upload_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fee_uploads**
> InlineResponse20018 get_fee_uploads(limit=limit, page=page)

List all Fee Upload Files

Returns a list of fee upload files within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeeUploadFileApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Fee Upload Files
    api_response = api_instance.get_fee_uploads(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeeUploadFileApi->get_fee_uploads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

