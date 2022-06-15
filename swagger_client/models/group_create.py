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

class GroupCreate(object):
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
        'name': 'str',
        'slug': 'str',
        'household_id': 'int',
        'firm_id': 'int',
        'minimum_ids': 'list[int]',
        'assignments': 'GroupcreateAssignments'
    }

    attribute_map = {
        'name': 'name',
        'slug': 'slug',
        'household_id': 'household_id',
        'firm_id': 'firm_id',
        'minimum_ids': 'minimum_ids',
        'assignments': 'assignments'
    }

    def __init__(self, name=None, slug=None, household_id=None, firm_id=None, minimum_ids=None, assignments=None):  # noqa: E501
        """GroupCreate - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._slug = None
        self._household_id = None
        self._firm_id = None
        self._minimum_ids = None
        self._assignments = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = slug
        if household_id is not None:
            self.household_id = household_id
        if firm_id is not None:
            self.firm_id = firm_id
        if minimum_ids is not None:
            self.minimum_ids = minimum_ids
        if assignments is not None:
            self.assignments = assignments

    @property
    def name(self):
        """Gets the name of this GroupCreate.  # noqa: E501


        :return: The name of this GroupCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupCreate.


        :param name: The name of this GroupCreate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this GroupCreate.  # noqa: E501


        :return: The slug of this GroupCreate.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this GroupCreate.


        :param slug: The slug of this GroupCreate.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def household_id(self):
        """Gets the household_id of this GroupCreate.  # noqa: E501


        :return: The household_id of this GroupCreate.  # noqa: E501
        :rtype: int
        """
        return self._household_id

    @household_id.setter
    def household_id(self, household_id):
        """Sets the household_id of this GroupCreate.


        :param household_id: The household_id of this GroupCreate.  # noqa: E501
        :type: int
        """

        self._household_id = household_id

    @property
    def firm_id(self):
        """Gets the firm_id of this GroupCreate.  # noqa: E501


        :return: The firm_id of this GroupCreate.  # noqa: E501
        :rtype: int
        """
        return self._firm_id

    @firm_id.setter
    def firm_id(self, firm_id):
        """Sets the firm_id of this GroupCreate.


        :param firm_id: The firm_id of this GroupCreate.  # noqa: E501
        :type: int
        """

        self._firm_id = firm_id

    @property
    def minimum_ids(self):
        """Gets the minimum_ids of this GroupCreate.  # noqa: E501


        :return: The minimum_ids of this GroupCreate.  # noqa: E501
        :rtype: list[int]
        """
        return self._minimum_ids

    @minimum_ids.setter
    def minimum_ids(self, minimum_ids):
        """Sets the minimum_ids of this GroupCreate.


        :param minimum_ids: The minimum_ids of this GroupCreate.  # noqa: E501
        :type: list[int]
        """

        self._minimum_ids = minimum_ids

    @property
    def assignments(self):
        """Gets the assignments of this GroupCreate.  # noqa: E501


        :return: The assignments of this GroupCreate.  # noqa: E501
        :rtype: GroupcreateAssignments
        """
        return self._assignments

    @assignments.setter
    def assignments(self, assignments):
        """Sets the assignments of this GroupCreate.


        :param assignments: The assignments of this GroupCreate.  # noqa: E501
        :type: GroupcreateAssignments
        """

        self._assignments = assignments

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
        if issubclass(GroupCreate, dict):
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
        if not isinstance(other, GroupCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other