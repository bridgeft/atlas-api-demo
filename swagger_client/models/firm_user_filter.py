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

class FirmUserFilter(object):
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
        'account_access_level': 'str'
    }

    attribute_map = {
        'id': 'id',
        'firm_id': 'firm_id',
        'account_access_level': 'account_access_level'
    }

    def __init__(self, id=None, firm_id=None, account_access_level=None):  # noqa: E501
        """FirmUserFilter - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._firm_id = None
        self._account_access_level = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if firm_id is not None:
            self.firm_id = firm_id
        if account_access_level is not None:
            self.account_access_level = account_access_level

    @property
    def id(self):
        """Gets the id of this FirmUserFilter.  # noqa: E501

        Unique ID for this user object  # noqa: E501

        :return: The id of this FirmUserFilter.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FirmUserFilter.

        Unique ID for this user object  # noqa: E501

        :param id: The id of this FirmUserFilter.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def firm_id(self):
        """Gets the firm_id of this FirmUserFilter.  # noqa: E501

        ID of the owning firm  # noqa: E501

        :return: The firm_id of this FirmUserFilter.  # noqa: E501
        :rtype: int
        """
        return self._firm_id

    @firm_id.setter
    def firm_id(self, firm_id):
        """Sets the firm_id of this FirmUserFilter.

        ID of the owning firm  # noqa: E501

        :param firm_id: The firm_id of this FirmUserFilter.  # noqa: E501
        :type: int
        """

        self._firm_id = firm_id

    @property
    def account_access_level(self):
        """Gets the account_access_level of this FirmUserFilter.  # noqa: E501

        The user's accessibility level with respect to accounts; can either have access to all accounts or be limited to a subset of them. Can either be all or limited.  # noqa: E501

        :return: The account_access_level of this FirmUserFilter.  # noqa: E501
        :rtype: str
        """
        return self._account_access_level

    @account_access_level.setter
    def account_access_level(self, account_access_level):
        """Sets the account_access_level of this FirmUserFilter.

        The user's accessibility level with respect to accounts; can either have access to all accounts or be limited to a subset of them. Can either be all or limited.  # noqa: E501

        :param account_access_level: The account_access_level of this FirmUserFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["all", "limited"]  # noqa: E501
        if account_access_level not in allowed_values:
            raise ValueError(
                "Invalid value for `account_access_level` ({0}), must be one of {1}"  # noqa: E501
                .format(account_access_level, allowed_values)
            )

        self._account_access_level = account_access_level

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
        if issubclass(FirmUserFilter, dict):
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
        if not isinstance(other, FirmUserFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other