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

class InvestmenttransactionsFilterBody(object):
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
        'plaid_investment_transaction_id': 'str',
        'plaid_account_id': 'str',
        'plaid_security_id': 'str',
        '_date': 'str',
        'name': 'str',
        'quantity': 'float',
        'amount': 'float',
        'price': 'float',
        'fees': 'float',
        'type': 'str',
        'subtype': 'str',
        'iso_currency_code': 'str',
        'unofficial_currency_code': 'str',
        'cancel_transaction_id': 'str',
        'household_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'plaid_investment_transaction_id': 'plaid_investment_transaction_id',
        'plaid_account_id': 'plaid_account_id',
        'plaid_security_id': 'plaid_security_id',
        '_date': 'date',
        'name': 'name',
        'quantity': 'quantity',
        'amount': 'amount',
        'price': 'price',
        'fees': 'fees',
        'type': 'type',
        'subtype': 'subtype',
        'iso_currency_code': 'iso_currency_code',
        'unofficial_currency_code': 'unofficial_currency_code',
        'cancel_transaction_id': 'cancel_transaction_id',
        'household_id': 'household_id'
    }

    def __init__(self, id=None, plaid_investment_transaction_id=None, plaid_account_id=None, plaid_security_id=None, _date=None, name=None, quantity=None, amount=None, price=None, fees=None, type=None, subtype=None, iso_currency_code=None, unofficial_currency_code=None, cancel_transaction_id=None, household_id=None):  # noqa: E501
        """InvestmenttransactionsFilterBody - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._plaid_investment_transaction_id = None
        self._plaid_account_id = None
        self._plaid_security_id = None
        self.__date = None
        self._name = None
        self._quantity = None
        self._amount = None
        self._price = None
        self._fees = None
        self._type = None
        self._subtype = None
        self._iso_currency_code = None
        self._unofficial_currency_code = None
        self._cancel_transaction_id = None
        self._household_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if plaid_investment_transaction_id is not None:
            self.plaid_investment_transaction_id = plaid_investment_transaction_id
        if plaid_account_id is not None:
            self.plaid_account_id = plaid_account_id
        if plaid_security_id is not None:
            self.plaid_security_id = plaid_security_id
        if _date is not None:
            self._date = _date
        if name is not None:
            self.name = name
        if quantity is not None:
            self.quantity = quantity
        if amount is not None:
            self.amount = amount
        if price is not None:
            self.price = price
        if fees is not None:
            self.fees = fees
        if type is not None:
            self.type = type
        if subtype is not None:
            self.subtype = subtype
        if iso_currency_code is not None:
            self.iso_currency_code = iso_currency_code
        if unofficial_currency_code is not None:
            self.unofficial_currency_code = unofficial_currency_code
        if cancel_transaction_id is not None:
            self.cancel_transaction_id = cancel_transaction_id
        if household_id is not None:
            self.household_id = household_id

    @property
    def id(self):
        """Gets the id of this InvestmenttransactionsFilterBody.  # noqa: E501

        Unique ID of the Heldaway Investment Transaction  # noqa: E501

        :return: The id of this InvestmenttransactionsFilterBody.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InvestmenttransactionsFilterBody.

        Unique ID of the Heldaway Investment Transaction  # noqa: E501

        :param id: The id of this InvestmenttransactionsFilterBody.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def plaid_investment_transaction_id(self):
        """Gets the plaid_investment_transaction_id of this InvestmenttransactionsFilterBody.  # noqa: E501

        The ID of the Investment transaction, unique across all Plaid transactions.  # noqa: E501

        :return: The plaid_investment_transaction_id of this InvestmenttransactionsFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._plaid_investment_transaction_id

    @plaid_investment_transaction_id.setter
    def plaid_investment_transaction_id(self, plaid_investment_transaction_id):
        """Sets the plaid_investment_transaction_id of this InvestmenttransactionsFilterBody.

        The ID of the Investment transaction, unique across all Plaid transactions.  # noqa: E501

        :param plaid_investment_transaction_id: The plaid_investment_transaction_id of this InvestmenttransactionsFilterBody.  # noqa: E501
        :type: str
        """

        self._plaid_investment_transaction_id = plaid_investment_transaction_id

    @property
    def plaid_account_id(self):
        """Gets the plaid_account_id of this InvestmenttransactionsFilterBody.  # noqa: E501

        The ID of the account against which this transaction posted.  # noqa: E501

        :return: The plaid_account_id of this InvestmenttransactionsFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._plaid_account_id

    @plaid_account_id.setter
    def plaid_account_id(self, plaid_account_id):
        """Sets the plaid_account_id of this InvestmenttransactionsFilterBody.

        The ID of the account against which this transaction posted.  # noqa: E501

        :param plaid_account_id: The plaid_account_id of this InvestmenttransactionsFilterBody.  # noqa: E501
        :type: str
        """

        self._plaid_account_id = plaid_account_id

    @property
    def plaid_security_id(self):
        """Gets the plaid_security_id of this InvestmenttransactionsFilterBody.  # noqa: E501

        The ID of the security assigned by Plaid to which this transaction is related.  # noqa: E501

        :return: The plaid_security_id of this InvestmenttransactionsFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._plaid_security_id

    @plaid_security_id.setter
    def plaid_security_id(self, plaid_security_id):
        """Sets the plaid_security_id of this InvestmenttransactionsFilterBody.

        The ID of the security assigned by Plaid to which this transaction is related.  # noqa: E501

        :param plaid_security_id: The plaid_security_id of this InvestmenttransactionsFilterBody.  # noqa: E501
        :type: str
        """

        self._plaid_security_id = plaid_security_id

    @property
    def _date(self):
        """Gets the _date of this InvestmenttransactionsFilterBody.  # noqa: E501

        Date The ISO-8601 posting date for the transaction, or transacted date for pending transactions.  # noqa: E501

        :return: The _date of this InvestmenttransactionsFilterBody.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this InvestmenttransactionsFilterBody.

        Date The ISO-8601 posting date for the transaction, or transacted date for pending transactions.  # noqa: E501

        :param _date: The _date of this InvestmenttransactionsFilterBody.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def name(self):
        """Gets the name of this InvestmenttransactionsFilterBody.  # noqa: E501

        The Institution???s description of the transaction.  # noqa: E501

        :return: The name of this InvestmenttransactionsFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InvestmenttransactionsFilterBody.

        The Institution???s description of the transaction.  # noqa: E501

        :param name: The name of this InvestmenttransactionsFilterBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def quantity(self):
        """Gets the quantity of this InvestmenttransactionsFilterBody.  # noqa: E501

        The Amount of the security involved in this transaction.  # noqa: E501

        :return: The quantity of this InvestmenttransactionsFilterBody.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this InvestmenttransactionsFilterBody.

        The Amount of the security involved in this transaction.  # noqa: E501

        :param quantity: The quantity of this InvestmenttransactionsFilterBody.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def amount(self):
        """Gets the amount of this InvestmenttransactionsFilterBody.  # noqa: E501

        The complete value of the transaction. Positive values when cash is debited, e.g. purchases of stock; negative values when cash is credited, e.g. sales of stock. Treatment remains the same for cash-only movements unassociated with securities.  # noqa: E501

        :return: The amount of this InvestmenttransactionsFilterBody.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InvestmenttransactionsFilterBody.

        The complete value of the transaction. Positive values when cash is debited, e.g. purchases of stock; negative values when cash is credited, e.g. sales of stock. Treatment remains the same for cash-only movements unassociated with securities.  # noqa: E501

        :param amount: The amount of this InvestmenttransactionsFilterBody.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def price(self):
        """Gets the price of this InvestmenttransactionsFilterBody.  # noqa: E501

        The price of the security at which this transaction occurred.  # noqa: E501

        :return: The price of this InvestmenttransactionsFilterBody.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this InvestmenttransactionsFilterBody.

        The price of the security at which this transaction occurred.  # noqa: E501

        :param price: The price of this InvestmenttransactionsFilterBody.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def fees(self):
        """Gets the fees of this InvestmenttransactionsFilterBody.  # noqa: E501

        The combined value of all fees applied to this transaction.  # noqa: E501

        :return: The fees of this InvestmenttransactionsFilterBody.  # noqa: E501
        :rtype: float
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this InvestmenttransactionsFilterBody.

        The combined value of all fees applied to this transaction.  # noqa: E501

        :param fees: The fees of this InvestmenttransactionsFilterBody.  # noqa: E501
        :type: float
        """

        self._fees = fees

    @property
    def type(self):
        """Gets the type of this InvestmenttransactionsFilterBody.  # noqa: E501

        Investment Transaction type assigned by Plaid  # noqa: E501

        :return: The type of this InvestmenttransactionsFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InvestmenttransactionsFilterBody.

        Investment Transaction type assigned by Plaid  # noqa: E501

        :param type: The type of this InvestmenttransactionsFilterBody.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def subtype(self):
        """Gets the subtype of this InvestmenttransactionsFilterBody.  # noqa: E501

        Investment Transaction subtype assigned by Plaid  # noqa: E501

        :return: The subtype of this InvestmenttransactionsFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this InvestmenttransactionsFilterBody.

        Investment Transaction subtype assigned by Plaid  # noqa: E501

        :param subtype: The subtype of this InvestmenttransactionsFilterBody.  # noqa: E501
        :type: str
        """

        self._subtype = subtype

    @property
    def iso_currency_code(self):
        """Gets the iso_currency_code of this InvestmenttransactionsFilterBody.  # noqa: E501

        The ISO-4217 currency code of the transaction. Always null if unofficial_currency_code is non-null.  # noqa: E501

        :return: The iso_currency_code of this InvestmenttransactionsFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._iso_currency_code

    @iso_currency_code.setter
    def iso_currency_code(self, iso_currency_code):
        """Sets the iso_currency_code of this InvestmenttransactionsFilterBody.

        The ISO-4217 currency code of the transaction. Always null if unofficial_currency_code is non-null.  # noqa: E501

        :param iso_currency_code: The iso_currency_code of this InvestmenttransactionsFilterBody.  # noqa: E501
        :type: str
        """

        self._iso_currency_code = iso_currency_code

    @property
    def unofficial_currency_code(self):
        """Gets the unofficial_currency_code of this InvestmenttransactionsFilterBody.  # noqa: E501

        The unofficial currency of the transaction. Always null if iso_currency_code is non-null. This is present if the price is denominated in an unrecognized currency e.g. Bitcoin, rewards points.  # noqa: E501

        :return: The unofficial_currency_code of this InvestmenttransactionsFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._unofficial_currency_code

    @unofficial_currency_code.setter
    def unofficial_currency_code(self, unofficial_currency_code):
        """Sets the unofficial_currency_code of this InvestmenttransactionsFilterBody.

        The unofficial currency of the transaction. Always null if iso_currency_code is non-null. This is present if the price is denominated in an unrecognized currency e.g. Bitcoin, rewards points.  # noqa: E501

        :param unofficial_currency_code: The unofficial_currency_code of this InvestmenttransactionsFilterBody.  # noqa: E501
        :type: str
        """

        self._unofficial_currency_code = unofficial_currency_code

    @property
    def cancel_transaction_id(self):
        """Gets the cancel_transaction_id of this InvestmenttransactionsFilterBody.  # noqa: E501

        Present only when the transaction type is cancel, and indicates the investment_transaction_id of the transaction which was cancelled.  # noqa: E501

        :return: The cancel_transaction_id of this InvestmenttransactionsFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._cancel_transaction_id

    @cancel_transaction_id.setter
    def cancel_transaction_id(self, cancel_transaction_id):
        """Sets the cancel_transaction_id of this InvestmenttransactionsFilterBody.

        Present only when the transaction type is cancel, and indicates the investment_transaction_id of the transaction which was cancelled.  # noqa: E501

        :param cancel_transaction_id: The cancel_transaction_id of this InvestmenttransactionsFilterBody.  # noqa: E501
        :type: str
        """

        self._cancel_transaction_id = cancel_transaction_id

    @property
    def household_id(self):
        """Gets the household_id of this InvestmenttransactionsFilterBody.  # noqa: E501

        The id of the household to which this transaction belongs  # noqa: E501

        :return: The household_id of this InvestmenttransactionsFilterBody.  # noqa: E501
        :rtype: int
        """
        return self._household_id

    @household_id.setter
    def household_id(self, household_id):
        """Sets the household_id of this InvestmenttransactionsFilterBody.

        The id of the household to which this transaction belongs  # noqa: E501

        :param household_id: The household_id of this InvestmenttransactionsFilterBody.  # noqa: E501
        :type: int
        """

        self._household_id = household_id

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
        if issubclass(InvestmenttransactionsFilterBody, dict):
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
        if not isinstance(other, InvestmenttransactionsFilterBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
