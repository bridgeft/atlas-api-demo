# GainlossFilterBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique resource id for the Transaction | [optional] 
**account_id** | **int** | The id of the Account associated with this Transaction | [optional] 
**open_date** | **datetime** | The date the corresponding lot was opened. Note that this field may be populated with the special date value \&quot;1900-01-01\&quot; which is to be understood as the absence of cost basis information for the corresponding closing fill | [optional] 
**close_date** | **datetime** | The date the closing fill was posted | [optional] 
**security_id** | **int** | The id of the Security associated with this Transaction | [optional] 
**direction** | **str** | Flag meant to indicate if the lot is long or short. Potential values L&#x3D;Long, S&#x3D;Short | [optional] 
**short_term** | **bool** | Indicates whether the gain loss is short term (less than a year) | [optional] 
**long_term** | **bool** | Indicates whether the gain loss is long term (more than a year) | [optional] 
**abs_open_units** | **float** | The total quantity of open shares prior to the transaction (e.g. 400 shares originally, 200 shares sold) | [optional] 
**abs_closed_units** | **float** | The total quantity of closed shares of the transaction | [optional] 
**open_value** | **float** | The cost basis of the open shares (in example above, the cost basis for the 400 shares) | [optional] 
**close_value** | **float** | The cost basis of the closed shares | [optional] 
**amount** | **float** | The dollar amount associated with the transaction (e.g. sale amount to close a long position, purchase amount to close a short position) | [optional] 
**is_cancel** | **bool** | Flag to indicate if this transaction is a cancel at the custodian | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

