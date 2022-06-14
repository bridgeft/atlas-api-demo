# swagger_client.AccountBalancesApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_balance**](AccountBalancesApi.md#get_account_balance) | **GET** /data/luca/account-balances/{id} | Retrieve an Account Balance
[**get_account_balances**](AccountBalancesApi.md#get_account_balances) | **GET** /data/luca/account-balances | List all Account Balances
[**get_account_current_balances**](AccountBalancesApi.md#get_account_current_balances) | **GET** /data/luca/account-balances/current | List all Current Luca Account Balances

# **get_account_balance**
> InlineResponse20080 get_account_balance(id, limit=limit, page=page)

Retrieve an Account Balance

Returns a single Account Balance based on its ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountBalancesApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve an Account Balance
    api_response = api_instance.get_account_balance(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountBalancesApi->get_account_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20080**](InlineResponse20080.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_balances**
> InlineResponse20079 get_account_balances(limit=limit, page=page)

List all Account Balances

Returns a list of all Account Balances

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountBalancesApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Account Balances
    api_response = api_instance.get_account_balances(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountBalancesApi->get_account_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20079**](InlineResponse20079.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_current_balances**
> InlineResponse20081 get_account_current_balances(limit=limit, page=page)

List all Current Luca Account Balances

Returns a list of Account Balances

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountBalancesApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Current Luca Account Balances
    api_response = api_instance.get_account_current_balances(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountBalancesApi->get_account_current_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20081**](InlineResponse20081.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

