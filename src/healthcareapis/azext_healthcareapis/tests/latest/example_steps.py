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
from knack.log import get_logger

logger = get_logger(__name__)

@try_manual
def step_healthcareapis_acr_add(test):
    test.cmd('az healthcareapis acr add '
             '--resource-group "{rg}" '
             '--resource-name "{service1}" '
             '--login-servers "test1.azurecr.io" ',
             checks=[
                 test.check("properties.acrConfiguration.loginServers[0]", "test1.azurecr.io"),
             ])


@try_manual
def step_healthcareapis_acr_list(test):
    acr_list = test.cmd('az healthcareapis acr list '
             '--resource-group "{rg}" '
             '--resource-name "{service1}" ',
             checks=[]).get_output_in_json()
    assert len(acr_list['loginServers']) == 1


@try_manual
def step_healthcareapis_acr_remove(test):
    test.cmd('az healthcareapis acr remove '
             '--resource-group "{rg}" '
             '--resource-name "{service1}" '
             '--login-servers "test1.azurecr.io" ',
             checks=[
                 test.check("properties.acrConfiguration.loginServers", []),
             ])


@try_manual
def step_healthcareapis_acr_reset(test):
    test.cmd('az healthcareapis acr reset '
             '--resource-group "{rg}" '
             '--resource-name "{service1}" '
             '--login-servers "test1.azurecr.io" ',
             checks=[
                 test.check("properties.acrConfiguration.loginServers[0]", "test1.azurecr.io"),
             ])


@try_manual
def step_healthcareapiscreateminimalparameters(test):
    test.cmd('az healthcareapis service create '
             '--resource-group "{rg}" '
             '--resource-name "{minimalParams}" '
             '--kind "fhir-Stu3" '
             '--location "{testingLocation}" ',
             checks=[
                 test.check("name", "{minimalParams}", case_sensitive=False),
                 test.check("location", "{testingLocation}", case_sensitive=False),
                 test.check("kind", "fhir-Stu3", case_sensitive=False),
                 test.check("properties.authenticationConfiguration.smartProxyEnabled", False),
                 test.check("properties.corsConfiguration.allowCredentials", False),
                 test.check("properties.cosmosDbConfiguration.offerThroughput", 1000),
                 test.check("properties.provisioningState", "Succeeded"),
                 test.check("properties.publicNetworkAccess", "Enabled", case_sensitive=False),
             ])


@try_manual
def step_healthcareapiscreatemaximumparameters(test):
    testFhir = test.cmd('az healthcareapis service create '
                        '--resource-group "{rg}" '
                        '--resource-name "{maximumParams}" '
                        '--identity-type "SystemAssigned" '
                        '--kind "{fhirr4}" '
                        '--location "{testingLocation}" '
                        '--authentication-configuration authority="https://login.microsoftonline.com/6c4a34fb-44bb-4cc7-bf56-9b4e264f1891" audience="https://{maximumParams}.azurehealthcareapis.com" smart-proxy-enabled=false '
                        '--cors-configuration allow-credentials=false headers="*" max-age=1440 methods="DELETE" methods="GET" methods="OPTIONS" methods="PATCH" methods="POST" methods="PUT" origins="*" '
                        '--cosmos-db-configuration offer-throughput=1500 '
                        '--export-configuration-storage-account-name "{sg}" '
                        '--public-network-access "Disabled" ',
                        checks=[
                            test.check("identity.type", "SystemAssigned", case_sensitive=False),
                            test.check("kind", "{fhirr4}"),
                            test.check("location", "{testingLocation}", case_sensitive=False),
                            test.check("name", "{maximumParams}", case_sensitive=False),
                            test.check("properties.authenticationConfiguration.smartProxyEnabled", False),
                            test.check("properties.corsConfiguration.allowCredentials", False),
                            test.check("properties.corsConfiguration.maxAge", 1440),
                            test.check("properties.cosmosDbConfiguration.offerThroughput", 1500),
                            test.check("properties.exportConfiguration.storageAccountName", "{sg}",
                                       case_sensitive=False),
                            test.check("properties.provisioningState", "Succeeded"),
                            test.check("properties.publicNetworkAccess", "Disabled", case_sensitive=False),
                        ]).get_output_in_json()

    corsConfiguration = testFhir['properties']['corsConfiguration']
    assert len(corsConfiguration['headers']) == 1
    assert len(corsConfiguration['origins']) == 1
    assert corsConfiguration['headers'][0] == "*"
    assert corsConfiguration['origins'][0] == "*"
    assert len(corsConfiguration['methods']) == 6
    assert "DELETE" in corsConfiguration['methods']
    assert "GET" in corsConfiguration['methods']
    assert "OPTIONS" in corsConfiguration['methods']
    assert "PATCH" in corsConfiguration['methods']
    assert "POST" in corsConfiguration['methods']
    assert "PUT" in corsConfiguration['methods']


@try_manual
def step_healthcareapisupdatemaximumparameters(test):
    testFhir = test.cmd('az healthcareapis service create '
                        '--resource-group "{rg}" '
                        '--resource-name "{maximumParams}" '
                        '--identity-type "None" '
                        '--kind "{fhirr4}" '
                        '--location "{testingLocation}" ',
                        checks=[
                            test.check("identity.type", "None", case_sensitive=False),
                            test.check("kind", "{fhirr4}"),
                            test.check("location", "{testingLocation}", case_sensitive=False),
                            test.check("name", "{maximumParams}", case_sensitive=False),
                            test.check("properties.authenticationConfiguration.smartProxyEnabled", False),
                            test.check("properties.corsConfiguration.allowCredentials", False),
                            test.check("properties.corsConfiguration.maxAge", None),
                            test.check("properties.cosmosDbConfiguration.offerThroughput", 1000),
                            test.check("properties.exportConfiguration.storageAccountName", None),
                            test.check("properties.provisioningState", "Succeeded"),
                            test.check("properties.publicNetworkAccess", "Enabled", case_sensitive=False),
                            test.check("properties.secondaryLocations", None),
                        ]).get_output_in_json()

    corsConfiguration = testFhir['properties']['corsConfiguration']
    assert len(corsConfiguration['headers']) == 0
    assert len(corsConfiguration['origins']) == 0
    assert len(corsConfiguration['methods']) == 0

    accessPolicies = testFhir['properties']['accessPolicies']
    assert len(accessPolicies) == 0

    privateEndpointConnections = testFhir['properties']['accessPolicies']
    assert len(privateEndpointConnections) == 0

    acrConfiguration = testFhir['properties']['acrConfiguration']['loginServers']
    assert len(acrConfiguration) == 0

    testFhir = test.cmd('az healthcareapis service create '
                        '--resource-group "{rg}" '
                        '--resource-name "{maximumParams}" '
                        '--public-network-access "Disabled" '
                        '--kind "{fhirr4}" '
                        '--location "{testingLocation}" ',
                        checks=[
                            test.check("identity.type", "None", case_sensitive=False),
                            test.check("kind", "{fhirr4}"),
                            test.check("location", "{testingLocation}", case_sensitive=False),
                            test.check("name", "{maximumParams}", case_sensitive=False),
                            test.check("properties.authenticationConfiguration.smartProxyEnabled", False),
                            test.check("properties.corsConfiguration.allowCredentials", False),
                            test.check("properties.corsConfiguration.maxAge", None),
                            test.check("properties.cosmosDbConfiguration.offerThroughput", 1000),
                            test.check("properties.exportConfiguration.storageAccountName", None),
                            test.check("properties.provisioningState", "Succeeded"),
                            test.check("properties.publicNetworkAccess", "Disabled", case_sensitive=False),
                            test.check("properties.secondaryLocations", None),
                        ]).get_output_in_json()

    corsConfiguration = testFhir['properties']['corsConfiguration']
    assert len(corsConfiguration['headers']) == 0
    assert len(corsConfiguration['origins']) == 0
    assert len(corsConfiguration['methods']) == 0

    accessPolicies = testFhir['properties']['accessPolicies']
    assert len(accessPolicies) == 0

    privateEndpointConnections = testFhir['properties']['accessPolicies']
    assert len(privateEndpointConnections) == 0

    acrConfiguration = testFhir['properties']['acrConfiguration']['loginServers']
    assert len(acrConfiguration) == 0


@try_manual
def step_servicedelete(test):
    test.cmd('az healthcareapis service delete '
             '--resource-group "{rg}" '
             '--resource-name "{minimalParams}" '
             '--yes ',
             checks=[])
    test.cmd('az healthcareapis service delete '
             '--resource-group "{rg}" '
             '--resource-name "{maximumParams}" '
             '--yes ',
             checks=[])


# EXAMPLE: /DicomServices/put/Create or update a Dicom Service
@try_manual
def step_workspace_dicom_service_create(test):
    test.cmd('az healthcareapis workspace dicom-service create '
             '--name "{myDicomService}" '
             '--location "westus2" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[
                 test.check("provisioningState", "Succeeded", case_sensitive=False),
                 test.check("location", "westus2", case_sensitive=False),
             ])
    test.cmd('az healthcareapis workspace dicom-service wait --created '
             '--name "{myDicomService}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[])


# EXAMPLE: /DicomServices/get/Get a dicomservice
@try_manual
def step_workspace_dicom_service_show(test):
    test.cmd('az healthcareapis workspace dicom-service show '
             '--name "{myDicomService}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[
                 test.check("provisioningState", "Succeeded", case_sensitive=False),
             ])


# EXAMPLE: /DicomServices/get/List dicomservices
@try_manual
def step_workspace_dicom_service_list(test):
    dicom_list = test.cmd('az healthcareapis workspace dicom-service list '
                          '--resource-group "{rg}" '
                          '--workspace-name "{myWorkspace}"',
                          checks=[]).get_output_in_json()
    assert len(dicom_list) == 1


# EXAMPLE: /DicomServices/patch/Update a dicomservice
@try_manual
def step_workspace_dicom_service_update(test):
    test.cmd('az healthcareapis workspace dicom-service update '
             '--name "{myDicomService}" '
             '--tags tagKey="tagValue" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[
                 test.check("tags.tagKey", "tagValue", case_sensitive=False),
             ])


# EXAMPLE: /DicomServices/delete/Delete a dicomservice
@try_manual
def step_workspace_dicom_service_delete(test):
    test.cmd('az healthcareapis workspace dicom-service delete -y '
             '--name "{myDicomService}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[])


# EXAMPLE: /FhirServices/put/Create or update a Fhir Service
@try_manual
def step_workspace_fhir_service_create(test):
    ref = test.cmd('az healthcareapis workspace fhir-service create '
             '--name "{myFhirService2}" '
             '--identity-type "SystemAssigned" '
             '--kind "fhir-R4" '
             '--location "westus2" '
             '--authentication-configuration audience="https://azurehealthcareapis.com" authority="https://login.micros'
             'oftonline.com/abfde7b2-df0f-47e6-aabf-2462b07508dc" smart-proxy-enabled=true '
             '--cors-configuration allow-credentials=false headers="*" max-age=1440 methods="DELETE" methods="GET" '
             'methods="OPTIONS" methods="PATCH" methods="POST" methods="PUT" origins="*" '
             '--export-configuration-storage-account-name "{sg}" '
             '--tags additionalProp1="string" additionalProp2="string" additionalProp3="string" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[
                 test.check("identity.type", "SystemAssigned", case_sensitive=False),
                 test.check("kind", "fhir-R4"),
                 test.check("location", "westus2", case_sensitive=False),
                 test.check("authenticationConfiguration.smartProxyEnabled", True),
                 test.check("corsConfiguration.allowCredentials", False),
                 test.check("corsConfiguration.maxAge", 1440),
                 test.check("exportConfiguration.storageAccountName", "{sg}",
                            case_sensitive=False),
                 test.check("provisioningState", "Succeeded"),
                 test.check("publicNetworkAccess", "Enabled", case_sensitive=False),
             ])
    return ref


# EXAMPLE: /FhirServices/get/Get a Fhir Service
@try_manual
def step_workspace_fhir_service_show(test):
    test.cmd('az healthcareapis workspace fhir-service show '
             '--name "{myFhirService2}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[
                 test.check("provisioningState", "Succeeded"),
             ])


# EXAMPLE: /FhirServices/get/List fhirservices
@try_manual
def step_workspace_fhir_service_list(test):
    fhir_list = test.cmd('az healthcareapis workspace fhir-service list '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[]).get_output_in_json()
    assert len(fhir_list) == 1


# EXAMPLE: /FhirServices/patch/Update a Fhir Service
@try_manual
def step_workspace_fhir_service_update(test):
    test.cmd('az healthcareapis workspace fhir-service update '
             '--name "{myFhirService2}" '
             '--tags tagKey="tagValue" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[
                 test.check("provisioningState", "Succeeded"),
             ])


# EXAMPLE: /FhirServices/delete/Delete a Fhir Service
@try_manual
def step_workspace_fhir_service_delete(test):
    test.cmd('az healthcareapis workspace fhir-service delete -y '
             '--name "{myFhirService2}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[])


# EXAMPLE: /IotConnectors/put/Create an IoT Connector
@try_manual
def step_workspace_iot_connector_create(test):
    # Message: The deviceMapping property cannot be null or empty. (--content) TODO
    test.cmd('az healthcareapis workspace iot-connector create '
             '--identity-type "SystemAssigned" '
             '--location "westus2" '
             '--content "{{\\"template\\":[{{\\"template\\":{{\\"deviceIdExpression\\":\\"$.deviceid\\",\\"timestampExp'
             'ression\\":\\"$.measurementdatetime\\",\\"typeMatchExpression\\":\\"$..[?(@heartrate)]\\",\\"typeName\\":'
             '\\"heartrate\\",\\"values\\":[{{\\"required\\":\\"true\\",\\"valueExpression\\":\\"$.heartrate\\",\\"valu'
             'eName\\":\\"hr\\"}}]}},\\"templateType\\":\\"JsonPathContent\\"}}],\\"templateType\\":\\"CollectionConten'
             't\\"}}" '
             '--ingestion-endpoint-configuration consumer-group="ConsumerGroupA" event-hub-name="MyEventHubName" '
             'fully-qualified-event-hub-namespace="myeventhub.servicesbus.windows.net" '
             '--tags additionalProp1="string" additionalProp2="string" additionalProp3="string" '
             '--name "{myIotConnector}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[
                 test.check("identity.type", "SystemAssigned", case_sensitive=False),
                 test.check("location", "westus2", case_sensitive=False),
                 test.check("tags.additionalProp1", "string"),
                 test.check("provisioningState", "Succeeded"),
             ])
    test.cmd('az healthcareapis workspace iot-connector wait --created '
             '--name "{myIotConnector}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[])


# EXAMPLE: /IotConnectors/get/Get an IoT Connector
@try_manual
def step_workspace_iot_connector_show(test):
    test.cmd('az healthcareapis workspace iot-connector show '
             '--name "{myIotConnector}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[
                 test.check("provisioningState", "Succeeded"),
             ])


# EXAMPLE: /IotConnectors/get/List iotconnectors
@try_manual
def step_workspace_iot_connector_list(test):
    iot_list = test.cmd('az healthcareapis workspace iot-connector list '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[]).get_output_in_json()
    len(iot_list) == 1


# EXAMPLE: /IotConnectors/patch/Patch an IoT Connector
@try_manual
def step_workspace_iot_connector_update(test):
    test.cmd('az healthcareapis workspace iot-connector update '
             '--name "{myIotConnector}" '
             '--identity-type "SystemAssigned" '
             '--tags additionalProp1="string" additionalProp2="string" additionalProp3="string" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[
                 test.check("provisioningState", "Succeeded"),
             ])


# EXAMPLE: /IotConnectorFhirDestination/put/Create or update an Iot Connector FHIR destination
@try_manual
def step_workspace_iot_connector_fhir_destination_create(test):
    test.cmd('az healthcareapis workspace iot-connector fhir-destination create '
             '--fhir-destination-name "{myFhirDestination}" '
             '--iot-connector-name "{myIotConnector}" '
             '--location "westus2" '
             '--content "{{\\"template\\":[{{\\"template\\":{{\\"codes\\":[{{\\"code\\":\\"8867-4\\",\\"display\\":\\"H'
             'eart rate\\",\\"system\\":\\"http://loinc.org\\"}}],\\"periodInterval\\":60,\\"typeName\\":\\"heartrate\\'
             '",\\"value\\":{{\\"defaultPeriod\\":5000,\\"unit\\":\\"count/min\\",\\"valueName\\":\\"hr\\",\\"valueType'
             '\\":\\"SampledData\\"}}}},\\"templateType\\":\\"CodeValueFhir\\"}}],\\"templateType\\":\\"CollectionFhirT'
             'emplate\\"}}" '
             '--fhir-service-resource-id "{myFhirResourceID}" '
             '--resource-identity-resolution-type "Create" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[
                 test.check("location", "westus2", case_sensitive=False),
                 test.check("provisioningState", "Succeeded"),
                 test.check("resourceIdentityResolutionType", "Create"),
             ])


# EXAMPLE: /FhirDestinations/get/List IoT Connectors
@try_manual
def step_workspace_iot_connector_fhir_destination_list(test):
    destination_list = test.cmd('az healthcareapis workspace iot-connector fhir-destination list '
             '--iot-connector-name "{myIotConnector}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[]).get_output_in_json()
    len(destination_list) == 1


# EXAMPLE: /IotConnectorFhirDestination/get/Get an IoT Connector destination
@try_manual
def step_workspace_iot_connector_fhir_destination_show(test):
    test.cmd('az healthcareapis workspace iot-connector fhir-destination show '
             '--fhir-destination-name "{myFhirDestination}" '
             '--iot-connector-name "{myIotConnector}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[
                 test.check("provisioningState", "Succeeded"),
             ])


# EXAMPLE: /IotConnectorFhirDestination/delete/Delete an IoT Connector destination
@try_manual
def step_workspace_iot_connector_fhir_destination_delete(test):
    test.cmd('az healthcareapis workspace iot-connector fhir-destination delete -y '
             '--fhir-destination-name "{myFhirDestination}" '
             '--iot-connector-name "{myIotConnector}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[])


# EXAMPLE: /IotConnectors/delete/Delete an IoT Connector
@try_manual
def step_workspace_iot_connector_delete(test):
    test.cmd('az healthcareapis workspace iot-connector delete -y '
             '--name "{myIotConnector}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[])


# EXAMPLE: /OperationResults/get/Get operation result
@try_manual
def step_operation_result_show(test):
    test.cmd('az healthcareapis operation-result show '
             '--location-name "westus2" '
             '--operation-result-id "{operation_result_id}"',
             checks=[])


# EXAMPLE: /PrivateEndpointConnections/put/PrivateEndpointConnection_CreateOrUpdate
@try_manual
def step_private_endpoint_connection_create(test):
    test.cmd('az healthcareapis private-endpoint-connection create '
             '--name "{myPrivateEndpointConnection}" '
             '--private-link-service-connection-state description="Auto-Approved" status="Approved" '
             '--resource-group "{rg}" '
             '--resource-name "{service1}"',
             checks=[])


# EXAMPLE: /PrivateEndpointConnections/get/PrivateEndpointConnection_GetConnection
@try_manual
def step_private_endpoint_connection_show(test):
    test.cmd('az healthcareapis private-endpoint-connection show '
             '--name "{myPrivateEndpointConnection}" '
             '--resource-group "{rg}" '
             '--resource-name "{service1}"',
             checks=[])


# EXAMPLE: /PrivateEndpointConnections/get/PrivateEndpointConnection_List
@try_manual
def step_private_endpoint_connection_list(test):
    test.cmd('az healthcareapis private-endpoint-connection list '
             '--resource-group "{rg}" '
             '--resource-name "{service1}"',
             checks=[])


# EXAMPLE: /PrivateEndpointConnections/delete/PrivateEndpointConnections_Delete
@try_manual
def step_private_endpoint_connection_delete(test):
    test.cmd('az healthcareapis private-endpoint-connection delete -y '
             '--name "{myPrivateEndpointConnection}" '
             '--resource-group "{rg}" '
             '--resource-name "{service1}"',
             checks=[])


# EXAMPLE: /PrivateLinkResources/get/PrivateLinkResources_Get
@try_manual
def step_private_link_resource_show(test):

    test.cmd('az healthcareapis private-link-resource show '
             '--group-name "fhir" '
             '--resource-group "{rg}" '
             '--resource-name "{service1}"',
             checks=[])


# EXAMPLE: /PrivateLinkResources/get/PrivateLinkResources_ListGroupIds
@try_manual
def step_private_link_resource_list(test):

    test.cmd('az healthcareapis private-link-resource list '
             '--resource-group "{rg}" '
             '--resource-name "{service1}"',
             checks=[])


# EXAMPLE: /Services/put/Create or Update a service with all parameters
@try_manual
def step_service_create(test):
    ref = test.cmd('az healthcareapis service create '
             '--resource-group "{rg}" '
             '--resource-name "{service1}" '
             '--kind "fhir-Stu3" '
             '--location "westus2" ',
             checks=[
                 test.check("name", "{service1}", case_sensitive=False),
                 test.check("location", "westus2", case_sensitive=False),
                 test.check("kind", "fhir-Stu3", case_sensitive=False),
             ])
    return ref


# EXAMPLE: /Services/put/Create or Update a service with minimum parameters
@try_manual
def step_service_create2(test):
    test.cmd('az healthcareapis service create '
             '--resource-group "{rg}" '
             '--resource-name "{service2}" '
             '--kind "fhir-R4" '
             '--location "westus2" '
             '--access-policies object-id="c487e7d1-3210-41a3-8ccc-e9372b78da47"',
             checks=[
                 test.check("name", "{service2}", case_sensitive=False),
                 test.check("location", "westus2", case_sensitive=False),
                 test.check("kind", "fhir-R4", case_sensitive=False),
             ])


# EXAMPLE: /Services/get/Get metadata
@try_manual
def step_service_show(test):
    test.cmd('az healthcareapis service show '
             '--resource-group "{rg}" '
             '--resource-name "{service1}"',
             checks=[
                 test.check("name", "{service1}", case_sensitive=False),
             ])


# EXAMPLE: /Services/get/List all services in resource group
@try_manual
def step_service_list(test):
    service_list = test.cmd('az healthcareapis service list '
             '--resource-group "{rg}"',
             checks=[]).get_output_in_json()
    assert len(service_list) == 2


# EXAMPLE: /Services/get/List all services in subscription
@try_manual
def step_service_list2(test):
    service_list = test.cmd('az healthcareapis service list '
             '-g ""',
             checks=[]).get_output_in_json()
    assert len(service_list) >= 2

# EXAMPLE: /Services/patch/Patch service
@try_manual
def step_service_update(test):
    test.cmd('az healthcareapis service update '
             '--resource-group "{rg}" '
             '--resource-name "{service1}" '
             '--tags tag1="value1" tag2="value2"',
             checks=[
                 test.check("tags.tag1", "value1", case_sensitive=False),
             ])


# EXAMPLE: /Services/delete/Delete service
@try_manual
def step_service_delete(test):
    test.cmd('az healthcareapis service delete -y '
             '--resource-group "{rg}" '
             '--resource-name "{service1}"',
             checks=[])


# EXAMPLE: /Workspaces/put/Create or update a workspace
@try_manual
def step_workspace_create(test):
    test.cmd('az healthcareapis workspace create '
             '--resource-group "{rg}" '
             '--location "westus2" '
             '--name "{myWorkspace}"',
             checks=[
                 test.check("name", "{myWorkspace}", case_sensitive=False),
                 test.check("location", "westus2", case_sensitive=False),
             ])
    test.cmd('az healthcareapis workspace wait --created '
             '--resource-group "{rg}" '
             '--name "{myWorkspace}"',
             checks=[])


# EXAMPLE: /Workspaces/get/Get workspace
@try_manual
def step_workspace_show(test):
    test.cmd('az healthcareapis workspace show '
             '--resource-group "{rg}" '
             '--name "{myWorkspace}"',
             checks=[
                 test.check("name", "{myWorkspace}", case_sensitive=False),
             ])


# EXAMPLE: /Workspaces/get/Get workspaces by resource group
@try_manual
def step_workspace_list(test):
    workspace_list = test.cmd('az healthcareapis workspace list '
             '--resource-group "{rg}"',
             checks=[]).get_output_in_json()
    len(workspace_list) == 1


# EXAMPLE: /Workspaces/get/Get workspaces by subscription
@try_manual
def step_workspace_list2(test):
    workspace_list = test.cmd('az healthcareapis workspace list '
             '-g ""',
             checks=[]).get_output_in_json()
    len(workspace_list) >= 1


# EXAMPLE: /Workspaces/patch/Update a workspace
@try_manual
def step_workspace_update(test):
    test.cmd('az healthcareapis workspace update '
             '--resource-group "{rg}" '
             '--name "{myWorkspace}" '
             '--tags tagKey="tagValue"',
             checks=[
                 test.check("name", "{myWorkspace}", case_sensitive=False),
                 test.check("tags.tagKey", "tagValue"),
             ])


# EXAMPLE: /WorkspacePrivateEndpointConnections/put/WorkspacePrivateEndpointConnection_CreateOrUpdate
@try_manual
def step_workspace_private_endpoint_connection_create(test):
    test.cmd('az healthcareapis workspace private-endpoint-connection create '
             '--private-endpoint-connection-name "{myPrivateEndpointConnection}" '
             '--private-link-service-connection-state description="Auto-Approved" status="Approved" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[])


# EXAMPLE: /WorkspacePrivateEndpointConnections/get/WorkspacePrivateEndpointConnection_GetConnection
@try_manual
def step_workspace_private_endpoint_connection_show(test):
    test.cmd('az healthcareapis workspace private-endpoint-connection show '
             '--private-endpoint-connection-name "{myPrivateEndpointConnection}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[])


# EXAMPLE: /WorkspacePrivateEndpointConnections/get/WorkspacePrivateEndpointConnection_List
@try_manual
def step_workspace_private_endpoint_connection_list(test):
    test.cmd('az healthcareapis workspace private-endpoint-connection list '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[])


# EXAMPLE: /WorkspacePrivateEndpointConnections/delete/WorkspacePrivateEndpointConnections_Delete
@try_manual
def step_workspace_private_endpoint_connection_delete(test):
    test.cmd('az healthcareapis workspace private-endpoint-connection delete -y '
             '--private-endpoint-connection-name "{myPrivateEndpointConnection}" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[])


# EXAMPLE: /WorkspacePrivateLinkResources/get/WorkspacePrivateLinkResources_Get
@try_manual
def step_workspace_private_link_resource_show(test):
    test.cmd('az healthcareapis workspace private-link-resource show '
             '--group-name "healthcareworkspace" '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[])


# EXAMPLE: /WorkspacePrivateLinkResources/get/WorkspacePrivateLinkResources_ListGroupIds
@try_manual
def step_workspace_private_link_resource_list(test):
    test.cmd('az healthcareapis workspace private-link-resource list '
             '--resource-group "{rg}" '
             '--workspace-name "{myWorkspace}"',
             checks=[])


# EXAMPLE: /Workspaces/delete/Delete a workspace
@try_manual
def step_workspace_delete(test):
    test.cmd('az healthcareapis workspace delete -y '
             '--resource-group "{rg}" '
             '--name "{myWorkspace}"',
             checks=[])
