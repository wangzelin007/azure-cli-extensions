# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Iterable, Optional, TypeVar
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_list_by_publisher_request(
    proxy_publisher_name,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2023-04-01-preview")  # type: str
    publisher_scope_name = kwargs.pop('publisher_scope_name')  # type: str
    publisher_location_name = kwargs.pop('publisher_location_name')  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.HybridNetwork/proxyPublishers/{proxyPublisherName}/networkFunctionDefinitionGroups")  # pylint: disable=line-too-long
    path_format_arguments = {
        "proxyPublisherName": _SERIALIZER.url("proxy_publisher_name", proxy_publisher_name, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]*$'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['publisherScopeName'] = _SERIALIZER.query("publisher_scope_name", publisher_scope_name, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]*$')
    _query_parameters['publisherLocationName'] = _SERIALIZER.query("publisher_location_name", publisher_location_name, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]*$')
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_get_request(
    proxy_publisher_name,  # type: str
    network_function_definition_group_name,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2023-04-01-preview")  # type: str
    publisher_scope_name = kwargs.pop('publisher_scope_name')  # type: str
    publisher_location_name = kwargs.pop('publisher_location_name')  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.HybridNetwork/proxyPublishers/{proxyPublisherName}/networkFunctionDefinitionGroups/{networkFunctionDefinitionGroupName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "proxyPublisherName": _SERIALIZER.url("proxy_publisher_name", proxy_publisher_name, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]*$'),
        "networkFunctionDefinitionGroupName": _SERIALIZER.url("network_function_definition_group_name", network_function_definition_group_name, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]*$'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['publisherScopeName'] = _SERIALIZER.query("publisher_scope_name", publisher_scope_name, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]*$')
    _query_parameters['publisherLocationName'] = _SERIALIZER.query("publisher_location_name", publisher_location_name, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]*$')
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )

# fmt: on
class ProxyNetworkFunctionDefinitionGroupsOperations(object):
    """ProxyNetworkFunctionDefinitionGroupsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~Microsoft.HybridNetwork.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list_by_publisher(
        self,
        publisher_scope_name,  # type: str
        publisher_location_name,  # type: str
        proxy_publisher_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.NetworkFunctionDefinitionGroupOverviewListResult"]
        """Lists all available network function definition group under a publisher.

        :param publisher_scope_name: The name of the publisher scope.
        :type publisher_scope_name: str
        :param publisher_location_name: The name of the publisher location.
        :type publisher_location_name: str
        :param proxy_publisher_name: The name of the proxy publisher.
        :type proxy_publisher_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either NetworkFunctionDefinitionGroupOverviewListResult
         or the result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~Microsoft.HybridNetwork.models.NetworkFunctionDefinitionGroupOverviewListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2023-04-01-preview")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.NetworkFunctionDefinitionGroupOverviewListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_publisher_request(
                    proxy_publisher_name=proxy_publisher_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    publisher_scope_name=publisher_scope_name,
                    publisher_location_name=publisher_location_name,
                    template_url=self.list_by_publisher.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_by_publisher_request(
                    proxy_publisher_name=proxy_publisher_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    publisher_scope_name=publisher_scope_name,
                    publisher_location_name=publisher_location_name,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("NetworkFunctionDefinitionGroupOverviewListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_by_publisher.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.HybridNetwork/proxyPublishers/{proxyPublisherName}/networkFunctionDefinitionGroups"}  # type: ignore

    @distributed_trace
    def get(
        self,
        publisher_scope_name,  # type: str
        publisher_location_name,  # type: str
        proxy_publisher_name,  # type: str
        network_function_definition_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.NetworkFunctionDefinitionGroupOverview"
        """Get information about network function definition overview.

        :param publisher_scope_name: The name of the publisher scope.
        :type publisher_scope_name: str
        :param publisher_location_name: The name of the publisher location.
        :type publisher_location_name: str
        :param proxy_publisher_name: The name of the proxy publisher.
        :type proxy_publisher_name: str
        :param network_function_definition_group_name: The name of the network function definition
         group.
        :type network_function_definition_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NetworkFunctionDefinitionGroupOverview, or the result of cls(response)
        :rtype: ~Microsoft.HybridNetwork.models.NetworkFunctionDefinitionGroupOverview
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.NetworkFunctionDefinitionGroupOverview"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2023-04-01-preview")  # type: str

        
        request = build_get_request(
            proxy_publisher_name=proxy_publisher_name,
            network_function_definition_group_name=network_function_definition_group_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            publisher_scope_name=publisher_scope_name,
            publisher_location_name=publisher_location_name,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('NetworkFunctionDefinitionGroupOverview', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.HybridNetwork/proxyPublishers/{proxyPublisherName}/networkFunctionDefinitionGroups/{networkFunctionDefinitionGroupName}"}  # type: ignore
