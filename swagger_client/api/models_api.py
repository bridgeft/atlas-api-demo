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


class ModelsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_many_models(self, body, **kwargs):  # noqa: E501
        """Create Models  # noqa: E501

        Returns a list of created Models  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_many_models(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[Paths1investmentManagement1modelspostrequestBodycontentapplication1jsonschema] body: (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20091
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_many_models_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_many_models_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_many_models_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Models  # noqa: E501

        Returns a list of created Models  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_many_models_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[Paths1investmentManagement1modelspostrequestBodycontentapplication1jsonschema] body: (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20091
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
                    " to method create_many_models" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_many_models`")  # noqa: E501

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
            '/investment-management/models/create-many', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20091',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_models(self, body, **kwargs):  # noqa: E501
        """Create a Model  # noqa: E501

        Returns the created model  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_models(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InvestmentmanagementModelsBody body: (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20092
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_models_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_models_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_models_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a Model  # noqa: E501

        Returns the created model  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_models_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InvestmentmanagementModelsBody body: (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20092
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
                    " to method create_models" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_models`")  # noqa: E501

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
            '/investment-management/models', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20092',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def detele_many_models(self, body, **kwargs):  # noqa: E501
        """Delete many Models  # noqa: E501

        Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.detele_many_models(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.detele_many_models_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.detele_many_models_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def detele_many_models_with_http_info(self, body, **kwargs):  # noqa: E501
        """Delete many Models  # noqa: E501

        Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.detele_many_models_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: None
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
                    " to method detele_many_models" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `detele_many_models`")  # noqa: E501

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
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/investment-management/models/delete-many', 'POST',
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

    def detele_model(self, id, **kwargs):  # noqa: E501
        """Delete a Model  # noqa: E501

        Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.detele_model(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.detele_model_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.detele_model_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def detele_model_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete a Model  # noqa: E501

        Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.detele_model_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: None
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
                    " to method detele_model" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `detele_model`")  # noqa: E501

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
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/investment-management/models/{id}', 'DELETE',
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

    def filter_models(self, **kwargs):  # noqa: E501
        """Filter all Models  # noqa: E501

        Returns a filtered list of Model  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.filter_models(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ModelsFilterBody body:
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20091
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.filter_models_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.filter_models_with_http_info(**kwargs)  # noqa: E501
            return data

    def filter_models_with_http_info(self, **kwargs):  # noqa: E501
        """Filter all Models  # noqa: E501

        Returns a filtered list of Model  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.filter_models_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ModelsFilterBody body:
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20091
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
                    " to method filter_models" % key
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
            '/investment-management/models/filter', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20091',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_model(self, id, **kwargs):  # noqa: E501
        """Retrieve a Model  # noqa: E501

        Returns a model based on a single ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_model(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20092
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_model_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_model_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_model_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve a Model  # noqa: E501

        Returns a model based on a single ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_model_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20092
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
                    " to method get_model" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_model`")  # noqa: E501

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
            '/investment-management/models/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20092',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_models(self, **kwargs):  # noqa: E501
        """List all Models  # noqa: E501

        Returns a list of models within the data field  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_models(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20091
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_models_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_models_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_models_with_http_info(self, **kwargs):  # noqa: E501
        """List all Models  # noqa: E501

        Returns a list of models within the data field  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_models_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20091
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
                    " to method get_models" % key
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
            '/investment-management/models', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20091',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_model(self, id, **kwargs):  # noqa: E501
        """Update a Model  # noqa: E501

        Returns the updated model  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_model(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20092
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_model_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_model_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_model_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update a Model  # noqa: E501

        Returns the updated model  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_model_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20092
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
                    " to method update_model" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_model`")  # noqa: E501

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
            '/investment-management/models/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20092',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_models(self, **kwargs):  # noqa: E501
        """Bulk Update Models  # noqa: E501

        Returns the updated models  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_models(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20091
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_models_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.update_models_with_http_info(**kwargs)  # noqa: E501
            return data

    def update_models_with_http_info(self, **kwargs):  # noqa: E501
        """Bulk Update Models  # noqa: E501

        Returns the updated models  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_models_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20091
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
                    " to method update_models" % key
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
            '/investment-management/models', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20091',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
