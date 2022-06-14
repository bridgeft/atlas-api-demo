# InlineResponse20075Data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique resource id for the Transaction | [optional] 
**account_id** | **int** | The id of the Account associated with this Transaction | [optional] 
**security_id** | **int** | The id of the Security associated with this Transaction | [optional] 
**type** | **str** | The type of Transfer. Possible values, DEP - cash deposit, WITH - cash withdrawal, TLO - transfer long to open - security transfers into an account, TLC - transfer long to close - security transfers out of an account | [optional] 
**is_cancel** | **bool** | Flag to indicate if this Transaction is a cancel from the custodian | [optional] 
**transaction_date** | **datetime** | The date of the transaction on a trade basis | [optional] 
**reported_date** | **datetime** | The date the custodian reports the transaction | [optional] 
**abs_units** | **float** | The quantity of shares for the Transfer | [optional] 
**unit_price** | **float** | he closing market price of the security on the transaction_date. Note, for cash, this is always 1 | [optional] 
**cost_basis_unit_price** | **float** | The unit cost price for shares being transferred | [optional] 
**transaction_fee** | **float** | Fees associated with the Transaction (e.g. commission) | [optional] 
**recon_id** | **int** | The id of a Reconciliation entered to adjust a transaction | [optional] 
**custodian** | **str** | Custodian the account data comes from. TDA&#x3D;TD Ameritrade, SWB&#x3D;Schwab, NFS&#x3D;Fidelity, PER&#x3D;Pershing, MLT&#x3D;MillenniumTrust, RJA&#x3D;RaymondJames, HDG&#x3D;Manual | [optional] 
**description** | **str** | Description of the transaction from the custodian | [optional] 
**origination_date** | **datetime** | Date when the transaction was originated | [optional] 
**cost_basis_known** | **bool** | Is the cost basis known for this transaction? | [optional] 
**replaced_transfer_id** | **int** | The id of the replaced transfer associated with this transaction | [optional] 
**created_at_utc** | **datetime** | Timestamp for when the record was created | [optional] 
**updated_at_utc** | **datetime** | Timestamp for when the record was updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

