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

class FeeStructure(object):
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
        'created_by_user_id': 'int',
        'firm_id': 'int',
        'name': 'str',
        'slug': 'str',
        'calculation_type': 'str',
        'collection_type': 'str',
        'frequency': 'str',
        'quarter_cycle': 'int',
        'balance_type': 'str',
        'flat_rate': 'float',
        'flat_dollar_fee': 'float',
        'tiers': 'list[FeeStructureTiers]',
        'created_at_utc': 'datetime',
        'updated_at_utc': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'created_by_user_id': 'created_by_user_id',
        'firm_id': 'firm_id',
        'name': 'name',
        'slug': 'slug',
        'calculation_type': 'calculation_type',
        'collection_type': 'collection_type',
        'frequency': 'frequency',
        'quarter_cycle': 'quarter_cycle',
        'balance_type': 'balance_type',
        'flat_rate': 'flat_rate',
        'flat_dollar_fee': 'flat_dollar_fee',
        'tiers': 'tiers',
        'created_at_utc': 'created_at_utc',
        'updated_at_utc': 'updated_at_utc'
    }

    def __init__(self, id=None, created_by_user_id=None, firm_id=None, name=None, slug=None, calculation_type=None, collection_type=None, frequency=None, quarter_cycle=None, balance_type=None, flat_rate=None, flat_dollar_fee=None, tiers=None, created_at_utc=None, updated_at_utc=None):  # noqa: E501
        """FeeStructure - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_by_user_id = None
        self._firm_id = None
        self._name = None
        self._slug = None
        self._calculation_type = None
        self._collection_type = None
        self._frequency = None
        self._quarter_cycle = None
        self._balance_type = None
        self._flat_rate = None
        self._flat_dollar_fee = None
        self._tiers = None
        self._created_at_utc = None
        self._updated_at_utc = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_by_user_id is not None:
            self.created_by_user_id = created_by_user_id
        if firm_id is not None:
            self.firm_id = firm_id
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = slug
        if calculation_type is not None:
            self.calculation_type = calculation_type
        if collection_type is not None:
            self.collection_type = collection_type
        if frequency is not None:
            self.frequency = frequency
        if quarter_cycle is not None:
            self.quarter_cycle = quarter_cycle
        if balance_type is not None:
            self.balance_type = balance_type
        if flat_rate is not None:
            self.flat_rate = flat_rate
        if flat_dollar_fee is not None:
            self.flat_dollar_fee = flat_dollar_fee
        if tiers is not None:
            self.tiers = tiers
        if created_at_utc is not None:
            self.created_at_utc = created_at_utc
        if updated_at_utc is not None:
            self.updated_at_utc = updated_at_utc

    @property
    def id(self):
        """Gets the id of this FeeStructure.  # noqa: E501

        The unique resource ID for this Fee Structure  # noqa: E501

        :return: The id of this FeeStructure.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FeeStructure.

        The unique resource ID for this Fee Structure  # noqa: E501

        :param id: The id of this FeeStructure.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def created_by_user_id(self):
        """Gets the created_by_user_id of this FeeStructure.  # noqa: E501

        The user ID of the creator User  # noqa: E501

        :return: The created_by_user_id of this FeeStructure.  # noqa: E501
        :rtype: int
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id):
        """Sets the created_by_user_id of this FeeStructure.

        The user ID of the creator User  # noqa: E501

        :param created_by_user_id: The created_by_user_id of this FeeStructure.  # noqa: E501
        :type: int
        """

        self._created_by_user_id = created_by_user_id

    @property
    def firm_id(self):
        """Gets the firm_id of this FeeStructure.  # noqa: E501

        The firm ID of the managing firm  # noqa: E501

        :return: The firm_id of this FeeStructure.  # noqa: E501
        :rtype: int
        """
        return self._firm_id

    @firm_id.setter
    def firm_id(self, firm_id):
        """Sets the firm_id of this FeeStructure.

        The firm ID of the managing firm  # noqa: E501

        :param firm_id: The firm_id of this FeeStructure.  # noqa: E501
        :type: int
        """

        self._firm_id = firm_id

    @property
    def name(self):
        """Gets the name of this FeeStructure.  # noqa: E501

        The name of this Fee Structure  # noqa: E501

        :return: The name of this FeeStructure.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeeStructure.

        The name of this Fee Structure  # noqa: E501

        :param name: The name of this FeeStructure.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this FeeStructure.  # noqa: E501

        The slugified name of this Fee Structure  # noqa: E501

        :return: The slug of this FeeStructure.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this FeeStructure.

        The slugified name of this Fee Structure  # noqa: E501

        :param slug: The slug of this FeeStructure.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def calculation_type(self):
        """Gets the calculation_type of this FeeStructure.  # noqa: E501

        See Billing Calculation Types  # noqa: E501

        :return: The calculation_type of this FeeStructure.  # noqa: E501
        :rtype: str
        """
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        """Sets the calculation_type of this FeeStructure.

        See Billing Calculation Types  # noqa: E501

        :param calculation_type: The calculation_type of this FeeStructure.  # noqa: E501
        :type: str
        """

        self._calculation_type = calculation_type

    @property
    def collection_type(self):
        """Gets the collection_type of this FeeStructure.  # noqa: E501

        R for Flat Rate, A for Flat Amount, G for Flat Group, D for Drop Through, T for Tiered Fee, and F for Free Fee  # noqa: E501

        :return: The collection_type of this FeeStructure.  # noqa: E501
        :rtype: str
        """
        return self._collection_type

    @collection_type.setter
    def collection_type(self, collection_type):
        """Sets the collection_type of this FeeStructure.

        R for Flat Rate, A for Flat Amount, G for Flat Group, D for Drop Through, T for Tiered Fee, and F for Free Fee  # noqa: E501

        :param collection_type: The collection_type of this FeeStructure.  # noqa: E501
        :type: str
        """
        allowed_values = ["R = Flat Rate", "A = Flat Amount", "G = Flat Group", "D = Drop Through", "T = Tiered Fee", "F = Free Fee"]  # noqa: E501
        if collection_type not in allowed_values:
            raise ValueError(
                "Invalid value for `collection_type` ({0}), must be one of {1}"  # noqa: E501
                .format(collection_type, allowed_values)
            )

        self._collection_type = collection_type

    @property
    def frequency(self):
        """Gets the frequency of this FeeStructure.  # noqa: E501

        See Frequency Codes  # noqa: E501

        :return: The frequency of this FeeStructure.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this FeeStructure.

        See Frequency Codes  # noqa: E501

        :param frequency: The frequency of this FeeStructure.  # noqa: E501
        :type: str
        """
        allowed_values = ["M = Monthly", "Q = Quarterly"]  # noqa: E501
        if frequency not in allowed_values:
            raise ValueError(
                "Invalid value for `frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(frequency, allowed_values)
            )

        self._frequency = frequency

    @property
    def quarter_cycle(self):
        """Gets the quarter_cycle of this FeeStructure.  # noqa: E501

        See Billing Quarter Cycle Codes  # noqa: E501

        :return: The quarter_cycle of this FeeStructure.  # noqa: E501
        :rtype: int
        """
        return self._quarter_cycle

    @quarter_cycle.setter
    def quarter_cycle(self, quarter_cycle):
        """Sets the quarter_cycle of this FeeStructure.

        See Billing Quarter Cycle Codes  # noqa: E501

        :param quarter_cycle: The quarter_cycle of this FeeStructure.  # noqa: E501
        :type: int
        """

        self._quarter_cycle = quarter_cycle

    @property
    def balance_type(self):
        """Gets the balance_type of this FeeStructure.  # noqa: E501

        E for end of period balance, A for average daily balance  # noqa: E501

        :return: The balance_type of this FeeStructure.  # noqa: E501
        :rtype: str
        """
        return self._balance_type

    @balance_type.setter
    def balance_type(self, balance_type):
        """Sets the balance_type of this FeeStructure.

        E for end of period balance, A for average daily balance  # noqa: E501

        :param balance_type: The balance_type of this FeeStructure.  # noqa: E501
        :type: str
        """
        allowed_values = ["E = End of period balance", "A = Average daily balance"]  # noqa: E501
        if balance_type not in allowed_values:
            raise ValueError(
                "Invalid value for `balance_type` ({0}), must be one of {1}"  # noqa: E501
                .format(balance_type, allowed_values)
            )

        self._balance_type = balance_type

    @property
    def flat_rate(self):
        """Gets the flat_rate of this FeeStructure.  # noqa: E501

        The flat rate for this Fee Structure. Must be between 0 and 99 inclusive. Will be stored and converted to a Percentage. (i.e. 1 -> 1% and 0.25 -> 0.25%)  # noqa: E501

        :return: The flat_rate of this FeeStructure.  # noqa: E501
        :rtype: float
        """
        return self._flat_rate

    @flat_rate.setter
    def flat_rate(self, flat_rate):
        """Sets the flat_rate of this FeeStructure.

        The flat rate for this Fee Structure. Must be between 0 and 99 inclusive. Will be stored and converted to a Percentage. (i.e. 1 -> 1% and 0.25 -> 0.25%)  # noqa: E501

        :param flat_rate: The flat_rate of this FeeStructure.  # noqa: E501
        :type: float
        """

        self._flat_rate = flat_rate

    @property
    def flat_dollar_fee(self):
        """Gets the flat_dollar_fee of this FeeStructure.  # noqa: E501

        The flat dollar fee for this Fee Structure  # noqa: E501

        :return: The flat_dollar_fee of this FeeStructure.  # noqa: E501
        :rtype: float
        """
        return self._flat_dollar_fee

    @flat_dollar_fee.setter
    def flat_dollar_fee(self, flat_dollar_fee):
        """Sets the flat_dollar_fee of this FeeStructure.

        The flat dollar fee for this Fee Structure  # noqa: E501

        :param flat_dollar_fee: The flat_dollar_fee of this FeeStructure.  # noqa: E501
        :type: float
        """

        self._flat_dollar_fee = flat_dollar_fee

    @property
    def tiers(self):
        """Gets the tiers of this FeeStructure.  # noqa: E501

        Tiers associated with the fee structure  # noqa: E501

        :return: The tiers of this FeeStructure.  # noqa: E501
        :rtype: list[FeeStructureTiers]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this FeeStructure.

        Tiers associated with the fee structure  # noqa: E501

        :param tiers: The tiers of this FeeStructure.  # noqa: E501
        :type: list[FeeStructureTiers]
        """

        self._tiers = tiers

    @property
    def created_at_utc(self):
        """Gets the created_at_utc of this FeeStructure.  # noqa: E501

        Timestamp for when the record was created  # noqa: E501

        :return: The created_at_utc of this FeeStructure.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at_utc

    @created_at_utc.setter
    def created_at_utc(self, created_at_utc):
        """Sets the created_at_utc of this FeeStructure.

        Timestamp for when the record was created  # noqa: E501

        :param created_at_utc: The created_at_utc of this FeeStructure.  # noqa: E501
        :type: datetime
        """

        self._created_at_utc = created_at_utc

    @property
    def updated_at_utc(self):
        """Gets the updated_at_utc of this FeeStructure.  # noqa: E501

        Timestamp for when the record was updated  # noqa: E501

        :return: The updated_at_utc of this FeeStructure.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_utc

    @updated_at_utc.setter
    def updated_at_utc(self, updated_at_utc):
        """Sets the updated_at_utc of this FeeStructure.

        Timestamp for when the record was updated  # noqa: E501

        :param updated_at_utc: The updated_at_utc of this FeeStructure.  # noqa: E501
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
        if issubclass(FeeStructure, dict):
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
        if not isinstance(other, FeeStructure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
