# swagger_client.HouseholdSecurityBalancesApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_household_security_balances**](HouseholdSecurityBalancesApi.md#get_household_security_balances) | **POST** /data/luca/household-security-balances | List mulitple Household Security Balances records

# **get_household_security_balances**
> InlineResponse20068 get_household_security_balances(body)

List mulitple Household Security Balances records

Returns a list of Household Security Balances

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HouseholdSecurityBalancesApi()
body = swagger_client.LucaHouseholdsecuritybalancesBody() # LucaHouseholdsecuritybalancesBody | 

try:
    # List mulitple Household Security Balances records
    api_response = api_instance.get_household_security_balances(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HouseholdSecurityBalancesApi->get_household_security_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LucaHouseholdsecuritybalancesBody**](LucaHouseholdsecuritybalancesBody.md)|  | 

### Return type

[**InlineResponse20068**](InlineResponse20068.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

