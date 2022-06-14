# swagger_client.ReportSettingsApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_report_settings**](ReportSettingsApi.md#filter_report_settings) | **POST** /reporting/report-settings/filter | Filter all Report Settings
[**get_report_setting**](ReportSettingsApi.md#get_report_setting) | **GET** /reporting/report-settings/{id} | Retrieve Report Settings
[**get_report_settings**](ReportSettingsApi.md#get_report_settings) | **GET** /reporting/report-settings | List all Report Settings
[**update_report_setting**](ReportSettingsApi.md#update_report_setting) | **PUT** /reporting/report-settings/{id} | Update Report Settings
[**update_report_settings**](ReportSettingsApi.md#update_report_settings) | **PUT** /reporting/report-settings | Bulk Update Report Settings

# **filter_report_settings**
> InlineResponse20050 filter_report_settings(body=body, limit=limit, page=page)

Filter all Report Settings

Returns a filtered list of Report Settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportSettingsApi()
body = swagger_client.ReportsettingsFilterBody() # ReportsettingsFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Report Settings
    api_response = api_instance.filter_report_settings(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportSettingsApi->filter_report_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportsettingsFilterBody**](ReportsettingsFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_setting**
> InlineResponse20051 get_report_setting(id, limit=limit, page=page)

Retrieve Report Settings

Returns report settings based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportSettingsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve Report Settings
    api_response = api_instance.get_report_setting(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportSettingsApi->get_report_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_settings**
> InlineResponse20050 get_report_settings(limit=limit, page=page)

List all Report Settings

Returns a list of Report Settings within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportSettingsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Report Settings
    api_response = api_instance.get_report_settings(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportSettingsApi->get_report_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_setting**
> InlineResponse20051 update_report_setting(id, limit=limit, page=page)

Update Report Settings

Returns the updated Report Settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportSettingsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update Report Settings
    api_response = api_instance.update_report_setting(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportSettingsApi->update_report_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_settings**
> InlineResponse20050 update_report_settings(limit=limit, page=page)

Bulk Update Report Settings

Returns the updated Report Settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportSettingsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Bulk Update Report Settings
    api_response = api_instance.update_report_settings(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportSettingsApi->update_report_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

