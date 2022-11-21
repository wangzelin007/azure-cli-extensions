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
    "reservations reservation split",
)
class Split(AAZCommand):
    """Split a `Reservation` into two `Reservation`s with specified quantity distribution.

    :example: Split a reservation
        az reservations reservation split --quantities "[2,8]" --reservation-id /providers/Microsoft.Capacity/reservationOrders/30000000-aaaa-bbbb-cccc-100000000004/reservations/40000000-aaaa-bbbb-cccc-100000000001 --reservation-order-id 30000000-aaaa-bbbb-cccc-100000000004
    """

    _aaz_info = {
        "version": "2022-03-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.capacity/reservationorders/{}/split", "2022-03-01"],
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
        _args_schema.reservation_order_id = AAZStrArg(
            options=["--reservation-order-id"],
            help="Order Id of the reservation",
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.quantities = AAZListArg(
            options=["--quantities"],
            arg_group="Properties",
            help="List of the quantities in the new reservations to create.",
        )
        _args_schema.reservation_id = AAZStrArg(
            options=["--reservation-id"],
            arg_group="Properties",
            help="Resource id of the reservation to be split. Format of the resource id should be /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}",
        )

        quantities = cls._args_schema.quantities
        quantities.Element = AAZIntArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.ReservationSplit(ctx=self.ctx)()
        self.post_operations()

    # @register_callback
    def pre_operations(self):
        pass

    # @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ReservationSplit(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/split",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "reservationOrderId", self.ctx.args.reservation_order_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-03-01",
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
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("quantities", AAZListType, ".quantities")
                properties.set_prop("reservationId", AAZStrType, ".reservation_id")

            quantities = _builder.get(".properties.quantities")
            if quantities is not None:
                quantities.set_elements(AAZIntType, ".")

            return self.serialize_content(_content_value)

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

            cls._schema_on_200 = AAZListType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.Element = AAZObjectType()

            _element = cls._schema_on_200.Element
            _element.etag = AAZIntType()
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.kind = AAZStrType()
            _element.location = AAZStrType()
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType()
            _element.sku = AAZObjectType()
            _build_schema_sku_name_read(_element.sku)
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.Element.properties
            properties.applied_scope_properties = AAZObjectType(
                serialized_name="appliedScopeProperties",
            )
            properties.applied_scope_type = AAZStrType(
                serialized_name="appliedScopeType",
            )
            properties.applied_scopes = AAZListType(
                serialized_name="appliedScopes",
            )
            _build_schema_applied_scopes_read(properties.applied_scopes)
            properties.archived = AAZBoolType()
            properties.benefit_start_time = AAZStrType(
                serialized_name="benefitStartTime",
            )
            properties.billing_plan = AAZStrType(
                serialized_name="billingPlan",
            )
            properties.billing_scope_id = AAZStrType(
                serialized_name="billingScopeId",
            )
            properties.capabilities = AAZStrType()
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.display_provisioning_state = AAZStrType(
                serialized_name="displayProvisioningState",
                flags={"read_only": True},
            )
            properties.effective_date_time = AAZStrType(
                serialized_name="effectiveDateTime",
            )
            properties.expiry_date = AAZStrType(
                serialized_name="expiryDate",
            )
            properties.extended_status_info = AAZObjectType(
                serialized_name="extendedStatusInfo",
            )
            properties.instance_flexibility = AAZStrType(
                serialized_name="instanceFlexibility",
            )
            properties.last_updated_date_time = AAZStrType(
                serialized_name="lastUpdatedDateTime",
                flags={"read_only": True},
            )
            properties.merge_properties = AAZObjectType(
                serialized_name="mergeProperties",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            properties.provisioning_sub_state = AAZStrType(
                serialized_name="provisioningSubState",
                flags={"read_only": True},
            )
            properties.purchase_date = AAZStrType(
                serialized_name="purchaseDate",
            )
            properties.quantity = AAZIntType()
            properties.renew = AAZBoolType()
            properties.renew_destination = AAZStrType(
                serialized_name="renewDestination",
            )
            properties.renew_properties = AAZObjectType(
                serialized_name="renewProperties",
            )
            properties.renew_source = AAZStrType(
                serialized_name="renewSource",
            )
            properties.reserved_resource_type = AAZStrType(
                serialized_name="reservedResourceType",
            )
            properties.sku_description = AAZStrType(
                serialized_name="skuDescription",
            )
            properties.split_properties = AAZObjectType(
                serialized_name="splitProperties",
            )
            properties.swap_properties = AAZObjectType(
                serialized_name="swapProperties",
            )
            properties.term = AAZStrType()
            properties.user_friendly_applied_scope_type = AAZStrType(
                serialized_name="userFriendlyAppliedScopeType",
                flags={"read_only": True},
            )
            properties.user_friendly_renew_state = AAZStrType(
                serialized_name="userFriendlyRenewState",
                flags={"read_only": True},
            )
            properties.utilization = AAZObjectType(
                flags={"read_only": True},
            )

            applied_scope_properties = cls._schema_on_200.Element.properties.applied_scope_properties
            applied_scope_properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            applied_scope_properties.management_group_id = AAZStrType(
                serialized_name="managementGroupId",
            )
            applied_scope_properties.tenant_id = AAZStrType(
                serialized_name="tenantId",
            )

            extended_status_info = cls._schema_on_200.Element.properties.extended_status_info
            extended_status_info.message = AAZStrType()
            extended_status_info.status_code = AAZStrType(
                serialized_name="statusCode",
            )

            merge_properties = cls._schema_on_200.Element.properties.merge_properties
            merge_properties.merge_destination = AAZStrType(
                serialized_name="mergeDestination",
            )
            merge_properties.merge_sources = AAZListType(
                serialized_name="mergeSources",
            )

            merge_sources = cls._schema_on_200.Element.properties.merge_properties.merge_sources
            merge_sources.Element = AAZStrType()

            renew_properties = cls._schema_on_200.Element.properties.renew_properties
            renew_properties.billing_currency_total = AAZObjectType(
                serialized_name="billingCurrencyTotal",
            )
            renew_properties.pricing_currency_total = AAZObjectType(
                serialized_name="pricingCurrencyTotal",
            )
            renew_properties.purchase_properties = AAZObjectType(
                serialized_name="purchaseProperties",
            )

            billing_currency_total = cls._schema_on_200.Element.properties.renew_properties.billing_currency_total
            billing_currency_total.amount = AAZFloatType()
            billing_currency_total.currency_code = AAZStrType(
                serialized_name="currencyCode",
            )

            pricing_currency_total = cls._schema_on_200.Element.properties.renew_properties.pricing_currency_total
            pricing_currency_total.amount = AAZFloatType()
            pricing_currency_total.currency_code = AAZStrType(
                serialized_name="currencyCode",
            )

            purchase_properties = cls._schema_on_200.Element.properties.renew_properties.purchase_properties
            purchase_properties.location = AAZStrType()
            purchase_properties.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            purchase_properties.sku = AAZObjectType()
            _build_schema_sku_name_read(purchase_properties.sku)

            properties = cls._schema_on_200.Element.properties.renew_properties.purchase_properties.properties
            properties.applied_scope_type = AAZStrType(
                serialized_name="appliedScopeType",
            )
            properties.applied_scopes = AAZListType(
                serialized_name="appliedScopes",
            )
            _build_schema_applied_scopes_read(properties.applied_scopes)
            properties.billing_plan = AAZStrType(
                serialized_name="billingPlan",
            )
            properties.billing_scope_id = AAZStrType(
                serialized_name="billingScopeId",
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.quantity = AAZIntType()
            properties.renew = AAZBoolType()
            properties.reserved_resource_properties = AAZObjectType(
                serialized_name="reservedResourceProperties",
            )
            properties.reserved_resource_type = AAZStrType(
                serialized_name="reservedResourceType",
            )
            properties.term = AAZStrType()

            reserved_resource_properties = cls._schema_on_200.Element.properties.renew_properties.purchase_properties.properties.reserved_resource_properties
            reserved_resource_properties.instance_flexibility = AAZStrType(
                serialized_name="instanceFlexibility",
            )

            split_properties = cls._schema_on_200.Element.properties.split_properties
            split_properties.split_destinations = AAZListType(
                serialized_name="splitDestinations",
            )
            split_properties.split_source = AAZStrType(
                serialized_name="splitSource",
            )

            split_destinations = cls._schema_on_200.Element.properties.split_properties.split_destinations
            split_destinations.Element = AAZStrType()

            swap_properties = cls._schema_on_200.Element.properties.swap_properties
            swap_properties.swap_destination = AAZStrType(
                serialized_name="swapDestination",
            )
            swap_properties.swap_source = AAZStrType(
                serialized_name="swapSource",
            )

            utilization = cls._schema_on_200.Element.properties.utilization
            utilization.aggregates = AAZListType(
                flags={"read_only": True},
            )
            utilization.trend = AAZStrType(
                flags={"read_only": True},
            )

            aggregates = cls._schema_on_200.Element.properties.utilization.aggregates
            aggregates.Element = AAZObjectType(
                flags={"read_only": True},
            )

            _element = cls._schema_on_200.Element.properties.utilization.aggregates.Element
            _element.grain = AAZFloatType(
                flags={"read_only": True},
            )
            _element.grain_unit = AAZStrType(
                serialized_name="grainUnit",
                flags={"read_only": True},
            )
            _element.value = AAZFloatType(
                flags={"read_only": True},
            )
            _element.value_unit = AAZStrType(
                serialized_name="valueUnit",
                flags={"read_only": True},
            )

            system_data = cls._schema_on_200.Element.system_data
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

            return cls._schema_on_200


_schema_applied_scopes_read = None


def _build_schema_applied_scopes_read(_schema):
    global _schema_applied_scopes_read
    if _schema_applied_scopes_read is not None:
        _schema.Element = _schema_applied_scopes_read.Element
        return

    _schema_applied_scopes_read = AAZListType()

    applied_scopes_read = _schema_applied_scopes_read
    applied_scopes_read.Element = AAZStrType()

    _schema.Element = _schema_applied_scopes_read.Element


_schema_sku_name_read = None


def _build_schema_sku_name_read(_schema):
    global _schema_sku_name_read
    if _schema_sku_name_read is not None:
        _schema.name = _schema_sku_name_read.name
        return

    _schema_sku_name_read = AAZObjectType()

    sku_name_read = _schema_sku_name_read
    sku_name_read.name = AAZStrType()

    _schema.name = _schema_sku_name_read.name


__all__ = ["Split"]
