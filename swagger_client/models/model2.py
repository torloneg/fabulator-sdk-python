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


class Model2(object):
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
        'email': 'str',
        'password': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'role': 'str'
    }

    attribute_map = {
        'email': 'email',
        'password': 'password',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'role': 'role'
    }

    def __init__(self, email=None, password=None, first_name=None, last_name=None, role=None):  # noqa: E501
        """Model2 - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._password = None
        self._first_name = None
        self._last_name = None
        self._role = None
        self.discriminator = None

        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

    @property
    def email(self):
        """Gets the email of this Model2.  # noqa: E501


        :return: The email of this Model2.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Model2.


        :param email: The email of this Model2.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def password(self):
        """Gets the password of this Model2.  # noqa: E501


        :return: The password of this Model2.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Model2.


        :param password: The password of this Model2.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if password is not None and len(password) > 15:
            raise ValueError("Invalid value for `password`, length must be less than or equal to `15`")  # noqa: E501
        if password is not None and len(password) < 5:
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `5`")  # noqa: E501

        self._password = password

    @property
    def first_name(self):
        """Gets the first_name of this Model2.  # noqa: E501


        :return: The first_name of this Model2.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Model2.


        :param first_name: The first_name of this Model2.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501
        if first_name is not None and len(first_name) > 30:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `30`")  # noqa: E501
        if first_name is not None and len(first_name) < 3:
            raise ValueError("Invalid value for `first_name`, length must be greater than or equal to `3`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Model2.  # noqa: E501


        :return: The last_name of this Model2.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Model2.


        :param last_name: The last_name of this Model2.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501
        if last_name is not None and len(last_name) > 30:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `30`")  # noqa: E501
        if last_name is not None and len(last_name) < 3:
            raise ValueError("Invalid value for `last_name`, length must be greater than or equal to `3`")  # noqa: E501

        self._last_name = last_name

    @property
    def role(self):
        """Gets the role of this Model2.  # noqa: E501


        :return: The role of this Model2.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Model2.


        :param role: The role of this Model2.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        allowed_values = ["user", "admin"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

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
        if issubclass(Model2, dict):
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
        if not isinstance(other, Model2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
