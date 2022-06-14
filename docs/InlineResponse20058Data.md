# InlineResponse20058Data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique resource id for the Transaction | [optional] 
**account_id** | **int** | The id of the Account associated with this Transaction | [optional] 
**security_id** | **int** | The id of the Security associated with this Transaction | [optional] 
**type** | **str** | The type of transaction. Possible values, BTO - buy to open, BTC - buy to close, STO - sell to open, STC - sell to close | [optional] 
**is_cancel** | **bool** | Flag to indicate if this Transaction is a cancel from the custodian | [optional] 
**transaction_date** | **datetime** | The date of the transaction on a trade basis | [optional] 
**reported_date** | **datetime** | The date the custodian reports the transaction | [optional] 
**abs_units** | **float** | The quantity of shares for the Transaction | [optional] 
**abs_amount** | **float** | The dollar amount associated with the Transaction | [optional] 
**transaction_fee** | **float** | Fees associated with the Transaction (e.g. commission) | [optional] 
**description** | **str** | Description of the transaction from the custodian | [optional] 
**custodian** | **str** | Custodian the account data comes from. TDA&#x3D;TD Ameritrade, SWB&#x3D;Schwab, NFS&#x3D;Fidelity, PER&#x3D;Pershing, MLT&#x3D;MillenniumTrust, RJA&#x3D;RaymondJames, HDG&#x3D;Manual | [optional] 
**created_at_utc** | **datetime** | Timestamp for when the record was created | [optional] 
**updated_at_utc** | **datetime** | Timestamp for when the record was updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

