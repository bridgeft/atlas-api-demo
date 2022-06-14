# InlineResponse200127Data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this strategy object | [optional] 
**name** | **str** | Name for the strategy | [optional] 
**firm_id** | **int** | Id of the firm this strategy is associated with | [optional] 
**description** | **str** | Description of the strategy | [optional] 
**investment_minimum** | **float** | Investment minimum | [optional] 
**fee** | **float** | Fee reported on the strategy | [optional] 
**benchmark_id** | **int** | Id of the benchmark associated with this strategy | [optional] 
**strategy_type** | **str** | Type of the strategy. | [optional] 
**tax_managed** | **bool** | Is the tax managed? | [optional] 
**risk_category** | **str** | Risk category of the strategy. CP for Capital Preservation, CO for Conservative, MC for Moderate Conservative, MO for Moderate, MG for Moderate Growth, GR for Growth, AG for Aggressive Growth | [optional] 
**search_tags** | **list[str]** | Search tags for the strategy | [optional] 
**asset_type** | **str** | Asset type of the strategy | [optional] 
**fact_sheet_available** | **bool** | Is the fact sheet available? | [optional] 
**esg** | **bool** | Is environmental, social, governance? | [optional] 
**etf_action_identifier** | **str** | Identifier for etc action | [optional] 
**security_allocations** | [**list[InlineResponse200127SecurityAllocations]**](InlineResponse200127SecurityAllocations.md) | Security allocation associated with this model | [optional] 
**created_at_utc** | **datetime** | Timestamp for when the record was created | [optional] 
**updated_at_utc** | **datetime** | Timestamp for when the record was updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

