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

class GainLoss(object):
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
        'account_id': 'int',
        'open_date': 'datetime',
        'close_date': 'datetime',
        'security_id': 'int',
        'direction': 'str',
        'short_term': 'bool',
        'long_term': 'bool',
        'abs_open_units': 'float',
        'abs_closed_units': 'float',
        'open_value': 'float',
        'close_value': 'float',
        'amount': 'float',
        'is_cancel': 'bool',
        'created_at_utc': 'datetime',
        'updated_at_utc': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'account_id': 'account_id',
        'open_date': 'open_date',
        'close_date': 'close_date',
        'security_id': 'security_id',
        'direction': 'direction',
        'short_term': 'short_term',
        'long_term': 'long_term',
        'abs_open_units': 'abs_open_units',
        'abs_closed_units': 'abs_closed_units',
        'open_value': 'open_value',
        'close_value': 'close_value',
        'amount': 'amount',
        'is_cancel': 'is_cancel',
        'created_at_utc': 'created_at_utc',
        'updated_at_utc': 'updated_at_utc'
    }

    def __init__(self, id=None, account_id=None, open_date=None, close_date=None, security_id=None, direction=None, short_term=None, long_term=None, abs_open_units=None, abs_closed_units=None, open_value=None, close_value=None, amount=None, is_cancel=None, created_at_utc=None, updated_at_utc=None):  # noqa: E501
        """GainLoss - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._account_id = None
        self._open_date = None
        self._close_date = None
        self._security_id = None
        self._direction = None
        self._short_term = None
        self._long_term = None
        self._abs_open_units = None
        self._abs_closed_units = None
        self._open_value = None
        self._close_value = None
        self._amount = None
        self._is_cancel = None
        self._created_at_utc = None
        self._updated_at_utc = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if account_id is not None:
            self.account_id = account_id
        if open_date is not None:
            self.open_date = open_date
        if close_date is not None:
            self.close_date = close_date
        if security_id is not None:
            self.security_id = security_id
        if direction is not None:
            self.direction = direction
        if short_term is not None:
            self.short_term = short_term
        if long_term is not None:
            self.long_term = long_term
        if abs_open_units is not None:
            self.abs_open_units = abs_open_units
        if abs_closed_units is not None:
            self.abs_closed_units = abs_closed_units
        if open_value is not None:
            self.open_value = open_value
        if close_value is not None:
            self.close_value = close_value
        if amount is not None:
            self.amount = amount
        if is_cancel is not None:
            self.is_cancel = is_cancel
        if created_at_utc is not None:
            self.created_at_utc = created_at_utc
        if updated_at_utc is not None:
            self.updated_at_utc = updated_at_utc

    @property
    def id(self):
        """Gets the id of this GainLoss.  # noqa: E501

        The unique resource id for the Transaction  # noqa: E501

        :return: The id of this GainLoss.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GainLoss.

        The unique resource id for the Transaction  # noqa: E501

        :param id: The id of this GainLoss.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this GainLoss.  # noqa: E501

        The id of the Account associated with this Transaction  # noqa: E501

        :return: The account_id of this GainLoss.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GainLoss.

        The id of the Account associated with this Transaction  # noqa: E501

        :param account_id: The account_id of this GainLoss.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def open_date(self):
        """Gets the open_date of this GainLoss.  # noqa: E501

        The date the corresponding lot was opened. Note that this field may be populated with the special date value \"1900-01-01\" which is to be understood as the absence of cost basis information for the corresponding closing fill  # noqa: E501

        :return: The open_date of this GainLoss.  # noqa: E501
        :rtype: datetime
        """
        return self._open_date

    @open_date.setter
    def open_date(self, open_date):
        """Sets the open_date of this GainLoss.

        The date the corresponding lot was opened. Note that this field may be populated with the special date value \"1900-01-01\" which is to be understood as the absence of cost basis information for the corresponding closing fill  # noqa: E501

        :param open_date: The open_date of this GainLoss.  # noqa: E501
        :type: datetime
        """

        self._open_date = open_date

    @property
    def close_date(self):
        """Gets the close_date of this GainLoss.  # noqa: E501

        The date the closing fill was posted  # noqa: E501

        :return: The close_date of this GainLoss.  # noqa: E501
        :rtype: datetime
        """
        return self._close_date

    @close_date.setter
    def close_date(self, close_date):
        """Sets the close_date of this GainLoss.

        The date the closing fill was posted  # noqa: E501

        :param close_date: The close_date of this GainLoss.  # noqa: E501
        :type: datetime
        """

        self._close_date = close_date

    @property
    def security_id(self):
        """Gets the security_id of this GainLoss.  # noqa: E501

        The id of the Security associated with this Transaction  # noqa: E501

        :return: The security_id of this GainLoss.  # noqa: E501
        :rtype: int
        """
        return self._security_id

    @security_id.setter
    def security_id(self, security_id):
        """Sets the security_id of this GainLoss.

        The id of the Security associated with this Transaction  # noqa: E501

        :param security_id: The security_id of this GainLoss.  # noqa: E501
        :type: int
        """

        self._security_id = security_id

    @property
    def direction(self):
        """Gets the direction of this GainLoss.  # noqa: E501

        Flag meant to indicate if the lot is long or short. Potential values L=Long, S=Short  # noqa: E501

        :return: The direction of this GainLoss.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this GainLoss.

        Flag meant to indicate if the lot is long or short. Potential values L=Long, S=Short  # noqa: E501

        :param direction: The direction of this GainLoss.  # noqa: E501
        :type: str
        """
        allowed_values = ["L=Long", "S=Short"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def short_term(self):
        """Gets the short_term of this GainLoss.  # noqa: E501

        Indicates whether the gain loss is short term (less than a year)  # noqa: E501

        :return: The short_term of this GainLoss.  # noqa: E501
        :rtype: bool
        """
        return self._short_term

    @short_term.setter
    def short_term(self, short_term):
        """Sets the short_term of this GainLoss.

        Indicates whether the gain loss is short term (less than a year)  # noqa: E501

        :param short_term: The short_term of this GainLoss.  # noqa: E501
        :type: bool
        """

        self._short_term = short_term

    @property
    def long_term(self):
        """Gets the long_term of this GainLoss.  # noqa: E501

        Indicates whether the gain loss is long term (more than a year)  # noqa: E501

        :return: The long_term of this GainLoss.  # noqa: E501
        :rtype: bool
        """
        return self._long_term

    @long_term.setter
    def long_term(self, long_term):
        """Sets the long_term of this GainLoss.

        Indicates whether the gain loss is long term (more than a year)  # noqa: E501

        :param long_term: The long_term of this GainLoss.  # noqa: E501
        :type: bool
        """

        self._long_term = long_term

    @property
    def abs_open_units(self):
        """Gets the abs_open_units of this GainLoss.  # noqa: E501

        The total quantity of open shares prior to the transaction (e.g. 400 shares originally, 200 shares sold)  # noqa: E501

        :return: The abs_open_units of this GainLoss.  # noqa: E501
        :rtype: float
        """
        return self._abs_open_units

    @abs_open_units.setter
    def abs_open_units(self, abs_open_units):
        """Sets the abs_open_units of this GainLoss.

        The total quantity of open shares prior to the transaction (e.g. 400 shares originally, 200 shares sold)  # noqa: E501

        :param abs_open_units: The abs_open_units of this GainLoss.  # noqa: E501
        :type: float
        """

        self._abs_open_units = abs_open_units

    @property
    def abs_closed_units(self):
        """Gets the abs_closed_units of this GainLoss.  # noqa: E501

        The total quantity of closed shares of the transaction  # noqa: E501

        :return: The abs_closed_units of this GainLoss.  # noqa: E501
        :rtype: float
        """
        return self._abs_closed_units

    @abs_closed_units.setter
    def abs_closed_units(self, abs_closed_units):
        """Sets the abs_closed_units of this GainLoss.

        The total quantity of closed shares of the transaction  # noqa: E501

        :param abs_closed_units: The abs_closed_units of this GainLoss.  # noqa: E501
        :type: float
        """

        self._abs_closed_units = abs_closed_units

    @property
    def open_value(self):
        """Gets the open_value of this GainLoss.  # noqa: E501

        The cost basis of the open shares (in example above, the cost basis for the 400 shares)  # noqa: E501

        :return: The open_value of this GainLoss.  # noqa: E501
        :rtype: float
        """
        return self._open_value

    @open_value.setter
    def open_value(self, open_value):
        """Sets the open_value of this GainLoss.

        The cost basis of the open shares (in example above, the cost basis for the 400 shares)  # noqa: E501

        :param open_value: The open_value of this GainLoss.  # noqa: E501
        :type: float
        """

        self._open_value = open_value

    @property
    def close_value(self):
        """Gets the close_value of this GainLoss.  # noqa: E501

        The cost basis of the closed shares  # noqa: E501

        :return: The close_value of this GainLoss.  # noqa: E501
        :rtype: float
        """
        return self._close_value

    @close_value.setter
    def close_value(self, close_value):
        """Sets the close_value of this GainLoss.

        The cost basis of the closed shares  # noqa: E501

        :param close_value: The close_value of this GainLoss.  # noqa: E501
        :type: float
        """

        self._close_value = close_value

    @property
    def amount(self):
        """Gets the amount of this GainLoss.  # noqa: E501

        The dollar amount associated with the transaction (e.g. sale amount to close a long position, purchase amount to close a short position)  # noqa: E501

        :return: The amount of this GainLoss.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GainLoss.

        The dollar amount associated with the transaction (e.g. sale amount to close a long position, purchase amount to close a short position)  # noqa: E501

        :param amount: The amount of this GainLoss.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def is_cancel(self):
        """Gets the is_cancel of this GainLoss.  # noqa: E501

        Flag to indicate if this transaction is a cancel at the custodian  # noqa: E501

        :return: The is_cancel of this GainLoss.  # noqa: E501
        :rtype: bool
        """
        return self._is_cancel

    @is_cancel.setter
    def is_cancel(self, is_cancel):
        """Sets the is_cancel of this GainLoss.

        Flag to indicate if this transaction is a cancel at the custodian  # noqa: E501

        :param is_cancel: The is_cancel of this GainLoss.  # noqa: E501
        :type: bool
        """

        self._is_cancel = is_cancel

    @property
    def created_at_utc(self):
        """Gets the created_at_utc of this GainLoss.  # noqa: E501

        Timestamp for when the record was created  # noqa: E501

        :return: The created_at_utc of this GainLoss.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at_utc

    @created_at_utc.setter
    def created_at_utc(self, created_at_utc):
        """Sets the created_at_utc of this GainLoss.

        Timestamp for when the record was created  # noqa: E501

        :param created_at_utc: The created_at_utc of this GainLoss.  # noqa: E501
        :type: datetime
        """

        self._created_at_utc = created_at_utc

    @property
    def updated_at_utc(self):
        """Gets the updated_at_utc of this GainLoss.  # noqa: E501

        Timestamp for when the record was updated  # noqa: E501

        :return: The updated_at_utc of this GainLoss.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_utc

    @updated_at_utc.setter
    def updated_at_utc(self, updated_at_utc):
        """Sets the updated_at_utc of this GainLoss.

        Timestamp for when the record was updated  # noqa: E501

        :param updated_at_utc: The updated_at_utc of this GainLoss.  # noqa: E501
        :type: datetime
        """

        self._updated_at_utc = updated_at_utc

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
        if issubclass(GainLoss, dict):
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
        if not isinstance(other, GainLoss):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
