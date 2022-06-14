# Assignments

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique resource id for this Account Group Assignment | [optional] 
**account_id** | **int** | The related account of this assignment | [optional] 
**group_id** | **int** | The related group of this assignment | [optional] 
**fee_location** | **int** | Numerical indicator for fee location behavior. Options are 0 (charged to itself), -1 (uncharged / charged to the group, where fees are distributed in prorate fashion by size), or a positive integer, which represents the ID of the account being charged. | [optional] 
**fee_location_option** | **str** | The desired fee location option. Options are S (self), G (group), or A (account). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

