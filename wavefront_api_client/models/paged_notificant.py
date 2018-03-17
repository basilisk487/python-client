# coding: utf-8

"""
    Wavefront Public API

    <p>The Wavefront public API enables you to interact with Wavefront servers using standard web service API tools. You can use the API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make API calls outside the Wavefront API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p><p>For legacy versions of the Wavefront API, see the <a href=\"/api-docs/ui/deprecated\">legacy API documentation</a>.</p>  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wavefront_api_client.models.notificant import Notificant  # noqa: F401,E501
from wavefront_api_client.models.sorting import Sorting  # noqa: F401,E501


class PagedNotificant(object):
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
        'items': 'list[Notificant]',
        'offset': 'int',
        'limit': 'int',
        'cursor': 'str',
        'total_items': 'int',
        'more_items': 'bool',
        'sort': 'Sorting'
    }

    attribute_map = {
        'items': 'items',
        'offset': 'offset',
        'limit': 'limit',
        'cursor': 'cursor',
        'total_items': 'totalItems',
        'more_items': 'moreItems',
        'sort': 'sort'
    }

    def __init__(self, items=None, offset=None, limit=None, cursor=None, total_items=None, more_items=None, sort=None):  # noqa: E501
        """PagedNotificant - a model defined in Swagger"""  # noqa: E501

        self._items = None
        self._offset = None
        self._limit = None
        self._cursor = None
        self._total_items = None
        self._more_items = None
        self._sort = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if cursor is not None:
            self.cursor = cursor
        if total_items is not None:
            self.total_items = total_items
        if more_items is not None:
            self.more_items = more_items
        if sort is not None:
            self.sort = sort

    @property
    def items(self):
        """Gets the items of this PagedNotificant.  # noqa: E501

        List of requested items  # noqa: E501

        :return: The items of this PagedNotificant.  # noqa: E501
        :rtype: list[Notificant]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this PagedNotificant.

        List of requested items  # noqa: E501

        :param items: The items of this PagedNotificant.  # noqa: E501
        :type: list[Notificant]
        """

        self._items = items

    @property
    def offset(self):
        """Gets the offset of this PagedNotificant.  # noqa: E501


        :return: The offset of this PagedNotificant.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PagedNotificant.


        :param offset: The offset of this PagedNotificant.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this PagedNotificant.  # noqa: E501


        :return: The limit of this PagedNotificant.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PagedNotificant.


        :param limit: The limit of this PagedNotificant.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def cursor(self):
        """Gets the cursor of this PagedNotificant.  # noqa: E501

        The id at which the current (limited) search can be continued to obtain more matching items  # noqa: E501

        :return: The cursor of this PagedNotificant.  # noqa: E501
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this PagedNotificant.

        The id at which the current (limited) search can be continued to obtain more matching items  # noqa: E501

        :param cursor: The cursor of this PagedNotificant.  # noqa: E501
        :type: str
        """

        self._cursor = cursor

    @property
    def total_items(self):
        """Gets the total_items of this PagedNotificant.  # noqa: E501

        An estimate (lower-bound) of the total number of items available for return.  May not be a tight estimate for facet queries  # noqa: E501

        :return: The total_items of this PagedNotificant.  # noqa: E501
        :rtype: int
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """Sets the total_items of this PagedNotificant.

        An estimate (lower-bound) of the total number of items available for return.  May not be a tight estimate for facet queries  # noqa: E501

        :param total_items: The total_items of this PagedNotificant.  # noqa: E501
        :type: int
        """

        self._total_items = total_items

    @property
    def more_items(self):
        """Gets the more_items of this PagedNotificant.  # noqa: E501

        Whether more items are available for return by increment offset or cursor  # noqa: E501

        :return: The more_items of this PagedNotificant.  # noqa: E501
        :rtype: bool
        """
        return self._more_items

    @more_items.setter
    def more_items(self, more_items):
        """Sets the more_items of this PagedNotificant.

        Whether more items are available for return by increment offset or cursor  # noqa: E501

        :param more_items: The more_items of this PagedNotificant.  # noqa: E501
        :type: bool
        """

        self._more_items = more_items

    @property
    def sort(self):
        """Gets the sort of this PagedNotificant.  # noqa: E501


        :return: The sort of this PagedNotificant.  # noqa: E501
        :rtype: Sorting
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this PagedNotificant.


        :param sort: The sort of this PagedNotificant.  # noqa: E501
        :type: Sorting
        """

        self._sort = sort

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PagedNotificant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
