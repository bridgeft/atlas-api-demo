# swagger_client.SecuritiesApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_securities**](SecuritiesApi.md#filter_securities) | **POST** /data/custodian/securities/filter | Filter all Securities
[**get_securities**](SecuritiesApi.md#get_securities) | **GET** /data/custodian/securities | List all Securities
[**get_security**](SecuritiesApi.md#get_security) | **GET** /data/custodian/securities/{id} | Retrieve a Security
[**get_security_compressed**](SecuritiesApi.md#get_security_compressed) | **GET** /data/custodian/securities/get-compressed | Get compressed Securities
[**get_security_fetch**](SecuritiesApi.md#get_security_fetch) | **POST** /data/custodian/securities/fetch | Fetch Securities
[**get_security_managed**](SecuritiesApi.md#get_security_managed) | **GET** /data/custodian/securities/managed | Get managed Securities
[**get_security_search**](SecuritiesApi.md#get_security_search) | **GET** /data/custodian/securities/search/{q} | Search for Securities
[**get_security_usd**](SecuritiesApi.md#get_security_usd) | **GET** /data/custodian/securities/get-usd | Get Security with USD

# **filter_securities**
> InlineResponse200112 filter_securities(body=body, limit=limit, page=page)

Filter all Securities

Returns a filtered list of Securities

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecuritiesApi()
body = swagger_client.SecuritiesFilterBody() # SecuritiesFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Securities
    api_response = api_instance.filter_securities(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecuritiesApi->filter_securities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecuritiesFilterBody**](SecuritiesFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200112**](InlineResponse200112.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_securities**
> InlineResponse200110 get_securities(limit=limit, page=page)

List all Securities

Returns a list of securities

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecuritiesApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Securities
    api_response = api_instance.get_securities(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecuritiesApi->get_securities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200110**](InlineResponse200110.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security**
> InlineResponse200111 get_security(id, limit=limit, page=page)

Retrieve a Security

Returns a single  security based on an ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecuritiesApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Security
    api_response = api_instance.get_security(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecuritiesApi->get_security: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200111**](InlineResponse200111.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_compressed**
> str get_security_compressed(limit=limit, page=page)

Get compressed Securities

Returns compressed and modified representations of all Securities that are being tracked

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecuritiesApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Get compressed Securities
    api_response = api_instance.get_security_compressed(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecuritiesApi->get_security_compressed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_fetch**
> InlineResponse200112 get_security_fetch(body, limit=limit, page=page)

Fetch Securities

Returns a list of securities based on the ids passed in

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecuritiesApi()
body = swagger_client.SecuritiesFetchBody() # SecuritiesFetchBody | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Fetch Securities
    api_response = api_instance.get_security_fetch(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecuritiesApi->get_security_fetch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecuritiesFetchBody**](SecuritiesFetchBody.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200112**](InlineResponse200112.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_managed**
> list[int] get_security_managed(limit=limit, page=page)

Get managed Securities

Returns a list of security ids that belong to the user's household and firm

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecuritiesApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Get managed Securities
    api_response = api_instance.get_security_managed(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecuritiesApi->get_security_managed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

**list[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_search**
> InlineResponse200111 get_security_search(q, limit=limit, page=page)

Search for Securities

Returns modified representations of Securities based on input parameters used for filtering

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecuritiesApi()
q = 'q_example' # str | The symbol or description of a Security to filter by
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Search for Securities
    api_response = api_instance.get_security_search(q, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecuritiesApi->get_security_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The symbol or description of a Security to filter by | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200111**](InlineResponse200111.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_usd**
> InlineResponse200113 get_security_usd(limit=limit, page=page)

Get Security with USD

Returns the first security object where the issue_type_code is 1

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecuritiesApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Get Security with USD
    api_response = api_instance.get_security_usd(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecuritiesApi->get_security_usd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200113**](InlineResponse200113.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

