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

from wavefront_api_client.models.dashboard import Dashboard  # noqa: F401,E501


class IntegrationDashboard(object):
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
        'description': 'str',
        'dashboard_obj': 'Dashboard',
        'url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'dashboard_obj': 'dashboardObj',
        'url': 'url'
    }

    def __init__(self, name=None, description=None, dashboard_obj=None, url=None):  # noqa: E501
        """IntegrationDashboard - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._dashboard_obj = None
        self._url = None
        self.discriminator = None

        self.name = name
        self.description = description
        if dashboard_obj is not None:
            self.dashboard_obj = dashboard_obj
        self.url = url

    @property
    def name(self):
        """Gets the name of this IntegrationDashboard.  # noqa: E501

        Dashboard name  # noqa: E501

        :return: The name of this IntegrationDashboard.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IntegrationDashboard.

        Dashboard name  # noqa: E501

        :param name: The name of this IntegrationDashboard.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this IntegrationDashboard.  # noqa: E501

        Dashboard description  # noqa: E501

        :return: The description of this IntegrationDashboard.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IntegrationDashboard.

        Dashboard description  # noqa: E501

        :param description: The description of this IntegrationDashboard.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def dashboard_obj(self):
        """Gets the dashboard_obj of this IntegrationDashboard.  # noqa: E501


        :return: The dashboard_obj of this IntegrationDashboard.  # noqa: E501
        :rtype: Dashboard
        """
        return self._dashboard_obj

    @dashboard_obj.setter
    def dashboard_obj(self, dashboard_obj):
        """Sets the dashboard_obj of this IntegrationDashboard.


        :param dashboard_obj: The dashboard_obj of this IntegrationDashboard.  # noqa: E501
        :type: Dashboard
        """

        self._dashboard_obj = dashboard_obj

    @property
    def url(self):
        """Gets the url of this IntegrationDashboard.  # noqa: E501

        URL path to the JSON definition of this dashboard  # noqa: E501

        :return: The url of this IntegrationDashboard.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IntegrationDashboard.

        URL path to the JSON definition of this dashboard  # noqa: E501

        :param url: The url of this IntegrationDashboard.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

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
        if not isinstance(other, IntegrationDashboard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other