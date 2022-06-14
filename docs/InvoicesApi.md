# swagger_client.InvoicesApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_invoice_bulk_download**](InvoicesApi.md#filter_invoice_bulk_download) | **POST** /billing/invoices/download | Bulk Download Billing Invoices
[**filter_invoices**](InvoicesApi.md#filter_invoices) | **POST** /billing/invoices/filter | Filter all Invoices
[**get_invoice**](InvoicesApi.md#get_invoice) | **GET** /billing/invoices/{id} | Retrieve an Invoice
[**get_invoice_download_stream**](InvoicesApi.md#get_invoice_download_stream) | **POST** /billing/invoices/download/{id} | Retrieve a Invoices download stream
[**get_invoices**](InvoicesApi.md#get_invoices) | **GET** /billing/invoices | List all Invoices

# **filter_invoice_bulk_download**
> InlineResponse20027 filter_invoice_bulk_download(body=body, limit=limit, page=page)

Bulk Download Billing Invoices

Starts and returns a bulk download job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
body = swagger_client.InvoicesDownloadBody() # InvoicesDownloadBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Bulk Download Billing Invoices
    api_response = api_instance.filter_invoice_bulk_download(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->filter_invoice_bulk_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvoicesDownloadBody**](InvoicesDownloadBody.md)|  | [optional] 
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

# **filter_invoices**
> InlineResponse20026 filter_invoices(body=body, limit=limit, page=page)

Filter all Invoices

Returns a filtered list of Invoices

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
body = swagger_client.InvoicesFilterBody() # InvoicesFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Invoices
    api_response = api_instance.filter_invoices(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->filter_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvoicesFilterBody**](InvoicesFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice**
> InlineResponse20025 get_invoice(id, limit=limit, page=page)

Retrieve an Invoice

Returns an invoice based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve an Invoice
    api_response = api_instance.get_invoice(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_download_stream**
> str get_invoice_download_stream(body, id, limit=limit, page=page)

Retrieve a Invoices download stream

Return the PDF binary for a specified Invoice

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
body = swagger_client.DownloadIdBody() # DownloadIdBody | 
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Invoices download stream
    api_response = api_instance.get_invoice_download_stream(body, id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice_download_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DownloadIdBody**](DownloadIdBody.md)|  | 
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

# **get_invoices**
> InlineResponse20024 get_invoices(limit=limit, page=page)

List all Invoices

Returns a list of invoices within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Invoices
    api_response = api_instance.get_invoices(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

