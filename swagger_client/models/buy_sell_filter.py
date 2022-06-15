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

class BuySellFilter(object):
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
        'security_id': 'int',
        'type': 'str',
        'is_cancel': 'bool',
        'transaction_date': 'datetime',
        'reported_date': 'datetime',
        'abs_units': 'float',
        'abs_amount': 'float',
        'transaction_fee': 'float',
        'description': 'str',
        'custodian': 'str'
    }

    attribute_map = {
        'id': 'id',
        'account_id': 'account_id',
        'security_id': 'security_id',
        'type': 'type',
        'is_cancel': 'is_cancel',
        'transaction_date': 'transaction_date',
        'reported_date': 'reported_date',
        'abs_units': 'abs_units',
        'abs_amount': 'abs_amount',
        'transaction_fee': 'transaction_fee',
        'description': 'description',
        'custodian': 'custodian'
    }

    def __init__(self, id=None, account_id=None, security_id=None, type=None, is_cancel=None, transaction_date=None, reported_date=None, abs_units=None, abs_amount=None, transaction_fee=None, description=None, custodian=None):  # noqa: E501
        """BuySellFilter - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._account_id = None
        self._security_id = None
        self._type = None
        self._is_cancel = None
        self._transaction_date = None
        self._reported_date = None
        self._abs_units = None
        self._abs_amount = None
        self._transaction_fee = None
        self._description = None
        self._custodian = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if account_id is not None:
            self.account_id = account_id
        if security_id is not None:
            self.security_id = security_id
        if type is not None:
            self.type = type
        if is_cancel is not None:
            self.is_cancel = is_cancel
        if transaction_date is not None:
            self.transaction_date = transaction_date
        if reported_date is not None:
            self.reported_date = reported_date
        if abs_units is not None:
            self.abs_units = abs_units
        if abs_amount is not None:
            self.abs_amount = abs_amount
        if transaction_fee is not None:
            self.transaction_fee = transaction_fee
        if description is not None:
            self.description = description
        if custodian is not None:
            self.custodian = custodian

    @property
    def id(self):
        """Gets the id of this BuySellFilter.  # noqa: E501

        The unique resource id for the Transaction  # noqa: E501

        :return: The id of this BuySellFilter.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BuySellFilter.

        The unique resource id for the Transaction  # noqa: E501

        :param id: The id of this BuySellFilter.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this BuySellFilter.  # noqa: E501

        The id of the Account associated with this Transaction  # noqa: E501

        :return: The account_id of this BuySellFilter.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this BuySellFilter.

        The id of the Account associated with this Transaction  # noqa: E501

        :param account_id: The account_id of this BuySellFilter.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def security_id(self):
        """Gets the security_id of this BuySellFilter.  # noqa: E501

        The id of the Security associated with this Transaction  # noqa: E501

        :return: The security_id of this BuySellFilter.  # noqa: E501
        :rtype: int
        """
        return self._security_id

    @security_id.setter
    def security_id(self, security_id):
        """Sets the security_id of this BuySellFilter.

        The id of the Security associated with this Transaction  # noqa: E501

        :param security_id: The security_id of this BuySellFilter.  # noqa: E501
        :type: int
        """

        self._security_id = security_id

    @property
    def type(self):
        """Gets the type of this BuySellFilter.  # noqa: E501

        The type of transaction. Possible values, BTO - buy to open, BTC - buy to close, STO - sell to open, STC - sell to close  # noqa: E501

        :return: The type of this BuySellFilter.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BuySellFilter.

        The type of transaction. Possible values, BTO - buy to open, BTC - buy to close, STO - sell to open, STC - sell to close  # noqa: E501

        :param type: The type of this BuySellFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["BTO = Buy To Open", "BTC = Buy To Close", "STO = Sell To Open", "STC = Sell To Close"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def is_cancel(self):
        """Gets the is_cancel of this BuySellFilter.  # noqa: E501

        Flag to indicate if this Transaction is a cancel from the custodian  # noqa: E501

        :return: The is_cancel of this BuySellFilter.  # noqa: E501
        :rtype: bool
        """
        return self._is_cancel

    @is_cancel.setter
    def is_cancel(self, is_cancel):
        """Sets the is_cancel of this BuySellFilter.

        Flag to indicate if this Transaction is a cancel from the custodian  # noqa: E501

        :param is_cancel: The is_cancel of this BuySellFilter.  # noqa: E501
        :type: bool
        """

        self._is_cancel = is_cancel

    @property
    def transaction_date(self):
        """Gets the transaction_date of this BuySellFilter.  # noqa: E501

        The date of the transaction on a trade basis  # noqa: E501

        :return: The transaction_date of this BuySellFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        """Sets the transaction_date of this BuySellFilter.

        The date of the transaction on a trade basis  # noqa: E501

        :param transaction_date: The transaction_date of this BuySellFilter.  # noqa: E501
        :type: datetime
        """

        self._transaction_date = transaction_date

    @property
    def reported_date(self):
        """Gets the reported_date of this BuySellFilter.  # noqa: E501

        The date the custodian reports the transaction  # noqa: E501

        :return: The reported_date of this BuySellFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._reported_date

    @reported_date.setter
    def reported_date(self, reported_date):
        """Sets the reported_date of this BuySellFilter.

        The date the custodian reports the transaction  # noqa: E501

        :param reported_date: The reported_date of this BuySellFilter.  # noqa: E501
        :type: datetime
        """

        self._reported_date = reported_date

    @property
    def abs_units(self):
        """Gets the abs_units of this BuySellFilter.  # noqa: E501

        The quantity of shares for the Transaction  # noqa: E501

        :return: The abs_units of this BuySellFilter.  # noqa: E501
        :rtype: float
        """
        return self._abs_units

    @abs_units.setter
    def abs_units(self, abs_units):
        """Sets the abs_units of this BuySellFilter.

        The quantity of shares for the Transaction  # noqa: E501

        :param abs_units: The abs_units of this BuySellFilter.  # noqa: E501
        :type: float
        """

        self._abs_units = abs_units

    @property
    def abs_amount(self):
        """Gets the abs_amount of this BuySellFilter.  # noqa: E501

        The dollar amount associated with the Transaction  # noqa: E501

        :return: The abs_amount of this BuySellFilter.  # noqa: E501
        :rtype: float
        """
        return self._abs_amount

    @abs_amount.setter
    def abs_amount(self, abs_amount):
        """Sets the abs_amount of this BuySellFilter.

        The dollar amount associated with the Transaction  # noqa: E501

        :param abs_amount: The abs_amount of this BuySellFilter.  # noqa: E501
        :type: float
        """

        self._abs_amount = abs_amount

    @property
    def transaction_fee(self):
        """Gets the transaction_fee of this BuySellFilter.  # noqa: E501

        Fees associated with the Transaction (e.g. commission)  # noqa: E501

        :return: The transaction_fee of this BuySellFilter.  # noqa: E501
        :rtype: float
        """
        return self._transaction_fee

    @transaction_fee.setter
    def transaction_fee(self, transaction_fee):
        """Sets the transaction_fee of this BuySellFilter.

        Fees associated with the Transaction (e.g. commission)  # noqa: E501

        :param transaction_fee: The transaction_fee of this BuySellFilter.  # noqa: E501
        :type: float
        """

        self._transaction_fee = transaction_fee

    @property
    def description(self):
        """Gets the description of this BuySellFilter.  # noqa: E501

        Description of the transaction from the custodian  # noqa: E501

        :return: The description of this BuySellFilter.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BuySellFilter.

        Description of the transaction from the custodian  # noqa: E501

        :param description: The description of this BuySellFilter.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def custodian(self):
        """Gets the custodian of this BuySellFilter.  # noqa: E501

        Custodian the account data comes from. TDA=TD Ameritrade, SWB=Schwab, NFS=Fidelity, PER=Pershing, MLT=MillenniumTrust, RJA=RaymondJames, HDG=Manual  # noqa: E501

        :return: The custodian of this BuySellFilter.  # noqa: E501
        :rtype: str
        """
        return self._custodian

    @custodian.setter
    def custodian(self, custodian):
        """Sets the custodian of this BuySellFilter.

        Custodian the account data comes from. TDA=TD Ameritrade, SWB=Schwab, NFS=Fidelity, PER=Pershing, MLT=MillenniumTrust, RJA=RaymondJames, HDG=Manual  # noqa: E501

        :param custodian: The custodian of this BuySellFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["TDA", "SWB", "NFS", "PER", "DST", "MLT", "RJA", "HDG"]  # noqa: E501
        if custodian not in allowed_values:
            raise ValueError(
                "Invalid value for `custodian` ({0}), must be one of {1}"  # noqa: E501
                .format(custodian, allowed_values)
            )

        self._custodian = custodian

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
        if issubclass(BuySellFilter, dict):
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
        if not isinstance(other, BuySellFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other