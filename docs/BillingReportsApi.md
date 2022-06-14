# swagger_client.BillingReportsApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**detele_billing_report**](BillingReportsApi.md#detele_billing_report) | **DELETE** /billing/reports/{id} | Delete a Billing Report
[**detele_many_billing_reports**](BillingReportsApi.md#detele_many_billing_reports) | **POST** /billing/reports/delete-many | Delete many Billing Reports
[**filter_billing_reports**](BillingReportsApi.md#filter_billing_reports) | **POST** /billing/reports/filter | Filter all Billing Reports
[**get_billing_report**](BillingReportsApi.md#get_billing_report) | **GET** /billing/reports/{id} | Retrieve a Billing Report
[**get_billing_reports**](BillingReportsApi.md#get_billing_reports) | **GET** /billing/reports | List all Billing Reports
[**start_billing_report_start_pdf**](BillingReportsApi.md#start_billing_report_start_pdf) | **POST** /billing/reports | Start a Billing Job

# **detele_billing_report**
> detele_billing_report(id, limit=limit, page=page)

Delete a Billing Report

Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingReportsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete a Billing Report
    api_instance.detele_billing_report(id, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling BillingReportsApi->detele_billing_report: %s\n" % e)
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

# **detele_many_billing_reports**
> detele_many_billing_reports(body, limit=limit, page=page)

Delete many Billing Reports

Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingReportsApi()
body = NULL # object | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete many Billing Reports
    api_instance.detele_many_billing_reports(body, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling BillingReportsApi->detele_many_billing_reports: %s\n" % e)
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

# **filter_billing_reports**
> InlineResponse20030 filter_billing_reports(body=body, limit=limit, page=page)

Filter all Billing Reports

Returns a filtered list of Billing Reports

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingReportsApi()
body = swagger_client.ReportsFilterBody() # ReportsFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Billing Reports
    api_response = api_instance.filter_billing_reports(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingReportsApi->filter_billing_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportsFilterBody**](ReportsFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_report**
> InlineResponse20029 get_billing_report(id, limit=limit, page=page)

Retrieve a Billing Report

Returns a Billing Report based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingReportsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Billing Report
    api_response = api_instance.get_billing_report(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingReportsApi->get_billing_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_reports**
> InlineResponse20028 get_billing_reports(limit=limit, page=page)

List all Billing Reports

Returns a list of Billing Reports within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingReportsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Billing Reports
    api_response = api_instance.get_billing_reports(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingReportsApi->get_billing_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_billing_report_start_pdf**
> InlineResponse20027 start_billing_report_start_pdf(body=body, limit=limit, page=page)

Start a Billing Job

Starts a Billing Job with PDF Reporting and returns the created Background Job Instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingReportsApi()
body = swagger_client.BillingReportsBody() # BillingReportsBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Start a Billing Job
    api_response = api_instance.start_billing_report_start_pdf(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingReportsApi->start_billing_report_start_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillingReportsBody**](BillingReportsBody.md)|  | [optional] 
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

