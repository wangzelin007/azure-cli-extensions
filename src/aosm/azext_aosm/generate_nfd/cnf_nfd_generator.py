# --------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved. Licensed under the MIT
# License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------
"""Contains a class for generating VNF NFDs and associated resources."""
import json
import os
import re
import shutil
import subprocess
import tarfile
from typing import Dict, List, Any, Tuple, Optional

import yaml
from azext_aosm.generate_nfd.nfd_generator_base import NFDGenerator
from knack.log import get_logger
from azext_aosm._configuration import CNFConfiguration, HelmPackageConfig
from azext_aosm.util.constants import CNF_DEFINITION_BICEP_SOURCE_TEMPLATE

logger = get_logger(__name__)


class CnfNfdGenerator(NFDGenerator):
    """
    _summary_

    :param NFDGenerator: _description_
    :type NFDGenerator: _type_
    """

    def __init__(self, config: CNFConfiguration):
        super(NFDGenerator, self).__init__()
        self.config = config
        self.bicep_template_name = CNF_DEFINITION_BICEP_SOURCE_TEMPLATE
        self.output_folder_name = self.config.build_output_folder_name
        self.tmp_folder_name = "tmp"

        self.artifacts = []
        self.nf_applications = []
        # JORDAN: need to add the bit to schema before properties?
        self.deployment_parameter_schema = {}

        self._bicep_path = os.path.join(
            self.output_folder_name, self.bicep_template_name
        )

    def generate_nfd(self):
        """Generate a VNF NFD which comprises an group, an Artifact Manifest and a NFDV."""
        # Create tmp folder.
        os.mkdir(self.tmp_folder_name)

        if self.bicep_path:
            print(f"Using the existing NFD bicep template {self.bicep_path}.")
            print(
                f"To generate a new NFD, delete the folder {os.path.dirname(self.bicep_path)} and re-run this command."
            )
        else:
            for helm_package in self.config.helm_packages:
                # Unpack the chart into the tmp folder
                helm_package = HelmPackageConfig(**helm_package)
                self._extract_chart(helm_package.path_to_chart)
                # Validate chartz
                
                # Get schema for each chart (extract mappings and take the schema bits we need from values.schema.json)
                # + Add that schema to the big schema.
                self.deployment_parameter_schema["properties"] = self.get_chart_mapping_schema(helm_package)

                # generate the NF application for the chart
                self.nf_applications.append(self.generate_nf_application(helm_package))
                # Workout the list of artifacts for the chart
                self.artifacts += self.get_artifact_list(helm_package)
                
                with open('artifacts.json', 'w') as file:
                    json.dump(self.artifacts, file, indent=4)
                
            # Write NFD bicep
            #' JRODAN: this needs to return the name of the file? so we can copy or we can just search for .bicep
            nfd_bicep_file = self.write_nfd_bicep_file()
            # Write schema to schema/deploymentParameterSchema.json
            # Write Artifact Mainfest bicep

            # Copy contents of tmp folder to output folder.
            #JORDAN: check what files we def want: bicep, schema and mappings (deployParams and configMappings folders)
            if not os.path.exists('output'):
                os.mkdir('output')
            nfd_bicep_path = os.path.join(self.tmp_folder_name,(nfd_bicep_file + '.bicep') )
            print(nfd_bicep_path)
            shutil.copy(nfd_bicep_path, 'output')
            
        # Delete tmp folder
        shutil.rmtree(self.tmp_folder_name)

    @property
    def bicep_path(self) -> Optional[str]:
        """Returns the path to the bicep file for the NFD if it has been created."""
        if os.path.exists(self._bicep_path):
            return self._bicep_path

        return None

    def _extract_chart(self, fname: str) -> None:
        """
        Extract the chart into the tmp folder.

        :param helm_package: The helm package to extract.
        :type helm_package: HelmPackageConfig
        """
        print("fname", fname)
        if fname.endswith("tar.gz") or fname.endswith("tgz"):
            tar = tarfile.open(fname, "r:gz")
            tar.extractall(path=self.tmp_folder_name)
            tar.close()
        elif fname.endswith("tar"):
            tar = tarfile.open(fname, "r:")
            tar.extractall(path=self.tmp_folder_name)
            tar.close()
        # JORDAN: avoiding tar extract errors, fix and remove later 
        else:
            shutil.copytree(fname, self.tmp_folder_name, dirs_exist_ok=True)

    def _create_nfd_folder(self) -> None:
        """
        Create the folder for the NFD bicep files.

        :raises RuntimeError: If the user aborts.
        """
        if os.path.exists(self.output_folder_name):
            carry_on = input(
                f"The folder {self.output_folder_name} already exists - delete it and continue? (y/n)"
            )
            if carry_on != "y":
                raise RuntimeError("User aborted!")

            shutil.rmtree(self.output_folder_name)

        logger.info("Create NFD bicep %s", self.output_folder_name)
        os.mkdir(self.output_folder_name)

    def write_nfd_bicep_file(self):
        # This will write the bicep file for the NFD.
        code_dir = os.path.dirname(__file__)
        arm_template_path = os.path.join(code_dir, "templates/cnfdefinition.json")

        with open(arm_template_path, "r", encoding="UTF-8") as f:
            cnf_arm_template_dict = json.load(f)

        cnf_arm_template_dict["resources"][0]["properties"][
            "networkFunctionTemplate"
        ]["networkFunctionApplications"] = self.nf_applications

        self.write_arm_to_bicep(cnf_arm_template_dict, f"{self.tmp_folder_name}/{self.config.nf_name}-nfdv.json")
        
        return f"{self.config.nf_name}-nfdv"
        
    def write_arm_to_bicep(self, arm_template_dict: Dict[Any, Any], arm_file: str):
        with open(arm_file, 'w', encoding="UTF-8") as f:
            print("Writing ARM template to json file.")
            json.dump(arm_template_dict, f, indent=4)
        try:
            cmd = f"az bicep decompile --file {os.path.abspath(arm_file)} --only-show-errors"
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            raise e
        finally:
            os.remove(arm_file)

    def generate_nf_application(
        self, helm_package: HelmPackageConfig
    ) -> Dict[str, Any]:
        (name, version) = self.get_chart_name_and_version(helm_package)
        return {
            "artifactType": "HelmPackage",
            "name": helm_package.name,
            "dependsOnProfile": helm_package.depends_on,
            "artifactProfile": {
                "artifactStore": {
                    "id": "[resourceId('Microsoft.HybridNetwork/publishers/artifactStores', parameters('publisherName'), parameters('acrArtifactStoreName'))]"
                },
                "helmArtifactProfile": {
                    "helmPackageName": name,
                    "helmPackageVersionRange": version,
                    "registryValuesPaths": [
                        "'global.registry.docker.repoPath'"
                    ],
                    "imagePullSecretsValuesPaths": [
                        "'global.registry.docker.imagePullSecrets'"
                    ],
                },
            },
            "deployParametersMappingRuleProfile": {
                "applicationEnablement": "'Enabled'",
                "helmMappingRuleProfile": {
                    "releaseNamespace": name,
                    "releaseName": name,
                    "helmPackageVersion": version,
                    ## will process this after and will remove the "" so it will be valid 
                    "values": f"string(loadJsonContent({self.generate_parmeter_mappings(helm_package)})",
                },
            },
        }

    def get_artifact_list(self, helm_package: HelmPackageConfig) -> List[Any]:
        artifact_list = []
        (chart_name, chart_version) = self.get_chart_name_and_version(helm_package)
        helm_artifact = {
            "artifactName" : chart_name,
            "artifactType" : "OCIArtifact",
            "artifactVersion": chart_version
        }
        artifact_list.append(helm_artifact)
       
        image_versions = {}
        path = os.path.join(self.tmp_folder_name, helm_package.name)

        for root, dirs, files in os.walk(path):
            for filename in files:
                if filename.endswith(".yaml") or filename.endswith(".yml"):
                    image_versions.update(self.find_images(os.path.join(root, filename)))
            
        for image_name,image_version in image_versions.items():
            artifact_list.append({
                "artifactName" : image_name,
                "artifactType" : "OCIArtifact",
                "artifactVersion": image_version
            })
        
        return artifact_list
        
    def find_images(self, filename):
        image_versions = {}
        with open(filename) as f:
            image_matches = [re.search(r"/(.+):(.+)", line) for line in f if "image:" in line ]
        
        for match in image_matches:
            if match and (match.group(1) not in image_versions):
                version = re.sub('[^a-zA-Z0-9]+$', '', match.group(2))
                image_versions[match.group(1)] = version
                
        return image_versions
    
    ## JORDAN: this is done cheating by not actually looking at the schema
    def get_chart_mapping_schema(self, helm_package: HelmPackageConfig) -> Dict[Any, Any]:
        # We need to take the mappings from the values.nondef.yaml file and generate the schema
        # from the values.schema.json file.
        # Basically take the bits of the schema that are relevant to the parameters requested.
        
        non_def_values = os.path.join(self.tmp_folder_name, helm_package.name, "values.nondef.yaml")
        values_schema = os.path.join(self.tmp_folder_name, helm_package.name, "values.schema.json")
        
        with open(non_def_values, 'r') as stream:
            values_data = yaml.load(stream, Loader=yaml.SafeLoader)
        
        with open(values_schema, 'r') as f:
            data = json.load(f)
            schema_data = data["properties"]
        # print(schema_data)
        deploy_params_list = []
        params_for_schema = self.find_deploy_params(values_data, schema_data, deploy_params_list, {})
        
        print("params", params_for_schema)
        schema_dict = {}
        for i in params_for_schema:
            schema_dict[i] = {"type": "string", "description": "no descr"}
   
        return schema_dict

    ## JORDAN: change this to save the key and value that has deployParam in it so we can check the schema for the key
    def find_deploy_params(self, nested_dict, schema_nested_dict, deploy_params_list, dict_path):
        for k,v in nested_dict.items():
            # #reset
            # dict_path = {}
            test = {}
            if isinstance(v, str) and "deployParameters" in v:
                # only add the parameter name (not deployParam. or anything after)
                param = v.split(".",1)[1]
                param = param.split('}', 1)[0]
                # dict_path[k] = param
                ## identify the zone param 
                deploy_params_list.append(param)
                test[k] = param
                print(deploy_params_list)
                print(test)
            elif hasattr(v, 'items'): #v is a dict
                # dict_path[k] = {}
                self.find_deploy_params(v, deploy_params_list, dict_path)
            # print("dict", dict_path)        
        return deploy_params_list
            
    def get_chart_name_and_version(
        self, helm_package: HelmPackageConfig
    ) -> Tuple[str, str]:
        
        chart = os.path.join(self.tmp_folder_name, helm_package.name, "Chart.yaml")
        
        with open(chart) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            chart_name = data["name"]
            chart_version = data["version"]
        
        return (chart_name, chart_version)

    def some_fun_to_check_ragistry_and_image_secret_path(self):
        # Need to work out what we are doing here???
        pass

    def generate_parmeter_mappings(self, helm_package: HelmPackageConfig) -> str:
        # Basically copy the values.nondef.yaml file to the right place.
        values = os.path.join(self.tmp_folder_name, helm_package.name, "values.nondef.yaml")
        
        mappings_folder_path = os.path.join(self.tmp_folder_name, "configMappings")
        mappings_filename = f"{helm_package.name}-mappings.json"
        if not os.path.exists(mappings_folder_path):
            os.mkdir(mappings_folder_path)

        mapping_file_path = os.path.join(mappings_folder_path, mappings_filename)

        with open(values) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        with open(mapping_file_path, 'w') as file:
            json.dump(data, file)

        return os.path.join("configMappings", mappings_filename)