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

from wavefront_api_client.models.event_time_range import EventTimeRange  # noqa: F401,E501
from wavefront_api_client.models.search_query import SearchQuery  # noqa: F401,E501


class EventSearchRequest(object):
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
        'cursor': 'str',
        'limit': 'int',
        'query': 'list[SearchQuery]',
        'time_range': 'EventTimeRange',
        'sort_time_ascending': 'bool'
    }

    attribute_map = {
        'cursor': 'cursor',
        'limit': 'limit',
        'query': 'query',
        'time_range': 'timeRange',
        'sort_time_ascending': 'sortTimeAscending'
    }

    def __init__(self, cursor=None, limit=None, query=None, time_range=None, sort_time_ascending=None):  # noqa: E501
        """EventSearchRequest - a model defined in Swagger"""  # noqa: E501

        self._cursor = None
        self._limit = None
        self._query = None
        self._time_range = None
        self._sort_time_ascending = None
        self.discriminator = None

        if cursor is not None:
            self.cursor = cursor
        if limit is not None:
            self.limit = limit
        if query is not None:
            self.query = query
        if time_range is not None:
            self.time_range = time_range
        if sort_time_ascending is not None:
            self.sort_time_ascending = sort_time_ascending

    @property
    def cursor(self):
        """Gets the cursor of this EventSearchRequest.  # noqa: E501

        The id (exclusive) from which search results resume returning.  Users should supply an entity 'id' to this property.  Its main purpose is to resume where a previous search left off because of the 'limit' parameter.  If a user supplies the last id in a set of results to cursor, while keeping the query the same, the system will return the next page of results  # noqa: E501

        :return: The cursor of this EventSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this EventSearchRequest.

        The id (exclusive) from which search results resume returning.  Users should supply an entity 'id' to this property.  Its main purpose is to resume where a previous search left off because of the 'limit' parameter.  If a user supplies the last id in a set of results to cursor, while keeping the query the same, the system will return the next page of results  # noqa: E501

        :param cursor: The cursor of this EventSearchRequest.  # noqa: E501
        :type: str
        """

        self._cursor = cursor

    @property
    def limit(self):
        """Gets the limit of this EventSearchRequest.  # noqa: E501


        :return: The limit of this EventSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this EventSearchRequest.


        :param limit: The limit of this EventSearchRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def query(self):
        """Gets the query of this EventSearchRequest.  # noqa: E501

        A list of queries by which to limit the search results  # noqa: E501

        :return: The query of this EventSearchRequest.  # noqa: E501
        :rtype: list[SearchQuery]
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this EventSearchRequest.

        A list of queries by which to limit the search results  # noqa: E501

        :param query: The query of this EventSearchRequest.  # noqa: E501
        :type: list[SearchQuery]
        """

        self._query = query

    @property
    def time_range(self):
        """Gets the time_range of this EventSearchRequest.  # noqa: E501


        :return: The time_range of this EventSearchRequest.  # noqa: E501
        :rtype: EventTimeRange
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this EventSearchRequest.


        :param time_range: The time_range of this EventSearchRequest.  # noqa: E501
        :type: EventTimeRange
        """

        self._time_range = time_range

    @property
    def sort_time_ascending(self):
        """Gets the sort_time_ascending of this EventSearchRequest.  # noqa: E501

        Whether to sort event results ascending in start time.  Default: false  # noqa: E501

        :return: The sort_time_ascending of this EventSearchRequest.  # noqa: E501
        :rtype: bool
        """
        return self._sort_time_ascending

    @sort_time_ascending.setter
    def sort_time_ascending(self, sort_time_ascending):
        """Sets the sort_time_ascending of this EventSearchRequest.

        Whether to sort event results ascending in start time.  Default: false  # noqa: E501

        :param sort_time_ascending: The sort_time_ascending of this EventSearchRequest.  # noqa: E501
        :type: bool
        """

        self._sort_time_ascending = sort_time_ascending

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
        if not isinstance(other, EventSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
