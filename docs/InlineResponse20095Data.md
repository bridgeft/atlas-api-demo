# InlineResponse20095Data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this user object | [optional] 
**firm_id** | **int** | ID of the owning firm | [optional] 
**account_access_level** | **str** | The user&#x27;s accessibility level with respect to accounts; can either have access to all accounts or be limited to a subset of them. Can either be all or limited. | [optional] 
**accessible_household_ids** | **list[int]** | If the user is limited to a subset of accounts, these are the accessible households | [optional] 
**permissions** | **list[str]** | Editable list of permissions assigned to the user. See Permissions Overview. | [optional] 
**granted_permissions** | **list[str]** | Read-only list of permissions that govern the user&#x27;s actual permissions, which are intersected with firm permissions. See Permissions Overview. | [optional] 
**is_owner** | **bool** | Is this user the owner of the associated firm? (Always false for a client) | [optional] 
**end_client_household_id** | **int** | The household of the end client. All client users should have a reference to the household. | [optional] 
**household_id** | **int** | Alias for end_client_household_id | [optional] 
**role_id** | **int** | The ID of the user-defined role. | [optional] 
**is_firm_user** | **bool** | Is the user an employee of the managing firm? (No) | [optional] 
**is_client_user** | **bool** | Is the user a client of the managing firm? (Yes) | [optional] 
**is_demo_user** | **bool** | Is the user a demo user? | [optional] 
**is_verified** | **bool** | Does the user have access to the account? | [optional] 
**verified_dt_utc** | **datetime** | Timestamp in UTC of when the user was verified. | [optional] 
**role_name** | **str** | The role of the user. Can either be end_client for client users, or firm_user for firm users. In this case it should be end_client. | [optional] 
**first_name** | **str** | User first name | [optional] 
**last_name** | **str** | User last name | [optional] 
**full_name** | **str** | User full name | [optional] 
**email** | **str** | User email | [optional] 
**is_active** | **bool** | Is the client user active? | [optional] 
**last_login** | **datetime** | Time when the client last logged in | [optional] 
**date_joined** | **datetime** | Date when the client joined | [optional] 
**usage_tier** | **str** | Usage teir associated with this user | [optional] 
**created_at_utc** | **datetime** | Timestamp for when the record was created | [optional] 
**updated_at_utc** | **datetime** | Timestamp for when the record was updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

