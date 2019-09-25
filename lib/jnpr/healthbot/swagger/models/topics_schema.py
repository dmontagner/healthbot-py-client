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

from jnpr.healthbot.swagger.models.topic_schema import TopicSchema  # noqa: F401,E501


class TopicsSchema(object):
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
        'topic': 'list[TopicSchema]'
    }

    attribute_map = {
        'topic': 'topic'
    }

    def __init__(self, topic=None):  # noqa: E501
        """TopicsSchema - a model defined in Swagger"""  # noqa: E501

        self._topic = None
        self.discriminator = None

        self.topic = topic

    @property
    def topic(self):
        """Gets the topic of this TopicsSchema.  # noqa: E501


        :return: The topic of this TopicsSchema.  # noqa: E501
        :rtype: list[TopicSchema]
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this TopicsSchema.


        :param topic: The topic of this TopicsSchema.  # noqa: E501
        :type: list[TopicSchema]
        """
        if topic is None:
            raise ValueError("Invalid value for `topic`, must not be `None`")  # noqa: E501

        self._topic = topic

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
        if not isinstance(other, TopicsSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
