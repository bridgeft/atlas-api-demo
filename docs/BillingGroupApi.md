# swagger_client.BillingGroupApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_billing_group_create_from_household**](BillingGroupApi.md#create_billing_group_create_from_household) | **POST** /billing/groups/create-from-households | Create Billing Groups from Households
[**create_billing_groups**](BillingGroupApi.md#create_billing_groups) | **POST** /billing/groups | Create a Billing Group
[**create_many_billing_groups**](BillingGroupApi.md#create_many_billing_groups) | **POST** /billing/groups/create-many | Create Billing Groups
[**detele_billing_group**](BillingGroupApi.md#detele_billing_group) | **DELETE** /billing/groups/{id} | Delete a Billing Group
[**detele_many_billing_groups**](BillingGroupApi.md#detele_many_billing_groups) | **POST** /billing/groups/delete-many | Delete many Billing Groups
[**filter_billing_groups**](BillingGroupApi.md#filter_billing_groups) | **POST** /billing/groups/filter | Filter all Billing Groups
[**get_billing_group**](BillingGroupApi.md#get_billing_group) | **GET** /billing/groups/{id} | Retrieve a Billing Group
[**get_billing_groups**](BillingGroupApi.md#get_billing_groups) | **GET** /billing/groups | List all Billing Groups
[**remove_assignment**](BillingGroupApi.md#remove_assignment) | **POST** /billing/groups/remove-assignment | Remove a Billing Group Assignment
[**update_billing_group**](BillingGroupApi.md#update_billing_group) | **PUT** /billing/groups/{id} | Update a Billing Group
[**update_billing_groups**](BillingGroupApi.md#update_billing_groups) | **PUT** /billing/groups | Bulk Update Billing Groups

# **create_billing_group_create_from_household**
> InlineResponse20014 create_billing_group_create_from_household(limit=limit, page=page)

Create Billing Groups from Households

Deletes existing Billing Groups, and recreates for the accounts of each household managed by the firm

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingGroupApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create Billing Groups from Households
    api_response = api_instance.create_billing_group_create_from_household(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingGroupApi->create_billing_group_create_from_household: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_billing_groups**
> InlineResponse20015 create_billing_groups(body, limit=limit, page=page)

Create a Billing Group

Returns the created billing group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingGroupApi()
body = swagger_client.BillingGroupsBody() # BillingGroupsBody | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create a Billing Group
    api_response = api_instance.create_billing_groups(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingGroupApi->create_billing_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillingGroupsBody**](BillingGroupsBody.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_many_billing_groups**
> InlineResponse20014 create_many_billing_groups(body, limit=limit, page=page)

Create Billing Groups

Returns a list of created Billing Groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingGroupApi()
body = [swagger_client.Paths1billing1groupspostrequestBodycontentapplication1jsonschema()] # list[Paths1billing1groupspostrequestBodycontentapplication1jsonschema] | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create Billing Groups
    api_response = api_instance.create_many_billing_groups(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingGroupApi->create_many_billing_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Paths1billing1groupspostrequestBodycontentapplication1jsonschema]**](Paths1billing1groupspostrequestBodycontentapplication1jsonschema.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detele_billing_group**
> detele_billing_group(id, limit=limit, page=page)

Delete a Billing Group

Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingGroupApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete a Billing Group
    api_instance.detele_billing_group(id, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling BillingGroupApi->detele_billing_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detele_many_billing_groups**
> detele_many_billing_groups(body, limit=limit, page=page)

Delete many Billing Groups

Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingGroupApi()
body = NULL # object | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete many Billing Groups
    api_instance.detele_many_billing_groups(body, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling BillingGroupApi->detele_many_billing_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_billing_groups**
> InlineResponse20014 filter_billing_groups(body=body, limit=limit, page=page)

Filter all Billing Groups

Returns a filtered list of Billing Group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingGroupApi()
body = swagger_client.GroupsFilterBody() # GroupsFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Billing Groups
    api_response = api_instance.filter_billing_groups(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingGroupApi->filter_billing_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupsFilterBody**](GroupsFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_group**
> InlineResponse20015 get_billing_group(id, limit=limit, page=page)

Retrieve a Billing Group

Returns a billing group based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingGroupApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Billing Group
    api_response = api_instance.get_billing_group(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingGroupApi->get_billing_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_groups**
> InlineResponse20014 get_billing_groups(limit=limit, page=page)

List all Billing Groups

Returns a list of billing groups within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingGroupApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Billing Groups
    api_response = api_instance.get_billing_groups(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingGroupApi->get_billing_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_assignment**
> remove_assignment(body, limit=limit, page=page)

Remove a Billing Group Assignment

Delete a single assignment tied to a Billing Group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingGroupApi()
body = swagger_client.GroupsRemoveassignmentBody() # GroupsRemoveassignmentBody | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Remove a Billing Group Assignment
    api_instance.remove_assignment(body, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling BillingGroupApi->remove_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupsRemoveassignmentBody**](GroupsRemoveassignmentBody.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_group**
> InlineResponse20015 update_billing_group(id, limit=limit, page=page)

Update a Billing Group

Returns the updated billing group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingGroupApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update a Billing Group
    api_response = api_instance.update_billing_group(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingGroupApi->update_billing_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_groups**
> InlineResponse20014 update_billing_groups(limit=limit, page=page)

Bulk Update Billing Groups

Returns the updated billing groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BillingGroupApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Bulk Update Billing Groups
    api_response = api_instance.update_billing_groups(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingGroupApi->update_billing_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

