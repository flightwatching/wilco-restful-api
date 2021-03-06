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


class ConstantV3IO(object):
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
        'description': 'str',
        'name': 'str',
        'value': 'str',
        'id': 'int'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'value': 'value',
        'id': 'id'
    }

    def __init__(self, description=None, name=None, value=None, id=None):  # noqa: E501
        """ConstantV3IO - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._name = None
        self._value = None
        self._id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if id is not None:
            self.id = id

    @property
    def description(self):
        """Gets the description of this ConstantV3IO.  # noqa: E501


        :return: The description of this ConstantV3IO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConstantV3IO.


        :param description: The description of this ConstantV3IO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this ConstantV3IO.  # noqa: E501


        :return: The name of this ConstantV3IO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConstantV3IO.


        :param name: The name of this ConstantV3IO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this ConstantV3IO.  # noqa: E501


        :return: The value of this ConstantV3IO.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ConstantV3IO.


        :param value: The value of this ConstantV3IO.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def id(self):
        """Gets the id of this ConstantV3IO.  # noqa: E501


        :return: The id of this ConstantV3IO.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConstantV3IO.


        :param id: The id of this ConstantV3IO.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if not isinstance(other, ConstantV3IO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
