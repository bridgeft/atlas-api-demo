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

class InlineResponse20087(object):
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
        'object': 'str',
        'has_next': 'bool',
        'has_previous': 'bool',
        'current_page': 'int',
        'total_pages': 'int',
        'page_size_limit': 'int',
        'total_items': 'int',
        'data': 'list[list[object]]'
    }

    attribute_map = {
        'object': 'object',
        'has_next': 'has_next',
        'has_previous': 'has_previous',
        'current_page': 'current_page',
        'total_pages': 'total_pages',
        'page_size_limit': 'page_size_limit',
        'total_items': 'total_items',
        'data': 'data'
    }

    def __init__(self, object=None, has_next=None, has_previous=None, current_page=None, total_pages=None, page_size_limit=None, total_items=None, data=None):  # noqa: E501
        """InlineResponse20087 - a model defined in Swagger"""  # noqa: E501
        self._object = None
        self._has_next = None
        self._has_previous = None
        self._current_page = None
        self._total_pages = None
        self._page_size_limit = None
        self._total_items = None
        self._data = None
        self.discriminator = None
        if object is not None:
            self.object = object
        if has_next is not None:
            self.has_next = has_next
        if has_previous is not None:
            self.has_previous = has_previous
        if current_page is not None:
            self.current_page = current_page
        if total_pages is not None:
            self.total_pages = total_pages
        if page_size_limit is not None:
            self.page_size_limit = page_size_limit
        if total_items is not None:
            self.total_items = total_items
        if data is not None:
            self.data = data

    @property
    def object(self):
        """Gets the object of this InlineResponse20087.  # noqa: E501


        :return: The object of this InlineResponse20087.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this InlineResponse20087.


        :param object: The object of this InlineResponse20087.  # noqa: E501
        :type: str
        """

        self._object = object

    @property
    def has_next(self):
        """Gets the has_next of this InlineResponse20087.  # noqa: E501


        :return: The has_next of this InlineResponse20087.  # noqa: E501
        :rtype: bool
        """
        return self._has_next

    @has_next.setter
    def has_next(self, has_next):
        """Sets the has_next of this InlineResponse20087.


        :param has_next: The has_next of this InlineResponse20087.  # noqa: E501
        :type: bool
        """

        self._has_next = has_next

    @property
    def has_previous(self):
        """Gets the has_previous of this InlineResponse20087.  # noqa: E501


        :return: The has_previous of this InlineResponse20087.  # noqa: E501
        :rtype: bool
        """
        return self._has_previous

    @has_previous.setter
    def has_previous(self, has_previous):
        """Sets the has_previous of this InlineResponse20087.


        :param has_previous: The has_previous of this InlineResponse20087.  # noqa: E501
        :type: bool
        """

        self._has_previous = has_previous

    @property
    def current_page(self):
        """Gets the current_page of this InlineResponse20087.  # noqa: E501


        :return: The current_page of this InlineResponse20087.  # noqa: E501
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this InlineResponse20087.


        :param current_page: The current_page of this InlineResponse20087.  # noqa: E501
        :type: int
        """

        self._current_page = current_page

    @property
    def total_pages(self):
        """Gets the total_pages of this InlineResponse20087.  # noqa: E501


        :return: The total_pages of this InlineResponse20087.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this InlineResponse20087.


        :param total_pages: The total_pages of this InlineResponse20087.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

    @property
    def page_size_limit(self):
        """Gets the page_size_limit of this InlineResponse20087.  # noqa: E501


        :return: The page_size_limit of this InlineResponse20087.  # noqa: E501
        :rtype: int
        """
        return self._page_size_limit

    @page_size_limit.setter
    def page_size_limit(self, page_size_limit):
        """Sets the page_size_limit of this InlineResponse20087.


        :param page_size_limit: The page_size_limit of this InlineResponse20087.  # noqa: E501
        :type: int
        """

        self._page_size_limit = page_size_limit

    @property
    def total_items(self):
        """Gets the total_items of this InlineResponse20087.  # noqa: E501


        :return: The total_items of this InlineResponse20087.  # noqa: E501
        :rtype: int
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """Sets the total_items of this InlineResponse20087.


        :param total_items: The total_items of this InlineResponse20087.  # noqa: E501
        :type: int
        """

        self._total_items = total_items

    @property
    def data(self):
        """Gets the data of this InlineResponse20087.  # noqa: E501


        :return: The data of this InlineResponse20087.  # noqa: E501
        :rtype: list[list[object]]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse20087.


        :param data: The data of this InlineResponse20087.  # noqa: E501
        :type: list[list[object]]
        """

        self._data = data

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
        if issubclass(InlineResponse20087, dict):
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
        if not isinstance(other, InlineResponse20087):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
