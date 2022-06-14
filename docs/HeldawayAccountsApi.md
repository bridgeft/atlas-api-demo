# swagger_client.HeldawayAccountsApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_heldaway_accounts**](HeldawayAccountsApi.md#filter_heldaway_accounts) | **POST** /heldaway/accounts/filter | Filter all Heldaway Accounts
[**get_heldaway_account**](HeldawayAccountsApi.md#get_heldaway_account) | **GET** /heldaway/accounts/{id} | Retrieve a Heldaway Account
[**get_heldaway_accounts**](HeldawayAccountsApi.md#get_heldaway_accounts) | **GET** /heldaway/accounts | List all Heldaway Accounts
[**update_heldaway_account**](HeldawayAccountsApi.md#update_heldaway_account) | **PUT** /heldaway/accounts/{id} | Update a Heldaway Account
[**update_heldaway_accounts**](HeldawayAccountsApi.md#update_heldaway_accounts) | **PUT** /heldaway/accounts | Bulk Update Heldaway Accounts

# **filter_heldaway_accounts**
> InlineResponse2006 filter_heldaway_accounts(body=body, limit=limit, page=page)

Filter all Heldaway Accounts

Returns a filtered list of Heldaway Accounts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HeldawayAccountsApi()
body = swagger_client.AccountsFilterBody1() # AccountsFilterBody1 |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Heldaway Accounts
    api_response = api_instance.filter_heldaway_accounts(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeldawayAccountsApi->filter_heldaway_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountsFilterBody1**](AccountsFilterBody1.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heldaway_account**
> InlineResponse2004 get_heldaway_account(id, limit=limit, page=page)

Retrieve a Heldaway Account

Returns a Heldaway Account based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HeldawayAccountsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Heldaway Account
    api_response = api_instance.get_heldaway_account(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeldawayAccountsApi->get_heldaway_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heldaway_accounts**
> InlineResponse2002 get_heldaway_accounts(limit=limit, page=page)

List all Heldaway Accounts

Returns a list of Heldaway Accounts within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HeldawayAccountsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Heldaway Accounts
    api_response = api_instance.get_heldaway_accounts(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeldawayAccountsApi->get_heldaway_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_heldaway_account**
> InlineResponse2005 update_heldaway_account(id, limit=limit, page=page)

Update a Heldaway Account

Returns the updated Heldaway Account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HeldawayAccountsApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update a Heldaway Account
    api_response = api_instance.update_heldaway_account(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeldawayAccountsApi->update_heldaway_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_heldaway_accounts**
> InlineResponse2003 update_heldaway_accounts(limit=limit, page=page)

Bulk Update Heldaway Accounts

Returns the updated Heldaway Accounts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HeldawayAccountsApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Bulk Update Heldaway Accounts
    api_response = api_instance.update_heldaway_accounts(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeldawayAccountsApi->update_heldaway_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

