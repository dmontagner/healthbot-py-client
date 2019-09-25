# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: healthbot-hackers@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.device_group_health_tree import DeviceGroupHealthTree  # noqa: F401,E501


class DeviceGroupHealthTree(object):
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
        'children': 'list[DeviceGroupHealthTree]',
        'color': 'str',
        'data': 'str',
        'name': 'str',
        'timestamp': 'datetime'
    }

    attribute_map = {
        'children': 'children',
        'color': 'color',
        'data': 'data',
        'name': 'name',
        'timestamp': 'timestamp'
    }

    def __init__(self, children=None, color=None, data=None, name=None, timestamp=None):  # noqa: E501
        """DeviceGroupHealthTree - a model defined in Swagger"""  # noqa: E501

        self._children = None
        self._color = None
        self._data = None
        self._name = None
        self._timestamp = None
        self.discriminator = None

        self.children = children
        if color is not None:
            self.color = color
        if data is not None:
            self.data = data
        self.name = name
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def children(self):
        """Gets the children of this DeviceGroupHealthTree.  # noqa: E501


        :return: The children of this DeviceGroupHealthTree.  # noqa: E501
        :rtype: list[DeviceGroupHealthTree]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this DeviceGroupHealthTree.


        :param children: The children of this DeviceGroupHealthTree.  # noqa: E501
        :type: list[DeviceGroupHealthTree]
        """
        if children is None:
            raise ValueError("Invalid value for `children`, must not be `None`")  # noqa: E501

        self._children = children

    @property
    def color(self):
        """Gets the color of this DeviceGroupHealthTree.  # noqa: E501


        :return: The color of this DeviceGroupHealthTree.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this DeviceGroupHealthTree.


        :param color: The color of this DeviceGroupHealthTree.  # noqa: E501
        :type: str
        """
        allowed_values = ["green", "yellow", "red"]  # noqa: E501
        if color not in allowed_values:
            raise ValueError(
                "Invalid value for `color` ({0}), must be one of {1}"  # noqa: E501
                .format(color, allowed_values)
            )

        self._color = color

    @property
    def data(self):
        """Gets the data of this DeviceGroupHealthTree.  # noqa: E501


        :return: The data of this DeviceGroupHealthTree.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this DeviceGroupHealthTree.


        :param data: The data of this DeviceGroupHealthTree.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def name(self):
        """Gets the name of this DeviceGroupHealthTree.  # noqa: E501


        :return: The name of this DeviceGroupHealthTree.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceGroupHealthTree.


        :param name: The name of this DeviceGroupHealthTree.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def timestamp(self):
        """Gets the timestamp of this DeviceGroupHealthTree.  # noqa: E501


        :return: The timestamp of this DeviceGroupHealthTree.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this DeviceGroupHealthTree.


        :param timestamp: The timestamp of this DeviceGroupHealthTree.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

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
        if not isinstance(other, DeviceGroupHealthTree):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
