# FilesFilterBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique resource id for the Shared File | [optional] 
**firm_id** | **int** | The firm id assigned to this Shared File | [optional] 
**uploaded_by_user_id** | **int** | The id of the User that created this Shared File | [optional] 
**sharing_scope** | **str** | Determines whether the sharing of this file is firm-wide (a) or restricted to households (h). See Entity ID Prefixes. | [optional] 
**shared_household_id** | **int** | Set when the file is sharing with the household scope | [optional] 
**size_bytes** | **int** | The size in bytes of this Shared File | [optional] 
**filename** | **str** | The S3 filename for this Shared File | [optional] 
**file_type** | **str** | See Shared File Types | [optional] 
**content_type** | **str** | The content type for this Shared File | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

