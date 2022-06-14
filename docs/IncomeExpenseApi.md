# swagger_client.IncomeExpenseApi

All URIs are relative to *https://api.bridgeft.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_income_expense**](IncomeExpenseApi.md#filter_income_expense) | **POST** /data/luca/income-expense/filter | Filter all Income Expenserecords
[**get_income_expense**](IncomeExpenseApi.md#get_income_expense) | **GET** /data/luca/income-expense/{id} | Retrieve an Income Expense record
[**get_income_expenses**](IncomeExpenseApi.md#get_income_expenses) | **GET** /data/luca/income-expense | List all Income Expense records

# **filter_income_expense**
> InlineResponse20061 filter_income_expense(body=body, limit=limit, page=page)

Filter all Income Expenserecords

Returns a filtered list of Income Expense records

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IncomeExpenseApi()
body = swagger_client.IncomeexpenseFilterBody() # IncomeexpenseFilterBody |  (optional)
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Filter all Income Expenserecords
    api_response = api_instance.filter_income_expense(body=body, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncomeExpenseApi->filter_income_expense: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IncomeexpenseFilterBody**](IncomeexpenseFilterBody.md)|  | [optional] 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20061**](InlineResponse20061.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_income_expense**
> InlineResponse20060 get_income_expense(id, limit=limit, page=page)

Retrieve an Income Expense record

Returns an Income Expense record based on its ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IncomeExpenseApi()
id = 56 # int | Unique ID for the object
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # Retrieve an Income Expense record
    api_response = api_instance.get_income_expense(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncomeExpenseApi->get_income_expense: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique ID for the object | 
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20060**](InlineResponse20060.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_income_expenses**
> InlineResponse20059 get_income_expenses(limit=limit, page=page)

List all Income Expense records

Returns a list of Income Expense

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IncomeExpenseApi()
limit = 56 # int | Number of items to return per page (optional)
page = 56 # int | Current page number (optional)

try:
    # List all Income Expense records
    api_response = api_instance.get_income_expenses(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncomeExpenseApi->get_income_expenses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return per page | [optional] 
 **page** | **int**| Current page number | [optional] 

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

