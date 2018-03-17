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

from wavefront_api_client.models.paged_proxy import PagedProxy  # noqa: F401,E501
from wavefront_api_client.models.response_status import ResponseStatus  # noqa: F401,E501


class ResponseContainerPagedProxy(object):
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
        'status': 'ResponseStatus',
        'response': 'PagedProxy'
    }

    attribute_map = {
        'status': 'status',
        'response': 'response'
    }

    def __init__(self, status=None, response=None):  # noqa: E501
        """ResponseContainerPagedProxy - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._response = None
        self.discriminator = None

        self.status = status
        if response is not None:
            self.response = response

    @property
    def status(self):
        """Gets the status of this ResponseContainerPagedProxy.  # noqa: E501


        :return: The status of this ResponseContainerPagedProxy.  # noqa: E501
        :rtype: ResponseStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseContainerPagedProxy.


        :param status: The status of this ResponseContainerPagedProxy.  # noqa: E501
        :type: ResponseStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def response(self):
        """Gets the response of this ResponseContainerPagedProxy.  # noqa: E501


        :return: The response of this ResponseContainerPagedProxy.  # noqa: E501
        :rtype: PagedProxy
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this ResponseContainerPagedProxy.


        :param response: The response of this ResponseContainerPagedProxy.  # noqa: E501
        :type: PagedProxy
        """

        self._response = response

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
        if not isinstance(other, ResponseContainerPagedProxy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
