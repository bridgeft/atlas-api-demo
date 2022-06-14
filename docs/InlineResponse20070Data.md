# InlineResponse20070Data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique resource ID for this Holdings object | [optional] 
**as_of_date** | **datetime** | The current date for this Holding | [optional] 
**security_id** | **int** | The id of the Security associated with this Holding | [optional] 
**account_id** | **int** | The id of the Account associated with this Holding | [optional] 
**household_id** | **int** | The id of the Household associated with this Holding | [optional] 
**direction** | **str** | Flag to indicate if Holding is Long or Short. Potential values, L &#x3D; Long, S &#x3D; Short | [optional] 
**first_open_date** | **datetime** | The original open date for the holding - this represents the earliest cost basis date available at the custodian. Note that this field may be populated with the special date value \&quot;\&quot;1900-01-01\&quot;\&quot; which is to be understood as the absence of cost basis information for at least one of the component positions in this holding | [optional] 
**first_origination_date** | **datetime** | The earliest origination date for the holding - this represents the earliest cost basis date available at the custodian in all time even for shares originated outside the account. Note that this field may be populated with the special date value \&quot;\&quot;1900-01-01\&quot;\&quot; which is to be understood as the absence of cost basis information for at least one of the component positions in this holding | [optional] 
**latest_open_date** | **datetime** | The most recent date for opening lots (e.g. last time more shares were purchased). Note that this field may be populated with the special date value \&quot;\&quot;1900-01-01\&quot;\&quot; which is to be understood as the absence of cost basis information for all of the component positions in this holding | [optional] 
**abs_units** | **float** | Quantity of shares for the holding - combine with direction to know if the position is long or short | [optional] 
**appraised_unit_price** | **float** | Market price of security on as_of_date | [optional] 
**abs_beginning_value** | **float** | Cost basis of the units | [optional] 
**realized_gain_loss** | **float** | Aggregates from Gain Loss end point; dollar gain or loss from trade activity | [optional] 
**cost_basis_known** | **bool** | Is the cost basis known for this holding? | [optional] 
**created_at_utc** | **datetime** | Timestamp for when the record was created | [optional] 
**updated_at_utc** | **datetime** | Timestamp for when the record was updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

