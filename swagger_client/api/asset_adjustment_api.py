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


class AssetAdjustmentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_asset_adjustments(self, body, **kwargs):  # noqa: E501
        """Create an Asset Adjustment  # noqa: E501

        Returns a created Asset Adjustment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_asset_adjustments(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BillingAssetadjustmentsBody body: (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_asset_adjustments_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_asset_adjustments_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_asset_adjustments_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create an Asset Adjustment  # noqa: E501

        Returns a created Asset Adjustment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_asset_adjustments_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BillingAssetadjustmentsBody body: (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20013
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
                    " to method create_asset_adjustments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_asset_adjustments`")  # noqa: E501

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
            '/billing/asset-adjustments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20013',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_many_asset_adjustments(self, **kwargs):  # noqa: E501
        """Create Asset Adjustments  # noqa: E501

        Returns the created Asset Adjustment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_many_asset_adjustments(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_many_asset_adjustments_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_many_asset_adjustments_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_many_asset_adjustments_with_http_info(self, **kwargs):  # noqa: E501
        """Create Asset Adjustments  # noqa: E501

        Returns the created Asset Adjustment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_many_asset_adjustments_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20012
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
                    " to method create_many_asset_adjustments" % key
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
            '/billing/asset-adjustments/create-many', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def detele_asset_adjustment(self, id, **kwargs):  # noqa: E501
        """Delete an Asset Adjustment  # noqa: E501

        Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.detele_asset_adjustment(id, async_req=True)
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
            return self.detele_asset_adjustment_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.detele_asset_adjustment_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def detele_asset_adjustment_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete an Asset Adjustment  # noqa: E501

        Returns the \"OK\" message and a json object with the id  of item deleted, if deletion was successful  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.detele_asset_adjustment_with_http_info(id, async_req=True)
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
                    " to method detele_asset_adjustment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `detele_asset_adjustment`")  # noqa: E501

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
            '/billing/asset-adjustments/{id}', 'DELETE',
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

    def detele_many_asset_adjustments(self, body, **kwargs):  # noqa: E501
        """Delete many Asset Adjustments  # noqa: E501

        Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.detele_many_asset_adjustments(body, async_req=True)
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
            return self.detele_many_asset_adjustments_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.detele_many_asset_adjustments_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def detele_many_asset_adjustments_with_http_info(self, body, **kwargs):  # noqa: E501
        """Delete many Asset Adjustments  # noqa: E501

        Returns the \"OK\" message and a json object with the number of items deleted, if deletion was successful  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.detele_many_asset_adjustments_with_http_info(body, async_req=True)
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
                    " to method detele_many_asset_adjustments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `detele_many_asset_adjustments`")  # noqa: E501

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
            '/billing/asset-adjustments/delete-many', 'POST',
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

    def filter_billing_asset_adjustment(self, **kwargs):  # noqa: E501
        """Filter all Asset Adjustment  # noqa: E501

        Returns a filtered list of Asset Adjustment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.filter_billing_asset_adjustment(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AssetadjustmentsFilterBody body:
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.filter_billing_asset_adjustment_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.filter_billing_asset_adjustment_with_http_info(**kwargs)  # noqa: E501
            return data

    def filter_billing_asset_adjustment_with_http_info(self, **kwargs):  # noqa: E501
        """Filter all Asset Adjustment  # noqa: E501

        Returns a filtered list of Asset Adjustment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.filter_billing_asset_adjustment_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AssetadjustmentsFilterBody body:
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20012
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
                    " to method filter_billing_asset_adjustment" % key
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
            '/billing/asset-adjustments/filter', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_asset_adjustment(self, id, **kwargs):  # noqa: E501
        """Retrieve an Asset Adjustment  # noqa: E501

        Returns an Asset Adjustment based on a single ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_asset_adjustment(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_asset_adjustment_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_asset_adjustment_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_asset_adjustment_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve an Asset Adjustment  # noqa: E501

        Returns an Asset Adjustment based on a single ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_asset_adjustment_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20013
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
                    " to method get_asset_adjustment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_asset_adjustment`")  # noqa: E501

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
            '/billing/asset-adjustments/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20013',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_asset_adjustments(self, **kwargs):  # noqa: E501
        """List all Asset Adjustments  # noqa: E501

        Returns a list of Asset Adjustments within the data field  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_asset_adjustments(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_asset_adjustments_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_asset_adjustments_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_asset_adjustments_with_http_info(self, **kwargs):  # noqa: E501
        """List all Asset Adjustments  # noqa: E501

        Returns a list of Asset Adjustments within the data field  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_asset_adjustments_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20012
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
                    " to method get_asset_adjustments" % key
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
            '/billing/asset-adjustments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_asset_adjustment(self, id, **kwargs):  # noqa: E501
        """Update an Asset Adjustment  # noqa: E501

        Returns the updated Asset Adjustment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_asset_adjustment(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_asset_adjustment_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_asset_adjustment_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_asset_adjustment_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update an Asset Adjustment  # noqa: E501

        Returns the updated Asset Adjustment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_asset_adjustment_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Unique ID for the object (required)
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20013
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
                    " to method update_asset_adjustment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_asset_adjustment`")  # noqa: E501

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
            '/billing/asset-adjustments/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20013',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_asset_adjustments(self, **kwargs):  # noqa: E501
        """Bulk Update Asset Adjustments  # noqa: E501

        Returns the updated Asset Adjustments  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_asset_adjustments(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_asset_adjustments_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.update_asset_adjustments_with_http_info(**kwargs)  # noqa: E501
            return data

    def update_asset_adjustments_with_http_info(self, **kwargs):  # noqa: E501
        """Bulk Update Asset Adjustments  # noqa: E501

        Returns the updated Asset Adjustments  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_asset_adjustments_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pager_limit: Number of items to return per page
        :param int pager_page: Current page number
        :return: InlineResponse20012
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
                    " to method update_asset_adjustments" % key
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
            '/billing/asset-adjustments', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
