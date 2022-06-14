# swagger_client.HouseholdBalancesApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_household_balances**](HouseholdBalancesApi.md#get_household_balances) | **POST** /data/luca/household-balances | List multiple Household Balances records
[**get_household_current_balances**](HouseholdBalancesApi.md#get_household_current_balances) | **GET** /data/luca/household-balances/current | List all Current Luca Household Balances

# **get_household_balances**
> InlineResponse20082 get_household_balances(body)

List multiple Household Balances records

Returns a list of Household Balances

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HouseholdBalancesApi()
body = swagger_client.LucaHouseholdbalancesBody() # LucaHouseholdbalancesBody | 

try:
    # List multiple Household Balances records
    api_response = api_instance.get_household_balances(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HouseholdBalancesApi->get_household_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LucaHouseholdbalancesBody**](LucaHouseholdbalancesBody.md)|  | 

### Return type

[**InlineResponse20082**](InlineResponse20082.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_household_current_balances**
> InlineResponse20083 get_household_current_balances()

List all Current Luca Household Balances

Returns a list of Household Balances

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HouseholdBalancesApi()

try:
    # List all Current Luca Household Balances
    api_response = api_instance.get_household_current_balances()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HouseholdBalancesApi->get_household_current_balances: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20083**](InlineResponse20083.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

