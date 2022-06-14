# AccountsFilterBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this account object | [optional] 
**name** | **str** | Populated from custodian data but can be modified by users | [optional] 
**firm_id** | **int** | ID of the owning firm | [optional] 
**inception_date** | **date** | Date of account inception, if applicable. May differ from opening date. | [optional] 
**close_date** | **date** | Date the account was closed, if applicable | [optional] 
**status** | **str** | Status of the account object. It can be funded, papered, closed or slate. Funded account is considered active account, Papered or Closed account is inactive, and Stale is unknown | [optional] 
**number** | **str** | Account number | [optional] 
**custodian** | **str** | Custodian the account data comes from. TDA&#x3D;TD Ameritrade, SWB&#x3D;Schwab, NFS&#x3D;Fidelity, PER&#x3D;Pershing, MLT&#x3D;MillenniumTrust, RJA&#x3D;RaymondJames, HDG&#x3D;Manual | [optional] 
**city** | **str** | City of the account-holder | [optional] 
**zip_code** | **str** | Zip code of the account-holder | [optional] 
**acct_type** | **str** | Type of account. Example, IRA Roth, 401k, etc. | [optional] 
**is_tax_deferred** | **bool** | True if this account is tax deferrable. This data is typically provided by the financial institution | [optional] 
**is_taxable** | **bool** | True if this account is taxable. This data is typically provided by the financial insitution | [optional] 
**payment_source** | **str** | C&#x3D;billed at the custodian D&#x3D;billed directly | [optional] 
**advisor_code** | **str** | Advisor code for this account object | [optional] 
**household_id** | **int** | Household Id this account belongs to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

