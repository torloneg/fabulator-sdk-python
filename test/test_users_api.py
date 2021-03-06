# coding: utf-8

"""
    Fabulator API

    Endpoint Fabulator project  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: torloneg@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.users_api import UsersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_users_v1_id(self):
        """Test case for delete_users_v1_id

        """
        pass

    def test_get_users_v1_info_id(self):
        """Test case for get_users_v1_info_id

        """
        pass

    def test_patch_users_v1_update_id_field_value(self):
        """Test case for patch_users_v1_update_id_field_value

        """
        pass

    def test_post_users_v1_add(self):
        """Test case for post_users_v1_add

        """
        pass

    def test_post_users_v1_login(self):
        """Test case for post_users_v1_login

        """
        pass

    def test_post_users_v1_query_skip_limit(self):
        """Test case for post_users_v1_query_skip_limit

        """
        pass

    def test_post_users_v1_reset_password_token(self):
        """Test case for post_users_v1_reset_password_token

        """
        pass

    def test_post_users_v1_send_password_reminder_email(self):
        """Test case for post_users_v1_send_password_reminder_email

        """
        pass

    def test_put_users_v1_update_id(self):
        """Test case for put_users_v1_update_id

        """
        pass


if __name__ == '__main__':
    unittest.main()
