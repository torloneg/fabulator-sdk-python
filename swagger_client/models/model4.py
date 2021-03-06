# coding: utf-8

"""
    Fabulator API

    Endpoint Fabulator project  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: torloneg@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.json import Json  # noqa: F401,E501


class Model4(object):
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
        'json': 'Json'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'json': 'json'
    }

    def __init__(self, name=None, description=None, json=None):  # noqa: E501
        """Model4 - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._json = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.json = json

    @property
    def name(self):
        """Gets the name of this Model4.  # noqa: E501


        :return: The name of this Model4.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Model4.


        :param name: The name of this Model4.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Model4.  # noqa: E501


        :return: The description of this Model4.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Model4.


        :param description: The description of this Model4.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def json(self):
        """Gets the json of this Model4.  # noqa: E501


        :return: The json of this Model4.  # noqa: E501
        :rtype: Json
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this Model4.


        :param json: The json of this Model4.  # noqa: E501
        :type: Json
        """
        if json is None:
            raise ValueError("Invalid value for `json`, must not be `None`")  # noqa: E501

        self._json = json

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
        if issubclass(Model4, dict):
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
        if not isinstance(other, Model4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
