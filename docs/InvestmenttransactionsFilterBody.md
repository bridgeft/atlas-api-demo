# InvestmenttransactionsFilterBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID of the Heldaway Investment Transaction | [optional] 
**plaid_investment_transaction_id** | **str** | The ID of the Investment transaction, unique across all Plaid transactions. | [optional] 
**plaid_account_id** | **str** | The ID of the account against which this transaction posted. | [optional] 
**plaid_security_id** | **str** | The ID of the security assigned by Plaid to which this transaction is related. | [optional] 
**_date** | **str** | Date The ISO-8601 posting date for the transaction, or transacted date for pending transactions. | [optional] 
**name** | **str** | The Institution’s description of the transaction. | [optional] 
**quantity** | **float** | The Amount of the security involved in this transaction. | [optional] 
**amount** | **float** | The complete value of the transaction. Positive values when cash is debited, e.g. purchases of stock; negative values when cash is credited, e.g. sales of stock. Treatment remains the same for cash-only movements unassociated with securities. | [optional] 
**price** | **float** | The price of the security at which this transaction occurred. | [optional] 
**fees** | **float** | The combined value of all fees applied to this transaction. | [optional] 
**type** | **str** | Investment Transaction type assigned by Plaid | [optional] 
**subtype** | **str** | Investment Transaction subtype assigned by Plaid | [optional] 
**iso_currency_code** | **str** | The ISO-4217 currency code of the transaction. Always null if unofficial_currency_code is non-null. | [optional] 
**unofficial_currency_code** | **str** | The unofficial currency of the transaction. Always null if iso_currency_code is non-null. This is present if the price is denominated in an unrecognized currency e.g. Bitcoin, rewards points. | [optional] 
**cancel_transaction_id** | **str** | Present only when the transaction type is cancel, and indicates the investment_transaction_id of the transaction which was cancelled. | [optional] 
**household_id** | **int** | The id of the household to which this transaction belongs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

