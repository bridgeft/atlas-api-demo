# swagger_client.ClientUserProfilesApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_user**](ClientUserProfilesApi.md#create_client_user) | **POST** /user-management/client-profiles | Create a Client User Profile
[**create_many_client_user_profiles**](ClientUserProfilesApi.md#create_many_client_user_profiles) | **POST** /user-management/client-profiles/create-many | Create Client User Profiles
[**detele_client_user**](ClientUserProfilesApi.md#detele_client_user) | **DELETE** /user-management/client-profiles/{id} | Delete a Client User Profile
[**detele_many_client_user_profiles**](ClientUserProfilesApi.md#detele_many_client_user_profiles) | **POST** /user-management/client-profiles/delete-many | Delete many Client User Profiles
[**filter_client_user_profiles**](ClientUserProfilesApi.md#filter_client_user_profiles) | **POST** /user-management/client-profiles/filter | Filter all Client User Profiles
[**get_client_user**](ClientUserProfilesApi.md#get_client_user) | **GET** /user-management/client-profiles/{id} | Retrieve a Client User Profile
[**get_client_user_profiles**](ClientUserProfilesApi.md#get_client_user_profiles) | **GET** /user-management/client-profiles | List all Client User Profiles
[**update_client_user**](ClientUserProfilesApi.md#update_client_user) | **PUT** /user-management/client-profiles/{id} | Update a Client User Profile
[**update_client_user_profiles**](ClientUserProfilesApi.md#update_client_user_profiles) | **PUT** /user-management/client-profiles | Bulk Update Client User Profiles

# **create_client_user**
> InlineResponse20099 create_client_user(body, limit=limit, page=page)

Create a Client User Profile

Returns the created Client User Profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientUserProfilesApi()
body = swagger_client.UsermanagementClientprofilesBody() # UsermanagementClientprofilesBody | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create a Client User Profile
    api_response = api_instance.create_client_user(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientUserProfilesApi->create_client_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsermanagementClientprofilesBody**](UsermanagementClientprofilesBody.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20099**](InlineResponse20099.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_many_client_user_profiles**
> InlineResponse20098 create_many_client_user_profiles(body, limit=limit, page=page)

Create Client User Profiles

Returns a list of created Client User Profiles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientUserProfilesApi()
body = [swagger_client.Paths1userManagement1clientProfilespostrequestBodycontentapplication1jsonschema()] # list[Paths1userManagement1clientProfilespostrequestBodycontentapplication1jsonschema] | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create Client User Profiles
    api_response = api_instance.create_many_client_user_profiles(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientUserProfilesApi->create_many_client_user_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Paths1userManagement1clientProfilespostrequestBodycontentapplication1jsonschema]**](Paths1userManagement1clientProfilespostrequestBodycontentapplication1jsonschema.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20098**](InlineResponse20098.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detele_client_user**
> detele_client_user(id, limit=limit, page=page)

Delete a Client User Profile

Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientUserProfilesApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete a Client User Profile
    api_instance.detele_client_user(id, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling ClientUserProfilesApi->detele_client_user: %s\n" % e)
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

# **detele_many_client_user_profiles**
> detele_many_client_user_profiles(body, limit=limit, page=page)

Delete many Client User Profiles

Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientUserProfilesApi()
body = NULL # object | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete many Client User Profiles
    api_instance.detele_many_client_user_profiles(body, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling ClientUserProfilesApi->detele_many_client_user_profiles: %s\n" % e)
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

# **filter_client_user_profiles**
> InlineResponse20098 filter_client_user_profiles(body=body, limit=limit, page=page)

Filter all Client User Profiles

Returns a filtered list of Client User Profiles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientUserProfilesApi()
body = swagger_client.ClientprofilesFilterBody() # ClientprofilesFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Client User Profiles
    api_response = api_instance.filter_client_user_profiles(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientUserProfilesApi->filter_client_user_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientprofilesFilterBody**](ClientprofilesFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20098**](InlineResponse20098.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_user**
> InlineResponse200100 get_client_user(id, limit=limit, page=page)

Retrieve a Client User Profile

Returns a Client User Profile based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientUserProfilesApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Client User Profile
    api_response = api_instance.get_client_user(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientUserProfilesApi->get_client_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200100**](InlineResponse200100.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_user_profiles**
> InlineResponse20097 get_client_user_profiles(limit=limit, page=page)

List all Client User Profiles

Returns a list of Client User Profiles within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientUserProfilesApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Client User Profiles
    api_response = api_instance.get_client_user_profiles(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientUserProfilesApi->get_client_user_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20097**](InlineResponse20097.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_user**
> InlineResponse200100 update_client_user(id, limit=limit, page=page)

Update a Client User Profile

Returns the updated Client User Profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientUserProfilesApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update a Client User Profile
    api_response = api_instance.update_client_user(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientUserProfilesApi->update_client_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse200100**](InlineResponse200100.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_user_profiles**
> InlineResponse20098 update_client_user_profiles(limit=limit, page=page)

Bulk Update Client User Profiles

Returns the updated Client User Profiles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientUserProfilesApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Bulk Update Client User Profiles
    api_response = api_instance.update_client_user_profiles(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientUserProfilesApi->update_client_user_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20098**](InlineResponse20098.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

