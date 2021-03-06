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

class GroupsFilterBody(object):
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
        'name': 'str',
        'slug': 'str',
        'household_id': 'int',
        'firm_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'slug': 'slug',
        'household_id': 'household_id',
        'firm_id': 'firm_id'
    }

    def __init__(self, id=None, name=None, slug=None, household_id=None, firm_id=None):  # noqa: E501
        """GroupsFilterBody - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._slug = None
        self._household_id = None
        self._firm_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = slug
        if household_id is not None:
            self.household_id = household_id
        if firm_id is not None:
            self.firm_id = firm_id

    @property
    def id(self):
        """Gets the id of this GroupsFilterBody.  # noqa: E501

        The unique resource ID for this Billing Group  # noqa: E501

        :return: The id of this GroupsFilterBody.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupsFilterBody.

        The unique resource ID for this Billing Group  # noqa: E501

        :param id: The id of this GroupsFilterBody.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GroupsFilterBody.  # noqa: E501

        The name of this Billing Group  # noqa: E501

        :return: The name of this GroupsFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupsFilterBody.

        The name of this Billing Group  # noqa: E501

        :param name: The name of this GroupsFilterBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this GroupsFilterBody.  # noqa: E501

        The sluggified name of this Billing Group  # noqa: E501

        :return: The slug of this GroupsFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this GroupsFilterBody.

        The sluggified name of this Billing Group  # noqa: E501

        :param slug: The slug of this GroupsFilterBody.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def household_id(self):
        """Gets the household_id of this GroupsFilterBody.  # noqa: E501

        The ID of the associated household for this Billing Group  # noqa: E501

        :return: The household_id of this GroupsFilterBody.  # noqa: E501
        :rtype: int
        """
        return self._household_id

    @household_id.setter
    def household_id(self, household_id):
        """Sets the household_id of this GroupsFilterBody.

        The ID of the associated household for this Billing Group  # noqa: E501

        :param household_id: The household_id of this GroupsFilterBody.  # noqa: E501
        :type: int
        """

        self._household_id = household_id

    @property
    def firm_id(self):
        """Gets the firm_id of this GroupsFilterBody.  # noqa: E501

        The firm ID of the managing firm for this Billing Group  # noqa: E501

        :return: The firm_id of this GroupsFilterBody.  # noqa: E501
        :rtype: int
        """
        return self._firm_id

    @firm_id.setter
    def firm_id(self, firm_id):
        """Sets the firm_id of this GroupsFilterBody.

        The firm ID of the managing firm for this Billing Group  # noqa: E501

        :param firm_id: The firm_id of this GroupsFilterBody.  # noqa: E501
        :type: int
        """

        self._firm_id = firm_id

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
        if issubclass(GroupsFilterBody, dict):
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
        if not isinstance(other, GroupsFilterBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
