# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
"""Constants used across aosm cli extension."""

# The types of definition that can be generated
VNF = "vnf"
CNF = "cnf"
NSD = "nsd"
SCHEMA = "schema"

# Names of files used in the repo
NF_TEMPLATE_BICEP_FILENAME = "nf_template.bicep"
NF_DEFINITION_BICEP_FILENAME = "nf_definition.bicep"
NF_DEFINITION_JSON_FILENAME = "nf_definition.json"
NF_DEFINITION_OUTPUT_BICEP_PREFIX = "nfd-bicep-"
NSD_SOURCE_TEMPLATE_BICEP_FILENAME = "nsd_template.bicep"
NSD_BICEP_FILENAME = "nsd_definition.bicep"
NSD_OUTPUT_BICEP_PREFIX = "nsd-bicep-templates"
NSD_ARTIFACT_MANIFEST_BICEP_FILENAME = "artifact_manifest.bicep"
NSD_ARTIFACT_MANIFEST_JSON_FILENAME = "artifact_manifest.json"
NSD_CONFIG_MAPPING_FILENAME = "configMappings.json"
NSD_ARTIFACT_MANIFEST_SOURCE_TEMPLATE_FILENAME = "artifact_manifest_template.bicep"

VNF_DEFINITION_BICEP_TEMPLATE_FILENAME = "vnfdefinition.bicep"
VNF_MANIFEST_BICEP_TEMPLATE_FILENAME = "vnfartifactmanifests.bicep"

CNF_DEFINITION_JINJA2_SOURCE_TEMPLATE_FILENAME = "cnfdefinition.bicep.j2"
CNF_MANIFEST_JINJA2_SOURCE_TEMPLATE_FILENAME = "cnfartifactmanifest.bicep.j2"
CNF_DEFINITION_BICEP_TEMPLATE_FILENAME = "cnfdefinition.bicep"
CNF_MANIFEST_BICEP_TEMPLATE_FILENAME = "cnfartifactmanifest.bicep"


# Names of directories used in the repo
CONFIG_MAPPINGS_DIR_NAME = "configMappings"
SCHEMAS_DIR_NAME = "schemas"
TEMPLATES_DIR_NAME = "templates"
GENERATED_VALUES_MAPPINGS_DIR_NAME = "generatedValuesMappings"

# Items used when building NFDs/NSDs
DEPLOYMENT_PARAMETERS_FILENAME = "deploymentParameters.json"
OPTIONAL_DEPLOYMENT_PARAMETERS_FILENAME = "optionalDeploymentParameters.txt"
TEMPLATE_PARAMETERS_FILENAME = "templateParameters.json"
VHD_PARAMETERS_FILENAME = "vhdParameters.json"
OPTIONAL_DEPLOYMENT_PARAMETERS_HEADING = (
    "# The following parameters are optional as they have default values.\n"
    "# If you do not wish to expose them in the NFD, find and remove them from both\n"
    f"# {DEPLOYMENT_PARAMETERS_FILENAME} and {TEMPLATE_PARAMETERS_FILENAME} (and {VHD_PARAMETERS_FILENAME} if\n"
    "they are there)\n"
    "# You can re-run the build command with the --order-params flag to order those\n"
    "# files with the optional parameters at the end of the file, and with the \n"
    "# --interactive flag to interactively choose y/n for each parameter to expose.\n\n"
)

# Deployment Schema
SCHEMA_PREFIX = {
    "$schema": "https://json-schema.org/draft-07/schema#",
    "title": "DeployParametersSchema",
    "type": "object",
    "properties": {},
}

# For CNF NFD Generator
# To match the image path if image: is present in the yaml file
IMAGE_START_STRING = "image:"
IMAGE_PATH_REGEX = r".Values\.([^\s})]*)"

# To match the image name and version if 'imagePullSecrets:' is present in the yaml file
IMAGE_PULL_SECRETS_START_STRING = "imagePullSecrets:"
IMAGE_NAME_AND_VERSION_REGEX = r"\/([^\s]*):([^\s)\"}]*)"

DEPLOYMENT_PARAMETER_MAPPING_REGEX = r"\{deployParameters.(.+?)\}"