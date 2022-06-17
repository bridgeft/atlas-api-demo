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


class IncomeExpenseApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def filter_income_expense(self, **kwargs):  # noqa: E501
        """Filter all Income Expenserecords  # noqa: E501

        Returns a filtered list of Income Expense records  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.filter_income_expense(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IncomeexpenseFilterBody body:
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20050
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.filter_income_expense_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.filter_income_expense_with_http_info(**kwargs)  # noqa: E501
            return data

    def filter_income_expense_with_http_info(self, **kwargs):  # noqa: E501
        """Filter all Income Expenserecords  # noqa: E501

        Returns a filtered list of Income Expense records  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.filter_income_expense_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IncomeexpenseFilterBody body:
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20050
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
                    " to method filter_income_expense" % key
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
            '/data/luca/income-expense/filter', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20050',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_income_expense(self, id, **kwargs):  # noqa: E501
        """Retrieve an Income Expense record  # noqa: E501

        Returns an Income Expense record based on its ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_income_expense(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20051
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_income_expense_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_income_expense_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_income_expense_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve an Income Expense record  # noqa: E501

        Returns an Income Expense record based on its ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_income_expense_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20051
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
                    " to method get_income_expense" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_income_expense`")  # noqa: E501

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
            '/data/luca/income-expense/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20051',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_income_expenses(self, **kwargs):  # noqa: E501
        """List all Income Expense records  # noqa: E501

        Returns a list of Income Expense  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_income_expenses(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20050
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_income_expenses_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_income_expenses_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_income_expenses_with_http_info(self, **kwargs):  # noqa: E501
        """List all Income Expense records  # noqa: E501

        Returns a list of Income Expense  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_income_expenses_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20050
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
                    " to method get_income_expenses" % key
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
            '/data/luca/income-expense', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20050',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
