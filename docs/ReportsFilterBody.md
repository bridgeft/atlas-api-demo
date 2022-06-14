# ReportsFilterBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique resource ID for this billing report | [optional] 
**firm_id** | **int** | The firm ID of the managing firm | [optional] 
**created_invoices** | **bool** | True if invoices were created when the report was created | [optional] 
**billing_date** | **datetime** | The input date to the billing report | [optional] 
**snapshot_date** | **datetime** | The closest date available to the billing date for which there&#x27;s data at the time of running the report | [optional] 
**run_date** | **datetime** | The most recent market date corresponding to when the report date | [optional] 
**created_date** | **datetime** | The calendar date on which the report was generated / created | [optional] 
**annual_fee** | **float** | Total fee and debited amount annualized | [optional] 
**annual_debit** | **float** | The annual debit amount for this billing report | [optional] 
**total_balance** | **float** | Sum of all group balances on the billing date | [optional] 
**aum_on_billing_date** | **float** | All assets under management on the billing date | [optional] 
**period_debit** | **float** | Total debited amount for the period | [optional] 
**direct_billed_period_debit** | **float** | The direct billed period debit for this billing report | [optional] 
**custodian_billed_period_debit** | **float** | The custodian billed period debit for this billing report | [optional] 
**split_payout** | **float** | Total payout of all splits for this period | [optional] 
**split_payout_annualized** | **float** | Split payout on an annualized basis | [optional] 
**firm_share** | **float** | The firm&#x27;s share for the period. Equals period_debit - split_payout. | [optional] 
**firm_share_annualized** | **float** | Firm&#x27;s annualized share. Equals annual_debit - split_payout_annualized. | [optional] 
**n_accounts** | **int** | The number of accounts for this billing report | [optional] 
**n_groups** | **int** | The number of groups for this billing report | [optional] 
**n_splits** | **int** | The number of billing splits for this billing report | [optional] 
**n_fee_structures** | **int** | The number of fee structures for this billing report | [optional] 
**fee_upload_file_id** | **int** | The corresponding fee upload file model instance | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

