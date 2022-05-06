# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=unused-argument

from azure.cli.core.util import sdk_no_wait


def healthcareapis_service_list(client,
                                resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list()


def healthcareapis_service_show(client,
                                resource_group_name,
                                resource_name):
    return client.get(resource_group_name=resource_group_name,
                      resource_name=resource_name)


def healthcareapis_service_create(client,
                                  resource_group_name,
                                  resource_name,
                                  kind,
                                  location,
                                  tags=None,
                                  etag=None,
                                  identity_type=None,
                                  access_policies=None,
                                  cosmos_db_configuration=None,
                                  authentication_configuration=None,
                                  cors_configuration=None,
                                  private_endpoint_connections=None,
                                  public_network_access=None,
                                  login_servers=None,
                                  oci_artifacts=None,
                                  export_configuration_storage_account_name=None,
                                  no_wait=False):
    service_description = {}
    service_description['kind'] = kind
    service_description['location'] = location
    if tags is not None:
        service_description['tags'] = tags
    if etag is not None:
        service_description['etag'] = etag
    service_description['identity'] = {}
    if type_ is not None:
        service_description['identity']['type'] = type_
    if len(service_description['identity']) == 0:
        del service_description['identity']
    service_description['properties'] = {}
    if access_policies is not None:
        service_description['properties']['access_policies'] = access_policies
    if cosmos_db_configuration is not None:
        service_description['properties']['cosmos_db_configuration'] = cosmos_db_configuration
    if authentication_configuration is not None:
        service_description['properties']['authentication_configuration'] = authentication_configuration
    if cors_configuration is not None:
        service_description['properties']['cors_configuration'] = cors_configuration
    if private_endpoint_connections is not None:
        service_description['properties']['private_endpoint_connections'] = private_endpoint_connections
    if public_network_access is not None:
        service_description['properties']['public_network_access'] = public_network_access
    service_description['properties']['acr_configuration'] = {}
    if login_servers is not None:
        service_description['properties']['acr_configuration']['login_servers'] = login_servers
    if oci_artifacts is not None:
        service_description['properties']['acr_configuration']['oci_artifacts'] = oci_artifacts
    if len(service_description['properties']['acr_configuration']) == 0:
        del service_description['properties']['acr_configuration']
    service_description['properties']['export_configuration'] = {}
    if export_configuration_storage_account_name is not None:
        service_description['properties']['export_configuration']['storage_account_name'] = export_configuration_storage_account_name
    if len(service_description['properties']['export_configuration']) == 0:
        del service_description['properties']['export_configuration']
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       resource_name=resource_name,
                       service_description=service_description)


def healthcareapis_service_update(client,
                                  resource_group_name,
                                  resource_name,
                                  tags=None,
                                  public_network_access=None,
                                  no_wait=False):
    service_patch_description = {}
    if tags is not None:
        service_patch_description['tags'] = tags
    if public_network_access is not None:
        service_patch_description['public_network_access'] = public_network_access
    return sdk_no_wait(no_wait,
                       client.begin_update,
                       resource_group_name=resource_group_name,
                       resource_name=resource_name,
                       service_patch_description=service_patch_description)


def healthcareapis_service_delete(client,
                                  resource_group_name,
                                  resource_name,
                                  no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       resource_name=resource_name)
def healthcareapis_operation_result_show(client,
                                         location_name,
                                         operation_result_id):
    return client.get(location_name=location_name,
                      operation_result_id=operation_result_id)


def healthcareapis_private_endpoint_connection_list(client,
                                                    resource_group_name,
                                                    resource_name):
    return client.list_by_service(resource_group_name=resource_group_name,
                                  resource_name=resource_name)


def healthcareapis_private_endpoint_connection_show(client,
                                                    resource_group_name,
                                                    resource_name,
                                                    private_endpoint_connection_name):
    return client.get(resource_group_name=resource_group_name,
                      resource_name=resource_name,
                      private_endpoint_connection_name=private_endpoint_connection_name)


def healthcareapis_private_endpoint_connection_create(client,
                                                      resource_group_name,
                                                      resource_name,
                                                      private_endpoint_connection_name,
                                                      private_link_service_connection_state=None,
                                                      no_wait=False):
    properties = {}
    if private_link_service_connection_state is not None:
        properties['private_link_service_connection_state'] = private_link_service_connection_state
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       resource_name=resource_name,
                       private_endpoint_connection_name=private_endpoint_connection_name,
                       properties=properties)


def healthcareapis_private_endpoint_connection_update(client,
                                                      resource_group_name,
                                                      resource_name,
                                                      private_endpoint_connection_name,
                                                      private_link_service_connection_state=None,
                                                      no_wait=False):
    properties = {}
    if private_link_service_connection_state is not None:
        properties['private_link_service_connection_state'] = private_link_service_connection_state
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       resource_name=resource_name,
                       private_endpoint_connection_name=private_endpoint_connection_name,
                       properties=properties)


def healthcareapis_private_endpoint_connection_delete(client,
                                                      resource_group_name,
                                                      resource_name,
                                                      private_endpoint_connection_name,
                                                      no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       resource_name=resource_name,
                       private_endpoint_connection_name=private_endpoint_connection_name)


def healthcareapis_private_link_resource_list(client,
                                              resource_group_name,
                                              resource_name):
    return client.list_by_service(resource_group_name=resource_group_name,
                                  resource_name=resource_name)


def healthcareapis_private_link_resource_show(client,
                                              resource_group_name,
                                              resource_name,
                                              group_name):
    return client.get(resource_group_name=resource_group_name,
                      resource_name=resource_name,
                      group_name=group_name)


def healthcareapis_workspace_list(client,
                                  resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def healthcareapis_workspace_show(client,
                                  resource_group_name,
                                  workspace_name):
    return client.get(resource_group_name=resource_group_name,
                      workspace_name=workspace_name)


def healthcareapis_workspace_create(client,
                                    resource_group_name,
                                    workspace_name,
                                    tags=None,
                                    etag=None,
                                    location=None,
                                    public_network_access=None,
                                    no_wait=False):
    workspace = {}
    if tags is not None:
        workspace['tags'] = tags
    if etag is not None:
        workspace['etag'] = etag
    if location is not None:
        workspace['location'] = location
    workspace['properties'] = {}
    if public_network_access is not None:
        workspace['properties']['public_network_access'] = public_network_access
    if len(workspace['properties']) == 0:
        del workspace['properties']
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       workspace=workspace)


def healthcareapis_workspace_update(client,
                                    resource_group_name,
                                    workspace_name,
                                    tags=None,
                                    no_wait=False):
    workspace_patch_resource = {}
    if tags is not None:
        workspace_patch_resource['tags'] = tags
    return sdk_no_wait(no_wait,
                       client.begin_update,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       workspace_patch_resource=workspace_patch_resource)


def healthcareapis_workspace_delete(client,
                                    resource_group_name,
                                    workspace_name,
                                    no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name)


def healthcareapis_workspace_dicom_service_list(client,
                                                resource_group_name,
                                                workspace_name):
    return client.list_by_workspace(resource_group_name=resource_group_name,
                                    workspace_name=workspace_name)


def healthcareapis_workspace_dicom_service_show(client,
                                                resource_group_name,
                                                workspace_name,
                                                dicom_service_name):
    return client.get(resource_group_name=resource_group_name,
                      workspace_name=workspace_name,
                      dicom_service_name=dicom_service_name)


def healthcareapis_workspace_dicom_service_create(client,
                                                  resource_group_name,
                                                  workspace_name,
                                                  dicom_service_name,
                                                  tags=None,
                                                  etag=None,
                                                  location=None,
                                                  type_=None,
                                                  user_assigned_identities=None,
                                                  public_network_access=None,
                                                  no_wait=False):
    dicomservice = {}
    if tags is not None:
        dicomservice['tags'] = tags
    if etag is not None:
        dicomservice['etag'] = etag
    if location is not None:
        dicomservice['location'] = location
    dicomservice['identity'] = {}
    if type_ is not None:
        dicomservice['identity']['type'] = type_
    if user_assigned_identities is not None:
        dicomservice['identity']['user_assigned_identities'] = user_assigned_identities
    if len(dicomservice['identity']) == 0:
        del dicomservice['identity']
    if public_network_access is not None:
        dicomservice['public_network_access'] = public_network_access
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       dicom_service_name=dicom_service_name,
                       dicomservice=dicomservice)


def healthcareapis_workspace_dicom_service_update(client,
                                                  resource_group_name,
                                                  dicom_service_name,
                                                  workspace_name,
                                                  tags=None,
                                                  type_=None,
                                                  user_assigned_identities=None,
                                                  no_wait=False):
    dicomservice_patch_resource = {}
    if tags is not None:
        dicomservice_patch_resource['tags'] = tags
    dicomservice_patch_resource['identity'] = {}
    if type_ is not None:
        dicomservice_patch_resource['identity']['type'] = type_
    if user_assigned_identities is not None:
        dicomservice_patch_resource['identity']['user_assigned_identities'] = user_assigned_identities
    if len(dicomservice_patch_resource['identity']) == 0:
        del dicomservice_patch_resource['identity']
    return sdk_no_wait(no_wait,
                       client.begin_update,
                       resource_group_name=resource_group_name,
                       dicom_service_name=dicom_service_name,
                       workspace_name=workspace_name,
                       dicomservice_patch_resource=dicomservice_patch_resource)


def healthcareapis_workspace_dicom_service_delete(client,
                                                  resource_group_name,
                                                  dicom_service_name,
                                                  workspace_name,
                                                  no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       dicom_service_name=dicom_service_name,
                       workspace_name=workspace_name)


def healthcareapis_workspace_iot_connector_list(client,
                                                resource_group_name,
                                                workspace_name):
    return client.list_by_workspace(resource_group_name=resource_group_name,
                                    workspace_name=workspace_name)


def healthcareapis_workspace_iot_connector_show(client,
                                                resource_group_name,
                                                workspace_name,
                                                iot_connector_name):
    return client.get(resource_group_name=resource_group_name,
                      workspace_name=workspace_name,
                      iot_connector_name=iot_connector_name)


def healthcareapis_workspace_iot_connector_create(client,
                                                  resource_group_name,
                                                  workspace_name,
                                                  iot_connector_name,
                                                  tags=None,
                                                  etag=None,
                                                  location=None,
                                                  type_=None,
                                                  user_assigned_identities=None,
                                                  ingestion_endpoint_configuration=None,
                                                  content=None,
                                                  no_wait=False):
    iot_connector = {}
    if tags is not None:
        iot_connector['tags'] = tags
    if etag is not None:
        iot_connector['etag'] = etag
    if location is not None:
        iot_connector['location'] = location
    iot_connector['identity'] = {}
    if type_ is not None:
        iot_connector['identity']['type'] = type_
    if user_assigned_identities is not None:
        iot_connector['identity']['user_assigned_identities'] = user_assigned_identities
    if len(iot_connector['identity']) == 0:
        del iot_connector['identity']
    if ingestion_endpoint_configuration is not None:
        iot_connector['ingestion_endpoint_configuration'] = ingestion_endpoint_configuration
    iot_connector['device_mapping'] = {}
    if content is not None:
        iot_connector['device_mapping']['content'] = content
    if len(iot_connector['device_mapping']) == 0:
        del iot_connector['device_mapping']
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       iot_connector_name=iot_connector_name,
                       iot_connector=iot_connector)


def healthcareapis_workspace_iot_connector_update(client,
                                                  resource_group_name,
                                                  iot_connector_name,
                                                  workspace_name,
                                                  tags=None,
                                                  type_=None,
                                                  user_assigned_identities=None,
                                                  no_wait=False):
    iot_connector_patch_resource = {}
    if tags is not None:
        iot_connector_patch_resource['tags'] = tags
    iot_connector_patch_resource['identity'] = {}
    if type_ is not None:
        iot_connector_patch_resource['identity']['type'] = type_
    if user_assigned_identities is not None:
        iot_connector_patch_resource['identity']['user_assigned_identities'] = user_assigned_identities
    if len(iot_connector_patch_resource['identity']) == 0:
        del iot_connector_patch_resource['identity']
    return sdk_no_wait(no_wait,
                       client.begin_update,
                       resource_group_name=resource_group_name,
                       iot_connector_name=iot_connector_name,
                       workspace_name=workspace_name,
                       iot_connector_patch_resource=iot_connector_patch_resource)


def healthcareapis_workspace_iot_connector_delete(client,
                                                  resource_group_name,
                                                  iot_connector_name,
                                                  workspace_name,
                                                  no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       iot_connector_name=iot_connector_name,
                       workspace_name=workspace_name)


def healthcareapis_workspace_iot_connector_fhir_destination_list(client,
                                                                 resource_group_name,
                                                                 workspace_name,
                                                                 iot_connector_name):
    return client.list_by_iot_connector(resource_group_name=resource_group_name,
                                        workspace_name=workspace_name,
                                        iot_connector_name=iot_connector_name)


def healthcareapis_workspace_iot_connector_fhir_destination_show(client,
                                                                 resource_group_name,
                                                                 workspace_name,
                                                                 iot_connector_name,
                                                                 fhir_destination_name):
    return client.get(resource_group_name=resource_group_name,
                      workspace_name=workspace_name,
                      iot_connector_name=iot_connector_name,
                      fhir_destination_name=fhir_destination_name)


def healthcareapis_workspace_iot_connector_fhir_destination_create(client,
                                                                   resource_group_name,
                                                                   workspace_name,
                                                                   iot_connector_name,
                                                                   fhir_destination_name,
                                                                   resource_identity_resolution_type,
                                                                   fhir_service_resource_id,
                                                                   etag=None,
                                                                   location=None,
                                                                   content=None,
                                                                   no_wait=False):
    iot_fhir_destination = {}
    if etag is not None:
        iot_fhir_destination['etag'] = etag
    if location is not None:
        iot_fhir_destination['location'] = location
    iot_fhir_destination['resource_identity_resolution_type'] = resource_identity_resolution_type
    iot_fhir_destination['fhir_service_resource_id'] = fhir_service_resource_id
    iot_fhir_destination['fhir_mapping'] = {}
    if content is not None:
        iot_fhir_destination['fhir_mapping']['content'] = content
    if len(iot_fhir_destination['fhir_mapping']) == 0:
        del iot_fhir_destination['fhir_mapping']
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       iot_connector_name=iot_connector_name,
                       fhir_destination_name=fhir_destination_name,
                       iot_fhir_destination=iot_fhir_destination)


def healthcareapis_workspace_iot_connector_fhir_destination_update(instance,
                                                                   resource_group_name,
                                                                   workspace_name,
                                                                   iot_connector_name,
                                                                   fhir_destination_name,
                                                                   resource_identity_resolution_type,
                                                                   fhir_service_resource_id,
                                                                   etag=None,
                                                                   location=None,
                                                                   content=None,
                                                                   no_wait=False):
    if etag is not None:
        instance.etag = etag
    if location is not None:
        instance.location = location
    instance.resource_identity_resolution_type = resource_identity_resolution_type
    instance.fhir_service_resource_id = fhir_service_resource_id
    if content is not None:
        instance.fhir_mapping.content = content
    return instance


def healthcareapis_workspace_iot_connector_fhir_destination_delete(client,
                                                                   resource_group_name,
                                                                   workspace_name,
                                                                   iot_connector_name,
                                                                   fhir_destination_name,
                                                                   no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       iot_connector_name=iot_connector_name,
                       fhir_destination_name=fhir_destination_name)


def healthcareapis_workspace_fhir_service_list(client,
                                               resource_group_name,
                                               workspace_name):
    return client.list_by_workspace(resource_group_name=resource_group_name,
                                    workspace_name=workspace_name)


def healthcareapis_workspace_fhir_service_show(client,
                                               resource_group_name,
                                               workspace_name,
                                               fhir_service_name):
    return client.get(resource_group_name=resource_group_name,
                      workspace_name=workspace_name,
                      fhir_service_name=fhir_service_name)


def healthcareapis_workspace_fhir_service_create(client,
                                                 resource_group_name,
                                                 workspace_name,
                                                 fhir_service_name,
                                                 tags=None,
                                                 etag=None,
                                                 location=None,
                                                 type_=None,
                                                 user_assigned_identities=None,
                                                 kind=None,
                                                 access_policies=None,
                                                 authentication_configuration=None,
                                                 cors_configuration=None,
                                                 public_network_access=None,
                                                 default=None,
                                                 resource_type_overrides=None,
                                                 storage_account_name=None,
                                                 login_servers=None,
                                                 oci_artifacts=None,
                                                 no_wait=False):
    fhirservice = {}
    if tags is not None:
        fhirservice['tags'] = tags
    if etag is not None:
        fhirservice['etag'] = etag
    if location is not None:
        fhirservice['location'] = location
    fhirservice['identity'] = {}
    if type_ is not None:
        fhirservice['identity']['type'] = type_
    if user_assigned_identities is not None:
        fhirservice['identity']['user_assigned_identities'] = user_assigned_identities
    if len(fhirservice['identity']) == 0:
        del fhirservice['identity']
    if kind is not None:
        fhirservice['kind'] = kind
    if access_policies is not None:
        fhirservice['access_policies'] = access_policies
    if authentication_configuration is not None:
        fhirservice['authentication_configuration'] = authentication_configuration
    if cors_configuration is not None:
        fhirservice['cors_configuration'] = cors_configuration
    if public_network_access is not None:
        fhirservice['public_network_access'] = public_network_access
    fhirservice['resource_version_policy_configuration'] = {}
    if default is not None:
        fhirservice['resource_version_policy_configuration']['default'] = default
    if resource_type_overrides is not None:
        fhirservice['resource_version_policy_configuration']['resource_type_overrides'] = resource_type_overrides
    if len(fhirservice['resource_version_policy_configuration']) == 0:
        del fhirservice['resource_version_policy_configuration']
    fhirservice['export_configuration'] = {}
    if storage_account_name is not None:
        fhirservice['export_configuration']['storage_account_name'] = storage_account_name
    if len(fhirservice['export_configuration']) == 0:
        del fhirservice['export_configuration']
    fhirservice['acr_configuration'] = {}
    if login_servers is not None:
        fhirservice['acr_configuration']['login_servers'] = login_servers
    if oci_artifacts is not None:
        fhirservice['acr_configuration']['oci_artifacts'] = oci_artifacts
    if len(fhirservice['acr_configuration']) == 0:
        del fhirservice['acr_configuration']
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       fhir_service_name=fhir_service_name,
                       fhirservice=fhirservice)


def healthcareapis_workspace_fhir_service_update(client,
                                                 resource_group_name,
                                                 fhir_service_name,
                                                 workspace_name,
                                                 tags=None,
                                                 type_=None,
                                                 user_assigned_identities=None,
                                                 no_wait=False):
    fhirservice_patch_resource = {}
    if tags is not None:
        fhirservice_patch_resource['tags'] = tags
    fhirservice_patch_resource['identity'] = {}
    if type_ is not None:
        fhirservice_patch_resource['identity']['type'] = type_
    if user_assigned_identities is not None:
        fhirservice_patch_resource['identity']['user_assigned_identities'] = user_assigned_identities
    if len(fhirservice_patch_resource['identity']) == 0:
        del fhirservice_patch_resource['identity']
    return sdk_no_wait(no_wait,
                       client.begin_update,
                       resource_group_name=resource_group_name,
                       fhir_service_name=fhir_service_name,
                       workspace_name=workspace_name,
                       fhirservice_patch_resource=fhirservice_patch_resource)


def healthcareapis_workspace_fhir_service_delete(client,
                                                 resource_group_name,
                                                 fhir_service_name,
                                                 workspace_name,
                                                 no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       fhir_service_name=fhir_service_name,
                       workspace_name=workspace_name)


def healthcareapis_workspace_private_endpoint_connection_list(client,
                                                              resource_group_name,
                                                              workspace_name):
    return client.list_by_workspace(resource_group_name=resource_group_name,
                                    workspace_name=workspace_name)


def healthcareapis_workspace_private_endpoint_connection_show(client,
                                                              resource_group_name,
                                                              workspace_name,
                                                              private_endpoint_connection_name):
    return client.get(resource_group_name=resource_group_name,
                      workspace_name=workspace_name,
                      private_endpoint_connection_name=private_endpoint_connection_name)


def healthcareapis_workspace_private_endpoint_connection_create(client,
                                                                resource_group_name,
                                                                workspace_name,
                                                                private_endpoint_connection_name,
                                                                private_link_service_connection_state=None,
                                                                no_wait=False):
    properties = {}
    if private_link_service_connection_state is not None:
        properties['private_link_service_connection_state'] = private_link_service_connection_state
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       private_endpoint_connection_name=private_endpoint_connection_name,
                       properties=properties)


def healthcareapis_workspace_private_endpoint_connection_update(instance,
                                                                resource_group_name,
                                                                workspace_name,
                                                                private_endpoint_connection_name,
                                                                private_link_service_connection_state=None,
                                                                no_wait=False):
    if private_link_service_connection_state is not None:
        instance.private_link_service_connection_state = private_link_service_connection_state
    return instance


def healthcareapis_workspace_private_endpoint_connection_delete(client,
                                                                resource_group_name,
                                                                workspace_name,
                                                                private_endpoint_connection_name,
                                                                no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       workspace_name=workspace_name,
                       private_endpoint_connection_name=private_endpoint_connection_name)


def healthcareapis_workspace_private_link_resource_list(client,
                                                        resource_group_name,
                                                        workspace_name):
    return client.list_by_workspace(resource_group_name=resource_group_name,
                                    workspace_name=workspace_name)


def healthcareapis_workspace_private_link_resource_show(client,
                                                        resource_group_name,
                                                        workspace_name,
                                                        group_name):
    return client.get(resource_group_name=resource_group_name,
                      workspace_name=workspace_name,
                      group_name=group_name)

