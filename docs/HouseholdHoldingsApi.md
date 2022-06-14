# swagger_client.HouseholdHoldingsApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_household_holdings**](HouseholdHoldingsApi.md#get_household_holdings) | **POST** /data/luca/household-holdings | List multiple Household Holdings records

# **get_household_holdings**
> InlineResponse20072 get_household_holdings(body)

List multiple Household Holdings records

Returns a list of Household Holdings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HouseholdHoldingsApi()
body = swagger_client.LucaHouseholdholdingsBody() # LucaHouseholdholdingsBody | 

try:
    # List multiple Household Holdings records
    api_response = api_instance.get_household_holdings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HouseholdHoldingsApi->get_household_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LucaHouseholdholdingsBody**](LucaHouseholdholdingsBody.md)|  | 

### Return type

[**InlineResponse20072**](InlineResponse20072.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

