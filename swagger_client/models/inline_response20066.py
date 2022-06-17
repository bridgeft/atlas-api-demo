# coding: utf-8

"""
    Atlas API

    RESTful API for controlling and interacting with Atlas data  # noqa: E501

    OpenAPI spec version: 2.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse20066(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'as_of_date': 'datetime',
        'prior_as_of_date': 'datetime',
        'account_id': 'int',
        'household_id': 'int',
        'beginning_period_value': 'float',
        'ending_period_value': 'float',
        'abs_cash_currency_contribution': 'float',
        'abs_cash_currency_withdrawal': 'float',
        'abs_security_contribution': 'float',
        'abs_security_withdrawal': 'float',
        'abs_income': 'float',
        'abs_expense': 'float',
        'abs_non_performance_income': 'float',
        'abs_non_performance_expense': 'float',
        'total_fee': 'float',
        'percentage_period_net_return': 'float',
        'percentage_period_gross_return': 'float',
        'cash_currency_impact': 'float',
        'cash_value': 'float',
        'security_holdings_value': 'float',
        'unrealized_gain_loss': 'float',
        'realized_gain_loss': 'float',
        'cash_currency_net_contribution': 'float',
        'security_net_contribution': 'float',
        'value': 'float',
        'created_at_utc': 'datetime',
        'updated_at_utc': 'datetime',
        'abs_outside_income': 'float',
        'abs_outside_expense': 'float',
        'abs_initialization_contribution': 'float',
        'abs_initialization_withdrawal': 'float',
        'manual_holding_appreciation': 'float'
    }

    attribute_map = {
        'id': 'id',
        'as_of_date': 'as_of_date',
        'prior_as_of_date': 'prior_as_of_date',
        'account_id': 'account_id',
        'household_id': 'household_id',
        'beginning_period_value': 'beginning_period_value',
        'ending_period_value': 'ending_period_value',
        'abs_cash_currency_contribution': 'abs_cash_currency_contribution',
        'abs_cash_currency_withdrawal': 'abs_cash_currency_withdrawal',
        'abs_security_contribution': 'abs_security_contribution',
        'abs_security_withdrawal': 'abs_security_withdrawal',
        'abs_income': 'abs_income',
        'abs_expense': 'abs_expense',
        'abs_non_performance_income': 'abs_non_performance_income',
        'abs_non_performance_expense': 'abs_non_performance_expense',
        'total_fee': 'total_fee',
        'percentage_period_net_return': 'percentage_period_net_return',
        'percentage_period_gross_return': 'percentage_period_gross_return',
        'cash_currency_impact': 'cash_currency_impact',
        'cash_value': 'cash_value',
        'security_holdings_value': 'security_holdings_value',
        'unrealized_gain_loss': 'unrealized_gain_loss',
        'realized_gain_loss': 'realized_gain_loss',
        'cash_currency_net_contribution': 'cash_currency_net_contribution',
        'security_net_contribution': 'security_net_contribution',
        'value': 'value',
        'created_at_utc': 'created_at_utc',
        'updated_at_utc': 'updated_at_utc',
        'abs_outside_income': 'abs_outside_income',
        'abs_outside_expense': 'abs_outside_expense',
        'abs_initialization_contribution': 'abs_initialization_contribution',
        'abs_initialization_withdrawal': 'abs_initialization_withdrawal',
        'manual_holding_appreciation': 'manual_holding_appreciation'
    }

    def __init__(self, id=None, as_of_date=None, prior_as_of_date=None, account_id=None, household_id=None, beginning_period_value=None, ending_period_value=None, abs_cash_currency_contribution=None, abs_cash_currency_withdrawal=None, abs_security_contribution=None, abs_security_withdrawal=None, abs_income=None, abs_expense=None, abs_non_performance_income=None, abs_non_performance_expense=None, total_fee=None, percentage_period_net_return=None, percentage_period_gross_return=None, cash_currency_impact=None, cash_value=None, security_holdings_value=None, unrealized_gain_loss=None, realized_gain_loss=None, cash_currency_net_contribution=None, security_net_contribution=None, value=None, created_at_utc=None, updated_at_utc=None, abs_outside_income=None, abs_outside_expense=None, abs_initialization_contribution=None, abs_initialization_withdrawal=None, manual_holding_appreciation=None):  # noqa: E501
        """InlineResponse20066 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._as_of_date = None
        self._prior_as_of_date = None
        self._account_id = None
        self._household_id = None
        self._beginning_period_value = None
        self._ending_period_value = None
        self._abs_cash_currency_contribution = None
        self._abs_cash_currency_withdrawal = None
        self._abs_security_contribution = None
        self._abs_security_withdrawal = None
        self._abs_income = None
        self._abs_expense = None
        self._abs_non_performance_income = None
        self._abs_non_performance_expense = None
        self._total_fee = None
        self._percentage_period_net_return = None
        self._percentage_period_gross_return = None
        self._cash_currency_impact = None
        self._cash_value = None
        self._security_holdings_value = None
        self._unrealized_gain_loss = None
        self._realized_gain_loss = None
        self._cash_currency_net_contribution = None
        self._security_net_contribution = None
        self._value = None
        self._created_at_utc = None
        self._updated_at_utc = None
        self._abs_outside_income = None
        self._abs_outside_expense = None
        self._abs_initialization_contribution = None
        self._abs_initialization_withdrawal = None
        self._manual_holding_appreciation = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if as_of_date is not None:
            self.as_of_date = as_of_date
        if prior_as_of_date is not None:
            self.prior_as_of_date = prior_as_of_date
        if account_id is not None:
            self.account_id = account_id
        if household_id is not None:
            self.household_id = household_id
        if beginning_period_value is not None:
            self.beginning_period_value = beginning_period_value
        if ending_period_value is not None:
            self.ending_period_value = ending_period_value
        if abs_cash_currency_contribution is not None:
            self.abs_cash_currency_contribution = abs_cash_currency_contribution
        if abs_cash_currency_withdrawal is not None:
            self.abs_cash_currency_withdrawal = abs_cash_currency_withdrawal
        if abs_security_contribution is not None:
            self.abs_security_contribution = abs_security_contribution
        if abs_security_withdrawal is not None:
            self.abs_security_withdrawal = abs_security_withdrawal
        if abs_income is not None:
            self.abs_income = abs_income
        if abs_expense is not None:
            self.abs_expense = abs_expense
        if abs_non_performance_income is not None:
            self.abs_non_performance_income = abs_non_performance_income
        if abs_non_performance_expense is not None:
            self.abs_non_performance_expense = abs_non_performance_expense
        if total_fee is not None:
            self.total_fee = total_fee
        if percentage_period_net_return is not None:
            self.percentage_period_net_return = percentage_period_net_return
        if percentage_period_gross_return is not None:
            self.percentage_period_gross_return = percentage_period_gross_return
        if cash_currency_impact is not None:
            self.cash_currency_impact = cash_currency_impact
        if cash_value is not None:
            self.cash_value = cash_value
        if security_holdings_value is not None:
            self.security_holdings_value = security_holdings_value
        if unrealized_gain_loss is not None:
            self.unrealized_gain_loss = unrealized_gain_loss
        if realized_gain_loss is not None:
            self.realized_gain_loss = realized_gain_loss
        if cash_currency_net_contribution is not None:
            self.cash_currency_net_contribution = cash_currency_net_contribution
        if security_net_contribution is not None:
            self.security_net_contribution = security_net_contribution
        if value is not None:
            self.value = value
        if created_at_utc is not None:
            self.created_at_utc = created_at_utc
        if updated_at_utc is not None:
            self.updated_at_utc = updated_at_utc
        if abs_outside_income is not None:
            self.abs_outside_income = abs_outside_income
        if abs_outside_expense is not None:
            self.abs_outside_expense = abs_outside_expense
        if abs_initialization_contribution is not None:
            self.abs_initialization_contribution = abs_initialization_contribution
        if abs_initialization_withdrawal is not None:
            self.abs_initialization_withdrawal = abs_initialization_withdrawal
        if manual_holding_appreciation is not None:
            self.manual_holding_appreciation = manual_holding_appreciation

    @property
    def id(self):
        """Gets the id of this InlineResponse20066.  # noqa: E501

        The unique resource ID for this Balance object  # noqa: E501

        :return: The id of this InlineResponse20066.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20066.

        The unique resource ID for this Balance object  # noqa: E501

        :param id: The id of this InlineResponse20066.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def as_of_date(self):
        """Gets the as_of_date of this InlineResponse20066.  # noqa: E501

        The current date for this Balance  # noqa: E501

        :return: The as_of_date of this InlineResponse20066.  # noqa: E501
        :rtype: datetime
        """
        return self._as_of_date

    @as_of_date.setter
    def as_of_date(self, as_of_date):
        """Sets the as_of_date of this InlineResponse20066.

        The current date for this Balance  # noqa: E501

        :param as_of_date: The as_of_date of this InlineResponse20066.  # noqa: E501
        :type: datetime
        """

        self._as_of_date = as_of_date

    @property
    def prior_as_of_date(self):
        """Gets the prior_as_of_date of this InlineResponse20066.  # noqa: E501

        The most recent date before the as_of_date  # noqa: E501

        :return: The prior_as_of_date of this InlineResponse20066.  # noqa: E501
        :rtype: datetime
        """
        return self._prior_as_of_date

    @prior_as_of_date.setter
    def prior_as_of_date(self, prior_as_of_date):
        """Sets the prior_as_of_date of this InlineResponse20066.

        The most recent date before the as_of_date  # noqa: E501

        :param prior_as_of_date: The prior_as_of_date of this InlineResponse20066.  # noqa: E501
        :type: datetime
        """

        self._prior_as_of_date = prior_as_of_date

    @property
    def account_id(self):
        """Gets the account_id of this InlineResponse20066.  # noqa: E501

        The id of the Account associated with this Balance  # noqa: E501

        :return: The account_id of this InlineResponse20066.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this InlineResponse20066.

        The id of the Account associated with this Balance  # noqa: E501

        :param account_id: The account_id of this InlineResponse20066.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def household_id(self):
        """Gets the household_id of this InlineResponse20066.  # noqa: E501

        The id of the Household associated with this Balance.  # noqa: E501

        :return: The household_id of this InlineResponse20066.  # noqa: E501
        :rtype: int
        """
        return self._household_id

    @household_id.setter
    def household_id(self, household_id):
        """Sets the household_id of this InlineResponse20066.

        The id of the Household associated with this Balance.  # noqa: E501

        :param household_id: The household_id of this InlineResponse20066.  # noqa: E501
        :type: int
        """

        self._household_id = household_id

    @property
    def beginning_period_value(self):
        """Gets the beginning_period_value of this InlineResponse20066.  # noqa: E501

        The beginning value of on the as_of_date. This is equal to the ending_period_value on the prior_as_of_date  # noqa: E501

        :return: The beginning_period_value of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._beginning_period_value

    @beginning_period_value.setter
    def beginning_period_value(self, beginning_period_value):
        """Sets the beginning_period_value of this InlineResponse20066.

        The beginning value of on the as_of_date. This is equal to the ending_period_value on the prior_as_of_date  # noqa: E501

        :param beginning_period_value: The beginning_period_value of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._beginning_period_value = beginning_period_value

    @property
    def ending_period_value(self):
        """Gets the ending_period_value of this InlineResponse20066.  # noqa: E501

        The ending value on the as_of_date  # noqa: E501

        :return: The ending_period_value of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._ending_period_value

    @ending_period_value.setter
    def ending_period_value(self, ending_period_value):
        """Sets the ending_period_value of this InlineResponse20066.

        The ending value on the as_of_date  # noqa: E501

        :param ending_period_value: The ending_period_value of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._ending_period_value = ending_period_value

    @property
    def abs_cash_currency_contribution(self):
        """Gets the abs_cash_currency_contribution of this InlineResponse20066.  # noqa: E501

        Total value of cash deposits  # noqa: E501

        :return: The abs_cash_currency_contribution of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._abs_cash_currency_contribution

    @abs_cash_currency_contribution.setter
    def abs_cash_currency_contribution(self, abs_cash_currency_contribution):
        """Sets the abs_cash_currency_contribution of this InlineResponse20066.

        Total value of cash deposits  # noqa: E501

        :param abs_cash_currency_contribution: The abs_cash_currency_contribution of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._abs_cash_currency_contribution = abs_cash_currency_contribution

    @property
    def abs_cash_currency_withdrawal(self):
        """Gets the abs_cash_currency_withdrawal of this InlineResponse20066.  # noqa: E501

        Total value of cash withdrawals  # noqa: E501

        :return: The abs_cash_currency_withdrawal of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._abs_cash_currency_withdrawal

    @abs_cash_currency_withdrawal.setter
    def abs_cash_currency_withdrawal(self, abs_cash_currency_withdrawal):
        """Sets the abs_cash_currency_withdrawal of this InlineResponse20066.

        Total value of cash withdrawals  # noqa: E501

        :param abs_cash_currency_withdrawal: The abs_cash_currency_withdrawal of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._abs_cash_currency_withdrawal = abs_cash_currency_withdrawal

    @property
    def abs_security_contribution(self):
        """Gets the abs_security_contribution of this InlineResponse20066.  # noqa: E501

        Total value of security deposits  # noqa: E501

        :return: The abs_security_contribution of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._abs_security_contribution

    @abs_security_contribution.setter
    def abs_security_contribution(self, abs_security_contribution):
        """Sets the abs_security_contribution of this InlineResponse20066.

        Total value of security deposits  # noqa: E501

        :param abs_security_contribution: The abs_security_contribution of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._abs_security_contribution = abs_security_contribution

    @property
    def abs_security_withdrawal(self):
        """Gets the abs_security_withdrawal of this InlineResponse20066.  # noqa: E501

        Total value of security withdrawals  # noqa: E501

        :return: The abs_security_withdrawal of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._abs_security_withdrawal

    @abs_security_withdrawal.setter
    def abs_security_withdrawal(self, abs_security_withdrawal):
        """Sets the abs_security_withdrawal of this InlineResponse20066.

        Total value of security withdrawals  # noqa: E501

        :param abs_security_withdrawal: The abs_security_withdrawal of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._abs_security_withdrawal = abs_security_withdrawal

    @property
    def abs_income(self):
        """Gets the abs_income of this InlineResponse20066.  # noqa: E501

        Total value of performance affecting income (e.g. dividends, interest)  # noqa: E501

        :return: The abs_income of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._abs_income

    @abs_income.setter
    def abs_income(self, abs_income):
        """Sets the abs_income of this InlineResponse20066.

        Total value of performance affecting income (e.g. dividends, interest)  # noqa: E501

        :param abs_income: The abs_income of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._abs_income = abs_income

    @property
    def abs_expense(self):
        """Gets the abs_expense of this InlineResponse20066.  # noqa: E501

        Total value of performance affecting expenses (e.g. ADR fees)  # noqa: E501

        :return: The abs_expense of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._abs_expense

    @abs_expense.setter
    def abs_expense(self, abs_expense):
        """Sets the abs_expense of this InlineResponse20066.

        Total value of performance affecting expenses (e.g. ADR fees)  # noqa: E501

        :param abs_expense: The abs_expense of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._abs_expense = abs_expense

    @property
    def abs_non_performance_income(self):
        """Gets the abs_non_performance_income of this InlineResponse20066.  # noqa: E501

        Total value of non-performance affecting income (e.g. return of principle)  # noqa: E501

        :return: The abs_non_performance_income of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._abs_non_performance_income

    @abs_non_performance_income.setter
    def abs_non_performance_income(self, abs_non_performance_income):
        """Sets the abs_non_performance_income of this InlineResponse20066.

        Total value of non-performance affecting income (e.g. return of principle)  # noqa: E501

        :param abs_non_performance_income: The abs_non_performance_income of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._abs_non_performance_income = abs_non_performance_income

    @property
    def abs_non_performance_expense(self):
        """Gets the abs_non_performance_expense of this InlineResponse20066.  # noqa: E501

        Total value of non-performance affecting expenses (e.g. tax withholding)  # noqa: E501

        :return: The abs_non_performance_expense of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._abs_non_performance_expense

    @abs_non_performance_expense.setter
    def abs_non_performance_expense(self, abs_non_performance_expense):
        """Sets the abs_non_performance_expense of this InlineResponse20066.

        Total value of non-performance affecting expenses (e.g. tax withholding)  # noqa: E501

        :param abs_non_performance_expense: The abs_non_performance_expense of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._abs_non_performance_expense = abs_non_performance_expense

    @property
    def total_fee(self):
        """Gets the total_fee of this InlineResponse20066.  # noqa: E501

        Total value of management fees  # noqa: E501

        :return: The total_fee of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._total_fee

    @total_fee.setter
    def total_fee(self, total_fee):
        """Sets the total_fee of this InlineResponse20066.

        Total value of management fees  # noqa: E501

        :param total_fee: The total_fee of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._total_fee = total_fee

    @property
    def percentage_period_net_return(self):
        """Gets the percentage_period_net_return of this InlineResponse20066.  # noqa: E501

        Daily, net time weighted return  # noqa: E501

        :return: The percentage_period_net_return of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._percentage_period_net_return

    @percentage_period_net_return.setter
    def percentage_period_net_return(self, percentage_period_net_return):
        """Sets the percentage_period_net_return of this InlineResponse20066.

        Daily, net time weighted return  # noqa: E501

        :param percentage_period_net_return: The percentage_period_net_return of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._percentage_period_net_return = percentage_period_net_return

    @property
    def percentage_period_gross_return(self):
        """Gets the percentage_period_gross_return of this InlineResponse20066.  # noqa: E501

        Daily, gross time weighted return  # noqa: E501

        :return: The percentage_period_gross_return of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._percentage_period_gross_return

    @percentage_period_gross_return.setter
    def percentage_period_gross_return(self, percentage_period_gross_return):
        """Sets the percentage_period_gross_return of this InlineResponse20066.

        Daily, gross time weighted return  # noqa: E501

        :param percentage_period_gross_return: The percentage_period_gross_return of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._percentage_period_gross_return = percentage_period_gross_return

    @property
    def cash_currency_impact(self):
        """Gets the cash_currency_impact of this InlineResponse20066.  # noqa: E501

        Change in cash on as_of_date from all sources (e.g. income, trade activity)  # noqa: E501

        :return: The cash_currency_impact of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._cash_currency_impact

    @cash_currency_impact.setter
    def cash_currency_impact(self, cash_currency_impact):
        """Sets the cash_currency_impact of this InlineResponse20066.

        Change in cash on as_of_date from all sources (e.g. income, trade activity)  # noqa: E501

        :param cash_currency_impact: The cash_currency_impact of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._cash_currency_impact = cash_currency_impact

    @property
    def cash_value(self):
        """Gets the cash_value of this InlineResponse20066.  # noqa: E501

        Value of cash on as_of_date  # noqa: E501

        :return: The cash_value of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._cash_value

    @cash_value.setter
    def cash_value(self, cash_value):
        """Sets the cash_value of this InlineResponse20066.

        Value of cash on as_of_date  # noqa: E501

        :param cash_value: The cash_value of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._cash_value = cash_value

    @property
    def security_holdings_value(self):
        """Gets the security_holdings_value of this InlineResponse20066.  # noqa: E501

        Market value of securities on as_of_date  # noqa: E501

        :return: The security_holdings_value of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._security_holdings_value

    @security_holdings_value.setter
    def security_holdings_value(self, security_holdings_value):
        """Sets the security_holdings_value of this InlineResponse20066.

        Market value of securities on as_of_date  # noqa: E501

        :param security_holdings_value: The security_holdings_value of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._security_holdings_value = security_holdings_value

    @property
    def unrealized_gain_loss(self):
        """Gets the unrealized_gain_loss of this InlineResponse20066.  # noqa: E501

        Value of gain or loss on as_of_date for open positions (calculated as market value of all positions minus cost basis of all positions)  # noqa: E501

        :return: The unrealized_gain_loss of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._unrealized_gain_loss

    @unrealized_gain_loss.setter
    def unrealized_gain_loss(self, unrealized_gain_loss):
        """Sets the unrealized_gain_loss of this InlineResponse20066.

        Value of gain or loss on as_of_date for open positions (calculated as market value of all positions minus cost basis of all positions)  # noqa: E501

        :param unrealized_gain_loss: The unrealized_gain_loss of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._unrealized_gain_loss = unrealized_gain_loss

    @property
    def realized_gain_loss(self):
        """Gets the realized_gain_loss of this InlineResponse20066.  # noqa: E501

        Value of gain or loss from closing transactions  # noqa: E501

        :return: The realized_gain_loss of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._realized_gain_loss

    @realized_gain_loss.setter
    def realized_gain_loss(self, realized_gain_loss):
        """Sets the realized_gain_loss of this InlineResponse20066.

        Value of gain or loss from closing transactions  # noqa: E501

        :param realized_gain_loss: The realized_gain_loss of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._realized_gain_loss = realized_gain_loss

    @property
    def cash_currency_net_contribution(self):
        """Gets the cash_currency_net_contribution of this InlineResponse20066.  # noqa: E501

        Net cash contribution (i.e. Cash Deposits minus Cash Withdrawals)  # noqa: E501

        :return: The cash_currency_net_contribution of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._cash_currency_net_contribution

    @cash_currency_net_contribution.setter
    def cash_currency_net_contribution(self, cash_currency_net_contribution):
        """Sets the cash_currency_net_contribution of this InlineResponse20066.

        Net cash contribution (i.e. Cash Deposits minus Cash Withdrawals)  # noqa: E501

        :param cash_currency_net_contribution: The cash_currency_net_contribution of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._cash_currency_net_contribution = cash_currency_net_contribution

    @property
    def security_net_contribution(self):
        """Gets the security_net_contribution of this InlineResponse20066.  # noqa: E501

        Net security contributions (i.e. Security Deposits minus Security Withdrawals)  # noqa: E501

        :return: The security_net_contribution of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._security_net_contribution

    @security_net_contribution.setter
    def security_net_contribution(self, security_net_contribution):
        """Sets the security_net_contribution of this InlineResponse20066.

        Net security contributions (i.e. Security Deposits minus Security Withdrawals)  # noqa: E501

        :param security_net_contribution: The security_net_contribution of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._security_net_contribution = security_net_contribution

    @property
    def value(self):
        """Gets the value of this InlineResponse20066.  # noqa: E501


        :return: The value of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this InlineResponse20066.


        :param value: The value of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def created_at_utc(self):
        """Gets the created_at_utc of this InlineResponse20066.  # noqa: E501

        Timestamp for when the record was created  # noqa: E501

        :return: The created_at_utc of this InlineResponse20066.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at_utc

    @created_at_utc.setter
    def created_at_utc(self, created_at_utc):
        """Sets the created_at_utc of this InlineResponse20066.

        Timestamp for when the record was created  # noqa: E501

        :param created_at_utc: The created_at_utc of this InlineResponse20066.  # noqa: E501
        :type: datetime
        """

        self._created_at_utc = created_at_utc

    @property
    def updated_at_utc(self):
        """Gets the updated_at_utc of this InlineResponse20066.  # noqa: E501

        Timestamp for when the record was updated  # noqa: E501

        :return: The updated_at_utc of this InlineResponse20066.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_utc

    @updated_at_utc.setter
    def updated_at_utc(self, updated_at_utc):
        """Sets the updated_at_utc of this InlineResponse20066.

        Timestamp for when the record was updated  # noqa: E501

        :param updated_at_utc: The updated_at_utc of this InlineResponse20066.  # noqa: E501
        :type: datetime
        """

        self._updated_at_utc = updated_at_utc

    @property
    def abs_outside_income(self):
        """Gets the abs_outside_income of this InlineResponse20066.  # noqa: E501

        Total value of outside income  # noqa: E501

        :return: The abs_outside_income of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._abs_outside_income

    @abs_outside_income.setter
    def abs_outside_income(self, abs_outside_income):
        """Sets the abs_outside_income of this InlineResponse20066.

        Total value of outside income  # noqa: E501

        :param abs_outside_income: The abs_outside_income of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._abs_outside_income = abs_outside_income

    @property
    def abs_outside_expense(self):
        """Gets the abs_outside_expense of this InlineResponse20066.  # noqa: E501

        Total value of outside expense  # noqa: E501

        :return: The abs_outside_expense of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._abs_outside_expense

    @abs_outside_expense.setter
    def abs_outside_expense(self, abs_outside_expense):
        """Sets the abs_outside_expense of this InlineResponse20066.

        Total value of outside expense  # noqa: E501

        :param abs_outside_expense: The abs_outside_expense of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._abs_outside_expense = abs_outside_expense

    @property
    def abs_initialization_contribution(self):
        """Gets the abs_initialization_contribution of this InlineResponse20066.  # noqa: E501

        Total value of initialized contribution  # noqa: E501

        :return: The abs_initialization_contribution of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._abs_initialization_contribution

    @abs_initialization_contribution.setter
    def abs_initialization_contribution(self, abs_initialization_contribution):
        """Sets the abs_initialization_contribution of this InlineResponse20066.

        Total value of initialized contribution  # noqa: E501

        :param abs_initialization_contribution: The abs_initialization_contribution of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._abs_initialization_contribution = abs_initialization_contribution

    @property
    def abs_initialization_withdrawal(self):
        """Gets the abs_initialization_withdrawal of this InlineResponse20066.  # noqa: E501

        Total value of initialized withdrawal  # noqa: E501

        :return: The abs_initialization_withdrawal of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._abs_initialization_withdrawal

    @abs_initialization_withdrawal.setter
    def abs_initialization_withdrawal(self, abs_initialization_withdrawal):
        """Sets the abs_initialization_withdrawal of this InlineResponse20066.

        Total value of initialized withdrawal  # noqa: E501

        :param abs_initialization_withdrawal: The abs_initialization_withdrawal of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._abs_initialization_withdrawal = abs_initialization_withdrawal

    @property
    def manual_holding_appreciation(self):
        """Gets the manual_holding_appreciation of this InlineResponse20066.  # noqa: E501

        Maunual holding apreciation amount  # noqa: E501

        :return: The manual_holding_appreciation of this InlineResponse20066.  # noqa: E501
        :rtype: float
        """
        return self._manual_holding_appreciation

    @manual_holding_appreciation.setter
    def manual_holding_appreciation(self, manual_holding_appreciation):
        """Sets the manual_holding_appreciation of this InlineResponse20066.

        Maunual holding apreciation amount  # noqa: E501

        :param manual_holding_appreciation: The manual_holding_appreciation of this InlineResponse20066.  # noqa: E501
        :type: float
        """

        self._manual_holding_appreciation = manual_holding_appreciation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse20066, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse20066):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
