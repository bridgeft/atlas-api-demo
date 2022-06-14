# swagger_client.HeldawayDepositoryTransactionsApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_heldaway_depository**](HeldawayDepositoryTransactionsApi.md#filter_heldaway_depository) | **POST** /heldaway/depository-transactions/filter | Filter all Heldaway Transactions
[**get_heldaway_depositories**](HeldawayDepositoryTransactionsApi.md#get_heldaway_depositories) | **GET** /heldaway/depository-transactions | List all Heldaway Transactions
[**get_heldaway_depository**](HeldawayDepositoryTransactionsApi.md#get_heldaway_depository) | **GET** /heldaway/depository-transactions/{id} | Retrieve a Heldaway Transaction

# **filter_heldaway_depository**
> InlineResponse200103 filter_heldaway_depository(body=body, limit=limit, page=page)

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
api_instance = swagger_client.HeldawayDepositoryTransactionsApi()
body = swagger_client.DepositorytransactionsFilterBody() # DepositorytransactionsFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Heldaway Transactions
    api_response = api_instance.filter_heldaway_depository(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeldawayDepositoryTransactionsApi->filter_heldaway_depository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DepositorytransactionsFilterBody**](DepositorytransactionsFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200103**](InlineResponse200103.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heldaway_depositories**
> InlineResponse200101 get_heldaway_depositories(limit=limit, page=page)

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
api_instance = swagger_client.HeldawayDepositoryTransactionsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Heldaway Transactions
    api_response = api_instance.get_heldaway_depositories(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeldawayDepositoryTransactionsApi->get_heldaway_depositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200101**](InlineResponse200101.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heldaway_depository**
> InlineResponse200102 get_heldaway_depository(id, limit=limit, page=page)

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
api_instance = swagger_client.HeldawayDepositoryTransactionsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Heldaway Transaction
    api_response = api_instance.get_heldaway_depository(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeldawayDepositoryTransactionsApi->get_heldaway_depository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200102**](InlineResponse200102.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

