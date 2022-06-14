# swagger_client.PrintableReportsApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**detele_many_printable_reports**](PrintableReportsApi.md#detele_many_printable_reports) | **POST** /reporting/printable-reports/delete-manyr | Delete many Printable Reports
[**detele_printable_report**](PrintableReportsApi.md#detele_printable_report) | **DELETE** /reporting/printable-reports/{id} | Delete a Printable Report
[**filter_printable_report_bulk_download**](PrintableReportsApi.md#filter_printable_report_bulk_download) | **POST** /reporting/printable-reports/download | Bulk Download Printable PDFs
[**filter_printable_report_start_pdf**](PrintableReportsApi.md#filter_printable_report_start_pdf) | **POST** /reporting/printable-reports/create | Start a PDFReport Job
[**filter_printable_reports**](PrintableReportsApi.md#filter_printable_reports) | **POST** /reporting/printable-reports/filter | Filter all Printable Reports
[**get_printable_report**](PrintableReportsApi.md#get_printable_report) | **GET** /reporting/printable-reports/{id} | Retrieve a Printable Report
[**get_printable_report_download_stream**](PrintableReportsApi.md#get_printable_report_download_stream) | **POST** /reporting/printable-reports/download/{id} | Retrieve a Printable download stream
[**get_printable_reports**](PrintableReportsApi.md#get_printable_reports) | **GET** /reporting/printable-reports | List all Printable Reports

# **detele_many_printable_reports**
> detele_many_printable_reports(body, limit=limit, page=page)

Delete many Printable Reports

Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PrintableReportsApi()
body = NULL # object | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete many Printable Reports
    api_instance.detele_many_printable_reports(body, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling PrintableReportsApi->detele_many_printable_reports: %s\n" % e)
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

# **detele_printable_report**
> detele_printable_report(id, limit=limit, page=page)

Delete a Printable Report

Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PrintableReportsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete a Printable Report
    api_instance.detele_printable_report(id, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling PrintableReportsApi->detele_printable_report: %s\n" % e)
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

# **filter_printable_report_bulk_download**
> InlineResponse20027 filter_printable_report_bulk_download(body=body, limit=limit, page=page)

Bulk Download Printable PDFs

Starts and returns a bulk download job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PrintableReportsApi()
body = swagger_client.PrintablereportsDownloadBody() # PrintablereportsDownloadBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Bulk Download Printable PDFs
    api_response = api_instance.filter_printable_report_bulk_download(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrintableReportsApi->filter_printable_report_bulk_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrintablereportsDownloadBody**](PrintablereportsDownloadBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_printable_report_start_pdf**
> InlineResponse20027 filter_printable_report_start_pdf(body=body, limit=limit, page=page)

Start a PDFReport Job

Starts a Background Job for PDF Reporting and returns the created Background Job Instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PrintableReportsApi()
body = swagger_client.PrintablereportsCreateBody() # PrintablereportsCreateBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Start a PDFReport Job
    api_response = api_instance.filter_printable_report_start_pdf(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrintableReportsApi->filter_printable_report_start_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrintablereportsCreateBody**](PrintablereportsCreateBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_printable_reports**
> InlineResponse20049 filter_printable_reports(body=body, limit=limit, page=page)

Filter all Printable Reports

Returns a filtered list of Printable Reports

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PrintableReportsApi()
body = swagger_client.PrintablereportsFilterBody() # PrintablereportsFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Printable Reports
    api_response = api_instance.filter_printable_reports(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrintableReportsApi->filter_printable_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrintablereportsFilterBody**](PrintablereportsFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_printable_report**
> InlineResponse20048 get_printable_report(id, limit=limit, page=page)

Retrieve a Printable Report

Returns a Printable Report based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PrintableReportsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Printable Report
    api_response = api_instance.get_printable_report(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrintableReportsApi->get_printable_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_printable_report_download_stream**
> str get_printable_report_download_stream(body, id, limit=limit, page=page)

Retrieve a Printable download stream

Return the PDF binary for a specified Printable Report

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PrintableReportsApi()
body = swagger_client.DownloadIdBody1() # DownloadIdBody1 | 
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Printable download stream
    api_response = api_instance.get_printable_report_download_stream(body, id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrintableReportsApi->get_printable_report_download_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DownloadIdBody1**](DownloadIdBody1.md)|  | 
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

# **get_printable_reports**
> InlineResponse20047 get_printable_reports(limit=limit, page=page)

List all Printable Reports

Returns a list of Printable Reports within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PrintableReportsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Printable Reports
    api_response = api_instance.get_printable_reports(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrintableReportsApi->get_printable_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

