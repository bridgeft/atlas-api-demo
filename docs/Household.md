# Household

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique household identifier | [optional] 
**name** | **str** | Populated from custodian data but can be modified by users | [optional] 
**firm_id** | **int** | ID of the owning firm | [optional] 
**entity_id** | **str** | See Entiti ID Prefixes | [optional] 
**opening_date** | **datetime** | Date the household was opened | [optional] 
**inception_date** | **datetime** | Date of household inception, if applicable. May differ from opening date | [optional] 
**close_date** | **datetime** | Date the household was closed, if applicable | [optional] 
**status** | **str** | See Account and Household Status Codes. | [optional] 
**benchmarks_ids** | **list[int]** | List of ids for benchmarks associated with the household | [optional] 
**is_account** | **bool** | Is this entity an account? (No) | [optional] 
**is_household** | **bool** | Is this entity a household? (Yes) | [optional] 
**last_reporting_date** | **datetime** | Most recent date that portfolio data was processed for this household | [optional] 
**first_account_reporting_date** | **datetime** | Earliest date that portfolio data was processed among accounts in this household | [optional] 
**last_account_reporting_date** | **datetime** | Most recent date that portfolio data was processed among accounts in this household | [optional] 
**short_name** | **str** | Short name for the household object | [optional] 
**created_at_utc** | **datetime** | Timestamp for when the record was created | [optional] 
**updated_at_utc** | **datetime** | Timestamp for when the record was updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

