# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


from .. import try_manual


# EXAMPLE: /DicomServices/put/Create or update a Dicom Service
@try_manual
def step_workspace_dicom_service_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace dicom-service create '
             '--name "{myDicomService}" '
             '--location "westus" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=[])
    test.cmd('az healthcareapis workspace dicom-service wait --created '
             '--name "{myDicomService}" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /DicomServices/get/Get a dicomservice
@try_manual
def step_workspace_dicom_service_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace dicom-service show '
             '--name "{myDicomService}" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /DicomServices/get/List dicomservices
@try_manual
def step_workspace_dicom_service_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace dicom-service list '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /DicomServices/patch/Update a dicomservice
@try_manual
def step_workspace_dicom_service_update(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace dicom-service update '
             '--name "{myDicomService}" '
             '--tags tagKey="tagValue" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /DicomServices/delete/Delete a dicomservice
@try_manual
def step_workspace_dicom_service_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace dicom-service delete -y '
             '--name "{myDicomService}" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /FhirServices/put/Create or update a Fhir Service
@try_manual
def step_workspace_fhir_service_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace fhir-service create '
             '--name "{myFhirService2}" '
             '--type "SystemAssigned" '
             '--kind "fhir-R4" '
             '--location "westus" '
             '--access-policies object-id="c487e7d1-3210-41a3-8ccc-e9372b78da47" '
             '--access-policies object-id="5b307da8-43d4-492b-8b66-b0294ade872f" '
             '--login-servers "test1.azurecr.io" '
             '--authentication-configuration audience="https://azurehealthcareapis.com" authority="https://login.micros'
             'oftonline.com/abfde7b2-df0f-47e6-aabf-2462b07508dc" smart-proxy-enabled=true '
             '--cors-configuration allow-credentials=false headers="*" max-age=1440 methods="DELETE" methods="GET" '
             'methods="OPTIONS" methods="PATCH" methods="POST" methods="PUT" origins="*" '
             '--storage-account-name "{sa}" '
             '--tags additionalProp1="string" additionalProp2="string" additionalProp3="string" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=[])
    test.cmd('az healthcareapis workspace fhir-service wait --created '
             '--name "{myFhirService2}" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /FhirServices/get/Get a Fhir Service
@try_manual
def step_workspace_fhir_service_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace fhir-service show '
             '--name "{myFhirService}" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /FhirServices/get/List fhirservices
@try_manual
def step_workspace_fhir_service_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace fhir-service list '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /FhirServices/patch/Update a Fhir Service
@try_manual
def step_workspace_fhir_service_update(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace fhir-service update '
             '--name "{myFhirService2}" '
             '--tags tagKey="tagValue" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /FhirServices/delete/Delete a Fhir Service
@try_manual
def step_workspace_fhir_service_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace fhir-service delete -y '
             '--name "{myFhirService2}" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /IotConnectors/put/Create an IoT Connector
@try_manual
def step_workspace_iot_connector_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace iot-connector create '
             '--type "SystemAssigned" '
             '--location "westus" '
             '--content "{{\\"template\\":[{{\\"template\\":{{\\"deviceIdExpression\\":\\"$.deviceid\\",\\"timestampExp'
             'ression\\":\\"$.measurementdatetime\\",\\"typeMatchExpression\\":\\"$..[?(@heartrate)]\\",\\"typeName\\":'
             '\\"heartrate\\",\\"values\\":[{{\\"required\\":\\"true\\",\\"valueExpression\\":\\"$.heartrate\\",\\"valu'
             'eName\\":\\"hr\\"}}]}},\\"templateType\\":\\"JsonPathContent\\"}}],\\"templateType\\":\\"CollectionConten'
             't\\"}}" '
             '--ingestion-endpoint-configuration consumer-group="ConsumerGroupA" event-hub-name="MyEventHubName" '
             'fully-qualified-event-hub-namespace="myeventhub.servicesbus.windows.net" '
             '--tags additionalProp1="string" additionalProp2="string" additionalProp3="string" '
             '--name "{myIotConnector}" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=[])
    test.cmd('az healthcareapis workspace iot-connector wait --created '
             '--name "{myIotConnector}" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /IotConnectors/get/Get an IoT Connector
@try_manual
def step_workspace_iot_connector_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace iot-connector show '
             '--name "{myIotConnector}" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /IotConnectors/get/List iotconnectors
@try_manual
def step_workspace_iot_connector_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace iot-connector list '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /IotConnectors/patch/Patch an IoT Connector
@try_manual
def step_workspace_iot_connector_update(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace iot-connector update '
             '--name "{myIotConnector}" '
             '--type "SystemAssigned" '
             '--tags additionalProp1="string" additionalProp2="string" additionalProp3="string" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /FhirDestinations/get/List IoT Connectors
@try_manual
def step_workspace_iot_connector_fhir_destination_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace iot-connector fhir-destination list '
             '--iot-connector-name "{myIotConnector}" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /IotConnectorFhirDestination/put/Create or update an Iot Connector FHIR destination
@try_manual
def step_workspace_iot_connector(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace iot-connector fhir-destination create '
             '--fhir-destination-name "{myFhirDestination}" '
             '--iot-connector-name "{myIotConnector}" '
             '--location "westus" '
             '--content "{{\\"template\\":[{{\\"template\\":{{\\"codes\\":[{{\\"code\\":\\"8867-4\\",\\"display\\":\\"H'
             'eart rate\\",\\"system\\":\\"http://loinc.org\\"}}],\\"periodInterval\\":60,\\"typeName\\":\\"heartrate\\'
             '",\\"value\\":{{\\"defaultPeriod\\":5000,\\"unit\\":\\"count/min\\",\\"valueName\\":\\"hr\\",\\"valueType'
             '\\":\\"SampledData\\"}}}},\\"templateType\\":\\"CodeValueFhir\\"}}],\\"templateType\\":\\"CollectionFhirT'
             'emplate\\"}}" '
             '--fhir-service-resource-id "subscriptions/11111111-2222-3333-4444-555566667777/resourceGroups/myrg/provid'
             'ers/Microsoft.HealthcareApis/workspaces/myworkspace/fhirservices/myfhirservice" '
             '--resource-identity-resolution-type "Create" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /IotConnectorFhirDestination/get/Get an IoT Connector destination
@try_manual
def step_workspace_iot_connector_fhir_destination_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace iot-connector fhir-destination show '
             '--fhir-destination-name "{myFhirDestination}" '
             '--iot-connector-name "{myIotConnector}" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /IotConnectorFhirDestination/delete/Delete an IoT Connector destination
@try_manual
def step_workspace_iot_connector2(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace iot-connector fhir-destination delete -y '
             '--fhir-destination-name "{myFhirDestination}" '
             '--iot-connector-name "{myIotConnector}" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /IotConnectors/delete/Delete an IoT Connector
@try_manual
def step_workspace_iot_connector_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace iot-connector delete -y '
             '--name "{myIotConnector}" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /OperationResults/get/Get operation result
@try_manual
def step_operation_result_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis operation-result show '
             '--location-name "westus" '
             '--operation-result-id "exampleid"',
             checks=checks)


# EXAMPLE: /PrivateEndpointConnections/put/PrivateEndpointConnection_CreateOrUpdate
@try_manual
def step_private_endpoint_connection_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis private-endpoint-connection create '
             '--name "{myPrivateEndpointConnection}" '
             '--private-link-service-connection-state description="Auto-Approved" status="Approved" '
             '--resource-group "{rg}" '
             '--resource-name "service1"',
             checks=checks)


# EXAMPLE: /PrivateEndpointConnections/get/PrivateEndpointConnection_GetConnection
@try_manual
def step_private_endpoint_connection_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis private-endpoint-connection show '
             '--name "{myPrivateEndpointConnection}" '
             '--resource-group "{rg}" '
             '--resource-name "service1"',
             checks=checks)


# EXAMPLE: /PrivateEndpointConnections/get/PrivateEndpointConnection_List
@try_manual
def step_private_endpoint_connection_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis private-endpoint-connection list '
             '--resource-group "{rg}" '
             '--resource-name "service1"',
             checks=checks)


# EXAMPLE: /PrivateEndpointConnections/delete/PrivateEndpointConnections_Delete
@try_manual
def step_private_endpoint_connection_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis private-endpoint-connection delete -y '
             '--name "{myPrivateEndpointConnection}" '
             '--resource-group "{rg}" '
             '--resource-name "service1"',
             checks=checks)


# EXAMPLE: /PrivateLinkResources/get/PrivateLinkResources_Get
@try_manual
def step_private_link_resource_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis private-link-resource show '
             '--group-name "fhir" '
             '--resource-group "{rg}" '
             '--resource-name "service1"',
             checks=checks)


# EXAMPLE: /PrivateLinkResources/get/PrivateLinkResources_ListGroupIds
@try_manual
def step_private_link_resource_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis private-link-resource list '
             '--resource-group "{rg}" '
             '--resource-name "service1"',
             checks=checks)


# EXAMPLE: /Services/put/Create or Update a service with all parameters
@try_manual
def step_service_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis service create '
             '--resource-group "{rg_2}" '
             '--resource-name "service1" '
             '--type "SystemAssigned" '
             '--kind "fhir-R4" '
             '--location "westus2" '
             '--access-policies object-id="c487e7d1-3210-41a3-8ccc-e9372b78da47" '
             '--access-policies object-id="5b307da8-43d4-492b-8b66-b0294ade872f" '
             '--authentication-configuration audience="https://azurehealthcareapis.com" authority="https://login.micros'
             'oftonline.com/abfde7b2-df0f-47e6-aabf-2462b07508dc" smart-proxy-enabled=true '
             '--cors-configuration allow-credentials=false headers="*" max-age=1440 methods="DELETE" methods="GET" '
             'methods="OPTIONS" methods="PATCH" methods="POST" methods="PUT" origins="*" '
             '--cosmos-db-configuration key-vault-key-uri="https://my-vault.vault.azure.net/keys/my-key" '
             'offer-throughput=1000 '
             '--storage-account-name "{sa}" '
             '--private-endpoint-connections "[]" '
             '--public-network-access "Disabled"',
             checks=checks)


# EXAMPLE: /Services/put/Create or Update a service with minimum parameters
@try_manual
def step_service_create2(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis service create '
             '--resource-group "{rg_2}" '
             '--resource-name "service2" '
             '--kind "fhir-R4" '
             '--location "westus2" '
             '--access-policies object-id="c487e7d1-3210-41a3-8ccc-e9372b78da47"',
             checks=checks)


# EXAMPLE: /Services/get/Get metadata
@try_manual
def step_service_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis service show '
             '--resource-group "{rg_2}" '
             '--resource-name "service1"',
             checks=checks)


# EXAMPLE: /Services/get/List all services in resource group
@try_manual
def step_service_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis service list '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Services/get/List all services in subscription
@try_manual
def step_service_list2(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis service list '
             '-g ""',
             checks=checks)


# EXAMPLE: /Services/patch/Patch service
@try_manual
def step_service_update(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis service update '
             '--resource-group "{rg_2}" '
             '--resource-name "service1" '
             '--tags tag1="value1" tag2="value2"',
             checks=checks)


# EXAMPLE: /Services/delete/Delete service
@try_manual
def step_service_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis service delete -y '
             '--resource-group "{rg_2}" '
             '--resource-name "service1"',
             checks=checks)


# EXAMPLE: /Workspaces/put/Create or update a workspace
@try_manual
def step_workspace_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace create '
             '--resource-group "{rg_3}" '
             '--location "westus" '
             '--name "{myWorkspace}"',
             checks=[])
    test.cmd('az healthcareapis workspace wait --created '
             '--resource-group "{rg_3}" '
             '--name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Workspaces/get/Get workspace
@try_manual
def step_workspace_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace show '
             '--resource-group "{rg_3}" '
             '--name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Workspaces/get/Get workspaces by resource group
@try_manual
def step_workspace_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace list '
             '--resource-group "{rg_3}"',
             checks=checks)


# EXAMPLE: /Workspaces/get/Get workspaces by subscription
@try_manual
def step_workspace_list2(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace list '
             '-g ""',
             checks=checks)


# EXAMPLE: /Workspaces/patch/Update a workspace
@try_manual
def step_workspace_update(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace update '
             '--resource-group "{rg_3}" '
             '--name "{myWorkspace}" '
             '--tags tagKey="tagValue"',
             checks=checks)


# EXAMPLE: /WorkspacePrivateEndpointConnections/put/WorkspacePrivateEndpointConnection_CreateOrUpdate
@try_manual
def step_workspace_private_endpoint_connection_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace private-endpoint-connection create '
             '--private-endpoint-connection-name "{myPrivateEndpointConnection}" '
             '--private-link-service-connection-state description="Auto-Approved" status="Approved" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /WorkspacePrivateEndpointConnections/get/WorkspacePrivateEndpointConnection_GetConnection
@try_manual
def step_workspace_private_endpoint_connection_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace private-endpoint-connection show '
             '--private-endpoint-connection-name "{myPrivateEndpointConnection}" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /WorkspacePrivateEndpointConnections/get/WorkspacePrivateEndpointConnection_List
@try_manual
def step_workspace_private_endpoint_connection_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace private-endpoint-connection list '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /WorkspacePrivateEndpointConnections/delete/WorkspacePrivateEndpointConnections_Delete
@try_manual
def step_workspace_private_endpoint_connection_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace private-endpoint-connection delete -y '
             '--private-endpoint-connection-name "{myPrivateEndpointConnection}" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /WorkspacePrivateLinkResources/get/WorkspacePrivateLinkResources_Get
@try_manual
def step_workspace_private_link_resource_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace private-link-resource show '
             '--group-name "healthcareworkspace" '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /WorkspacePrivateLinkResources/get/WorkspacePrivateLinkResources_ListGroupIds
@try_manual
def step_workspace_private_link_resource_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace private-link-resource list '
             '--resource-group "{rg_3}" '
             '--workspace-name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Workspaces/delete/Delete a workspace
@try_manual
def step_workspace_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthcareapis workspace delete -y '
             '--resource-group "{rg_3}" '
             '--name "{myWorkspace}"',
             checks=checks)
