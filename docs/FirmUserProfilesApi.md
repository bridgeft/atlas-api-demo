# swagger_client.FirmUserProfilesApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_firm_user**](FirmUserProfilesApi.md#create_firm_user) | **POST** /user-management/firm-profiles | Create a Firm User Profile
[**create_many_firm_user_profiles**](FirmUserProfilesApi.md#create_many_firm_user_profiles) | **POST** /user-management/firm-profiles/create-many | Create Firm User Profiles
[**detele_firm_user**](FirmUserProfilesApi.md#detele_firm_user) | **DELETE** /user-management/firm-profiles/{id} | Delete a Firm User Profile
[**detele_many_firm_user_profiles**](FirmUserProfilesApi.md#detele_many_firm_user_profiles) | **POST** /user-management/firm-profiles/delete-many | Delete many Firm User Profiles
[**filter_firm_user_profiles**](FirmUserProfilesApi.md#filter_firm_user_profiles) | **POST** /user-management/firm-profiles/filter | Filter all Firm User Profiles
[**get_firm_user**](FirmUserProfilesApi.md#get_firm_user) | **GET** /user-management/firm-profiles/{id} | Retrieve a Firm User Profile
[**get_firm_user_profiles**](FirmUserProfilesApi.md#get_firm_user_profiles) | **GET** /user-management/firm-profiles | List all Firm User Profiles
[**update_firm_user**](FirmUserProfilesApi.md#update_firm_user) | **PUT** /user-management/firm-profiles/{id} | Update a Firm User Profile
[**update_firm_user_profiles**](FirmUserProfilesApi.md#update_firm_user_profiles) | **PUT** /user-management/firm-profiles | Bulk Update Firm User Profiles

# **create_firm_user**
> InlineResponse20095 create_firm_user(body, limit=limit, page=page)

Create a Firm User Profile

Returns the created Firm User Profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirmUserProfilesApi()
body = swagger_client.UsermanagementFirmprofilesBody() # UsermanagementFirmprofilesBody | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create a Firm User Profile
    api_response = api_instance.create_firm_user(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmUserProfilesApi->create_firm_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsermanagementFirmprofilesBody**](UsermanagementFirmprofilesBody.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20095**](InlineResponse20095.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_many_firm_user_profiles**
> InlineResponse20094 create_many_firm_user_profiles(body, limit=limit, page=page)

Create Firm User Profiles

Returns a list of created Firm User Profiles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirmUserProfilesApi()
body = [swagger_client.Paths1userManagement1firmProfilespostrequestBodycontentapplication1jsonschema()] # list[Paths1userManagement1firmProfilespostrequestBodycontentapplication1jsonschema] | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Create Firm User Profiles
    api_response = api_instance.create_many_firm_user_profiles(body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmUserProfilesApi->create_many_firm_user_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Paths1userManagement1firmProfilespostrequestBodycontentapplication1jsonschema]**](Paths1userManagement1firmProfilespostrequestBodycontentapplication1jsonschema.md)|  | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20094**](InlineResponse20094.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detele_firm_user**
> detele_firm_user(id, limit=limit, page=page)

Delete a Firm User Profile

Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirmUserProfilesApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete a Firm User Profile
    api_instance.detele_firm_user(id, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling FirmUserProfilesApi->detele_firm_user: %s\n" % e)
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

# **detele_many_firm_user_profiles**
> detele_many_firm_user_profiles(body, limit=limit, page=page)

Delete many Firm User Profiles

Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirmUserProfilesApi()
body = NULL # object | 
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Delete many Firm User Profiles
    api_instance.detele_many_firm_user_profiles(body, limit=limit, page=page)
except ApiException as e:
    print("Exception when calling FirmUserProfilesApi->detele_many_firm_user_profiles: %s\n" % e)
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

# **filter_firm_user_profiles**
> InlineResponse20094 filter_firm_user_profiles(body=body, limit=limit, page=page)

Filter all Firm User Profiles

Returns a filtered list of Firm User Profiles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirmUserProfilesApi()
body = swagger_client.FirmprofilesFilterBody() # FirmprofilesFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Firm User Profiles
    api_response = api_instance.filter_firm_user_profiles(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmUserProfilesApi->filter_firm_user_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirmprofilesFilterBody**](FirmprofilesFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20094**](InlineResponse20094.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firm_user**
> InlineResponse20096 get_firm_user(id, limit=limit, page=page)

Retrieve a Firm User Profile

Returns a Firm User Profile based on a single ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirmUserProfilesApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve a Firm User Profile
    api_response = api_instance.get_firm_user(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmUserProfilesApi->get_firm_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20096**](InlineResponse20096.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firm_user_profiles**
> InlineResponse20093 get_firm_user_profiles(limit=limit, page=page)

List all Firm User Profiles

Returns a list of Firm User Profiles within the data field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirmUserProfilesApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Firm User Profiles
    api_response = api_instance.get_firm_user_profiles(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmUserProfilesApi->get_firm_user_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20093**](InlineResponse20093.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_firm_user**
> InlineResponse20096 update_firm_user(id, limit=limit, page=page)

Update a Firm User Profile

Returns the updated Firm User Profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirmUserProfilesApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Update a Firm User Profile
    api_response = api_instance.update_firm_user(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmUserProfilesApi->update_firm_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20096**](InlineResponse20096.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_firm_user_profiles**
> InlineResponse20094 update_firm_user_profiles(limit=limit, page=page)

Bulk Update Firm User Profiles

Returns the updated Firm User Profiles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FirmUserProfilesApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Bulk Update Firm User Profiles
    api_response = api_instance.update_firm_user_profiles(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmUserProfilesApi->update_firm_user_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20094**](InlineResponse20094.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

