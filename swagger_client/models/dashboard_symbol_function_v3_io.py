# coding: utf-8

"""
    WILCO API

    This  API allows you to pull and push data with your WILCO deployment [https://github.com/flightwatching/wilco-api](https://github.com/flightwatching/wilco-api) or on  [www.flightwatching.com](www.flightwatching.com).   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@flightwatching.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import pprint
import re  # noqa: F401

import six


class DashboardSymbolFunctionV3IO(object):
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
        'params': 'str',
        'id': 'int',
        'body': 'str',
        'name': 'str'
    }

    attribute_map = {
        'params': 'params',
        'id': 'id',
        'body': 'body',
        'name': 'name'
    }

    def __init__(self, params=None, id=None, body=None, name=None):  # noqa: E501
        """DashboardSymbolFunctionV3IO - a model defined in Swagger"""  # noqa: E501

        self._params = None
        self._id = None
        self._body = None
        self._name = None
        self.discriminator = None

        if params is not None:
            self.params = params
        if id is not None:
            self.id = id
        if body is not None:
            self.body = body
        if name is not None:
            self.name = name

    @property
    def params(self):
        """Gets the params of this DashboardSymbolFunctionV3IO.  # noqa: E501


        :return: The params of this DashboardSymbolFunctionV3IO.  # noqa: E501
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this DashboardSymbolFunctionV3IO.


        :param params: The params of this DashboardSymbolFunctionV3IO.  # noqa: E501
        :type: str
        """

        self._params = params

    @property
    def id(self):
        """Gets the id of this DashboardSymbolFunctionV3IO.  # noqa: E501


        :return: The id of this DashboardSymbolFunctionV3IO.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DashboardSymbolFunctionV3IO.


        :param id: The id of this DashboardSymbolFunctionV3IO.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def body(self):
        """Gets the body of this DashboardSymbolFunctionV3IO.  # noqa: E501


        :return: The body of this DashboardSymbolFunctionV3IO.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DashboardSymbolFunctionV3IO.


        :param body: The body of this DashboardSymbolFunctionV3IO.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def name(self):
        """Gets the name of this DashboardSymbolFunctionV3IO.  # noqa: E501


        :return: The name of this DashboardSymbolFunctionV3IO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DashboardSymbolFunctionV3IO.


        :param name: The name of this DashboardSymbolFunctionV3IO.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, DashboardSymbolFunctionV3IO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
