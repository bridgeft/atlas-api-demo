# swagger_client.HeldawayInvestmentTransactionsApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_heldaway_investments**](HeldawayInvestmentTransactionsApi.md#filter_heldaway_investments) | **POST** /heldaway/investment-transactions/filter | Filter all Heldaway Transactions
[**get_heldaway_investment**](HeldawayInvestmentTransactionsApi.md#get_heldaway_investment) | **GET** /heldaway/investment-transactions/{id} | Retrieve a Heldaway Transaction
[**get_heldaway_investments**](HeldawayInvestmentTransactionsApi.md#get_heldaway_investments) | **GET** /heldaway/investment-transactions | List all Heldaway Transactions

# **filter_heldaway_investments**
> InlineResponse200106 filter_heldaway_investments(body=body, limit=limit, page=page)

Filter all Heldaway Transactions

Returns a filtered list of Heldaway Transactions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HeldawayInvestmentTransactionsApi()
body = swagger_client.InvestmenttransactionsFilterBody() # InvestmenttransactionsFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Heldaway Transactions
    api_response = api_instance.filter_heldaway_investments(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeldawayInvestmentTransactionsApi->filter_heldaway_investments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvestmenttransactionsFilterBody**](InvestmenttransactionsFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200106**](InlineResponse200106.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heldaway_investment**
> InlineResponse200105 get_heldaway_investment(id, limit=limit, page=page)

Retrieve a Heldaway Transaction

Returns a heldaway transaction based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HeldawayInvestmentTransactionsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Heldaway Transaction
    api_response = api_instance.get_heldaway_investment(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeldawayInvestmentTransactionsApi->get_heldaway_investment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200105**](InlineResponse200105.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heldaway_investments**
> InlineResponse200104 get_heldaway_investments(limit=limit, page=page)

List all Heldaway Transactions

Returns a list of all heldaway transactions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HeldawayInvestmentTransactionsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Heldaway Transactions
    api_response = api_instance.get_heldaway_investments(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeldawayInvestmentTransactionsApi->get_heldaway_investments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200104**](InlineResponse200104.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

