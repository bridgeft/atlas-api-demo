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


class StrategiesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_many_strategies(self, body, **kwargs):  # noqa: E501
        """Create strategies  # noqa: E501

        Returns a list of created strategies  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_many_strategies(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[Paths1investmentManagement1strategiespostrequestBodycontentapplication1jsonschema] body: (required)
        :param int limit: Number of items to return per page
        :param int page: Current page number
        :return: InlineResponse200126
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_many_strategies_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_many_strategies_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_many_strategies_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create strategies  # noqa: E501

        Returns a list of created strategies  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_many_strategies_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[Paths1investmentManagement1strategiespostrequestBodycontentapplication1jsonschema] body: (required)
        :param int limit: Number of items to return per page
        :param int page: Current page number
        :return: InlineResponse200126
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'limit', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_many_strategies" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_many_strategies`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

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
            '/investment-management/strategies/create-many', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200126',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_strategies(self, body, **kwargs):  # noqa: E501
        """Create a Strategy  # noqa: E501

        Returns the created strategy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_strategies(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InvestmentmanagementStrategiesBody body: (required)
        :param int limit: Number of items to return per page
        :param int page: Current page number
        :return: InlineResponse200127
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_strategies_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_strategies_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_strategies_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a Strategy  # noqa: E501

        Returns the created strategy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_strategies_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InvestmentmanagementStrategiesBody body: (required)
        :param int limit: Number of items to return per page
        :param int page: Current page number
        :return: InlineResponse200127
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'limit', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_strategies" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_strategies`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

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
            '/investment-management/strategies', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200127',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def detele_many_strategies(self, body, **kwargs):  # noqa: E501
        """Delete many Strategies  # noqa: E501

        Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.detele_many_strategies(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: (required)
        :param int limit: Number of items to return per page
        :param int page: Current page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.detele_many_strategies_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.detele_many_strategies_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def detele_many_strategies_with_http_info(self, body, **kwargs):  # noqa: E501
        """Delete many Strategies  # noqa: E501

        Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.detele_many_strategies_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: (required)
        :param int limit: Number of items to return per page
        :param int page: Current page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'limit', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method detele_many_strategies" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `detele_many_strategies`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/investment-management/strategies/delete-many', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def detele_strategy(self, id, **kwargs):  # noqa: E501
        """Delete a Strategy  # noqa: E501

        Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.detele_strategy(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int limit: Number of items to return per page
        :param int page: Current page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.detele_strategy_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.detele_strategy_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def detele_strategy_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete a Strategy  # noqa: E501

        Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.detele_strategy_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int limit: Number of items to return per page
        :param int page: Current page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'limit', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method detele_strategy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `detele_strategy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/investment-management/strategies/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def filter_strategies(self, **kwargs):  # noqa: E501
        """Filter all Strategies  # noqa: E501

        Returns a filtered list of Strategy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.filter_strategies(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StrategiesFilterBody body:
        :param int limit: Number of items to return per page
        :param int page: Current page number
        :return: InlineResponse200126
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.filter_strategies_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.filter_strategies_with_http_info(**kwargs)  # noqa: E501
            return data

    def filter_strategies_with_http_info(self, **kwargs):  # noqa: E501
        """Filter all Strategies  # noqa: E501

        Returns a filtered list of Strategy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.filter_strategies_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StrategiesFilterBody body:
        :param int limit: Number of items to return per page
        :param int page: Current page number
        :return: InlineResponse200126
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'limit', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method filter_strategies" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

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
            '/investment-management/strategies/filter', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200126',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_strategies(self, **kwargs):  # noqa: E501
        """List all Strategies  # noqa: E501

        Returns a list of strategies within the data field  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_strategies(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of items to return per page
        :param int page: Current page number
        :return: InlineResponse200125
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_strategies_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_strategies_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_strategies_with_http_info(self, **kwargs):  # noqa: E501
        """List all Strategies  # noqa: E501

        Returns a list of strategies within the data field  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_strategies_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of items to return per page
        :param int page: Current page number
        :return: InlineResponse200125
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_strategies" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

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
            '/investment-management/strategies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200125',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_strategy(self, id, **kwargs):  # noqa: E501
        """Retrieve a Strategy  # noqa: E501

        Returns a strategy based on a single ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_strategy(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int limit: Number of items to return per page
        :param int page: Current page number
        :return: InlineResponse200128
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_strategy_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_strategy_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_strategy_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve a Strategy  # noqa: E501

        Returns a strategy based on a single ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_strategy_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int limit: Number of items to return per page
        :param int page: Current page number
        :return: InlineResponse200128
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'limit', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_strategy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_strategy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

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
            '/investment-management/strategies/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200128',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_strategies(self, **kwargs):  # noqa: E501
        """Bulk Update Strategies  # noqa: E501

        Returns the updated strategies  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_strategies(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of items to return per page
        :param int page: Current page number
        :return: InlineResponse200126
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_strategies_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.update_strategies_with_http_info(**kwargs)  # noqa: E501
            return data

    def update_strategies_with_http_info(self, **kwargs):  # noqa: E501
        """Bulk Update Strategies  # noqa: E501

        Returns the updated strategies  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_strategies_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of items to return per page
        :param int page: Current page number
        :return: InlineResponse200126
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_strategies" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

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
            '/investment-management/strategies', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200126',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_strategy(self, id, **kwargs):  # noqa: E501
        """Update a Strategy  # noqa: E501

        Returns the updated strategy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_strategy(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int limit: Number of items to return per page
        :param int page: Current page number
        :return: InlineResponse200128
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_strategy_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_strategy_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_strategy_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update a Strategy  # noqa: E501

        Returns the updated strategy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_strategy_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int limit: Number of items to return per page
        :param int page: Current page number
        :return: InlineResponse200128
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'limit', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_strategy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_strategy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

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
            '/investment-management/strategies/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200128',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
