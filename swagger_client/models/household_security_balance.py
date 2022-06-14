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

class HouseholdSecurityBalance(object):
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
        'as_of_date': 'datetime',
        'household_id': 'int',
        'security_id': 'int',
        'units': 'float',
        'realized_gl': 'float',
        'abs_income': 'float',
        'abs_expense': 'float',
        'appraised_unit_price': 'float',
        'appraised_value': 'float',
        'beginning_value': 'float',
        'holding_period_return': 'float',
        'transfer_out_unrealized_gain_loss': 'float'
    }

    attribute_map = {
        'as_of_date': 'as_of_date',
        'household_id': 'household_id',
        'security_id': 'security_id',
        'units': 'units',
        'realized_gl': 'realized_gl',
        'abs_income': 'abs_income',
        'abs_expense': 'abs_expense',
        'appraised_unit_price': 'appraised_unit_price',
        'appraised_value': 'appraised_value',
        'beginning_value': 'beginning_value',
        'holding_period_return': 'holding_period_return',
        'transfer_out_unrealized_gain_loss': 'transfer_out_unrealized_gain_loss'
    }

    def __init__(self, as_of_date=None, household_id=None, security_id=None, units=None, realized_gl=None, abs_income=None, abs_expense=None, appraised_unit_price=None, appraised_value=None, beginning_value=None, holding_period_return=None, transfer_out_unrealized_gain_loss=None):  # noqa: E501
        """HouseholdSecurityBalance - a model defined in Swagger"""  # noqa: E501
        self._as_of_date = None
        self._household_id = None
        self._security_id = None
        self._units = None
        self._realized_gl = None
        self._abs_income = None
        self._abs_expense = None
        self._appraised_unit_price = None
        self._appraised_value = None
        self._beginning_value = None
        self._holding_period_return = None
        self._transfer_out_unrealized_gain_loss = None
        self.discriminator = None
        if as_of_date is not None:
            self.as_of_date = as_of_date
        if household_id is not None:
            self.household_id = household_id
        if security_id is not None:
            self.security_id = security_id
        if units is not None:
            self.units = units
        if realized_gl is not None:
            self.realized_gl = realized_gl
        if abs_income is not None:
            self.abs_income = abs_income
        if abs_expense is not None:
            self.abs_expense = abs_expense
        if appraised_unit_price is not None:
            self.appraised_unit_price = appraised_unit_price
        if appraised_value is not None:
            self.appraised_value = appraised_value
        if beginning_value is not None:
            self.beginning_value = beginning_value
        if holding_period_return is not None:
            self.holding_period_return = holding_period_return
        if transfer_out_unrealized_gain_loss is not None:
            self.transfer_out_unrealized_gain_loss = transfer_out_unrealized_gain_loss

    @property
    def as_of_date(self):
        """Gets the as_of_date of this HouseholdSecurityBalance.  # noqa: E501

        The current date for this Security Balance  # noqa: E501

        :return: The as_of_date of this HouseholdSecurityBalance.  # noqa: E501
        :rtype: datetime
        """
        return self._as_of_date

    @as_of_date.setter
    def as_of_date(self, as_of_date):
        """Sets the as_of_date of this HouseholdSecurityBalance.

        The current date for this Security Balance  # noqa: E501

        :param as_of_date: The as_of_date of this HouseholdSecurityBalance.  # noqa: E501
        :type: datetime
        """

        self._as_of_date = as_of_date

    @property
    def household_id(self):
        """Gets the household_id of this HouseholdSecurityBalance.  # noqa: E501

        The id of the Household associated with this Security Balance  # noqa: E501

        :return: The household_id of this HouseholdSecurityBalance.  # noqa: E501
        :rtype: int
        """
        return self._household_id

    @household_id.setter
    def household_id(self, household_id):
        """Sets the household_id of this HouseholdSecurityBalance.

        The id of the Household associated with this Security Balance  # noqa: E501

        :param household_id: The household_id of this HouseholdSecurityBalance.  # noqa: E501
        :type: int
        """

        self._household_id = household_id

    @property
    def security_id(self):
        """Gets the security_id of this HouseholdSecurityBalance.  # noqa: E501

        The id of the Security associated with this Security Balance  # noqa: E501

        :return: The security_id of this HouseholdSecurityBalance.  # noqa: E501
        :rtype: int
        """
        return self._security_id

    @security_id.setter
    def security_id(self, security_id):
        """Sets the security_id of this HouseholdSecurityBalance.

        The id of the Security associated with this Security Balance  # noqa: E501

        :param security_id: The security_id of this HouseholdSecurityBalance.  # noqa: E501
        :type: int
        """

        self._security_id = security_id

    @property
    def units(self):
        """Gets the units of this HouseholdSecurityBalance.  # noqa: E501

        The number of shares  # noqa: E501

        :return: The units of this HouseholdSecurityBalance.  # noqa: E501
        :rtype: float
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this HouseholdSecurityBalance.

        The number of shares  # noqa: E501

        :param units: The units of this HouseholdSecurityBalance.  # noqa: E501
        :type: float
        """

        self._units = units

    @property
    def realized_gl(self):
        """Gets the realized_gl of this HouseholdSecurityBalance.  # noqa: E501

        Aggregates from Gain Loss end point; dollar gain or loss from trade activity  # noqa: E501

        :return: The realized_gl of this HouseholdSecurityBalance.  # noqa: E501
        :rtype: float
        """
        return self._realized_gl

    @realized_gl.setter
    def realized_gl(self, realized_gl):
        """Sets the realized_gl of this HouseholdSecurityBalance.

        Aggregates from Gain Loss end point; dollar gain or loss from trade activity  # noqa: E501

        :param realized_gl: The realized_gl of this HouseholdSecurityBalance.  # noqa: E501
        :type: float
        """

        self._realized_gl = realized_gl

    @property
    def abs_income(self):
        """Gets the abs_income of this HouseholdSecurityBalance.  # noqa: E501

        Aggregates from Income Expense end point; value of performance affecting income such as dividends  # noqa: E501

        :return: The abs_income of this HouseholdSecurityBalance.  # noqa: E501
        :rtype: float
        """
        return self._abs_income

    @abs_income.setter
    def abs_income(self, abs_income):
        """Sets the abs_income of this HouseholdSecurityBalance.

        Aggregates from Income Expense end point; value of performance affecting income such as dividends  # noqa: E501

        :param abs_income: The abs_income of this HouseholdSecurityBalance.  # noqa: E501
        :type: float
        """

        self._abs_income = abs_income

    @property
    def abs_expense(self):
        """Gets the abs_expense of this HouseholdSecurityBalance.  # noqa: E501

        Aggregates from Income Expense end point; value of performance affecting expenses such as ADR fees  # noqa: E501

        :return: The abs_expense of this HouseholdSecurityBalance.  # noqa: E501
        :rtype: float
        """
        return self._abs_expense

    @abs_expense.setter
    def abs_expense(self, abs_expense):
        """Sets the abs_expense of this HouseholdSecurityBalance.

        Aggregates from Income Expense end point; value of performance affecting expenses such as ADR fees  # noqa: E501

        :param abs_expense: The abs_expense of this HouseholdSecurityBalance.  # noqa: E501
        :type: float
        """

        self._abs_expense = abs_expense

    @property
    def appraised_unit_price(self):
        """Gets the appraised_unit_price of this HouseholdSecurityBalance.  # noqa: E501

        The market price of the security on the as_of_date  # noqa: E501

        :return: The appraised_unit_price of this HouseholdSecurityBalance.  # noqa: E501
        :rtype: float
        """
        return self._appraised_unit_price

    @appraised_unit_price.setter
    def appraised_unit_price(self, appraised_unit_price):
        """Sets the appraised_unit_price of this HouseholdSecurityBalance.

        The market price of the security on the as_of_date  # noqa: E501

        :param appraised_unit_price: The appraised_unit_price of this HouseholdSecurityBalance.  # noqa: E501
        :type: float
        """

        self._appraised_unit_price = appraised_unit_price

    @property
    def appraised_value(self):
        """Gets the appraised_value of this HouseholdSecurityBalance.  # noqa: E501

        Market value of the security on the as_of_date (calculated as units * appraised_unit_price)  # noqa: E501

        :return: The appraised_value of this HouseholdSecurityBalance.  # noqa: E501
        :rtype: float
        """
        return self._appraised_value

    @appraised_value.setter
    def appraised_value(self, appraised_value):
        """Sets the appraised_value of this HouseholdSecurityBalance.

        Market value of the security on the as_of_date (calculated as units * appraised_unit_price)  # noqa: E501

        :param appraised_value: The appraised_value of this HouseholdSecurityBalance.  # noqa: E501
        :type: float
        """

        self._appraised_value = appraised_value

    @property
    def beginning_value(self):
        """Gets the beginning_value of this HouseholdSecurityBalance.  # noqa: E501

        Cost basis of the units  # noqa: E501

        :return: The beginning_value of this HouseholdSecurityBalance.  # noqa: E501
        :rtype: float
        """
        return self._beginning_value

    @beginning_value.setter
    def beginning_value(self, beginning_value):
        """Sets the beginning_value of this HouseholdSecurityBalance.

        Cost basis of the units  # noqa: E501

        :param beginning_value: The beginning_value of this HouseholdSecurityBalance.  # noqa: E501
        :type: float
        """

        self._beginning_value = beginning_value

    @property
    def holding_period_return(self):
        """Gets the holding_period_return of this HouseholdSecurityBalance.  # noqa: E501

        Security level return on the as_of_date  # noqa: E501

        :return: The holding_period_return of this HouseholdSecurityBalance.  # noqa: E501
        :rtype: float
        """
        return self._holding_period_return

    @holding_period_return.setter
    def holding_period_return(self, holding_period_return):
        """Sets the holding_period_return of this HouseholdSecurityBalance.

        Security level return on the as_of_date  # noqa: E501

        :param holding_period_return: The holding_period_return of this HouseholdSecurityBalance.  # noqa: E501
        :type: float
        """

        self._holding_period_return = holding_period_return

    @property
    def transfer_out_unrealized_gain_loss(self):
        """Gets the transfer_out_unrealized_gain_loss of this HouseholdSecurityBalance.  # noqa: E501

        Unrealized gain loss that has transfered out  # noqa: E501

        :return: The transfer_out_unrealized_gain_loss of this HouseholdSecurityBalance.  # noqa: E501
        :rtype: float
        """
        return self._transfer_out_unrealized_gain_loss

    @transfer_out_unrealized_gain_loss.setter
    def transfer_out_unrealized_gain_loss(self, transfer_out_unrealized_gain_loss):
        """Sets the transfer_out_unrealized_gain_loss of this HouseholdSecurityBalance.

        Unrealized gain loss that has transfered out  # noqa: E501

        :param transfer_out_unrealized_gain_loss: The transfer_out_unrealized_gain_loss of this HouseholdSecurityBalance.  # noqa: E501
        :type: float
        """

        self._transfer_out_unrealized_gain_loss = transfer_out_unrealized_gain_loss

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
        if issubclass(HouseholdSecurityBalance, dict):
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
        if not isinstance(other, HouseholdSecurityBalance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
