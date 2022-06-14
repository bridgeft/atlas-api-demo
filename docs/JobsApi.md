# swagger_client.JobsApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_jobs**](JobsApi.md#clear_jobs) | **POST** /jobs/clear | Clear a Job
[**filter_jobs**](JobsApi.md#filter_jobs) | **POST** /jobs/filter | Filter all Jobs
[**get_job**](JobsApi.md#get_job) | **GET** /jobs/{id} | Retrieve a Job
[**get_jobs**](JobsApi.md#get_jobs) | **GET** /jobs/ | List all Jobs

# **clear_jobs**
> InlineResponse20055 clear_jobs(limit=limit, page=page)

Clear a Job

Deletes the Background Jobs associated with the user's profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Clear a Job
    api_response = api_instance.clear_jobs(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->clear_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_jobs**
> InlineResponse20054 filter_jobs(body=body, limit=limit, page=page)

Filter all Jobs

Return a filtered list of all Jobs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
body = swagger_client.JobsFilterBody() # JobsFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Jobs
    api_response = api_instance.filter_jobs(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->filter_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobsFilterBody**](JobsFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> InlineResponse20027 get_job(id, limit=limit, page=page)

Retrieve a Job

Returns a Job based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Job
    api_response = api_instance.get_job(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs**
> InlineResponse20054 get_jobs(limit=limit, page=page)

List all Jobs

Returns a list of jobs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Jobs
    api_response = api_instance.get_jobs(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->get_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

