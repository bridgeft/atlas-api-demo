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

class ApiKey(object):
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
        'description': 'str',
        'name': 'str',
        'key': 'str',
        'user_id': 'int',
        'created_at_utc': 'datetime',
        'updated_at_utc': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'name': 'name',
        'key': 'key',
        'user_id': 'user_id',
        'created_at_utc': 'created_at_utc',
        'updated_at_utc': 'updated_at_utc'
    }

    def __init__(self, id=None, description=None, name=None, key=None, user_id=None, created_at_utc=None, updated_at_utc=None):  # noqa: E501
        """ApiKey - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._description = None
        self._name = None
        self._key = None
        self._user_id = None
        self._created_at_utc = None
        self._updated_at_utc = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if key is not None:
            self.key = key
        if user_id is not None:
            self.user_id = user_id
        if created_at_utc is not None:
            self.created_at_utc = created_at_utc
        if updated_at_utc is not None:
            self.updated_at_utc = updated_at_utc

    @property
    def id(self):
        """Gets the id of this ApiKey.  # noqa: E501

        The unique resource id for the api key  # noqa: E501

        :return: The id of this ApiKey.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiKey.

        The unique resource id for the api key  # noqa: E501

        :param id: The id of this ApiKey.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def description(self):
        """Gets the description of this ApiKey.  # noqa: E501

        Description of the api key  # noqa: E501

        :return: The description of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiKey.

        Description of the api key  # noqa: E501

        :param description: The description of this ApiKey.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this ApiKey.  # noqa: E501

        Name for the api key  # noqa: E501

        :return: The name of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiKey.

        Name for the api key  # noqa: E501

        :param name: The name of this ApiKey.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def key(self):
        """Gets the key of this ApiKey.  # noqa: E501

        The key value  # noqa: E501

        :return: The key of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ApiKey.

        The key value  # noqa: E501

        :param key: The key of this ApiKey.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def user_id(self):
        """Gets the user_id of this ApiKey.  # noqa: E501

        User id associated with the api key  # noqa: E501

        :return: The user_id of this ApiKey.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ApiKey.

        User id associated with the api key  # noqa: E501

        :param user_id: The user_id of this ApiKey.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def created_at_utc(self):
        """Gets the created_at_utc of this ApiKey.  # noqa: E501

        Timestamp for when the record was created  # noqa: E501

        :return: The created_at_utc of this ApiKey.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at_utc

    @created_at_utc.setter
    def created_at_utc(self, created_at_utc):
        """Sets the created_at_utc of this ApiKey.

        Timestamp for when the record was created  # noqa: E501

        :param created_at_utc: The created_at_utc of this ApiKey.  # noqa: E501
        :type: datetime
        """

        self._created_at_utc = created_at_utc

    @property
    def updated_at_utc(self):
        """Gets the updated_at_utc of this ApiKey.  # noqa: E501

        Timestamp for when the record was updated  # noqa: E501

        :return: The updated_at_utc of this ApiKey.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_utc

    @updated_at_utc.setter
    def updated_at_utc(self, updated_at_utc):
        """Sets the updated_at_utc of this ApiKey.

        Timestamp for when the record was updated  # noqa: E501

        :param updated_at_utc: The updated_at_utc of this ApiKey.  # noqa: E501
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
        if issubclass(ApiKey, dict):
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
        if not isinstance(other, ApiKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
