# swagger_client.BenchmarksApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_benchmarks**](BenchmarksApi.md#create_benchmarks) | **POST** /reporting/benchmarks | Create a Benchmark
[**create_many_benchmarks**](BenchmarksApi.md#create_many_benchmarks) | **POST** /reporting/benchmarks/create-many | Create Benchmarks
[**detele_benchmark**](BenchmarksApi.md#detele_benchmark) | **DELETE** /reporting/benchmarks/{id} | Delete a Benchmark
[**detele_many_benchmarks**](BenchmarksApi.md#detele_many_benchmarks) | **POST** /reporting/benchmarks/delete-many | Delete many Benchmarks
[**filter_benchmarks**](BenchmarksApi.md#filter_benchmarks) | **POST** /reporting/benchmarks/filter | Filter all Benchmarks
[**get_benchmark**](BenchmarksApi.md#get_benchmark) | **GET** /reporting/benchmarks/{id} | Retrieve a Benchmark
[**get_benchmarks**](BenchmarksApi.md#get_benchmarks) | **GET** /reporting/benchmarks | List all Benchmarks
[**update_benchmark**](BenchmarksApi.md#update_benchmark) | **PUT** /reporting/benchmarks/{id} | Update a Benchmark
[**update_benchmarks**](BenchmarksApi.md#update_benchmarks) | **PUT** /reporting/benchmarks | Bulk Update Benchmarks

# **create_benchmarks**
> InlineResponse2006 create_benchmarks(body, limit=limit, page=page)

Create a Benchmark

Returns the created Benchmark

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BenchmarksApi()
body = swagger_client.ReportingBenchmarksBody() # ReportingBenchmarksBody | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create a Benchmark
    api_response = api_instance.create_benchmarks(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BenchmarksApi->create_benchmarks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportingBenchmarksBody**](ReportingBenchmarksBody.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_many_benchmarks**
> InlineResponse20042 create_many_benchmarks(body, limit=limit, page=page)

Create Benchmarks

Returns a list of created Benchmarks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BenchmarksApi()
body = [swagger_client.Paths1reporting1benchmarkspostrequestBodycontentapplication1jsonschema()] # list[Paths1reporting1benchmarkspostrequestBodycontentapplication1jsonschema] | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create Benchmarks
    api_response = api_instance.create_many_benchmarks(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BenchmarksApi->create_many_benchmarks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Paths1reporting1benchmarkspostrequestBodycontentapplication1jsonschema]**](Paths1reporting1benchmarkspostrequestBodycontentapplication1jsonschema.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detele_benchmark**
> detele_benchmark(id, limit=limit, page=page)

Delete a Benchmark

Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BenchmarksApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete a Benchmark
    api_instance.detele_benchmark(id, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling BenchmarksApi->detele_benchmark: %s\n" % e)
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

# **detele_many_benchmarks**
> detele_many_benchmarks(body, limit=limit, page=page)

Delete many Benchmarks

Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BenchmarksApi()
body = NULL # object | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete many Benchmarks
    api_instance.detele_many_benchmarks(body, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling BenchmarksApi->detele_many_benchmarks: %s\n" % e)
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

# **filter_benchmarks**
> InlineResponse2006 filter_benchmarks(body=body, limit=limit, page=page)

Filter all Benchmarks

Returns a filtered list of Benchmarks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BenchmarksApi()
body = swagger_client.BenchmarksFilterBody() # BenchmarksFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Benchmarks
    api_response = api_instance.filter_benchmarks(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BenchmarksApi->filter_benchmarks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BenchmarksFilterBody**](BenchmarksFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_benchmark**
> InlineResponse2006 get_benchmark(id, limit=limit, page=page)

Retrieve a Benchmark

Returns a Benchmark based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BenchmarksApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Benchmark
    api_response = api_instance.get_benchmark(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BenchmarksApi->get_benchmark: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_benchmarks**
> InlineResponse20042 get_benchmarks(limit=limit, page=page)

List all Benchmarks

Returns a list of Benchmarks within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BenchmarksApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Benchmarks
    api_response = api_instance.get_benchmarks(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BenchmarksApi->get_benchmarks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_benchmark**
> InlineResponse2006 update_benchmark(id, limit=limit, page=page)

Update a Benchmark

Returns the updated Benchmark

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BenchmarksApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update a Benchmark
    api_response = api_instance.update_benchmark(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BenchmarksApi->update_benchmark: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_benchmarks**
> InlineResponse20042 update_benchmarks(limit=limit, page=page)

Bulk Update Benchmarks

Returns the updated Benchmarks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BenchmarksApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Bulk Update Benchmarks
    api_response = api_instance.update_benchmarks(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BenchmarksApi->update_benchmarks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

