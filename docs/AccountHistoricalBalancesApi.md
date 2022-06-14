# swagger_client.AccountHistoricalBalancesApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_historical_balance**](AccountHistoricalBalancesApi.md#get_account_historical_balance) | **GET** /data/luca/account-historical-balances/{id} | Retrieve an Account Historical Balance
[**get_account_historical_balances**](AccountHistoricalBalancesApi.md#get_account_historical_balances) | **GET** /data/luca/account-historical-balances | List all Account Historical Balances
[**get_account_historical_current_balances**](AccountHistoricalBalancesApi.md#get_account_historical_current_balances) | **GET** /data/luca/account-historical-balances/current | List all Current Luca Account Historical Balances

# **get_account_historical_balance**
> InlineResponse20085 get_account_historical_balance(id, limit=limit, page=page)

Retrieve an Account Historical Balance

Returns a single Account Historical Balance based on its ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountHistoricalBalancesApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve an Account Historical Balance
    api_response = api_instance.get_account_historical_balance(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountHistoricalBalancesApi->get_account_historical_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20085**](InlineResponse20085.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_historical_balances**
> InlineResponse20084 get_account_historical_balances(limit=limit, page=page)

List all Account Historical Balances

Returns a list of all Account Historical Balances

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountHistoricalBalancesApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Account Historical Balances
    api_response = api_instance.get_account_historical_balances(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountHistoricalBalancesApi->get_account_historical_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20084**](InlineResponse20084.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_historical_current_balances**
> InlineResponse20086 get_account_historical_current_balances(limit=limit, page=page)

List all Current Luca Account Historical Balances

Returns a list of Account Historical Balances

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountHistoricalBalancesApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Current Luca Account Historical Balances
    api_response = api_instance.get_account_historical_current_balances(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountHistoricalBalancesApi->get_account_historical_current_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20086**](InlineResponse20086.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

