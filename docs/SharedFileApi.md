# swagger_client.SharedFileApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file**](SharedFileApi.md#create_file) | **POST** /file-sharing/files | Create a Shared File
[**detele_file**](SharedFileApi.md#detele_file) | **DELETE** /file-sharing/files/{id} | Delete a Shared File
[**filter_files**](SharedFileApi.md#filter_files) | **POST** /file-sharing/files/filter | Filter all Shared Files
[**get_file**](SharedFileApi.md#get_file) | **GET** /file-sharing/files/{id} | Retrieve a Shared File
[**get_file_download_stream**](SharedFileApi.md#get_file_download_stream) | **POST** /file-sharing/files/download/{id} | Retrieve a Shared File download stream
[**get_files**](SharedFileApi.md#get_files) | **GET** /file-sharing/files | List all Shared Files
[**read_upload_files**](SharedFileApi.md#read_upload_files) | **POST** /file-sharing/files/upload | Upload Shared Files

# **create_file**
> InlineResponse200118 create_file(body, limit=limit, page=page)

Create a Shared File

Returns the created Shared File

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SharedFileApi()
body = swagger_client.FilesharingFilesBody() # FilesharingFilesBody | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create a Shared File
    api_response = api_instance.create_file(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedFileApi->create_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FilesharingFilesBody**](FilesharingFilesBody.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200118**](InlineResponse200118.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detele_file**
> detele_file(id, limit=limit, page=page)

Delete a Shared File

Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SharedFileApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete a Shared File
    api_instance.detele_file(id, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling SharedFileApi->detele_file: %s\n" % e)
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

# **filter_files**
> InlineResponse200120 filter_files(body=body, limit=limit, page=page)

Filter all Shared Files

Returns a filtered list of Shared Files

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SharedFileApi()
body = swagger_client.FilesFilterBody() # FilesFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Shared Files
    api_response = api_instance.filter_files(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedFileApi->filter_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FilesFilterBody**](FilesFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200120**](InlineResponse200120.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> InlineResponse200119 get_file(id, limit=limit, page=page)

Retrieve a Shared File

Returns an shared file based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SharedFileApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Shared File
    api_response = api_instance.get_file(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedFileApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200119**](InlineResponse200119.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_download_stream**
> str get_file_download_stream(body, id, limit=limit, page=page)

Retrieve a Shared File download stream

Return the PDF binary for a specified Shared File

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SharedFileApi()
body = swagger_client.DownloadIdBody2() # DownloadIdBody2 | 
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Shared File download stream
    api_response = api_instance.get_file_download_stream(body, id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedFileApi->get_file_download_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DownloadIdBody2**](DownloadIdBody2.md)|  | 
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files**
> InlineResponse200117 get_files(limit=limit, page=page)

List all Shared Files

Returns a list of Shared Files within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SharedFileApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Shared Files
    api_response = api_instance.get_files(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedFileApi->get_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200117**](InlineResponse200117.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_upload_files**
> InlineResponse200120 read_upload_files(body, limit=limit, page=page)

Upload Shared Files

Uploads Shared Files and returns the list of upload files

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SharedFileApi()
body = swagger_client.FilesUploadBody() # FilesUploadBody | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Upload Shared Files
    api_response = api_instance.read_upload_files(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedFileApi->read_upload_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FilesUploadBody**](FilesUploadBody.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200120**](InlineResponse200120.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

