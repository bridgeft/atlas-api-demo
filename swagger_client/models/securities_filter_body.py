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

class SecuritiesFilterBody(object):
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
        'symbol': 'str',
        'description': 'str',
        'master_asset_class': 'str',
        'broad_code': 'str',
        'sic_code': 'str',
        'issue_code': 'str'
    }

    attribute_map = {
        'id': 'id',
        'symbol': 'symbol',
        'description': 'description',
        'master_asset_class': 'master_asset_class',
        'broad_code': 'broad_code',
        'sic_code': 'sic_code',
        'issue_code': 'issue_code'
    }

    def __init__(self, id=None, symbol=None, description=None, master_asset_class=None, broad_code=None, sic_code=None, issue_code=None):  # noqa: E501
        """SecuritiesFilterBody - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._symbol = None
        self._description = None
        self._master_asset_class = None
        self._broad_code = None
        self._sic_code = None
        self._issue_code = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if symbol is not None:
            self.symbol = symbol
        if description is not None:
            self.description = description
        if master_asset_class is not None:
            self.master_asset_class = master_asset_class
        if broad_code is not None:
            self.broad_code = broad_code
        if sic_code is not None:
            self.sic_code = sic_code
        if issue_code is not None:
            self.issue_code = issue_code

    @property
    def id(self):
        """Gets the id of this SecuritiesFilterBody.  # noqa: E501

        The unique resource id for the Security  # noqa: E501

        :return: The id of this SecuritiesFilterBody.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SecuritiesFilterBody.

        The unique resource id for the Security  # noqa: E501

        :param id: The id of this SecuritiesFilterBody.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def symbol(self):
        """Gets the symbol of this SecuritiesFilterBody.  # noqa: E501

        The symbol used to represent the Security  # noqa: E501

        :return: The symbol of this SecuritiesFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this SecuritiesFilterBody.

        The symbol used to represent the Security  # noqa: E501

        :param symbol: The symbol of this SecuritiesFilterBody.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def description(self):
        """Gets the description of this SecuritiesFilterBody.  # noqa: E501

        The description of the Security  # noqa: E501

        :return: The description of this SecuritiesFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SecuritiesFilterBody.

        The description of the Security  # noqa: E501

        :param description: The description of this SecuritiesFilterBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def master_asset_class(self):
        """Gets the master_asset_class of this SecuritiesFilterBody.  # noqa: E501

        See https://docs.quovo.com/data-dictionary/#holding%C2%A0types  # noqa: E501

        :return: The master_asset_class of this SecuritiesFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._master_asset_class

    @master_asset_class.setter
    def master_asset_class(self, master_asset_class):
        """Sets the master_asset_class of this SecuritiesFilterBody.

        See https://docs.quovo.com/data-dictionary/#holding%C2%A0types  # noqa: E501

        :param master_asset_class: The master_asset_class of this SecuritiesFilterBody.  # noqa: E501
        :type: str
        """

        self._master_asset_class = master_asset_class

    @property
    def broad_code(self):
        """Gets the broad_code of this SecuritiesFilterBody.  # noqa: E501

        The broad code of the Security  # noqa: E501

        :return: The broad_code of this SecuritiesFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._broad_code

    @broad_code.setter
    def broad_code(self, broad_code):
        """Sets the broad_code of this SecuritiesFilterBody.

        The broad code of the Security  # noqa: E501

        :param broad_code: The broad_code of this SecuritiesFilterBody.  # noqa: E501
        :type: str
        """

        self._broad_code = broad_code

    @property
    def sic_code(self):
        """Gets the sic_code of this SecuritiesFilterBody.  # noqa: E501

        The sic code of the security  # noqa: E501

        :return: The sic_code of this SecuritiesFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._sic_code

    @sic_code.setter
    def sic_code(self, sic_code):
        """Sets the sic_code of this SecuritiesFilterBody.

        The sic code of the security  # noqa: E501

        :param sic_code: The sic_code of this SecuritiesFilterBody.  # noqa: E501
        :type: str
        """

        self._sic_code = sic_code

    @property
    def issue_code(self):
        """Gets the issue_code of this SecuritiesFilterBody.  # noqa: E501

        An internal mapping of the Security's issue code  # noqa: E501

        :return: The issue_code of this SecuritiesFilterBody.  # noqa: E501
        :rtype: str
        """
        return self._issue_code

    @issue_code.setter
    def issue_code(self, issue_code):
        """Sets the issue_code of this SecuritiesFilterBody.

        An internal mapping of the Security's issue code  # noqa: E501

        :param issue_code: The issue_code of this SecuritiesFilterBody.  # noqa: E501
        :type: str
        """

        self._issue_code = issue_code

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
        if issubclass(SecuritiesFilterBody, dict):
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
        if not isinstance(other, SecuritiesFilterBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
