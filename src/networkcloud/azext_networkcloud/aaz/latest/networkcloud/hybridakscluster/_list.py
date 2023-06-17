# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "networkcloud hybridakscluster list",
    is_experimental=True,
)
class List(AAZCommand):
    """List additional details related to Hybrid AKS provisioned clusters in the provided resource group or subscription.

    :example: List Hybrid AKS provisioned clusters data for resource group
        az networkcloud hybridakscluster list --resource-group "resourceGroupName"

    :example: List Hybrid AKS provisioned clusters data for subscription
        az networkcloud hybridakscluster list
    """

    _aaz_info = {
        "version": "2022-12-12-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.networkcloud/hybridaksclusters", "2022-12-12-preview"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.networkcloud/hybridaksclusters", "2022-12-12-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        condition_1 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.resource_group) is not True
        if condition_0:
            self.HybridAksClustersListByResourceGroup(ctx=self.ctx)()
        if condition_1:
            self.HybridAksClustersListBySubscription(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class HybridAksClustersListByResourceGroup(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/hybridAksClusters",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-12-12-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.extended_location = AAZObjectType(
                serialized_name="extendedLocation",
                flags={"required": True},
            )
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            extended_location = cls._schema_on_200.value.Element.extended_location
            extended_location.name = AAZStrType(
                flags={"required": True},
            )
            extended_location.type = AAZStrType(
                flags={"required": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.associated_network_ids = AAZListType(
                serialized_name="associatedNetworkIds",
                flags={"required": True},
            )
            properties.cloud_services_network_id = AAZStrType(
                serialized_name="cloudServicesNetworkId",
                flags={"read_only": True},
            )
            properties.cluster_id = AAZStrType(
                serialized_name="clusterId",
                flags={"read_only": True},
            )
            properties.control_plane_count = AAZIntType(
                serialized_name="controlPlaneCount",
                flags={"required": True},
            )
            properties.control_plane_nodes = AAZListType(
                serialized_name="controlPlaneNodes",
                flags={"read_only": True},
            )
            properties.default_cni_network_id = AAZStrType(
                serialized_name="defaultCniNetworkId",
                flags={"read_only": True},
            )
            properties.detailed_status = AAZStrType(
                serialized_name="detailedStatus",
                flags={"read_only": True},
            )
            properties.detailed_status_message = AAZStrType(
                serialized_name="detailedStatusMessage",
                flags={"read_only": True},
            )
            properties.hybrid_aks_provisioned_cluster_id = AAZStrType(
                serialized_name="hybridAksProvisionedClusterId",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.volumes = AAZListType(
                flags={"read_only": True},
            )
            properties.worker_count = AAZIntType(
                serialized_name="workerCount",
                flags={"required": True},
            )
            properties.worker_nodes = AAZListType(
                serialized_name="workerNodes",
                flags={"read_only": True},
            )

            associated_network_ids = cls._schema_on_200.value.Element.properties.associated_network_ids
            associated_network_ids.Element = AAZStrType()

            control_plane_nodes = cls._schema_on_200.value.Element.properties.control_plane_nodes
            control_plane_nodes.Element = AAZObjectType()
            _ListHelper._build_schema_node_configuration_read(control_plane_nodes.Element)

            volumes = cls._schema_on_200.value.Element.properties.volumes
            volumes.Element = AAZStrType()

            worker_nodes = cls._schema_on_200.value.Element.properties.worker_nodes
            worker_nodes.Element = AAZObjectType()
            _ListHelper._build_schema_node_configuration_read(worker_nodes.Element)

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200

    class HybridAksClustersListBySubscription(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.NetworkCloud/hybridAksClusters",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-12-12-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.extended_location = AAZObjectType(
                serialized_name="extendedLocation",
                flags={"required": True},
            )
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            extended_location = cls._schema_on_200.value.Element.extended_location
            extended_location.name = AAZStrType(
                flags={"required": True},
            )
            extended_location.type = AAZStrType(
                flags={"required": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.associated_network_ids = AAZListType(
                serialized_name="associatedNetworkIds",
                flags={"required": True},
            )
            properties.cloud_services_network_id = AAZStrType(
                serialized_name="cloudServicesNetworkId",
                flags={"read_only": True},
            )
            properties.cluster_id = AAZStrType(
                serialized_name="clusterId",
                flags={"read_only": True},
            )
            properties.control_plane_count = AAZIntType(
                serialized_name="controlPlaneCount",
                flags={"required": True},
            )
            properties.control_plane_nodes = AAZListType(
                serialized_name="controlPlaneNodes",
                flags={"read_only": True},
            )
            properties.default_cni_network_id = AAZStrType(
                serialized_name="defaultCniNetworkId",
                flags={"read_only": True},
            )
            properties.detailed_status = AAZStrType(
                serialized_name="detailedStatus",
                flags={"read_only": True},
            )
            properties.detailed_status_message = AAZStrType(
                serialized_name="detailedStatusMessage",
                flags={"read_only": True},
            )
            properties.hybrid_aks_provisioned_cluster_id = AAZStrType(
                serialized_name="hybridAksProvisionedClusterId",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.volumes = AAZListType(
                flags={"read_only": True},
            )
            properties.worker_count = AAZIntType(
                serialized_name="workerCount",
                flags={"required": True},
            )
            properties.worker_nodes = AAZListType(
                serialized_name="workerNodes",
                flags={"read_only": True},
            )

            associated_network_ids = cls._schema_on_200.value.Element.properties.associated_network_ids
            associated_network_ids.Element = AAZStrType()

            control_plane_nodes = cls._schema_on_200.value.Element.properties.control_plane_nodes
            control_plane_nodes.Element = AAZObjectType()
            _ListHelper._build_schema_node_configuration_read(control_plane_nodes.Element)

            volumes = cls._schema_on_200.value.Element.properties.volumes
            volumes.Element = AAZStrType()

            worker_nodes = cls._schema_on_200.value.Element.properties.worker_nodes
            worker_nodes.Element = AAZObjectType()
            _ListHelper._build_schema_node_configuration_read(worker_nodes.Element)

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""

    _schema_node_configuration_read = None

    @classmethod
    def _build_schema_node_configuration_read(cls, _schema):
        if cls._schema_node_configuration_read is not None:
            _schema.agent_pool_id = cls._schema_node_configuration_read.agent_pool_id
            _schema.agent_pool_name = cls._schema_node_configuration_read.agent_pool_name
            _schema.cpu_cores = cls._schema_node_configuration_read.cpu_cores
            _schema.disk_size_gb = cls._schema_node_configuration_read.disk_size_gb
            _schema.memory_size_gb = cls._schema_node_configuration_read.memory_size_gb
            _schema.node_pool_name = cls._schema_node_configuration_read.node_pool_name
            _schema.nodes = cls._schema_node_configuration_read.nodes
            _schema.vm_count = cls._schema_node_configuration_read.vm_count
            _schema.vm_size = cls._schema_node_configuration_read.vm_size
            return

        cls._schema_node_configuration_read = _schema_node_configuration_read = AAZObjectType()

        node_configuration_read = _schema_node_configuration_read
        node_configuration_read.agent_pool_id = AAZStrType(
            serialized_name="agentPoolId",
            flags={"read_only": True},
        )
        node_configuration_read.agent_pool_name = AAZStrType(
            serialized_name="agentPoolName",
            flags={"read_only": True},
        )
        node_configuration_read.cpu_cores = AAZIntType(
            serialized_name="cpuCores",
            flags={"read_only": True},
        )
        node_configuration_read.disk_size_gb = AAZIntType(
            serialized_name="diskSizeGB",
            flags={"read_only": True},
        )
        node_configuration_read.memory_size_gb = AAZIntType(
            serialized_name="memorySizeGB",
            flags={"read_only": True},
        )
        node_configuration_read.node_pool_name = AAZStrType(
            serialized_name="nodePoolName",
            flags={"read_only": True},
        )
        node_configuration_read.nodes = AAZListType(
            flags={"read_only": True},
        )
        node_configuration_read.vm_count = AAZIntType(
            serialized_name="vmCount",
            flags={"read_only": True},
        )
        node_configuration_read.vm_size = AAZStrType(
            serialized_name="vmSize",
            flags={"read_only": True},
        )

        nodes = _schema_node_configuration_read.nodes
        nodes.Element = AAZObjectType()

        _element = _schema_node_configuration_read.nodes.Element
        _element.bare_metal_machine_id = AAZStrType(
            serialized_name="bareMetalMachineId",
            flags={"read_only": True},
        )
        _element.image_id = AAZStrType(
            serialized_name="imageId",
            flags={"read_only": True},
        )
        _element.network_attachments = AAZListType(
            serialized_name="networkAttachments",
            flags={"read_only": True},
        )
        _element.node_name = AAZStrType(
            serialized_name="nodeName",
            flags={"read_only": True},
        )
        _element.power_state = AAZStrType(
            serialized_name="powerState",
            flags={"read_only": True},
        )

        network_attachments = _schema_node_configuration_read.nodes.Element.network_attachments
        network_attachments.Element = AAZObjectType()

        _element = _schema_node_configuration_read.nodes.Element.network_attachments.Element
        _element.attached_network_id = AAZStrType(
            serialized_name="attachedNetworkId",
            flags={"required": True},
        )
        _element.default_gateway = AAZStrType(
            serialized_name="defaultGateway",
        )
        _element.ip_allocation_method = AAZStrType(
            serialized_name="ipAllocationMethod",
            flags={"required": True},
        )
        _element.ipv4_address = AAZStrType(
            serialized_name="ipv4Address",
        )
        _element.ipv6_address = AAZStrType(
            serialized_name="ipv6Address",
        )
        _element.mac_address = AAZStrType(
            serialized_name="macAddress",
            flags={"read_only": True},
        )
        _element.network_attachment_name = AAZStrType(
            serialized_name="networkAttachmentName",
        )

        _schema.agent_pool_id = cls._schema_node_configuration_read.agent_pool_id
        _schema.agent_pool_name = cls._schema_node_configuration_read.agent_pool_name
        _schema.cpu_cores = cls._schema_node_configuration_read.cpu_cores
        _schema.disk_size_gb = cls._schema_node_configuration_read.disk_size_gb
        _schema.memory_size_gb = cls._schema_node_configuration_read.memory_size_gb
        _schema.node_pool_name = cls._schema_node_configuration_read.node_pool_name
        _schema.nodes = cls._schema_node_configuration_read.nodes
        _schema.vm_count = cls._schema_node_configuration_read.vm_count
        _schema.vm_size = cls._schema_node_configuration_read.vm_size


__all__ = ["List"]
