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

class HouseholdsFilterBody(object):
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
        'firm_id': 'int',
        'entity_id': 'str',
        'opening_date': 'datetime',
        'inception_date': 'datetime',
        'close_date': 'datetime',
        'status': 'str',
        'short_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'firm_id': 'firm_id',
        'entity_id': 'entity_id',
        'opening_date': 'opening_date',
        'inception_date': 'inception_date',
        'close_date': 'close_date',
        'status': 'status',
        'short_name': 'short_name'
    }

    def __init__(self, id=None, name=None, firm_id=None, entity_id=None, opening_date=None, inception_date=None, close_date=None, status=None, short_name=None):  # noqa: E501
        """HouseholdsFilterBody - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._firm_id = None
        self._entity_id = None
        self._opening_date = None
        self._inception_date = None
        self._close_date = None
        self._status = None
        self._short_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if firm_id is not None:
            self.firm_id = firm_id
        if entity_id is not None:
            self.entity_id = entity_id
        if opening_date is not None:
            self.opening_date = opening_date
        if inception_date is not None:
            self.inception_date = inception_date
        if close_date is not None:
            self.close_date = close_date
        if status is not None:
            self.status = status
        if short_name is not None:
            self.short_name = short_name

    @property
    def id(self):
        """Gets the id of this HouseholdsFilterBody.  # noqa: E501

        Unique household identifier  # noqa: E501

        :return: The id of this HouseholdsFilterBody.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HouseholdsFilterBody.

        Unique household identifier  # noqa: E501

        :param id: The id of this HouseholdsFilterBody.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this HouseholdsFilterBody.  # noqa: E501

        Populated from custodian data but can be modified by users  # noqa: E501

        :return: The name of this HouseholdsFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HouseholdsFilterBody.

        Populated from custodian data but can be modified by users  # noqa: E501

        :param name: The name of this HouseholdsFilterBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def firm_id(self):
        """Gets the firm_id of this HouseholdsFilterBody.  # noqa: E501

        ID of the owning firm  # noqa: E501

        :return: The firm_id of this HouseholdsFilterBody.  # noqa: E501
        :rtype: int
        """
        return self._firm_id

    @firm_id.setter
    def firm_id(self, firm_id):
        """Sets the firm_id of this HouseholdsFilterBody.

        ID of the owning firm  # noqa: E501

        :param firm_id: The firm_id of this HouseholdsFilterBody.  # noqa: E501
        :type: int
        """

        self._firm_id = firm_id

    @property
    def entity_id(self):
        """Gets the entity_id of this HouseholdsFilterBody.  # noqa: E501

        See Entiti ID Prefixes  # noqa: E501

        :return: The entity_id of this HouseholdsFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this HouseholdsFilterBody.

        See Entiti ID Prefixes  # noqa: E501

        :param entity_id: The entity_id of this HouseholdsFilterBody.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def opening_date(self):
        """Gets the opening_date of this HouseholdsFilterBody.  # noqa: E501

        Date the household was opened  # noqa: E501

        :return: The opening_date of this HouseholdsFilterBody.  # noqa: E501
        :rtype: datetime
        """
        return self._opening_date

    @opening_date.setter
    def opening_date(self, opening_date):
        """Sets the opening_date of this HouseholdsFilterBody.

        Date the household was opened  # noqa: E501

        :param opening_date: The opening_date of this HouseholdsFilterBody.  # noqa: E501
        :type: datetime
        """

        self._opening_date = opening_date

    @property
    def inception_date(self):
        """Gets the inception_date of this HouseholdsFilterBody.  # noqa: E501

        Date of household inception, if applicable. May differ from opening date  # noqa: E501

        :return: The inception_date of this HouseholdsFilterBody.  # noqa: E501
        :rtype: datetime
        """
        return self._inception_date

    @inception_date.setter
    def inception_date(self, inception_date):
        """Sets the inception_date of this HouseholdsFilterBody.

        Date of household inception, if applicable. May differ from opening date  # noqa: E501

        :param inception_date: The inception_date of this HouseholdsFilterBody.  # noqa: E501
        :type: datetime
        """

        self._inception_date = inception_date

    @property
    def close_date(self):
        """Gets the close_date of this HouseholdsFilterBody.  # noqa: E501

        Date the household was closed, if applicable  # noqa: E501

        :return: The close_date of this HouseholdsFilterBody.  # noqa: E501
        :rtype: datetime
        """
        return self._close_date

    @close_date.setter
    def close_date(self, close_date):
        """Sets the close_date of this HouseholdsFilterBody.

        Date the household was closed, if applicable  # noqa: E501

        :param close_date: The close_date of this HouseholdsFilterBody.  # noqa: E501
        :type: datetime
        """

        self._close_date = close_date

    @property
    def status(self):
        """Gets the status of this HouseholdsFilterBody.  # noqa: E501

        See Account and Household Status Codes.  # noqa: E501

        :return: The status of this HouseholdsFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this HouseholdsFilterBody.

        See Account and Household Status Codes.  # noqa: E501

        :param status: The status of this HouseholdsFilterBody.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def short_name(self):
        """Gets the short_name of this HouseholdsFilterBody.  # noqa: E501

        Short name for the household object  # noqa: E501

        :return: The short_name of this HouseholdsFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this HouseholdsFilterBody.

        Short name for the household object  # noqa: E501

        :param short_name: The short_name of this HouseholdsFilterBody.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

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
        if issubclass(HouseholdsFilterBody, dict):
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
        if not isinstance(other, HouseholdsFilterBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
