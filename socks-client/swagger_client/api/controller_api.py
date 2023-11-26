# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
    
    def close(self):
        self.api_client.close()


    def add_socks(self, body, **kwargs):  # noqa: E501
        """add_socks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_socks(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SockRequest body: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_socks_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_socks_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_socks_with_http_info(self, body, **kwargs):  # noqa: E501
        """add_socks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_socks_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SockRequest body: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_socks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_socks`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/socks/income', 'POST',
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

    def delete_socks(self, body, **kwargs):  # noqa: E501
        """delete_socks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_socks(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SockRequest body: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_socks_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_socks_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def delete_socks_with_http_info(self, body, **kwargs):  # noqa: E501
        """delete_socks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_socks_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SockRequest body: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_socks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `delete_socks`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/socks/outcome', 'POST',
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

    def get_sock_quantity(self, color, operation, cotton_part, **kwargs):  # noqa: E501
        """get_sock_quantity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sock_quantity(color, operation, cotton_part, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str color: (required)
        :param str operation: (required)
        :param int cotton_part: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sock_quantity_with_http_info(color, operation, cotton_part, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sock_quantity_with_http_info(color, operation, cotton_part, **kwargs)  # noqa: E501
            return data

    def get_sock_quantity_with_http_info(self, color, operation, cotton_part, **kwargs):  # noqa: E501
        """get_sock_quantity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sock_quantity_with_http_info(color, operation, cotton_part, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str color: (required)
        :param str operation: (required)
        :param int cotton_part: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['color', 'operation', 'cotton_part']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sock_quantity" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'color' is set
        if ('color' not in params or
                params['color'] is None):
            raise ValueError("Missing the required parameter `color` when calling `get_sock_quantity`")  # noqa: E501
        # verify the required parameter 'operation' is set
        if ('operation' not in params or
                params['operation'] is None):
            raise ValueError("Missing the required parameter `operation` when calling `get_sock_quantity`")  # noqa: E501
        # verify the required parameter 'cotton_part' is set
        if ('cotton_part' not in params or
                params['cotton_part'] is None):
            raise ValueError("Missing the required parameter `cotton_part` when calling `get_sock_quantity`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'color' in params:
            query_params.append(('color', params['color']))  # noqa: E501
        if 'operation' in params:
            query_params.append(('operation', params['operation']))  # noqa: E501
        if 'cotton_part' in params:
            query_params.append(('cottonPart', params['cotton_part']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/socks', 'GET',
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
