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

class InlineResponse20078Data(object):
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
        'open_date': 'datetime',
        'origination_date': 'datetime',
        'security_id': 'int',
        'lot_id': 'int',
        'security_ledger_id': 'int',
        'account_id': 'int',
        'direction': 'str',
        'abs_open_units': 'float',
        'cost_basis_unit_price': 'float',
        'appraised_unit_price': 'float',
        'realized_gain_loss': 'float',
        'abs_closed_units': 'float',
        'cost_basis_known': 'bool',
        'created_at_utc': 'datetime',
        'updated_at_utc': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'as_of_date': 'as_of_date',
        'open_date': 'open_date',
        'origination_date': 'origination_date',
        'security_id': 'security_id',
        'lot_id': 'lot_id',
        'security_ledger_id': 'security_ledger_id',
        'account_id': 'account_id',
        'direction': 'direction',
        'abs_open_units': 'abs_open_units',
        'cost_basis_unit_price': 'cost_basis_unit_price',
        'appraised_unit_price': 'appraised_unit_price',
        'realized_gain_loss': 'realized_gain_loss',
        'abs_closed_units': 'abs_closed_units',
        'cost_basis_known': 'cost_basis_known',
        'created_at_utc': 'created_at_utc',
        'updated_at_utc': 'updated_at_utc'
    }

    def __init__(self, id=None, as_of_date=None, open_date=None, origination_date=None, security_id=None, lot_id=None, security_ledger_id=None, account_id=None, direction=None, abs_open_units=None, cost_basis_unit_price=None, appraised_unit_price=None, realized_gain_loss=None, abs_closed_units=None, cost_basis_known=None, created_at_utc=None, updated_at_utc=None):  # noqa: E501
        """InlineResponse20078Data - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._as_of_date = None
        self._open_date = None
        self._origination_date = None
        self._security_id = None
        self._lot_id = None
        self._security_ledger_id = None
        self._account_id = None
        self._direction = None
        self._abs_open_units = None
        self._cost_basis_unit_price = None
        self._appraised_unit_price = None
        self._realized_gain_loss = None
        self._abs_closed_units = None
        self._cost_basis_known = None
        self._created_at_utc = None
        self._updated_at_utc = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if as_of_date is not None:
            self.as_of_date = as_of_date
        if open_date is not None:
            self.open_date = open_date
        if origination_date is not None:
            self.origination_date = origination_date
        if security_id is not None:
            self.security_id = security_id
        if lot_id is not None:
            self.lot_id = lot_id
        if security_ledger_id is not None:
            self.security_ledger_id = security_ledger_id
        if account_id is not None:
            self.account_id = account_id
        if direction is not None:
            self.direction = direction
        if abs_open_units is not None:
            self.abs_open_units = abs_open_units
        if cost_basis_unit_price is not None:
            self.cost_basis_unit_price = cost_basis_unit_price
        if appraised_unit_price is not None:
            self.appraised_unit_price = appraised_unit_price
        if realized_gain_loss is not None:
            self.realized_gain_loss = realized_gain_loss
        if abs_closed_units is not None:
            self.abs_closed_units = abs_closed_units
        if cost_basis_known is not None:
            self.cost_basis_known = cost_basis_known
        if created_at_utc is not None:
            self.created_at_utc = created_at_utc
        if updated_at_utc is not None:
            self.updated_at_utc = updated_at_utc

    @property
    def id(self):
        """Gets the id of this InlineResponse20078Data.  # noqa: E501

        The unique resource id for this Position  # noqa: E501

        :return: The id of this InlineResponse20078Data.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20078Data.

        The unique resource id for this Position  # noqa: E501

        :param id: The id of this InlineResponse20078Data.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def as_of_date(self):
        """Gets the as_of_date of this InlineResponse20078Data.  # noqa: E501

        The current date for this Position  # noqa: E501

        :return: The as_of_date of this InlineResponse20078Data.  # noqa: E501
        :rtype: datetime
        """
        return self._as_of_date

    @as_of_date.setter
    def as_of_date(self, as_of_date):
        """Sets the as_of_date of this InlineResponse20078Data.

        The current date for this Position  # noqa: E501

        :param as_of_date: The as_of_date of this InlineResponse20078Data.  # noqa: E501
        :type: datetime
        """

        self._as_of_date = as_of_date

    @property
    def open_date(self):
        """Gets the open_date of this InlineResponse20078Data.  # noqa: E501

        The date this position was opened in the account.Note that this field may be populated with the special date value \"\"1900-01-01\"\" which is to be understood as the absence of cost basis information for the lot associated with this position  # noqa: E501

        :return: The open_date of this InlineResponse20078Data.  # noqa: E501
        :rtype: datetime
        """
        return self._open_date

    @open_date.setter
    def open_date(self, open_date):
        """Sets the open_date of this InlineResponse20078Data.

        The date this position was opened in the account.Note that this field may be populated with the special date value \"\"1900-01-01\"\" which is to be understood as the absence of cost basis information for the lot associated with this position  # noqa: E501

        :param open_date: The open_date of this InlineResponse20078Data.  # noqa: E501
        :type: datetime
        """

        self._open_date = open_date

    @property
    def origination_date(self):
        """Gets the origination_date of this InlineResponse20078Data.  # noqa: E501

        The date that this position originated in all time. For example, a position transferred in would have an origination_date of the date that the position was first opened in whichever account it was opened. Note that this field may be populated with the special date value \"\"1900-01-01\"\" which is to be understood as the absence of cost basis information for the lot associated with this position  # noqa: E501

        :return: The origination_date of this InlineResponse20078Data.  # noqa: E501
        :rtype: datetime
        """
        return self._origination_date

    @origination_date.setter
    def origination_date(self, origination_date):
        """Sets the origination_date of this InlineResponse20078Data.

        The date that this position originated in all time. For example, a position transferred in would have an origination_date of the date that the position was first opened in whichever account it was opened. Note that this field may be populated with the special date value \"\"1900-01-01\"\" which is to be understood as the absence of cost basis information for the lot associated with this position  # noqa: E501

        :param origination_date: The origination_date of this InlineResponse20078Data.  # noqa: E501
        :type: datetime
        """

        self._origination_date = origination_date

    @property
    def security_id(self):
        """Gets the security_id of this InlineResponse20078Data.  # noqa: E501

        The id of the Security associated with this Position  # noqa: E501

        :return: The security_id of this InlineResponse20078Data.  # noqa: E501
        :rtype: int
        """
        return self._security_id

    @security_id.setter
    def security_id(self, security_id):
        """Sets the security_id of this InlineResponse20078Data.

        The id of the Security associated with this Position  # noqa: E501

        :param security_id: The security_id of this InlineResponse20078Data.  # noqa: E501
        :type: int
        """

        self._security_id = security_id

    @property
    def lot_id(self):
        """Gets the lot_id of this InlineResponse20078Data.  # noqa: E501

        The id of the lot associated with this Position  # noqa: E501

        :return: The lot_id of this InlineResponse20078Data.  # noqa: E501
        :rtype: int
        """
        return self._lot_id

    @lot_id.setter
    def lot_id(self, lot_id):
        """Sets the lot_id of this InlineResponse20078Data.

        The id of the lot associated with this Position  # noqa: E501

        :param lot_id: The lot_id of this InlineResponse20078Data.  # noqa: E501
        :type: int
        """

        self._lot_id = lot_id

    @property
    def security_ledger_id(self):
        """Gets the security_ledger_id of this InlineResponse20078Data.  # noqa: E501

        The id of the security ledger associated with this Position  # noqa: E501

        :return: The security_ledger_id of this InlineResponse20078Data.  # noqa: E501
        :rtype: int
        """
        return self._security_ledger_id

    @security_ledger_id.setter
    def security_ledger_id(self, security_ledger_id):
        """Sets the security_ledger_id of this InlineResponse20078Data.

        The id of the security ledger associated with this Position  # noqa: E501

        :param security_ledger_id: The security_ledger_id of this InlineResponse20078Data.  # noqa: E501
        :type: int
        """

        self._security_ledger_id = security_ledger_id

    @property
    def account_id(self):
        """Gets the account_id of this InlineResponse20078Data.  # noqa: E501

        The id of the Account associated with this Position  # noqa: E501

        :return: The account_id of this InlineResponse20078Data.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this InlineResponse20078Data.

        The id of the Account associated with this Position  # noqa: E501

        :param account_id: The account_id of this InlineResponse20078Data.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def direction(self):
        """Gets the direction of this InlineResponse20078Data.  # noqa: E501

        Flag to indicate if Holding is Long or Short. Potential values, L = Long, S = Short  # noqa: E501

        :return: The direction of this InlineResponse20078Data.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this InlineResponse20078Data.

        Flag to indicate if Holding is Long or Short. Potential values, L = Long, S = Short  # noqa: E501

        :param direction: The direction of this InlineResponse20078Data.  # noqa: E501
        :type: str
        """
        allowed_values = ["L = Long", "S = Short"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def abs_open_units(self):
        """Gets the abs_open_units of this InlineResponse20078Data.  # noqa: E501

        Quantity of shares for the Position  # noqa: E501

        :return: The abs_open_units of this InlineResponse20078Data.  # noqa: E501
        :rtype: float
        """
        return self._abs_open_units

    @abs_open_units.setter
    def abs_open_units(self, abs_open_units):
        """Sets the abs_open_units of this InlineResponse20078Data.

        Quantity of shares for the Position  # noqa: E501

        :param abs_open_units: The abs_open_units of this InlineResponse20078Data.  # noqa: E501
        :type: float
        """

        self._abs_open_units = abs_open_units

    @property
    def cost_basis_unit_price(self):
        """Gets the cost_basis_unit_price of this InlineResponse20078Data.  # noqa: E501

        Unit cost price for the position (i.e. tax lot)  # noqa: E501

        :return: The cost_basis_unit_price of this InlineResponse20078Data.  # noqa: E501
        :rtype: float
        """
        return self._cost_basis_unit_price

    @cost_basis_unit_price.setter
    def cost_basis_unit_price(self, cost_basis_unit_price):
        """Sets the cost_basis_unit_price of this InlineResponse20078Data.

        Unit cost price for the position (i.e. tax lot)  # noqa: E501

        :param cost_basis_unit_price: The cost_basis_unit_price of this InlineResponse20078Data.  # noqa: E501
        :type: float
        """

        self._cost_basis_unit_price = cost_basis_unit_price

    @property
    def appraised_unit_price(self):
        """Gets the appraised_unit_price of this InlineResponse20078Data.  # noqa: E501

        Market price of the security on the as_of_date  # noqa: E501

        :return: The appraised_unit_price of this InlineResponse20078Data.  # noqa: E501
        :rtype: float
        """
        return self._appraised_unit_price

    @appraised_unit_price.setter
    def appraised_unit_price(self, appraised_unit_price):
        """Sets the appraised_unit_price of this InlineResponse20078Data.

        Market price of the security on the as_of_date  # noqa: E501

        :param appraised_unit_price: The appraised_unit_price of this InlineResponse20078Data.  # noqa: E501
        :type: float
        """

        self._appraised_unit_price = appraised_unit_price

    @property
    def realized_gain_loss(self):
        """Gets the realized_gain_loss of this InlineResponse20078Data.  # noqa: E501

        Dollar gain or loss from trade activity for this security on the as_of_date  # noqa: E501

        :return: The realized_gain_loss of this InlineResponse20078Data.  # noqa: E501
        :rtype: float
        """
        return self._realized_gain_loss

    @realized_gain_loss.setter
    def realized_gain_loss(self, realized_gain_loss):
        """Sets the realized_gain_loss of this InlineResponse20078Data.

        Dollar gain or loss from trade activity for this security on the as_of_date  # noqa: E501

        :param realized_gain_loss: The realized_gain_loss of this InlineResponse20078Data.  # noqa: E501
        :type: float
        """

        self._realized_gain_loss = realized_gain_loss

    @property
    def abs_closed_units(self):
        """Gets the abs_closed_units of this InlineResponse20078Data.  # noqa: E501

        Quantity of shares closed  # noqa: E501

        :return: The abs_closed_units of this InlineResponse20078Data.  # noqa: E501
        :rtype: float
        """
        return self._abs_closed_units

    @abs_closed_units.setter
    def abs_closed_units(self, abs_closed_units):
        """Sets the abs_closed_units of this InlineResponse20078Data.

        Quantity of shares closed  # noqa: E501

        :param abs_closed_units: The abs_closed_units of this InlineResponse20078Data.  # noqa: E501
        :type: float
        """

        self._abs_closed_units = abs_closed_units

    @property
    def cost_basis_known(self):
        """Gets the cost_basis_known of this InlineResponse20078Data.  # noqa: E501

        Is the cost basis known for this position?  # noqa: E501

        :return: The cost_basis_known of this InlineResponse20078Data.  # noqa: E501
        :rtype: bool
        """
        return self._cost_basis_known

    @cost_basis_known.setter
    def cost_basis_known(self, cost_basis_known):
        """Sets the cost_basis_known of this InlineResponse20078Data.

        Is the cost basis known for this position?  # noqa: E501

        :param cost_basis_known: The cost_basis_known of this InlineResponse20078Data.  # noqa: E501
        :type: bool
        """

        self._cost_basis_known = cost_basis_known

    @property
    def created_at_utc(self):
        """Gets the created_at_utc of this InlineResponse20078Data.  # noqa: E501

        Timestamp for when the record was created  # noqa: E501

        :return: The created_at_utc of this InlineResponse20078Data.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at_utc

    @created_at_utc.setter
    def created_at_utc(self, created_at_utc):
        """Sets the created_at_utc of this InlineResponse20078Data.

        Timestamp for when the record was created  # noqa: E501

        :param created_at_utc: The created_at_utc of this InlineResponse20078Data.  # noqa: E501
        :type: datetime
        """

        self._created_at_utc = created_at_utc

    @property
    def updated_at_utc(self):
        """Gets the updated_at_utc of this InlineResponse20078Data.  # noqa: E501

        Timestamp for when the record was updated  # noqa: E501

        :return: The updated_at_utc of this InlineResponse20078Data.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_utc

    @updated_at_utc.setter
    def updated_at_utc(self, updated_at_utc):
        """Sets the updated_at_utc of this InlineResponse20078Data.

        Timestamp for when the record was updated  # noqa: E501

        :param updated_at_utc: The updated_at_utc of this InlineResponse20078Data.  # noqa: E501
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
        if issubclass(InlineResponse20078Data, dict):
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
        if not isinstance(other, InlineResponse20078Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
