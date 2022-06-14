# InlineResponse20048Data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this printable report object | [optional] 
**firm_id** | **int** | ID of the owning firm | [optional] 
**account_id** | **int** | ID of the account that the report is on. Null if household_id is non-null | [optional] 
**household_id** | **int** | ID of the household that the report is on. Null if account_id is non-null | [optional] 
**created_by_user_id** | **int** | ID of the user that created the report | [optional] 
**report_date** | **datetime** | Report date | [optional] 
**frequency** | **str** | See Frequency Codes | [optional] 
**start_date** | **datetime** | start date | [optional] 
**end_date** | **datetime** | End date | [optional] 
**timestamp_utc** | **datetime** | Created/last updated timestamp in UTC | [optional] 
**dt_utc** | **datetime** | Created/last updated timestamp in datetime UTC | [optional] 
**size_bytes** | **int** | Size of the printable report in bytes | [optional] 
**client_accessible** | **bool** | If true, the report is accessible in the client portal | [optional] 
**tags** | **list[str]** | List of specified tags, if applicable (system-generated reports are always untagged) | [optional] 
**sub_reports** | **list[str]** | List of sub-reports included in this printable report | [optional] 
**state** | **str** | 0 if the report is generating, R if it&#x27;s ready, and E if it&#x27;s failed | [optional] 
**error_message** | **str** | Error message if in error state E | [optional] 
**download_url** | **str** | Download link which specifies the url to generate and return a binary stream for the Printable PDF | [optional] 
**created_at_utc** | **datetime** | Timestamp for when the record was created | [optional] 
**updated_at_utc** | **datetime** | Timestamp for when the record was updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

