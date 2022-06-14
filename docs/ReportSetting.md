# ReportSetting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this report settings object | [optional] 
**firm_id** | **int** | ID of the owning firm | [optional] 
**user_id** | **int** | ID of the user concerned with creating the report. If null, applied settings will be firm-wide. Otherwise, the settings are specific to the given user | [optional] 
**component** | **str** | Specifies to which area these settings apply (i.e., printable reports, the advisor&#x27;s default settings, the client&#x27;s default settings). Can either be printable, advisor_defaults, client_defaults, or user | [optional] 
**account_summary** | **bool** | Include account summary? | [optional] 
**consolidated_summary** | **bool** | Include consolidated summary? | [optional] 
**performance_summary** | **bool** | Include performance summary? | [optional] 
**benchmark_perf_summary** | **bool** | Include benchmark performance summary? | [optional] 
**performance_chart** | **bool** | Include performance chart? | [optional] 
**appraisals** | **bool** | Include appraisals? | [optional] 
**asset_allocation_top_holdings** | **bool** | Include asset allocation top holdings? | [optional] 
**buy_sells** | **bool** | Include buys and sells? | [optional] 
**deposits_withdrawals** | **bool** | Include deposits and withdrawals? | [optional] 
**income** | **bool** | Include income? | [optional] 
**realized_gain_loss** | **bool** | Include realized gain loss? | [optional] 
**management_fees** | **bool** | Include management fees? | [optional] 
**net_investment_chart** | **bool** | Include net investment chart? | [optional] 
**portfolio_snapshot** | **bool** | Include portfolio snapshot? | [optional] 
**household_performance_attribution** | **bool** | Include household performance attribute? | [optional] 
**target_vs_actual_allocation** | **bool** | Include target vs actual allocation? | [optional] 
**security_performance** | **bool** | Include security performance? | [optional] 
**appraisals_wo_cost_basis** | **bool** | Include appraisals without cost basis? | [optional] 
**risk_return_chart** | **bool** | Include risk return chart? | [optional] 
**security_exclusions** | **bool** | Include security exclusions? | [optional] 
**created_at_utc** | **datetime** | Timestamp for when the record was created | [optional] 
**updated_at_utc** | **datetime** | Timestamp for when the record was updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

