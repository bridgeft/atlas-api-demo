# AccountsFilterBody1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this account object | [optional] 
**firm_id** | **int** | ID of the owning firm | [optional] 
**plaid_item_id** | **int** | ID of the associated Plaid connection | [optional] 
**plaid_account_id** | **int** | Account associated with this plaid account object | [optional] 
**household_id** | **int** | ID of the household to which this account belongs | [optional] 
**type** | **str** | See Account Schema on Plaid&#x27;s API Documentation; https://plaid.com/docs/#account-schema | [optional] 
**subtype** | **str** | See Account Schema on Plaid&#x27;s API Documentation; https://plaid.com/docs/#account-schema | [optional] 
**institution_name** | **str** | Name of the account-holder institution | [optional] 
**official_name** | **str** | Official name of the account assigned by the institution | [optional] 
**mask** | **str** | Last four alphanumeric digits of the account number | [optional] 
**name** | **str** | Account name | [optional] 
**balances** | [**HeldawayaccountsfilterBalances**](HeldawayaccountsfilterBalances.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

