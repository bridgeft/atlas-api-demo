# swagger_client.HouseholdHistoricalBalancesApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_household_historical_balances**](HouseholdHistoricalBalancesApi.md#get_household_historical_balances) | **POST** /data/luca/household-historical-balances | List multiple Household Historical Balances

# **get_household_historical_balances**
> InlineResponse20087 get_household_historical_balances(body)

List multiple Household Historical Balances

Returns a list of Household Historical Balances

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HouseholdHistoricalBalancesApi()
body = swagger_client.LucaHouseholdhistoricalbalancesBody() # LucaHouseholdhistoricalbalancesBody | 

try:
    # List multiple Household Historical Balances
    api_response = api_instance.get_household_historical_balances(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HouseholdHistoricalBalancesApi->get_household_historical_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LucaHouseholdhistoricalbalancesBody**](LucaHouseholdhistoricalbalancesBody.md)|  | 

### Return type

[**InlineResponse20087**](InlineResponse20087.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

