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

class InlineResponse2004Data(object):
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
        'firm_id': 'int',
        'plaid_item_id': 'int',
        'plaid_account_id': 'int',
        'household_id': 'int',
        'type': 'str',
        'subtype': 'str',
        'institution_name': 'str',
        'official_name': 'str',
        'mask': 'str',
        'name': 'str',
        'balances': 'HeldawayaccountsfilterBalances',
        'verification_status': 'str',
        'created_at_utc': 'datetime',
        'updated_at_utc': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'firm_id': 'firm_id',
        'plaid_item_id': 'plaid_item_id',
        'plaid_account_id': 'plaid_account_id',
        'household_id': 'household_id',
        'type': 'type',
        'subtype': 'subtype',
        'institution_name': 'institution_name',
        'official_name': 'official_name',
        'mask': 'mask',
        'name': 'name',
        'balances': 'balances',
        'verification_status': 'verification_status',
        'created_at_utc': 'created_at_utc',
        'updated_at_utc': 'updated_at_utc'
    }

    def __init__(self, id=None, firm_id=None, plaid_item_id=None, plaid_account_id=None, household_id=None, type=None, subtype=None, institution_name=None, official_name=None, mask=None, name=None, balances=None, verification_status=None, created_at_utc=None, updated_at_utc=None):  # noqa: E501
        """InlineResponse2004Data - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._firm_id = None
        self._plaid_item_id = None
        self._plaid_account_id = None
        self._household_id = None
        self._type = None
        self._subtype = None
        self._institution_name = None
        self._official_name = None
        self._mask = None
        self._name = None
        self._balances = None
        self._verification_status = None
        self._created_at_utc = None
        self._updated_at_utc = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if firm_id is not None:
            self.firm_id = firm_id
        if plaid_item_id is not None:
            self.plaid_item_id = plaid_item_id
        if plaid_account_id is not None:
            self.plaid_account_id = plaid_account_id
        if household_id is not None:
            self.household_id = household_id
        if type is not None:
            self.type = type
        if subtype is not None:
            self.subtype = subtype
        if institution_name is not None:
            self.institution_name = institution_name
        if official_name is not None:
            self.official_name = official_name
        if mask is not None:
            self.mask = mask
        if name is not None:
            self.name = name
        if balances is not None:
            self.balances = balances
        if verification_status is not None:
            self.verification_status = verification_status
        if created_at_utc is not None:
            self.created_at_utc = created_at_utc
        if updated_at_utc is not None:
            self.updated_at_utc = updated_at_utc

    @property
    def id(self):
        """Gets the id of this InlineResponse2004Data.  # noqa: E501

        Unique ID for this account object  # noqa: E501

        :return: The id of this InlineResponse2004Data.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2004Data.

        Unique ID for this account object  # noqa: E501

        :param id: The id of this InlineResponse2004Data.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def firm_id(self):
        """Gets the firm_id of this InlineResponse2004Data.  # noqa: E501

        ID of the owning firm  # noqa: E501

        :return: The firm_id of this InlineResponse2004Data.  # noqa: E501
        :rtype: int
        """
        return self._firm_id

    @firm_id.setter
    def firm_id(self, firm_id):
        """Sets the firm_id of this InlineResponse2004Data.

        ID of the owning firm  # noqa: E501

        :param firm_id: The firm_id of this InlineResponse2004Data.  # noqa: E501
        :type: int
        """

        self._firm_id = firm_id

    @property
    def plaid_item_id(self):
        """Gets the plaid_item_id of this InlineResponse2004Data.  # noqa: E501

        ID of the associated Plaid connection  # noqa: E501

        :return: The plaid_item_id of this InlineResponse2004Data.  # noqa: E501
        :rtype: int
        """
        return self._plaid_item_id

    @plaid_item_id.setter
    def plaid_item_id(self, plaid_item_id):
        """Sets the plaid_item_id of this InlineResponse2004Data.

        ID of the associated Plaid connection  # noqa: E501

        :param plaid_item_id: The plaid_item_id of this InlineResponse2004Data.  # noqa: E501
        :type: int
        """

        self._plaid_item_id = plaid_item_id

    @property
    def plaid_account_id(self):
        """Gets the plaid_account_id of this InlineResponse2004Data.  # noqa: E501

        Account associated with this plaid account object  # noqa: E501

        :return: The plaid_account_id of this InlineResponse2004Data.  # noqa: E501
        :rtype: int
        """
        return self._plaid_account_id

    @plaid_account_id.setter
    def plaid_account_id(self, plaid_account_id):
        """Sets the plaid_account_id of this InlineResponse2004Data.

        Account associated with this plaid account object  # noqa: E501

        :param plaid_account_id: The plaid_account_id of this InlineResponse2004Data.  # noqa: E501
        :type: int
        """

        self._plaid_account_id = plaid_account_id

    @property
    def household_id(self):
        """Gets the household_id of this InlineResponse2004Data.  # noqa: E501

        ID of the household to which this account belongs  # noqa: E501

        :return: The household_id of this InlineResponse2004Data.  # noqa: E501
        :rtype: int
        """
        return self._household_id

    @household_id.setter
    def household_id(self, household_id):
        """Sets the household_id of this InlineResponse2004Data.

        ID of the household to which this account belongs  # noqa: E501

        :param household_id: The household_id of this InlineResponse2004Data.  # noqa: E501
        :type: int
        """

        self._household_id = household_id

    @property
    def type(self):
        """Gets the type of this InlineResponse2004Data.  # noqa: E501

        See Account Schema on Plaid's API Documentation; https://plaid.com/docs/#account-schema  # noqa: E501

        :return: The type of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse2004Data.

        See Account Schema on Plaid's API Documentation; https://plaid.com/docs/#account-schema  # noqa: E501

        :param type: The type of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def subtype(self):
        """Gets the subtype of this InlineResponse2004Data.  # noqa: E501

        See Account Schema on Plaid's API Documentation; https://plaid.com/docs/#account-schema  # noqa: E501

        :return: The subtype of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this InlineResponse2004Data.

        See Account Schema on Plaid's API Documentation; https://plaid.com/docs/#account-schema  # noqa: E501

        :param subtype: The subtype of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._subtype = subtype

    @property
    def institution_name(self):
        """Gets the institution_name of this InlineResponse2004Data.  # noqa: E501

        Name of the account-holder institution  # noqa: E501

        :return: The institution_name of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._institution_name

    @institution_name.setter
    def institution_name(self, institution_name):
        """Sets the institution_name of this InlineResponse2004Data.

        Name of the account-holder institution  # noqa: E501

        :param institution_name: The institution_name of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._institution_name = institution_name

    @property
    def official_name(self):
        """Gets the official_name of this InlineResponse2004Data.  # noqa: E501

        Official name of the account assigned by the institution  # noqa: E501

        :return: The official_name of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._official_name

    @official_name.setter
    def official_name(self, official_name):
        """Sets the official_name of this InlineResponse2004Data.

        Official name of the account assigned by the institution  # noqa: E501

        :param official_name: The official_name of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._official_name = official_name

    @property
    def mask(self):
        """Gets the mask of this InlineResponse2004Data.  # noqa: E501

        Last four alphanumeric digits of the account number  # noqa: E501

        :return: The mask of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._mask

    @mask.setter
    def mask(self, mask):
        """Sets the mask of this InlineResponse2004Data.

        Last four alphanumeric digits of the account number  # noqa: E501

        :param mask: The mask of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._mask = mask

    @property
    def name(self):
        """Gets the name of this InlineResponse2004Data.  # noqa: E501

        Account name  # noqa: E501

        :return: The name of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2004Data.

        Account name  # noqa: E501

        :param name: The name of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def balances(self):
        """Gets the balances of this InlineResponse2004Data.  # noqa: E501


        :return: The balances of this InlineResponse2004Data.  # noqa: E501
        :rtype: HeldawayaccountsfilterBalances
        """
        return self._balances

    @balances.setter
    def balances(self, balances):
        """Sets the balances of this InlineResponse2004Data.


        :param balances: The balances of this InlineResponse2004Data.  # noqa: E501
        :type: HeldawayaccountsfilterBalances
        """

        self._balances = balances

    @property
    def verification_status(self):
        """Gets the verification_status of this InlineResponse2004Data.  # noqa: E501

        See https://plaid.com/docs/#account-verification-status  # noqa: E501

        :return: The verification_status of this InlineResponse2004Data.  # noqa: E501
        :rtype: str
        """
        return self._verification_status

    @verification_status.setter
    def verification_status(self, verification_status):
        """Sets the verification_status of this InlineResponse2004Data.

        See https://plaid.com/docs/#account-verification-status  # noqa: E501

        :param verification_status: The verification_status of this InlineResponse2004Data.  # noqa: E501
        :type: str
        """

        self._verification_status = verification_status

    @property
    def created_at_utc(self):
        """Gets the created_at_utc of this InlineResponse2004Data.  # noqa: E501

        Timestamp for when the record was created  # noqa: E501

        :return: The created_at_utc of this InlineResponse2004Data.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at_utc

    @created_at_utc.setter
    def created_at_utc(self, created_at_utc):
        """Sets the created_at_utc of this InlineResponse2004Data.

        Timestamp for when the record was created  # noqa: E501

        :param created_at_utc: The created_at_utc of this InlineResponse2004Data.  # noqa: E501
        :type: datetime
        """

        self._created_at_utc = created_at_utc

    @property
    def updated_at_utc(self):
        """Gets the updated_at_utc of this InlineResponse2004Data.  # noqa: E501

        Timestamp for when the record was updated  # noqa: E501

        :return: The updated_at_utc of this InlineResponse2004Data.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_utc

    @updated_at_utc.setter
    def updated_at_utc(self, updated_at_utc):
        """Sets the updated_at_utc of this InlineResponse2004Data.

        Timestamp for when the record was updated  # noqa: E501

        :param updated_at_utc: The updated_at_utc of this InlineResponse2004Data.  # noqa: E501
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
        if issubclass(InlineResponse2004Data, dict):
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
        if not isinstance(other, InlineResponse2004Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
