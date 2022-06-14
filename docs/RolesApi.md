# swagger_client.RolesApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_many_user_roles**](RolesApi.md#create_many_user_roles) | **POST** /user-management/roles/create-many | Create Roles
[**create_user_role**](RolesApi.md#create_user_role) | **POST** /user-management/roles | Create a Role
[**detele_many_user_roles**](RolesApi.md#detele_many_user_roles) | **POST** /user-management/roles/delete-many | Delete many Roles
[**detele_user_role**](RolesApi.md#detele_user_role) | **DELETE** /user-management/roles/{id} | Delete a Role
[**filter_user_roles**](RolesApi.md#filter_user_roles) | **POST** /user-management/roles/filter | Filter all Roles
[**get_user_role**](RolesApi.md#get_user_role) | **GET** /user-management/roles/{id} | Retrieve a Role
[**get_user_roles**](RolesApi.md#get_user_roles) | **GET** /user-management/roles | List all Roles
[**update_user_role**](RolesApi.md#update_user_role) | **PUT** /user-management/roles/{id} | Update a Role
[**update_user_roles**](RolesApi.md#update_user_roles) | **PUT** /user-management/roles | Bulk Update Roles

# **create_many_user_roles**
> list[list[Paths1userManagement1rolespostresponses200contentapplication1jsonschemapropertiesdataitems]] create_many_user_roles(body, limit=limit, page=page)

Create Roles

Returns a list of created Roles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
body = [swagger_client.Paths1userManagement1rolespostrequestBodycontentapplication1jsonschema()] # list[Paths1userManagement1rolespostrequestBodycontentapplication1jsonschema] | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create Roles
    api_response = api_instance.create_many_user_roles(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->create_many_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Paths1userManagement1rolespostrequestBodycontentapplication1jsonschema]**](Paths1userManagement1rolespostrequestBodycontentapplication1jsonschema.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

**list[list[Paths1userManagement1rolespostresponses200contentapplication1jsonschemapropertiesdataitems]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_role**
> InlineResponse20091 create_user_role(body, limit=limit, page=page)

Create a Role

Returns the created Role

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
body = swagger_client.UsermanagementRolesBody() # UsermanagementRolesBody | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create a Role
    api_response = api_instance.create_user_role(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->create_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsermanagementRolesBody**](UsermanagementRolesBody.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20091**](InlineResponse20091.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detele_many_user_roles**
> detele_many_user_roles(body, limit=limit, page=page)

Delete many Roles

Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
body = NULL # object | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete many Roles
    api_instance.detele_many_user_roles(body, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling RolesApi->detele_many_user_roles: %s\n" % e)
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

# **detele_user_role**
> detele_user_role(id, limit=limit, page=page)

Delete a Role

Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete a Role
    api_instance.detele_user_role(id, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling RolesApi->detele_user_role: %s\n" % e)
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

# **filter_user_roles**
> InlineResponse20090 filter_user_roles(body=body, limit=limit, page=page)

Filter all Roles

Returns a filtered list of Roles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
body = swagger_client.RolesFilterBody() # RolesFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Roles
    api_response = api_instance.filter_user_roles(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->filter_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RolesFilterBody**](RolesFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20090**](InlineResponse20090.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_role**
> InlineResponse20092 get_user_role(id, limit=limit, page=page)

Retrieve a Role

Returns a Role based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Role
    api_response = api_instance.get_user_role(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20092**](InlineResponse20092.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_roles**
> InlineResponse20090 get_user_roles(limit=limit, page=page)

List all Roles

Returns a list of Roles within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Roles
    api_response = api_instance.get_user_roles(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20090**](InlineResponse20090.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_role**
> InlineResponse20092 update_user_role(id, limit=limit, page=page)

Update a Role

Returns the updated Role

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update a Role
    api_response = api_instance.update_user_role(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->update_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20092**](InlineResponse20092.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_roles**
> InlineResponse20090 update_user_roles(limit=limit, page=page)

Bulk Update Roles

Returns the updated Roles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Bulk Update Roles
    api_response = api_instance.update_user_roles(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->update_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20090**](InlineResponse20090.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

