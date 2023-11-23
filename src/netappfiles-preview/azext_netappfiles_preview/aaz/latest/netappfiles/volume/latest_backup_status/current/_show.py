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
    "netappfiles volume latest-backup-status current show",
    is_preview=True,
)
class Show(AAZCommand):
    """Get the latest status of the backup for a volume
    """

    _aaz_info = {
        "version": "2022-11-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.netapp/netappaccounts/{}/capacitypools/{}/volumes/{}/latestbackupstatus/current", "2022-11-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.account_name = AAZStrArg(
            options=["-a", "--account-name"],
            help="The name of the NetApp account",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9\-_]{0,127}$",
            ),
        )
        _args_schema.pool_name = AAZStrArg(
            options=["-p", "--pool-name"],
            help="The name of the capacity pool",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9\-_]{0,63}$",
                max_length=64,
                min_length=1,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.volume_name = AAZStrArg(
            options=["--volume-name"],
            help="The name of the volume",
            required=True,
            id_part="child_name_2",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z][a-zA-Z0-9\-_]{0,63}$",
                max_length=64,
                min_length=1,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.BackupsGetLatestStatus(ctx=self.ctx)()
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

    class BackupsGetLatestStatus(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/latestBackupStatus/current",
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
                    "accountName", self.ctx.args.account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "poolName", self.ctx.args.pool_name,
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
                **self.serialize_url_param(
                    "volumeName", self.ctx.args.volume_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-11-01-preview",
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
            _schema_on_200.error_message = AAZStrType(
                serialized_name="errorMessage",
                flags={"read_only": True},
            )
            _schema_on_200.healthy = AAZBoolType(
                flags={"read_only": True},
            )
            _schema_on_200.last_transfer_size = AAZIntType(
                serialized_name="lastTransferSize",
                flags={"read_only": True},
            )
            _schema_on_200.last_transfer_type = AAZStrType(
                serialized_name="lastTransferType",
                flags={"read_only": True},
            )
            _schema_on_200.mirror_state = AAZStrType(
                serialized_name="mirrorState",
                flags={"read_only": True},
            )
            _schema_on_200.relationship_status = AAZStrType(
                serialized_name="relationshipStatus",
                flags={"read_only": True},
            )
            _schema_on_200.total_transfer_bytes = AAZIntType(
                serialized_name="totalTransferBytes",
                flags={"read_only": True},
            )
            _schema_on_200.transfer_progress_bytes = AAZIntType(
                serialized_name="transferProgressBytes",
                flags={"read_only": True},
            )
            _schema_on_200.unhealthy_reason = AAZStrType(
                serialized_name="unhealthyReason",
                flags={"read_only": True},
            )

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]
