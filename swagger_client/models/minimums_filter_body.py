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

class MinimumsFilterBody(object):
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
        'name': 'str',
        'value': 'float',
        'value_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'firm_id': 'firm_id',
        'name': 'name',
        'value': 'value',
        'value_type': 'value_type'
    }

    def __init__(self, id=None, firm_id=None, name=None, value=None, value_type=None):  # noqa: E501
        """MinimumsFilterBody - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._firm_id = None
        self._name = None
        self._value = None
        self._value_type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if firm_id is not None:
            self.firm_id = firm_id
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if value_type is not None:
            self.value_type = value_type

    @property
    def id(self):
        """Gets the id of this MinimumsFilterBody.  # noqa: E501

        The unique resource ID for this Billing Minimum  # noqa: E501

        :return: The id of this MinimumsFilterBody.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MinimumsFilterBody.

        The unique resource ID for this Billing Minimum  # noqa: E501

        :param id: The id of this MinimumsFilterBody.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def firm_id(self):
        """Gets the firm_id of this MinimumsFilterBody.  # noqa: E501

        The firm ID of the managing firm  # noqa: E501

        :return: The firm_id of this MinimumsFilterBody.  # noqa: E501
        :rtype: int
        """
        return self._firm_id

    @firm_id.setter
    def firm_id(self, firm_id):
        """Sets the firm_id of this MinimumsFilterBody.

        The firm ID of the managing firm  # noqa: E501

        :param firm_id: The firm_id of this MinimumsFilterBody.  # noqa: E501
        :type: int
        """

        self._firm_id = firm_id

    @property
    def name(self):
        """Gets the name of this MinimumsFilterBody.  # noqa: E501

        The name of this Billing Minimum  # noqa: E501

        :return: The name of this MinimumsFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MinimumsFilterBody.

        The name of this Billing Minimum  # noqa: E501

        :param name: The name of this MinimumsFilterBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this MinimumsFilterBody.  # noqa: E501

        The value of this Billing Minimum  # noqa: E501

        :return: The value of this MinimumsFilterBody.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MinimumsFilterBody.

        The value of this Billing Minimum  # noqa: E501

        :param value: The value of this MinimumsFilterBody.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def value_type(self):
        """Gets the value_type of this MinimumsFilterBody.  # noqa: E501

        F for flat amount, P for percentage  # noqa: E501

        :return: The value_type of this MinimumsFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this MinimumsFilterBody.

        F for flat amount, P for percentage  # noqa: E501

        :param value_type: The value_type of this MinimumsFilterBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["F = Flat amount", "P = Percentage"]  # noqa: E501
        if value_type not in allowed_values:
            raise ValueError(
                "Invalid value for `value_type` ({0}), must be one of {1}"  # noqa: E501
                .format(value_type, allowed_values)
            )

        self._value_type = value_type

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
        if issubclass(MinimumsFilterBody, dict):
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
        if not isinstance(other, MinimumsFilterBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
