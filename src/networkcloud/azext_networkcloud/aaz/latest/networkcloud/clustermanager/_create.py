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
    "networkcloud clustermanager create",
    is_experimental=True,
)
class Create(AAZCommand):
    """Create a new cluster manager or update properties of the cluster manager if it exists.

    :example: Create or update cluster manager
        az networkcloud clustermanager create --name "clusterManagerName" --location "location" --analytics-workspace-id "/subscriptions/subscriptionId/resourceGroups/resourceGroupName/providers/microsoft.operationalInsights/workspaces/logAnalyticsWorkspaceName" --fabric-controller-id "/subscriptions/subscriptionId/resourceGroups/resourceGroupName/providers/Microsoft.ManagedNetworkFabric/networkFabricControllers/fabricControllerName" --managed-resource-group-configuration name="my-managed-rg" --tags key1="myvalue1" key2="myvalue2" --resource-group "resourceGroupName"
    """

    _aaz_info = {
        "version": "2022-12-12-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.networkcloud/clustermanagers/{}", "2022-12-12-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.cluster_manager_name = AAZStrArg(
            options=["-n", "--name", "--cluster-manager-name"],
            help="The name of the cluster manager.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^([a-zA-Z0-9][a-zA-Z0-9-_]{0,28}[a-zA-Z0-9])$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "ClusterManagerParameters"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="ClusterManagerParameters",
            help="The geo-location where the resource lives",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="ClusterManagerParameters",
            help="Resource tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.analytics_workspace_id = AAZStrArg(
            options=["--analytics-workspace-id"],
            arg_group="Properties",
            help="The resource ID of the Log Analytics workspace that is used for the logs collection.",
        )
        _args_schema.availability_zones = AAZListArg(
            options=["--availability-zones"],
            arg_group="Properties",
            help="Field deprecated, this value will no longer influence the cluster manager allocation process and will be removed in a future version. The Azure availability zones within the region that will be used to support the cluster manager resource.",
        )
        _args_schema.fabric_controller_id = AAZStrArg(
            options=["--fabric-controller-id"],
            arg_group="Properties",
            help="The resource ID of the fabric controller that has one to one mapping with the cluster manager.",
            required=True,
        )
        _args_schema.managed_resource_group_configuration = AAZObjectArg(
            options=["--managed-resource-group-configuration"],
            arg_group="Properties",
            help="The configuration of the managed resource group associated with the resource.",
        )
        _args_schema.vm_size = AAZStrArg(
            options=["--vm-size"],
            arg_group="Properties",
            help="Field deprecated, this value will no longer influence the cluster manager allocation process and will be removed in a future version. The size of the Azure virtual machines to use for hosting the cluster manager resource.",
        )

        availability_zones = cls._args_schema.availability_zones
        availability_zones.Element = AAZStrArg()

        managed_resource_group_configuration = cls._args_schema.managed_resource_group_configuration
        managed_resource_group_configuration.location = AAZStrArg(
            options=["location"],
            help="The location of the managed resource group. If not specified, the location of the parent resource is chosen.",
        )
        managed_resource_group_configuration.name = AAZStrArg(
            options=["name"],
            help="The name for the managed resource group. If not specified, the unique name is automatically generated.",
            fmt=AAZStrArgFormat(
                max_length=75,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.ClusterManagersCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ClusterManagersCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusterManagers/{clusterManagerName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "clusterManagerName", self.ctx.args.cluster_manager_name,
                    required=True,
                ),
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
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("analyticsWorkspaceId", AAZStrType, ".analytics_workspace_id")
                properties.set_prop("availabilityZones", AAZListType, ".availability_zones")
                properties.set_prop("fabricControllerId", AAZStrType, ".fabric_controller_id", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("managedResourceGroupConfiguration", AAZObjectType, ".managed_resource_group_configuration")
                properties.set_prop("vmSize", AAZStrType, ".vm_size")

            availability_zones = _builder.get(".properties.availabilityZones")
            if availability_zones is not None:
                availability_zones.set_elements(AAZStrType, ".")

            managed_resource_group_configuration = _builder.get(".properties.managedResourceGroupConfiguration")
            if managed_resource_group_configuration is not None:
                managed_resource_group_configuration.set_prop("location", AAZStrType, ".location")
                managed_resource_group_configuration.set_prop("name", AAZStrType, ".name")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.analytics_workspace_id = AAZStrType(
                serialized_name="analyticsWorkspaceId",
            )
            properties.availability_zones = AAZListType(
                serialized_name="availabilityZones",
            )
            properties.cluster_versions = AAZListType(
                serialized_name="clusterVersions",
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
            properties.fabric_controller_id = AAZStrType(
                serialized_name="fabricControllerId",
                flags={"required": True},
            )
            properties.managed_resource_group_configuration = AAZObjectType(
                serialized_name="managedResourceGroupConfiguration",
            )
            properties.manager_extended_location = AAZObjectType(
                serialized_name="managerExtendedLocation",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.vm_size = AAZStrType(
                serialized_name="vmSize",
            )

            availability_zones = cls._schema_on_200_201.properties.availability_zones
            availability_zones.Element = AAZStrType()

            cluster_versions = cls._schema_on_200_201.properties.cluster_versions
            cluster_versions.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.cluster_versions.Element
            _element.support_expiry_date = AAZStrType(
                serialized_name="supportExpiryDate",
                flags={"read_only": True},
            )
            _element.target_cluster_version = AAZStrType(
                serialized_name="targetClusterVersion",
                flags={"read_only": True},
            )

            managed_resource_group_configuration = cls._schema_on_200_201.properties.managed_resource_group_configuration
            managed_resource_group_configuration.location = AAZStrType()
            managed_resource_group_configuration.name = AAZStrType()

            manager_extended_location = cls._schema_on_200_201.properties.manager_extended_location
            manager_extended_location.name = AAZStrType(
                flags={"required": True},
            )
            manager_extended_location.type = AAZStrType(
                flags={"required": True},
            )

            system_data = cls._schema_on_200_201.system_data
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

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
