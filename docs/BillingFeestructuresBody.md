# BillingFeestructuresBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by_user_id** | **int** | The user ID of the creator User | [optional] 
**firm_id** | **int** | The firm ID of the managing firm | [optional] 
**name** | **str** | The name of this Fee Structure | [optional] 
**slug** | **str** | The slugified name of this Fee Structure | [optional] 
**calculation_type** | **str** | See Billing Calculation Types | [optional] 
**collection_type** | **str** | R for Flat Rate, A for Flat Amount, G for Flat Group, D for Drop Through, T for Tiered Fee, and F for Free Fee | [optional] 
**frequency** | **str** | See Frequency Codes | [optional] 
**quarter_cycle** | **int** | See Billing Quarter Cycle Codes | [optional] 
**balance_type** | **str** | E for end of period balance, A for average daily balance | [optional] 
**flat_rate** | **float** | The flat rate for this Fee Structure. Must be between 0 and 99 inclusive. Will be stored and converted to a Percentage. (i.e. 1 -&gt; 1% and 0.25 -&gt; 0.25%) | [optional] 
**flat_dollar_fee** | **float** | The flat dollar fee for this Fee Structure | [optional] 
**tiers** | [**list[BillingfeestructuresTiers]**](BillingfeestructuresTiers.md) | Tiers associated with the fee structure | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

