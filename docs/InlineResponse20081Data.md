# InlineResponse20081Data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique resource ID for this Balance object | [optional] 
**as_of_date** | **datetime** | The current date for this Balance | [optional] 
**prior_as_of_date** | **datetime** | The most recent date before the as_of_date | [optional] 
**account_id** | **int** | The id of the Account associated with this Balance | [optional] 
**household_id** | **int** | The id of the Household associated with this Balance. | [optional] 
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
**percentage_period_net_return** | **float** | Daily, net time weighted return | [optional] 
**percentage_period_gross_return** | **float** | Daily, gross time weighted return | [optional] 
**cash_currency_impact** | **float** | Change in cash on as_of_date from all sources (e.g. income, trade activity) | [optional] 
**cash_value** | **float** | Value of cash on as_of_date | [optional] 
**security_holdings_value** | **float** | Market value of securities on as_of_date | [optional] 
**unrealized_gain_loss** | **float** | Value of gain or loss on as_of_date for open positions (calculated as market value of all positions minus cost basis of all positions) | [optional] 
**realized_gain_loss** | **float** | Value of gain or loss from closing transactions | [optional] 
**cash_currency_net_contribution** | **float** | Net cash contribution (i.e. Cash Deposits minus Cash Withdrawals) | [optional] 
**security_net_contribution** | **float** | Net security contributions (i.e. Security Deposits minus Security Withdrawals) | [optional] 
**value** | **float** |  | [optional] 
**created_at_utc** | **datetime** | Timestamp for when the record was created | [optional] 
**updated_at_utc** | **datetime** | Timestamp for when the record was updated | [optional] 
**abs_outside_income** | **float** | Total value of outside income | [optional] 
**abs_outside_expense** | **float** | Total value of outside expense | [optional] 
**abs_initialization_contribution** | **float** | Total value of initialized contribution | [optional] 
**abs_initialization_withdrawal** | **float** | Total value of initialized withdrawal | [optional] 
**manual_holding_appreciation** | **float** | Maunual holding apreciation amount | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

