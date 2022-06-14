# InlineResponse20066Data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique resource ID for this Security Balance object | [optional] 
**as_of_date** | **datetime** | The current date for this Security Balance | [optional] 
**account_id** | **int** | The id of the Account associated with this Security Balance | [optional] 
**household_id** | **int** | The id of the Household associated with this Security Balance | [optional] 
**security_id** | **int** | The id of the Security associated with this Security Balance | [optional] 
**units** | **float** | The number of shares | [optional] 
**realized_gl** | **float** | Aggregates from Gain Loss end point; dollar gain or loss from trade activity | [optional] 
**abs_income** | **float** | Aggregates from Income Expense end point; value of performance affecting income such as dividends | [optional] 
**abs_expense** | **float** | Aggregates from Income Expense end point; value of performance affecting expenses such as ADR fees | [optional] 
**appraised_unit_price** | **float** | The market price of the security on the as_of_date | [optional] 
**appraised_value** | **float** | Market value of the security on the as_of_date (calculated as units * appraised_unit_price) | [optional] 
**beginning_value** | **float** | Cost basis of the units | [optional] 
**holding_period_return** | **float** | Security level return on the as_of_date | [optional] 
**transfer_out_unrealized_gain_loss** | **float** | Unrealized gain loss that has transfered out | [optional] 
**created_at_utc** | **datetime** | Timestamp for when the record was created | [optional] 
**updated_at_utc** | **datetime** | Timestamp for when the record was updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

