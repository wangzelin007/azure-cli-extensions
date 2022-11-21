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
    "nginx deployment configuration update",
)
class Update(AAZCommand):
    """Update an Nginx configuration

    :example: Update content of the first file in a configuration
        az nginx deployment configuration update --name default --deployment-name myDeployment --resource-group myResourceGroup --files [0].content="aHR0cCB7CiAgICB1cHN0cmVhbSBhcHAgewogICAgICAgIHpvbmUgYXBwIDY0azsKICAgICAgICBsZWFzdF9jb25uOwogICAgICAgIHNlcnZlciAxMC4wLjEuNDo4MDAwOwogICAgfQoKICAgIHNlcnZlciB7CiAgICAgICAgbGlzdGVuIDgwOwogICAgICAgIHNlcnZlcl9uYW1lICouZXhhbXBsZS5jb207CgogICAgICAgIGxvY2F0aW9uIC8gewogICAgICAgICAgICBwcm94eV9zZXRfaGVhZGVyIEhvc3QgJGhvc3Q7CiAgICAgICAgICAgIHByb3h5X3NldF9oZWFkZXIgWC1SZWFsLUlQICRyZW1vdGVfYWRkcjsKICAgICAgICAgICAgcHJveHlfc2V0X2hlYWRlciBYLVByb3h5LUFwcCBhcHA7CiAgICAgICAgICAgIHByb3h5X3NldF9oZWFkZXIgR2l0aHViLVJ1bi1JZCAwMDAwMDA7CiAgICAgICAgICAgIHByb3h5X2J1ZmZlcmluZyBvbjsKICAgICAgICAgICAgcHJveHlfYnVmZmVyX3NpemUgNGs7CiAgICAgICAgICAgIHByb3h5X2J1ZmZlcnMgOCA4azsKICAgICAgICAgICAgcHJveHlfcmVhZF90aW1lb3V0IDYwczsKICAgICAgICAgICAgcHJveHlfcGFzcyBodHRwOi8vYXBwOwogICAgICAgICAgICBoZWFsdGhfY2hlY2s7CiAgICAgICAgfQogICAgICAgIAogICAgfQp9"
    """

    _aaz_info = {
        "version": "2022-08-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/nginx.nginxplus/nginxdeployments/{}/configurations/{}", "2022-08-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

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
        _args_schema.configuration_name = AAZStrArg(
            options=["-n", "--name", "--configuration-name"],
            help="The name of configuration, only 'default' is supported value due to the singleton of Nginx conf",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.deployment_name = AAZStrArg(
            options=["--deployment-name"],
            help="The name of targeted Nginx deployment",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Body",
            nullable=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Body",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.files = AAZListArg(
            options=["--files"],
            arg_group="Properties",
            nullable=True,
        )
        _args_schema.package = AAZObjectArg(
            options=["--package"],
            arg_group="Properties",
            nullable=True,
        )
        _args_schema.protected_files = AAZListArg(
            options=["--protected-files"],
            arg_group="Properties",
            nullable=True,
        )
        _args_schema.provisioning_state = AAZStrArg(
            options=["--provisioning-state"],
            help="State of the configuration deployment",
            arg_group="Properties",
            nullable=True,
            enum={"Accepted": "Accepted", "Canceled": "Canceled", "Creating": "Creating", "Deleted": "Deleted", "Deleting": "Deleting", "Failed": "Failed", "NotSpecified": "NotSpecified", "Succeeded": "Succeeded", "Updating": "Updating"},
        )
        _args_schema.root_file = AAZStrArg(
            options=["--root-file"],
            help="Aligns with your Nginx configuration structure",
            arg_group="Properties",
            nullable=True,
        )

        files = cls._args_schema.files
        files.Element = AAZObjectArg(
            nullable=True,
        )
        cls._build_args_nginx_configuration_file_update(files.Element)

        package = cls._args_schema.package
        package.data = AAZStrArg(
            options=["data"],
            nullable=True,
        )

        protected_files = cls._args_schema.protected_files
        protected_files.Element = AAZObjectArg(
            nullable=True,
        )
        cls._build_args_nginx_configuration_file_update(protected_files.Element)
        return cls._args_schema

    _args_nginx_configuration_file_update = None

    @classmethod
    def _build_args_nginx_configuration_file_update(cls, _schema):
        if cls._args_nginx_configuration_file_update is not None:
            _schema.content = cls._args_nginx_configuration_file_update.content
            _schema.virtual_path = cls._args_nginx_configuration_file_update.virtual_path
            return

        cls._args_nginx_configuration_file_update = AAZObjectArg(
            nullable=True,
        )

        nginx_configuration_file_update = cls._args_nginx_configuration_file_update
        nginx_configuration_file_update.content = AAZStrArg(
            options=["content"],
            nullable=True,
        )
        nginx_configuration_file_update.virtual_path = AAZStrArg(
            options=["virtual-path"],
            nullable=True,
        )

        _schema.content = cls._args_nginx_configuration_file_update.content
        _schema.virtual_path = cls._args_nginx_configuration_file_update.virtual_path

    def _execute_operations(self):
        self.ConfigurationsGet(ctx=self.ctx)()
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        yield self.ConfigurationsCreateOrUpdate(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ConfigurationsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Nginx.NginxPlus/nginxDeployments/{deploymentName}/configurations/{configurationName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"
        
        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-08-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "configurationName", self.ctx.args.configuration_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "deploymentName", self.ctx.args.deployment_name,
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
            _build_schema_nginx_configuration_read(cls._schema_on_200)

            return cls._schema_on_200

    class ConfigurationsCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Nginx.NginxPlus/nginxDeployments/{deploymentName}/configurations/{configurationName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"
        
        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-08-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "configurationName", self.ctx.args.configuration_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "deploymentName", self.ctx.args.deployment_name,
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
                value=self.ctx.vars.instance,
            )

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
            _build_schema_nginx_configuration_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("properties", AAZObjectType)
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("files", AAZListType, ".files")
                properties.set_prop("package", AAZObjectType, ".package")
                properties.set_prop("protectedFiles", AAZListType, ".protected_files")
                properties.set_prop("provisioningState", AAZStrType, ".provisioning_state")
                properties.set_prop("rootFile", AAZStrType, ".root_file")

            files = _builder.get(".properties.files")
            if files is not None:
                _build_schema_nginx_configuration_file_update(files.set_elements(AAZObjectType, "."))

            package = _builder.get(".properties.package")
            if package is not None:
                package.set_prop("data", AAZStrType, ".data")

            protected_files = _builder.get(".properties.protectedFiles")
            if protected_files is not None:
                _build_schema_nginx_configuration_file_update(protected_files.set_elements(AAZObjectType, "."))

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


def _build_schema_nginx_configuration_file_update(_builder):
    if _builder is None:
        return
    _builder.set_prop("content", AAZStrType, ".content")
    _builder.set_prop("virtualPath", AAZStrType, ".virtual_path")


_schema_nginx_configuration_file_read = None


def _build_schema_nginx_configuration_file_read(_schema):
    global _schema_nginx_configuration_file_read
    if _schema_nginx_configuration_file_read is not None:
        _schema.content = _schema_nginx_configuration_file_read.content
        _schema.virtual_path = _schema_nginx_configuration_file_read.virtual_path
        return

    _schema_nginx_configuration_file_read = AAZObjectType()

    nginx_configuration_file_read = _schema_nginx_configuration_file_read
    nginx_configuration_file_read.content = AAZStrType()
    nginx_configuration_file_read.virtual_path = AAZStrType(
        serialized_name="virtualPath",
    )

    _schema.content = _schema_nginx_configuration_file_read.content
    _schema.virtual_path = _schema_nginx_configuration_file_read.virtual_path


_schema_nginx_configuration_read = None


def _build_schema_nginx_configuration_read(_schema):
    global _schema_nginx_configuration_read
    if _schema_nginx_configuration_read is not None:
        _schema.id = _schema_nginx_configuration_read.id
        _schema.location = _schema_nginx_configuration_read.location
        _schema.name = _schema_nginx_configuration_read.name
        _schema.properties = _schema_nginx_configuration_read.properties
        _schema.system_data = _schema_nginx_configuration_read.system_data
        _schema.tags = _schema_nginx_configuration_read.tags
        _schema.type = _schema_nginx_configuration_read.type
        return

    _schema_nginx_configuration_read = AAZObjectType()

    nginx_configuration_read = _schema_nginx_configuration_read
    nginx_configuration_read.id = AAZStrType(
        flags={"read_only": True},
    )
    nginx_configuration_read.location = AAZStrType()
    nginx_configuration_read.name = AAZStrType(
        flags={"read_only": True},
    )
    nginx_configuration_read.properties = AAZObjectType()
    nginx_configuration_read.system_data = AAZObjectType(
        serialized_name="systemData",
        flags={"read_only": True},
    )
    nginx_configuration_read.tags = AAZDictType()
    nginx_configuration_read.type = AAZStrType(
        flags={"read_only": True},
    )

    properties = _schema_nginx_configuration_read.properties
    properties.files = AAZListType()
    properties.package = AAZObjectType()
    properties.protected_files = AAZListType(
        serialized_name="protectedFiles",
    )
    properties.provisioning_state = AAZStrType(
        serialized_name="provisioningState",
    )
    properties.root_file = AAZStrType(
        serialized_name="rootFile",
    )

    files = _schema_nginx_configuration_read.properties.files
    files.Element = AAZObjectType()
    _build_schema_nginx_configuration_file_read(files.Element)

    package = _schema_nginx_configuration_read.properties.package
    package.data = AAZStrType()

    protected_files = _schema_nginx_configuration_read.properties.protected_files
    protected_files.Element = AAZObjectType()
    _build_schema_nginx_configuration_file_read(protected_files.Element)

    system_data = _schema_nginx_configuration_read.system_data
    system_data.created_at = AAZStrType(
        serialized_name="createdAt",
        flags={"read_only": True},
    )
    system_data.created_by = AAZStrType(
        serialized_name="createdBy",
        flags={"read_only": True},
    )
    system_data.created_by_type = AAZStrType(
        serialized_name="createdByType",
        flags={"read_only": True},
    )
    system_data.last_modified_at = AAZStrType(
        serialized_name="lastModifiedAt",
        flags={"read_only": True},
    )
    system_data.last_modified_by = AAZStrType(
        serialized_name="lastModifiedBy",
        flags={"read_only": True},
    )
    system_data.last_modified_by_type = AAZStrType(
        serialized_name="lastModifiedByType",
        flags={"read_only": True},
    )

    tags = _schema_nginx_configuration_read.tags
    tags.Element = AAZStrType()

    _schema.id = _schema_nginx_configuration_read.id
    _schema.location = _schema_nginx_configuration_read.location
    _schema.name = _schema_nginx_configuration_read.name
    _schema.properties = _schema_nginx_configuration_read.properties
    _schema.system_data = _schema_nginx_configuration_read.system_data
    _schema.tags = _schema_nginx_configuration_read.tags
    _schema.type = _schema_nginx_configuration_read.type


__all__ = ["Update"]
