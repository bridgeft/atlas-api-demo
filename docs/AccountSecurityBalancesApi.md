# swagger_client.AccountSecurityBalancesApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_account_security_balances**](AccountSecurityBalancesApi.md#filter_account_security_balances) | **POST** /data/luca/account-security-balances/filter | Filter all Account Security Balances records
[**get_account_security_balance**](AccountSecurityBalancesApi.md#get_account_security_balance) | **GET** /data/luca/account-security-balances/{id} | Retrieve an Account Security Balance record
[**get_account_security_balances**](AccountSecurityBalancesApi.md#get_account_security_balances) | **GET** /data/luca/account-security-balances | List all Account Security Balances records

# **filter_account_security_balances**
> InlineResponse20067 filter_account_security_balances(body=body, limit=limit, page=page)

Filter all Account Security Balances records

Returns a filtered list of Account Security Balances records

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountSecurityBalancesApi()
body = swagger_client.AccountsecuritybalancesFilterBody() # AccountsecuritybalancesFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Account Security Balances records
    api_response = api_instance.filter_account_security_balances(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountSecurityBalancesApi->filter_account_security_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountsecuritybalancesFilterBody**](AccountsecuritybalancesFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20067**](InlineResponse20067.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_security_balance**
> InlineResponse20066 get_account_security_balance(id, limit=limit, page=page)

Retrieve an Account Security Balance record

Returns a Account Security Balance record based on its ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountSecurityBalancesApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve an Account Security Balance record
    api_response = api_instance.get_account_security_balance(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountSecurityBalancesApi->get_account_security_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20066**](InlineResponse20066.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_security_balances**
> InlineResponse20065 get_account_security_balances(limit=limit, page=page)

List all Account Security Balances records

Returns a list of Account Security Balances

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountSecurityBalancesApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Account Security Balances records
    api_response = api_instance.get_account_security_balances(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountSecurityBalancesApi->get_account_security_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20065**](InlineResponse20065.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

