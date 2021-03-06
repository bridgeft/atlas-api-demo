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


class SecuritiesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def filter_securities(self, **kwargs):  # noqa: E501
        """Filter all Securities  # noqa: E501

        Returns a filtered list of Securities  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.filter_securities(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SecuritiesFilterBody body:
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20085
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.filter_securities_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.filter_securities_with_http_info(**kwargs)  # noqa: E501
            return data

    def filter_securities_with_http_info(self, **kwargs):  # noqa: E501
        """Filter all Securities  # noqa: E501

        Returns a filtered list of Securities  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.filter_securities_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SecuritiesFilterBody body:
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20085
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
                    " to method filter_securities" % key
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
            '/data/custodian/securities/filter', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20085',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_securities(self, **kwargs):  # noqa: E501
        """List all Securities  # noqa: E501

        Returns a list of securities  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_securities(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20085
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_securities_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_securities_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_securities_with_http_info(self, **kwargs):  # noqa: E501
        """List all Securities  # noqa: E501

        Returns a list of securities  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_securities_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20085
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
                    " to method get_securities" % key
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
            '/data/custodian/securities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20085',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_security(self, id, **kwargs):  # noqa: E501
        """Retrieve a Security  # noqa: E501

        Returns a single  security based on an ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_security(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20086
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_security_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_security_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_security_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve a Security  # noqa: E501

        Returns a single  security based on an ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_security_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20086
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
                    " to method get_security" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_security`")  # noqa: E501

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
            '/data/custodian/securities/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20086',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_security_compressed(self, **kwargs):  # noqa: E501
        """Get compressed Securities  # noqa: E501

        Returns compressed and modified representations of all Securities that are being tracked  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_security_compressed(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_security_compressed_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_security_compressed_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_security_compressed_with_http_info(self, **kwargs):  # noqa: E501
        """Get compressed Securities  # noqa: E501

        Returns compressed and modified representations of all Securities that are being tracked  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_security_compressed_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: str
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
                    " to method get_security_compressed" % key
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
            '/data/custodian/securities/get-compressed', 'GET',
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

    def get_security_fetch(self, body, **kwargs):  # noqa: E501
        """Fetch Securities  # noqa: E501

        Returns a list of securities based on the ids passed in  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_security_fetch(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SecuritiesFetchBody body: (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20085
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_security_fetch_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.get_security_fetch_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def get_security_fetch_with_http_info(self, body, **kwargs):  # noqa: E501
        """Fetch Securities  # noqa: E501

        Returns a list of securities based on the ids passed in  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_security_fetch_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SecuritiesFetchBody body: (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20085
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
                    " to method get_security_fetch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `get_security_fetch`")  # noqa: E501

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
            '/data/custodian/securities/fetch', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20085',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_security_managed(self, **kwargs):  # noqa: E501
        """Get managed Securities  # noqa: E501

        Returns a list of security ids that belong to the user's household and firm  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_security_managed(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_security_managed_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_security_managed_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_security_managed_with_http_info(self, **kwargs):  # noqa: E501
        """Get managed Securities  # noqa: E501

        Returns a list of security ids that belong to the user's household and firm  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_security_managed_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: list[int]
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
                    " to method get_security_managed" % key
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
            '/data/custodian/securities/managed', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[int]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_security_search(self, q, **kwargs):  # noqa: E501
        """Search for Securities  # noqa: E501

        Returns modified representations of Securities based on input parameters used for filtering  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_security_search(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: The symbol or description of a Security to filter by (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20086
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_security_search_with_http_info(q, **kwargs)  # noqa: E501
        else:
            (data) = self.get_security_search_with_http_info(q, **kwargs)  # noqa: E501
            return data

    def get_security_search_with_http_info(self, q, **kwargs):  # noqa: E501
        """Search for Securities  # noqa: E501

        Returns modified representations of Securities based on input parameters used for filtering  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_security_search_with_http_info(q, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: The symbol or description of a Security to filter by (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20086
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['q', 'pager_limit', 'pager_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_security_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'q' is set
        if ('q' not in params or
                params['q'] is None):
            raise ValueError("Missing the required parameter `q` when calling `get_security_search`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'q' in params:
            path_params['q'] = params['q']  # noqa: E501

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
            '/data/custodian/securities/search/{q}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20086',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_security_usd(self, **kwargs):  # noqa: E501
        """Get Security with USD  # noqa: E501

        Returns the first security object where the issue_type_code is 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_security_usd(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20086
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_security_usd_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_security_usd_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_security_usd_with_http_info(self, **kwargs):  # noqa: E501
        """Get Security with USD  # noqa: E501

        Returns the first security object where the issue_type_code is 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_security_usd_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20086
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
                    " to method get_security_usd" % key
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
            '/data/custodian/securities/get-usd', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20086',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
