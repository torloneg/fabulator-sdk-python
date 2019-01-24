# coding: utf-8

"""
    Fabulator API

    Endpoint Fabulator project  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: torloneg@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ExecuteApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def post_execute_v1_local_domain_key(self, domain, key, **kwargs):  # noqa: E501
        """post_execute_v1_local_domain_key  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_execute_v1_local_domain_key(domain, key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: (required)
        :param str key: (required)
        :param Model5 body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_execute_v1_local_domain_key_with_http_info(domain, key, **kwargs)  # noqa: E501
        else:
            (data) = self.post_execute_v1_local_domain_key_with_http_info(domain, key, **kwargs)  # noqa: E501
            return data

    def post_execute_v1_local_domain_key_with_http_info(self, domain, key, **kwargs):  # noqa: E501
        """post_execute_v1_local_domain_key  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_execute_v1_local_domain_key_with_http_info(domain, key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: (required)
        :param str key: (required)
        :param Model5 body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain', 'key', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_execute_v1_local_domain_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `post_execute_v1_local_domain_key`")  # noqa: E501
        # verify the required parameter 'key' is set
        if ('key' not in params or
                params['key'] is None):
            raise ValueError("Missing the required parameter `key` when calling `post_execute_v1_local_domain_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain' in params:
            path_params['domain'] = params['domain']  # noqa: E501
        if 'key' in params:
            path_params['key'] = params['key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/execute/v1/local/{domain}/{key}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_execute_v1_rule_idrule(self, idrule, **kwargs):  # noqa: E501
        """post_execute_v1_rule_idrule  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_execute_v1_rule_idrule(idrule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str idrule: (required)
        :param Model5 body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_execute_v1_rule_idrule_with_http_info(idrule, **kwargs)  # noqa: E501
        else:
            (data) = self.post_execute_v1_rule_idrule_with_http_info(idrule, **kwargs)  # noqa: E501
            return data

    def post_execute_v1_rule_idrule_with_http_info(self, idrule, **kwargs):  # noqa: E501
        """post_execute_v1_rule_idrule  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_execute_v1_rule_idrule_with_http_info(idrule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str idrule: (required)
        :param Model5 body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['idrule', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_execute_v1_rule_idrule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'idrule' is set
        if ('idrule' not in params or
                params['idrule'] is None):
            raise ValueError("Missing the required parameter `idrule` when calling `post_execute_v1_rule_idrule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'idrule' in params:
            path_params['idrule'] = params['idrule']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/execute/v1/rule/{idrule}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_execute_v1_rule_idrule_example_idexample(self, idrule, idexample, **kwargs):  # noqa: E501
        """post_execute_v1_rule_idrule_example_idexample  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_execute_v1_rule_idrule_example_idexample(idrule, idexample, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str idrule: (required)
        :param str idexample: (required)
        :param str idsentence:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_execute_v1_rule_idrule_example_idexample_with_http_info(idrule, idexample, **kwargs)  # noqa: E501
        else:
            (data) = self.post_execute_v1_rule_idrule_example_idexample_with_http_info(idrule, idexample, **kwargs)  # noqa: E501
            return data

    def post_execute_v1_rule_idrule_example_idexample_with_http_info(self, idrule, idexample, **kwargs):  # noqa: E501
        """post_execute_v1_rule_idrule_example_idexample  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_execute_v1_rule_idrule_example_idexample_with_http_info(idrule, idexample, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str idrule: (required)
        :param str idexample: (required)
        :param str idsentence:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['idrule', 'idexample', 'idsentence']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_execute_v1_rule_idrule_example_idexample" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'idrule' is set
        if ('idrule' not in params or
                params['idrule'] is None):
            raise ValueError("Missing the required parameter `idrule` when calling `post_execute_v1_rule_idrule_example_idexample`")  # noqa: E501
        # verify the required parameter 'idexample' is set
        if ('idexample' not in params or
                params['idexample'] is None):
            raise ValueError("Missing the required parameter `idexample` when calling `post_execute_v1_rule_idrule_example_idexample`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'idrule' in params:
            path_params['idrule'] = params['idrule']  # noqa: E501
        if 'idexample' in params:
            path_params['idexample'] = params['idexample']  # noqa: E501

        query_params = []
        if 'idsentence' in params:
            query_params.append(('idsentence', params['idsentence']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/execute/v1/rule/{idrule}/example/{idexample}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)