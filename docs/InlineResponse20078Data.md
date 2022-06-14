# InlineResponse20078Data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique resource id for this Position | [optional] 
**as_of_date** | **datetime** | The current date for this Position | [optional] 
**open_date** | **datetime** | The date this position was opened in the account.Note that this field may be populated with the special date value \&quot;\&quot;1900-01-01\&quot;\&quot; which is to be understood as the absence of cost basis information for the lot associated with this position | [optional] 
**origination_date** | **datetime** | The date that this position originated in all time. For example, a position transferred in would have an origination_date of the date that the position was first opened in whichever account it was opened. Note that this field may be populated with the special date value \&quot;\&quot;1900-01-01\&quot;\&quot; which is to be understood as the absence of cost basis information for the lot associated with this position | [optional] 
**security_id** | **int** | The id of the Security associated with this Position | [optional] 
**lot_id** | **int** | The id of the lot associated with this Position | [optional] 
**security_ledger_id** | **int** | The id of the security ledger associated with this Position | [optional] 
**account_id** | **int** | The id of the Account associated with this Position | [optional] 
**direction** | **str** | Flag to indicate if Holding is Long or Short. Potential values, L &#x3D; Long, S &#x3D; Short | [optional] 
**abs_open_units** | **float** | Quantity of shares for the Position | [optional] 
**cost_basis_unit_price** | **float** | Unit cost price for the position (i.e. tax lot) | [optional] 
**appraised_unit_price** | **float** | Market price of the security on the as_of_date | [optional] 
**realized_gain_loss** | **float** | Dollar gain or loss from trade activity for this security on the as_of_date | [optional] 
**abs_closed_units** | **float** | Quantity of shares closed | [optional] 
**cost_basis_known** | **bool** | Is the cost basis known for this position? | [optional] 
**created_at_utc** | **datetime** | Timestamp for when the record was created | [optional] 
**updated_at_utc** | **datetime** | Timestamp for when the record was updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

