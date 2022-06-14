# InvoicesFilterBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique resource ID for this Invoice | [optional] 
**firm_id** | **int** | The firm ID of the managing firm | [optional] 
**billing_group_id** | **int** | The billing group ID for this Invoice | [optional] 
**snapshot_date** | **datetime** | The snapshot date for this Invoice | [optional] 
**billing_report_id** | **int** | The associated billing report ID for this Invoice | [optional] 
**annual_fee** | **float** | The total fee and debited amount annualized just for this billing group | [optional] 
**annual_debit** | **float** | The annual debit for this Invoice | [optional] 
**total_balance** | **float** | The total group balance on the snapshot date | [optional] 
**period_debit** | **float** | The total debited amount for the period just for this billing group on the snapshot date | [optional] 
**direct_billed_period_debit** | **float** | The direct billed period debit for this Invoice. | [optional] 
**custodian_billed_period_debit** | **float** | The custodian billed period debit for this Invoice | [optional] 
**n_accounts** | **int** | The number of accounts in the report | [optional] 
**n_fee_structures** | **int** | The number of fee structures in the report | [optional] 
**due_date** | **datetime** | Invoice due date, calculated using firm settings at the time the invoice was generated | [optional] 
**is_paid** | **bool** | Is the invoice paid? | [optional] 
**group_id** | **int** | Group Id of this invoice | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

