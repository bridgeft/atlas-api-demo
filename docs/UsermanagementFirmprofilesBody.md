# UsermanagementFirmprofilesBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firm_id** | **int** | ID of the owning firm | [optional] 
**account_access_level** | **str** | The user&#x27;s accessibility level with respect to accounts; can either have access to all accounts or be limited to a subset of them. Can either be all or limited. | [optional] 
**accessible_household_ids** | **list[int]** | If the user is limited to a subset of accounts, these are the accessible households | [optional] 
**permissions** | **list[str]** | Editable list of permissions assigned to the user. See Permissions Overview. | [optional] 
**is_owner** | **bool** | Is this user the owner of the associated firm? (Always false for a client) | [optional] 
**role_id** | **int** | The ID of the user-defined role. | [optional] 
**first_name** | **str** | User first name | [optional] 
**last_name** | **str** | User last name | [optional] 
**email** | **str** | User email | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

