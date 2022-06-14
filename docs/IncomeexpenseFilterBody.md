# IncomeexpenseFilterBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique resource id for the Transaction | [optional] 
**account_id** | **int** | The id of the Account associated with this Transaction | [optional] 
**security_id** | **int** | The id of the Security associated with this Transaction | [optional] 
**type** | **str** | The type of transaction. Possible values, INC&#x3D;income, EXP&#x3D;expense | [optional] 
**is_cancel** | **bool** | Flag to indicate if this Transaction is a cancel from the custodian | [optional] 
**transaction_date** | **datetime** | The date of the transaction on a trade basis | [optional] 
**reported_date** | **datetime** | The date the custodian reports the transaction | [optional] 
**abs_amount** | **float** | The dollar amount associated with the Transaction | [optional] 
**transaction_fee** | **float** | Fees associated with the Transaction (e.g. commission) | [optional] 
**is_performance_impact** | **bool** | Flag to indicate if the Transaction affects the time-weighted return performance calculation | [optional] 
**is_positive_cash_impact** | **bool** | Flag to indicate if the Transaction increases the cash balance | [optional] 
**description** | **str** | Description of the transaction from the custodian | [optional] 
**custodian** | **str** | Custodian the account data comes from. TDA&#x3D;TD Ameritrade, SWB&#x3D;Schwab, NFS&#x3D;Fidelity, PER&#x3D;Pershing, MLT&#x3D;MillenniumTrust, RJA&#x3D;RaymondJames, HDG&#x3D;Manual | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

