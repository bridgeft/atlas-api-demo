# InlineResponse200102Data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique resource id for this Heldaway Transaction | [optional] 
**plaid_transaction_id** | **int** | The ID of the transaction on Plaid | [optional] 
**plaid_account_id** | **int** | The Plaid account id associated with this heldaway transaction | [optional] 
**plaid_item_id** | **int** | The id of the heldaway connection associated with this transaction | [optional] 
**household_id** | **int** | The id of the household to which this transaction belongs | [optional] 
**firm_id** | **int** | The id of the firm managing this heldaway transaction | [optional] 
**categories** | **list[str]** | A hierarchical array of the categories to which this transaction belongs | [optional] 
**category_id** | **str** | The ID of the category to which this transaction belongs | [optional] 
**plaid_transaction_type** | **str** | The type of Transaction determined by Plaid | [optional] 
**name** | **str** | Description of the transaction | [optional] 
**merchant_name** | **str** | Clean name of the merchant if applicable | [optional] 
**amount** | **float** | The settled dollar value. Positive values when money moves out of the account; negative values when money moves in. For example, purchases are positive; credit card payments, direct deposits, refunds are negative | [optional] 
**iso_currency_code** | **str** | The ISO currency code of the transaction. Always null if unofficial_currency_code is non-null. | [optional] 
**unofficial_currency_code** | **str** | The currency code associated with the transaction, if not recognized as an ISO code. For example, cryptocurrencies such as BTC. Always null if iso_currency_code is non-null. | [optional] 
**_date** | **datetime** | For pending transactions, Plaid returns the date the transaction occurred; for posted transactions, Plaid returns the date the transaction posts. Both dates are returned in an ISO 8601 format ( YYYY-MM-DD ). Dates reflect the date posted by the bank and are not standardized to a timezone by Plaid. | [optional] 
**authorized_date** | **datetime** | The date that the transaction was authorized. Dates are returned in an ISO 8601 format ( YYYY-MM-DD ). | [optional] 
**location** | **object** | Information about where the transaction occurred. The location key will always be an Object, but no location data elements are guaranteed. | [optional] 
**payment_meta** | **object** | Information about a transfer payment. The payment_meta key will always be an Object, but no payment_meta data elements are guaranteed. This object will be deprecated in the future. | [optional] 
**payment_channel** | **object** | The channel used to make a payment. Possible values are; online, in store, other. This field will replace the transaction_type field. | [optional] 
**pending** | **bool** | When true, identifies the transaction as pending or unsettled. Pending transaction details (name, type, amount, category ID) may change before they are settled. | [optional] 
**account_owner** | **str** | The name of the account owner. This field is not typically populated and only relevant when dealing with sub-accounts. | [optional] 
**transaction_code** | **str** | The transaction code | [optional] 
**plaid_pending_transaction** | **str** | Information about the plaid pending transaction | [optional] 
**created_at_utc** | **datetime** | Timestamp for when the record was created | [optional] 
**updated_at_utc** | **datetime** | Timestamp for when the record was updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

