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

from swagger_client.models.notification_schema_httppost import NotificationSchemaHttppost  # noqa: F401,E501
from swagger_client.models.notification_schema_kafkapublish import NotificationSchemaKafkapublish  # noqa: F401,E501
from swagger_client.models.notification_schema_slack import NotificationSchemaSlack  # noqa: F401,E501


class NotificationSchema(object):
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
        'http_post': 'NotificationSchemaHttppost',
        'notification_name': 'str',
        'slack': 'NotificationSchemaSlack',
        'kafka_publish': 'NotificationSchemaKafkapublish'
    }

    attribute_map = {
        'description': 'description',
        'http_post': 'http-post',
        'notification_name': 'notification-name',
        'slack': 'slack',
        'kafka_publish': 'kafka-publish'
    }

    def __init__(self, description=None, http_post=None, notification_name=None, slack=None, kafka_publish=None):  # noqa: E501
        """NotificationSchema - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._http_post = None
        self._notification_name = None
        self._slack = None
        self._kafka_publish = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if http_post is not None:
            self.http_post = http_post
        self.notification_name = notification_name
        if slack is not None:
            self.slack = slack
        if kafka_publish is not None:
            self.kafka_publish = kafka_publish

    @property
    def description(self):
        """Gets the description of this NotificationSchema.  # noqa: E501

        Description about the notification  # noqa: E501

        :return: The description of this NotificationSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NotificationSchema.

        Description about the notification  # noqa: E501

        :param description: The description of this NotificationSchema.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def http_post(self):
        """Gets the http_post of this NotificationSchema.  # noqa: E501


        :return: The http_post of this NotificationSchema.  # noqa: E501
        :rtype: NotificationSchemaHttppost
        """
        return self._http_post

    @http_post.setter
    def http_post(self, http_post):
        """Sets the http_post of this NotificationSchema.


        :param http_post: The http_post of this NotificationSchema.  # noqa: E501
        :type: NotificationSchemaHttppost
        """

        self._http_post = http_post

    @property
    def notification_name(self):
        """Gets the notification_name of this NotificationSchema.  # noqa: E501

        Name of the notification. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The notification_name of this NotificationSchema.  # noqa: E501
        :rtype: str
        """
        return self._notification_name

    @notification_name.setter
    def notification_name(self, notification_name):
        """Sets the notification_name of this NotificationSchema.

        Name of the notification. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param notification_name: The notification_name of this NotificationSchema.  # noqa: E501
        :type: str
        """
        if notification_name is None:
            raise ValueError("Invalid value for `notification_name`, must not be `None`")  # noqa: E501
        if notification_name is not None and len(notification_name) > 64:
            raise ValueError("Invalid value for `notification_name`, length must be less than or equal to `64`")  # noqa: E501
        if notification_name is not None and not re.search('^[a-zA-Z][a-zA-Z0-9_-]*$', notification_name):  # noqa: E501
            raise ValueError("Invalid value for `notification_name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._notification_name = notification_name

    @property
    def slack(self):
        """Gets the slack of this NotificationSchema.  # noqa: E501


        :return: The slack of this NotificationSchema.  # noqa: E501
        :rtype: NotificationSchemaSlack
        """
        return self._slack

    @slack.setter
    def slack(self, slack):
        """Sets the slack of this NotificationSchema.


        :param slack: The slack of this NotificationSchema.  # noqa: E501
        :type: NotificationSchemaSlack
        """

        self._slack = slack

    @property
    def kafka_publish(self):
        """Gets the kafka_publish of this NotificationSchema.  # noqa: E501


        :return: The kafka_publish of this NotificationSchema.  # noqa: E501
        :rtype: NotificationSchemaKafkapublish
        """
        return self._kafka_publish

    @kafka_publish.setter
    def kafka_publish(self, kafka_publish):
        """Sets the kafka_publish of this NotificationSchema.


        :param kafka_publish: The kafka_publish of this NotificationSchema.  # noqa: E501
        :type: NotificationSchemaKafkapublish
        """

        self._kafka_publish = kafka_publish

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
        if not isinstance(other, NotificationSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
