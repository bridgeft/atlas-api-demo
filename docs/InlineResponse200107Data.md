# InlineResponse200107Data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique resource id for this Heldaway Position | [optional] 
**plaid_account_id** | **int** | The Plaid account id associated with this heldaway position | [optional] 
**plaid_item_id** | **int** | The id of the heldaway connection that owns this position | [optional] 
**household_id** | **int** | The id of the household to which this position belongs | [optional] 
**firm_id** | **int** | The id of the firm managing this heldaway position | [optional] 
**cost_basis** | **float** | The cost basis of the holding, if it is available from the institution | [optional] 
**iso_currency_code** | **str** | Unit of currency that is displayed where null is defaulted to USD | [optional] 
**unofficial_currency_code** | **str** | The unofficial currency of the holding. | [optional] 
**institution_price** | **float** | The last price given by the institution for this security. | [optional] 
**institution_price_as_of** | **datetime** | The date at which institution_price was current. | [optional] 
**quantity** | **float** | The amount of shares of this position | [optional] 
**security** | **str** | JSON string containing information about the security | [optional] 
**institution_value** | **float** | The total value of the position | [optional] 
**created_at_utc** | **datetime** | Timestamp for when the record was created | [optional] 
**updated_at_utc** | **datetime** | Timestamp for when the record was updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

