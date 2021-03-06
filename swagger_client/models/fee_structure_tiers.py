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

class FeeStructureTiers(object):
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
        'min_balance': 'float',
        'max_balance': 'float',
        'rate': 'float',
        'fee_structure_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'min_balance': 'min_balance',
        'max_balance': 'max_balance',
        'rate': 'rate',
        'fee_structure_id': 'fee_structure_id'
    }

    def __init__(self, id=None, min_balance=None, max_balance=None, rate=None, fee_structure_id=None):  # noqa: E501
        """FeeStructureTiers - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._min_balance = None
        self._max_balance = None
        self._rate = None
        self._fee_structure_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if min_balance is not None:
            self.min_balance = min_balance
        if max_balance is not None:
            self.max_balance = max_balance
        if rate is not None:
            self.rate = rate
        if fee_structure_id is not None:
            self.fee_structure_id = fee_structure_id

    @property
    def id(self):
        """Gets the id of this FeeStructureTiers.  # noqa: E501

        Id associated with the tier object  # noqa: E501

        :return: The id of this FeeStructureTiers.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FeeStructureTiers.

        Id associated with the tier object  # noqa: E501

        :param id: The id of this FeeStructureTiers.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def min_balance(self):
        """Gets the min_balance of this FeeStructureTiers.  # noqa: E501

        Minimum balance for the tier  # noqa: E501

        :return: The min_balance of this FeeStructureTiers.  # noqa: E501
        :rtype: float
        """
        return self._min_balance

    @min_balance.setter
    def min_balance(self, min_balance):
        """Sets the min_balance of this FeeStructureTiers.

        Minimum balance for the tier  # noqa: E501

        :param min_balance: The min_balance of this FeeStructureTiers.  # noqa: E501
        :type: float
        """

        self._min_balance = min_balance

    @property
    def max_balance(self):
        """Gets the max_balance of this FeeStructureTiers.  # noqa: E501

        Maximum balance for the tier  # noqa: E501

        :return: The max_balance of this FeeStructureTiers.  # noqa: E501
        :rtype: float
        """
        return self._max_balance

    @max_balance.setter
    def max_balance(self, max_balance):
        """Sets the max_balance of this FeeStructureTiers.

        Maximum balance for the tier  # noqa: E501

        :param max_balance: The max_balance of this FeeStructureTiers.  # noqa: E501
        :type: float
        """

        self._max_balance = max_balance

    @property
    def rate(self):
        """Gets the rate of this FeeStructureTiers.  # noqa: E501

        Rate for the tier  # noqa: E501

        :return: The rate of this FeeStructureTiers.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this FeeStructureTiers.

        Rate for the tier  # noqa: E501

        :param rate: The rate of this FeeStructureTiers.  # noqa: E501
        :type: float
        """

        self._rate = rate

    @property
    def fee_structure_id(self):
        """Gets the fee_structure_id of this FeeStructureTiers.  # noqa: E501

        Fee structure id associated with this tier  # noqa: E501

        :return: The fee_structure_id of this FeeStructureTiers.  # noqa: E501
        :rtype: int
        """
        return self._fee_structure_id

    @fee_structure_id.setter
    def fee_structure_id(self, fee_structure_id):
        """Sets the fee_structure_id of this FeeStructureTiers.

        Fee structure id associated with this tier  # noqa: E501

        :param fee_structure_id: The fee_structure_id of this FeeStructureTiers.  # noqa: E501
        :type: int
        """

        self._fee_structure_id = fee_structure_id

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
        if issubclass(FeeStructureTiers, dict):
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
        if not isinstance(other, FeeStructureTiers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
