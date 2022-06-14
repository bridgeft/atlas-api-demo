# InlineResponse20086Data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique resource ID for this Historical Balance object | [optional] 
**as_of_date** | **datetime** | The current date for this Historical Balance | [optional] 
**prior_as_of_date** | **datetime** | The most recent date before the as_of_date | [optional] 
**account_id** | **int** | The id of the Account associated with this Historical Balance | [optional] 
**household_id** | **int** | The id of the Household associated with this Historical Balance | [optional] 
**beginning_period_value** | **float** | The beginning value of on the as_of_date. This is equal to the ending_period_value on the prior_as_of_date | [optional] 
**ending_period_value** | **float** | The ending value on the as_of_date | [optional] 
**abs_cash_currency_contribution** | **float** | Total value of cash deposits | [optional] 
**abs_cash_currency_withdrawal** | **float** | Total value of cash withdrawals | [optional] 
**abs_security_contribution** | **float** | Total value of security deposits | [optional] 
**abs_security_withdrawal** | **float** | Total value of security withdrawals | [optional] 
**abs_income** | **float** | Total value of performance affecting income (e.g. dividends, interest) | [optional] 
**abs_expense** | **float** | Total value of performance affecting expenses (e.g. ADR fees) | [optional] 
**abs_non_performance_income** | **float** | Total value of non-performance affecting income (e.g. return of principle) | [optional] 
**abs_non_performance_expense** | **float** | Total value of non-performance affecting expenses (e.g. tax withholding) | [optional] 
**total_fee** | **float** | Total value of management fees | [optional] 
**percentage_period_net_return** | **float** | Net return for period (note can be monthly, daily - depends on what data is provided) | [optional] 
**percentage_period_gross_return** | **float** | Gross return for period (note can be monthly, daily - depends on what data is provided) | [optional] 
**total_contribution** | **float** | Total cash and security contributions | [optional] 
**total_withdrawal** | **float** | Total cash and security withdrawals | [optional] 
**custodian** | **str** | Custodian the account data comes from TDA&#x3D;TD Ameritrade, SWB&#x3D;Schwab, NFS&#x3D;Fidelity, PER&#x3D;Pershing, MLT&#x3D;MillenniumTrust, RJA&#x3D;RaymondJames, HDG&#x3D;Manual | [optional] 
**account_number** | **str** | Account number at the custodian | [optional] 
**frequency** | **str** | Frequency of return provided (e.g. M for monthly) | [optional] 
**contribution_period_weight** | **float** | Used to represent timing of cash flow in a month. Potential values 1 &#x3D; end of month, 0.5 &#x3D; mid-month, 0 &#x3D; beginning of month | [optional] 
**withdrawal_period_weight** | **float** | Used to represent timing of cash flow in a month. Potential values 1 &#x3D; end of month, 0.5 &#x3D; mid-month, 0 &#x3D; beginning of month | [optional] 
**npni_period_weight** | **float** | Used to represent timing of cash flow in a month. Potential values 1 &#x3D; end of month, 0.5 &#x3D; mid-month, 0 &#x3D; beginning of month | [optional] 
**created_at_utc** | **datetime** | Timestamp for when the record was created | [optional] 
**updated_at_utc** | **datetime** | Timestamp for when the record was updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

