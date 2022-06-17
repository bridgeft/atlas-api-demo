# coding: utf-8

"""
    Atlas API

    RESTful API for controlling and interacting with Atlas data  # noqa: E501

    OpenAPI spec version: 2.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class HeldawayAccountsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def filter_heldaway_accounts(self, **kwargs):  # noqa: E501
        """Filter all Heldaway Accounts  # noqa: E501

        Returns a filtered list of Heldaway Accounts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.filter_heldaway_accounts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountsFilterBody1 body:
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.filter_heldaway_accounts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.filter_heldaway_accounts_with_http_info(**kwargs)  # noqa: E501
            return data

    def filter_heldaway_accounts_with_http_info(self, **kwargs):  # noqa: E501
        """Filter all Heldaway Accounts  # noqa: E501

        Returns a filtered list of Heldaway Accounts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.filter_heldaway_accounts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountsFilterBody1 body:
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'pager_limit', 'pager_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method filter_heldaway_accounts" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pager_limit' in params:
            query_params.append(('pager.limit', params['pager_limit']))  # noqa: E501
        if 'pager_page' in params:
            query_params.append(('pager.page', params['pager_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/heldaway/accounts/filter', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_heldaway_account(self, id, **kwargs):  # noqa: E501
        """Retrieve a Heldaway Account  # noqa: E501

        Returns a Heldaway Account based on a single ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_heldaway_account(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_heldaway_account_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_heldaway_account_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_heldaway_account_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve a Heldaway Account  # noqa: E501

        Returns a Heldaway Account based on a single ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_heldaway_account_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'pager_limit', 'pager_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_heldaway_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_heldaway_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'pager_limit' in params:
            query_params.append(('pager.limit', params['pager_limit']))  # noqa: E501
        if 'pager_page' in params:
            query_params.append(('pager.page', params['pager_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/heldaway/accounts/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_heldaway_accounts(self, **kwargs):  # noqa: E501
        """List all Heldaway Accounts  # noqa: E501

        Returns a list of Heldaway Accounts within the data field  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_heldaway_accounts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_heldaway_accounts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_heldaway_accounts_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_heldaway_accounts_with_http_info(self, **kwargs):  # noqa: E501
        """List all Heldaway Accounts  # noqa: E501

        Returns a list of Heldaway Accounts within the data field  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_heldaway_accounts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pager_limit', 'pager_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_heldaway_accounts" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pager_limit' in params:
            query_params.append(('pager.limit', params['pager_limit']))  # noqa: E501
        if 'pager_page' in params:
            query_params.append(('pager.page', params['pager_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/heldaway/accounts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_heldaway_account(self, id, **kwargs):  # noqa: E501
        """Update a Heldaway Account  # noqa: E501

        Returns the updated Heldaway Account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_heldaway_account(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_heldaway_account_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_heldaway_account_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_heldaway_account_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update a Heldaway Account  # noqa: E501

        Returns the updated Heldaway Account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_heldaway_account_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'pager_limit', 'pager_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_heldaway_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_heldaway_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'pager_limit' in params:
            query_params.append(('pager.limit', params['pager_limit']))  # noqa: E501
        if 'pager_page' in params:
            query_params.append(('pager.page', params['pager_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/heldaway/accounts/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_heldaway_accounts(self, **kwargs):  # noqa: E501
        """Bulk Update Heldaway Accounts  # noqa: E501

        Returns the updated Heldaway Accounts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_heldaway_accounts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_heldaway_accounts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.update_heldaway_accounts_with_http_info(**kwargs)  # noqa: E501
            return data

    def update_heldaway_accounts_with_http_info(self, **kwargs):  # noqa: E501
        """Bulk Update Heldaway Accounts  # noqa: E501

        Returns the updated Heldaway Accounts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_heldaway_accounts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pager_limit', 'pager_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_heldaway_accounts" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pager_limit' in params:
            query_params.append(('pager.limit', params['pager_limit']))  # noqa: E501
        if 'pager_page' in params:
            query_params.append(('pager.page', params['pager_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/heldaway/accounts', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
