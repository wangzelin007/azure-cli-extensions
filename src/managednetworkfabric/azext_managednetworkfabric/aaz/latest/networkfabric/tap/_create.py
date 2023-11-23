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
    "networkfabric tap create",
)
class Create(AAZCommand):
    """Create a Network Tap resource

    :example: Create a Network Tap
        az networkfabric tap create --resource-group "example-rg" --location "westus3" --resource-name "example-networktap" --network-packet-broker-id "/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourcegroups/example-rg/providers/Microsoft.ManagedNetworkFabric/networkPacketBrokers/example-networkPacketBroker" --polling-type "Pull" --destinations "[{name:'example-destinaionName',destinationType:IsolationDomain,destinationId:'/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourcegroups/example-rg/providers/Microsoft.ManagedNetworkFabric/l3IsloationDomains/example-l3Domain/internalNetworks/example-internalNetwork',isolationDomainProperties:{encapsulation:None,neighborGroupIds:['/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourcegroups/example-rg/providers/Microsoft.ManagedNetworkFabric/neighborGroups/example-neighborGroup']},destinationTapRuleId:'/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourcegroups/example-rg/providers/Microsoft.ManagedNetworkFabric/networkTapRules/example-destinationTapRule'}]"

    :example: Help text for sub parameters under the specific parent can be viewed by using the shorthand syntax '??'. See https://github.com/Azure/azure-cli/tree/dev/doc/shorthand_syntax.md for more about shorthand syntax.
        az networkfabric tap create --destinations "??"
    """

    _aaz_info = {
        "version": "2023-06-15",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.managednetworkfabric/networktaps/{}", "2023-06-15"],
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
        _args_schema.resource_name = AAZStrArg(
            options=["--resource-name"],
            help="Name of the Network Tap.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of the resource group",
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Body",
            help="Location of Azure region",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Body",
            help="Resource tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.annotation = AAZStrArg(
            options=["--annotation"],
            arg_group="Properties",
            help="Description for underlying resource.",
        )
        _args_schema.destinations = AAZListArg(
            options=["--destinations"],
            arg_group="Properties",
            help="List of destinations to send the filter traffic.",
            required=True,
        )
        _args_schema.network_packet_broker_id = AAZResourceIdArg(
            options=["--npb-id", "--network-packet-broker-id"],
            arg_group="Properties",
            help="ARM resource ID of the Network Packet Broker.",
            required=True,
        )
        _args_schema.polling_type = AAZStrArg(
            options=["--polling-type"],
            arg_group="Properties",
            help="Network tap rule file polling type. Default value is Pull. Example: Pull.",
            enum={"Pull": "Pull", "Push": "Push"},
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )

        destinations = cls._args_schema.destinations
        destinations.Element = AAZObjectArg()

        _element = cls._args_schema.destinations.Element
        _element.destination_id = AAZResourceIdArg(
            options=["destination-id"],
            help="The destination Id. ARM Resource ID of either NNI or Internal Networks.",
            required=True,
        )
        _element.destination_tap_rule_id = AAZResourceIdArg(
            options=["destination-tap-rule-id"],
            help="ARM Resource ID of destination Tap Rule that contains match configurations.",
        )
        _element.destination_type = AAZStrArg(
            options=["destination-type"],
            help="Type of destination. Input can be IsolationDomain or Direct. Example: Direct.",
            required=True,
            enum={"Direct": "Direct", "IsolationDomain": "IsolationDomain"},
        )
        _element.isolation_domain_properties = AAZObjectArg(
            options=["isolation-domain-properties"],
            help="Isolation Domain Properties.",
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="Destination name.",
            required=True,
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )

        isolation_domain_properties = cls._args_schema.destinations.Element.isolation_domain_properties
        isolation_domain_properties.encapsulation = AAZStrArg(
            options=["encapsulation"],
            help="Type of encapsulation. Example: GRE.",
            enum={"GRE": "GRE", "None": "None"},
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )
        isolation_domain_properties.neighbor_group_ids = AAZListArg(
            options=["neighbor-group-ids"],
            help="List of Neighbor Group IDs.",
        )

        neighbor_group_ids = cls._args_schema.destinations.Element.isolation_domain_properties.neighbor_group_ids
        neighbor_group_ids.Element = AAZResourceIdArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.NetworkTapsCreate(ctx=self.ctx)()
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

    class NetworkTapsCreate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkTaps/{networkTapName}",
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
                    "networkTapName", self.ctx.args.resource_name,
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
                    "api-version", "2023-06-15",
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
                properties.set_prop("annotation", AAZStrType, ".annotation")
                properties.set_prop("destinations", AAZListType, ".destinations", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("networkPacketBrokerId", AAZStrType, ".network_packet_broker_id", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("pollingType", AAZStrType, ".polling_type")

            destinations = _builder.get(".properties.destinations")
            if destinations is not None:
                destinations.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.destinations[]")
            if _elements is not None:
                _elements.set_prop("destinationId", AAZStrType, ".destination_id", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("destinationTapRuleId", AAZStrType, ".destination_tap_rule_id")
                _elements.set_prop("destinationType", AAZStrType, ".destination_type", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("isolationDomainProperties", AAZObjectType, ".isolation_domain_properties")
                _elements.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})

            isolation_domain_properties = _builder.get(".properties.destinations[].isolationDomainProperties")
            if isolation_domain_properties is not None:
                isolation_domain_properties.set_prop("encapsulation", AAZStrType, ".encapsulation")
                isolation_domain_properties.set_prop("neighborGroupIds", AAZListType, ".neighbor_group_ids")

            neighbor_group_ids = _builder.get(".properties.destinations[].isolationDomainProperties.neighborGroupIds")
            if neighbor_group_ids is not None:
                neighbor_group_ids.set_elements(AAZStrType, ".")

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
            properties.administrative_state = AAZStrType(
                serialized_name="administrativeState",
                flags={"read_only": True},
            )
            properties.annotation = AAZStrType()
            properties.configuration_state = AAZStrType(
                serialized_name="configurationState",
                flags={"read_only": True},
            )
            properties.destinations = AAZListType(
                flags={"required": True},
            )
            properties.network_packet_broker_id = AAZStrType(
                serialized_name="networkPacketBrokerId",
                flags={"required": True},
            )
            properties.polling_type = AAZStrType(
                serialized_name="pollingType",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.source_tap_rule_id = AAZStrType(
                serialized_name="sourceTapRuleId",
                flags={"read_only": True},
            )

            destinations = cls._schema_on_200_201.properties.destinations
            destinations.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.destinations.Element
            _element.destination_id = AAZStrType(
                serialized_name="destinationId",
                flags={"required": True},
            )
            _element.destination_tap_rule_id = AAZStrType(
                serialized_name="destinationTapRuleId",
            )
            _element.destination_type = AAZStrType(
                serialized_name="destinationType",
                flags={"required": True},
            )
            _element.isolation_domain_properties = AAZObjectType(
                serialized_name="isolationDomainProperties",
            )
            _element.name = AAZStrType(
                flags={"required": True},
            )

            isolation_domain_properties = cls._schema_on_200_201.properties.destinations.Element.isolation_domain_properties
            isolation_domain_properties.encapsulation = AAZStrType()
            isolation_domain_properties.neighbor_group_ids = AAZListType(
                serialized_name="neighborGroupIds",
            )

            neighbor_group_ids = cls._schema_on_200_201.properties.destinations.Element.isolation_domain_properties.neighbor_group_ids
            neighbor_group_ids.Element = AAZStrType()

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
