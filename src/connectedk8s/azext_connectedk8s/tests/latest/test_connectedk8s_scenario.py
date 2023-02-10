# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest
import json
import requests
import platform
import stat
from knack.util import CLIError
import azext_connectedk8s._constants as consts
import urllib.request
import shutil
from azure.cli.core import get_default_cli
from azure.cli.core.azclierror import ManualInterrupt, InvalidArgumentValueError, UnclassifiedUserFault, CLIInternalError, FileOperationError, ClientRequestError, DeploymentError, ValidationError, ArgumentUsageError, MutuallyExclusiveArgumentError, RequiredArgumentMissingError, ResourceNotFoundError
import subprocess
from subprocess import Popen, PIPE, run, STDOUT, call, DEVNULL

from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer, live_only)  # pylint: disable=import-error

TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


def _get_test_data_file(filename):
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(curr_dir, 'data', filename).replace('\\', '\\\\')


def install_helm_client():
    # Return helm client path set by user
    if os.getenv('HELM_CLIENT_PATH'):
        return os.getenv('HELM_CLIENT_PATH')

    # Fetch system related info
    operating_system = platform.system().lower()
    machine_type = platform.machine()


    # Set helm binary download & install locations
    if(operating_system == 'windows'):
        download_location_string = f'.azure\\helm\\{consts.HELM_VERSION}\\helm-{consts.HELM_VERSION}-{operating_system}-amd64.zip'
        install_location_string = f'.azure\\helm\\{consts.HELM_VERSION}\\{operating_system}-amd64\\helm.exe'
        requestUri = f'{consts.HELM_STORAGE_URL}/helm/helm-{consts.HELM_VERSION}-{operating_system}-amd64.zip'
    elif(operating_system == 'linux' or operating_system == 'darwin'):
        download_location_string = f'.azure/helm/{consts.HELM_VERSION}/helm-{consts.HELM_VERSION}-{operating_system}-amd64.tar.gz'
        install_location_string = f'.azure/helm/{consts.HELM_VERSION}/{operating_system}-amd64/helm'
        requestUri = f'{consts.HELM_STORAGE_URL}/helm/helm-{consts.HELM_VERSION}-{operating_system}-amd64.tar.gz'
    else:
        raise ClientRequestError(f'The {operating_system} platform is not currently supported for installing helm client.')

    download_location = os.path.expanduser(os.path.join('~', download_location_string))
    download_dir = os.path.dirname(download_location)
    install_location = os.path.expanduser(os.path.join('~', install_location_string))

    # Download compressed halm binary if not already present
    if not os.path.isfile(download_location):
        # Creating the helm folder if it doesnt exist
        if not os.path.exists(download_dir):
            try:
                os.makedirs(download_dir)
            except Exception as e:
                raise ClientRequestError("Failed to create helm directory." + str(e))

        # Downloading compressed helm client executable
        try:
            response = urllib.request.urlopen(requestUri)
        except Exception as e:
            raise CLIInternalError("Failed to download helm client.", recommendation="Please check your internet connection." + str(e))

        responseContent = response.read()
        response.close()

        # Creating the compressed helm binaries
        try:
            with open(download_location, 'wb') as f:
                f.write(responseContent)
        except Exception as e:
            raise ClientRequestError("Failed to create helm executable." + str(e), recommendation="Please ensure that you delete the directory '{}' before trying again.".format(download_dir))

    # Extract compressed helm binary
    if not os.path.isfile(install_location):
        try:
            shutil.unpack_archive(download_location, download_dir)
            os.chmod(install_location, os.stat(install_location).st_mode | stat.S_IXUSR)
        except Exception as e:
            raise ClientRequestError("Failed to extract helm executable." + str(e), recommendation="Please ensure that you delete the directory '{}' before trying again.".format(download_dir))

    return install_location


def install_kubectl_client():
    # Return kubectl client path set by user
    try:

        # Fetching the current directory where the cli installs the kubectl executable
        home_dir = os.path.expanduser('~')
        kubectl_filepath = os.path.join(home_dir, '.azure', 'kubectl-client')

        try:
            os.mkdir(kubectl_filepath)
        except FileExistsError:
            pass

        operating_system = platform.system().lower()
        # Setting path depending on the OS being used
        if operating_system == 'windows':
            kubectl_path = os.path.join(kubectl_filepath, 'kubectl.exe')
        elif operating_system == 'linux' or operating_system == 'darwin':
            kubectl_path = os.path.join(kubectl_filepath, 'kubectl')
        else:
            raise ClientRequestError(f'The {operating_system} platform is not currently supported for installing kubectl client.')

        if os.path.isfile(kubectl_path):
            return kubectl_path

        # Downloading kubectl executable if its not present in the machine
        get_default_cli().invoke(['aks', 'install-cli', '--install-location', kubectl_path])
        # Return the path of the kubectl executable
        return kubectl_path

    except Exception as e:
        raise CLIInternalError("Unable to install kubectl. Error: ", str(e))


class Connectedk8sScenarioTest(ScenarioTest):

    @live_only()
    @ResourceGroupPreparer(name_prefix='conk8stest', location='eastus2euap', random_name_length=16)
    def test_connect(self,resource_group):
        
        managed_cluster_name = self.create_random_name(prefix='test-connect', length=24)
        kubeconfig="%s" % (_get_test_data_file(managed_cluster_name + '-config.yaml')) 
        self.kwargs.update({
            'rg': resource_group,
            'name': self.create_random_name(prefix='cc-', length=12),
            'kubeconfig': kubeconfig,
            'managed_cluster_name': managed_cluster_name
        })

        self.cmd('aks create -g {rg} -n {managed_cluster_name} --generate-ssh-keys')
        self.cmd('aks get-credentials -g {rg} -n {managed_cluster_name} -f {kubeconfig}')
        self.cmd('connectedk8s connect -g {rg} -n {name} -l eastus --tags foo=doo --kube-config {kubeconfig} --kube-context {managed_cluster_name}', checks=[
            self.check('tags.foo', 'doo'),
            self.check('resourceGroup', '{rg}'),
            self.check('name', '{name}')
        ])

        self.cmd('connectedk8s delete -g {rg} -n {name} --kube-config {kubeconfig} --kube-context {managed_cluster_name} -y')
        self.cmd('aks delete -g {rg} -n {managed_cluster_name} -y')

        # delete the kube config
        os.remove("%s" % (_get_test_data_file(managed_cluster_name + '-config.yaml')))


    @live_only()
    @ResourceGroupPreparer(name_prefix='conk8stest', location='eastus2euap', random_name_length=16)
    def test_forcedelete(self,resource_group):

        managed_cluster_name = self.create_random_name(prefix='test-force-delete', length=24)
        kubeconfig="%s" % (_get_test_data_file(managed_cluster_name + '-config.yaml')) 
        self.kwargs.update({
            'rg': resource_group,
            'name': self.create_random_name(prefix='cc-', length=12),
            'kubeconfig': kubeconfig,
            # 'kubeconfig': "%s" % (_get_test_data_file(managed_cluster_name + '-config.yaml')),
            'managed_cluster_name': managed_cluster_name
        })

        self.cmd('aks create -g {rg} -n {managed_cluster_name} --generate-ssh-keys')
        self.cmd('aks get-credentials -g {rg} -n {managed_cluster_name} -f {kubeconfig}')
        self.cmd('connectedk8s connect -g {rg} -n {name} -l eastus --tags foo=doo --kube-config {kubeconfig} --kube-context {managed_cluster_name}', checks=[
            self.check('tags.foo', 'doo'),
            self.check('name', '{name}')
        ])
        self.cmd('connectedk8s show -g {rg} -n {name}', checks=[
            self.check('name', '{name}'),
            self.check('resourceGroup', '{rg}'),
            self.check('tags.foo', 'doo')
        ])

        # Simulating the condition in which the azure-arc namespace got deleted
        # connectedk8s delete command fails in this case
        kubectl_client_location = install_kubectl_client()
        subprocess.run([kubectl_client_location, "delete", "namespace", "azure-arc","--kube-config", kubeconfig])

        # Using the force delete command
        # -y to supress the prompts
        self.cmd('connectedk8s delete -g {rg} -n {name} --kube-config {kubeconfig} --kube-context {managed_cluster_name} --force -y')
        self.cmd('aks delete -g {rg} -n {managed_cluster_name} -y')

        # delete the kube config
        os.remove("%s" % (_get_test_data_file(managed_cluster_name + '-config.yaml')))


    @live_only()
    @ResourceGroupPreparer(name_prefix='conk8stest', location='eastus2euap', random_name_length=16)
    def test_enable_disable_features(self,resource_group):

        managed_cluster_name = self.create_random_name(prefix='test-enable-disable', length=24)
        kubeconfig="%s" % (_get_test_data_file(managed_cluster_name + '-config.yaml')) 
        self.kwargs.update({
            'rg': resource_group,
            'name': self.create_random_name(prefix='cc-', length=12),
            'kubeconfig': kubeconfig,
            'managed_cluster_name': managed_cluster_name
        })

        self.cmd('aks create -g {rg} -n {managed_cluster_name} --generate-ssh-keys')
        self.cmd('aks get-credentials -g {rg} -n {managed_cluster_name} -f {kubeconfig}')
        self.cmd('connectedk8s connect -g {rg} -n {name} -l eastus --tags foo=doo --kube-config {kubeconfig} --kube-context {managed_cluster_name}', checks=[
            self.check('tags.foo', 'doo'),
            self.check('name', '{name}')
        ])
        self.cmd('connectedk8s show -g {rg} -n {name}', checks=[
            self.check('name', '{name}'),
            self.check('resourceGroup', '{rg}'),
            self.check('tags.foo', 'doo')
        ])

        os.environ.setdefault('KUBECONFIG', kubeconfig)
        helm_client_location = install_helm_client()
        cmd = [helm_client_location, 'get', 'values', 'azure-arc', "--namespace", "azure-arc-release", "-ojson"]

        # scenario-1 : custom loc off , custom loc on  (no dependencies)
        self.cmd('connectedk8s disable-features -n {name} -g {rg} --features custom-locations --kube-config {kubeconfig} --kube-context {managed_cluster_name} -y')
        cmd_output = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE)
        _, error_helm_delete = cmd_output.communicate()
        assert(cmd_output.returncode == 0)
        changed_cmd = json.loads(cmd_output.communicate()[0].strip())
        assert(changed_cmd["systemDefaultValues"]['customLocations']['enabled'] == bool(0))

        self.cmd('connectedk8s enable-features -n {name} -g {rg} --features custom-locations --kube-config {kubeconfig} --kube-context {managed_cluster_name}')
        cmd_output1 = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE)
        _, error_helm_delete = cmd_output1.communicate()
        assert(cmd_output1.returncode == 0)
        changed_cmd1 = json.loads(cmd_output1.communicate()[0].strip())
        assert(changed_cmd1["systemDefaultValues"]['customLocations']['enabled'] == bool(1))

        # scenario-2 : custom loc on , check if cluster connect gets off that results in an error
        with self.assertRaisesRegexp(CLIError, "Disabling 'cluster-connect' feature is not allowed when 'custom-locations' feature is enabled."):
            self.cmd('connectedk8s disable-features -n {name} -g {rg} --features cluster-connect --kube-config {kubeconfig} --kube-context {managed_cluster_name} -y')

        # scenario-3 : off custom location and cluster connect , then on custom loc and check if cluster connect gets on
        self.cmd('connectedk8s disable-features -n {name} -g {rg} --features custom-locations --kube-config {kubeconfig} --kube-context {managed_cluster_name} -y')
        cmd_output1 = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE)
        _, error_helm_delete = cmd_output1.communicate()
        assert(cmd_output1.returncode == 0)
        changed_cmd1 = json.loads(cmd_output1.communicate()[0].strip())
        assert(changed_cmd1["systemDefaultValues"]['customLocations']['enabled'] == bool(0))

        self.cmd('connectedk8s disable-features -n {name} -g {rg} --features cluster-connect --kube-config {kubeconfig} --kube-context {managed_cluster_name} -y')
        cmd_output1 = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE)
        _, error_helm_delete = cmd_output1.communicate()
        assert(cmd_output1.returncode == 0)
        changed_cmd1 = json.loads(cmd_output1.communicate()[0].strip())
        assert(changed_cmd1["systemDefaultValues"]['clusterconnect-agent']['enabled'] == bool(0))

        self.cmd('connectedk8s enable-features -n {name} -g {rg} --features custom-locations --kube-config {kubeconfig} --kube-context {managed_cluster_name}')
        cmd_output1 = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE)
        _, error_helm_delete = cmd_output1.communicate()
        assert(cmd_output1.returncode == 0)
        changed_cmd1 = json.loads(cmd_output1.communicate()[0].strip())
        assert(changed_cmd1["systemDefaultValues"]['customLocations']['enabled'] == bool(1))
        assert(changed_cmd1["systemDefaultValues"]['clusterconnect-agent']['enabled'] == bool(1))

        # scenario-4: azure rbac off , azure rbac on using app id and app secret
        self.cmd('connectedk8s disable-features -n {name} -g {rg} --features azure-rbac --kube-config {kubeconfig} --kube-context {managed_cluster_name} -y')
        cmd_output1 = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE)
        _, error_helm_delete = cmd_output1.communicate()
        assert(cmd_output1.returncode == 0)
        changed_cmd1 = json.loads(cmd_output1.communicate()[0].strip())
        assert(changed_cmd1["systemDefaultValues"]['guard']['enabled'] == bool(0))

        self.cmd('az connectedk8s enable-features -n {name} -g {rg} --kube-config {kubeconfig} --kube-context {managed_cluster_name} --features azure-rbac --app-id ffba4043-836e-4dcc-906c-fbf60bf54eef --app-secret="6a6ae7a7-4260-40d3-ba00-af909f2ca8f0"')

        # deleting the cluster
        self.cmd('connectedk8s delete -g {rg} -n {name} --kube-config {kubeconfig} --kube-context {managed_cluster_name} -y')
        self.cmd('aks delete -g {rg} -n {managed_cluster_name} -y')

        # delete the kube config
        os.remove("%s" % (_get_test_data_file(managed_cluster_name + '-config.yaml')))


    @live_only()
    @ResourceGroupPreparer(name_prefix='conk8stest', location='eastus2euap', random_name_length=16)
    def test_connectedk8s_list(self,resource_group):

        managed_cluster_name = self.create_random_name(prefix='first', length=24)
        managed_cluster_name_second = self.create_random_name(prefix='second', length=24)
        kubeconfig="%s" % (_get_test_data_file(managed_cluster_name + '-config.yaml')) 
        kubeconfigpls="%s" % (_get_test_data_file('pls-config.yaml'))
        name = self.create_random_name(prefix='cc-', length=12)
        name_second = self.create_random_name(prefix='cc-', length=12)
        managed_cluster_list=[]
        managed_cluster_list.append(name)
        managed_cluster_list.append(name_second)
        managed_cluster_list.sort() 
        self.kwargs.update({
            'rg': resource_group,
            'name': name,
            'name_second': name_second,
            'kubeconfig': kubeconfig,
            'kubeconfigpls': kubeconfigpls,
            'managed_cluster_name': managed_cluster_name,
            'managed_cluster_name_second': managed_cluster_name_second
        })

        self.cmd('aks create -g {rg} -n {managed_cluster_name} --generate-ssh-keys')
        self.cmd('aks get-credentials -g {rg} -n {managed_cluster_name} -f {kubeconfig}')
        self.cmd('connectedk8s connect -g {rg} -n {name} -l eastus --tags foo=doo --kube-config {kubeconfig} --kube-context {managed_cluster_name}', checks=[
            self.check('tags.foo', 'doo'),
            self.check('name', '{name}')
        ])
        self.cmd('connectedk8s show -g {rg} -n {name}', checks=[
            self.check('name', '{name}'),
            self.check('resourceGroup', '{rg}'),
            self.check('tags.foo', 'doo')
        ])

        self.cmd('aks create -g {rg} -n {managed_cluster_name_second} --generate-ssh-keys')
        self.cmd('aks get-credentials -g {rg} -n {managed_cluster_name_second} -f {kubeconfigpls}')
        self.cmd('connectedk8s connect -g {rg} -n {name_second} -l eastus --tags foo=doo --kube-config {kubeconfigpls} --kube-context {managed_cluster_name_second}', checks=[
            self.check('tags.foo', 'doo'),
            self.check('name', '{name_second}')
        ])
        self.cmd('connectedk8s show -g {rg} -n {name_second}', checks=[
            self.check('name', '{name_second}'),
            self.check('resourceGroup', '{rg}'),
            self.check('tags.foo', 'doo')
        ])

        clusters_list = self.cmd('az connectedk8s list -g {rg}').get_output_in_json()
        # fetching names of all clusters
        cluster_name_list=[]
        for clusterdesc in clusters_list:
            cluster_name_list.append(clusterdesc['name'])

        assert(len(cluster_name_list) == len(managed_cluster_list))

        # checking if the output is correct with original list of cluster names
        cluster_name_list.sort()
        for i in range(0,len(cluster_name_list)):
            assert(cluster_name_list[i] == managed_cluster_list[i])

        # deleting the clusters
        # self.cmd('aks get-credentials -g {rg} -n {managed_cluster_name_second} -f {kubeconfigpls}')
        self.cmd('connectedk8s delete -g {rg} -n {name_second} --kube-config {kubeconfigpls} --kube-context {managed_cluster_name_second} -y')
        self.cmd('aks delete -g {rg} -n {managed_cluster_name_second} -y')

        # self.cmd('aks get-credentials -g {rg} -n {managed_cluster_name} -f {kubeconfig}')
        self.cmd('connectedk8s delete -g {rg} -n {name} --kube-config {kubeconfig} --kube-context {managed_cluster_name} -y')
        self.cmd('aks delete -g {rg} -n {managed_cluster_name} -y')

        # delete the kube config
        os.remove("%s" % (_get_test_data_file(managed_cluster_name + '-config.yaml')))
        os.remove("%s" % (_get_test_data_file('pls-config.yaml')))


    @live_only()
    @ResourceGroupPreparer(name_prefix='conk8stest', location='eastus2euap', random_name_length=16)
    def test_upgrade(self,resource_group):

        managed_cluster_name = self.create_random_name(prefix='test-upgrade', length=24)
        kubeconfig="%s" % (_get_test_data_file(managed_cluster_name + '-config.yaml')) 
        self.kwargs.update({
            'name': self.create_random_name(prefix='cc-', length=12),
            'rg': resource_group,
            'kubeconfig': kubeconfig,
            'managed_cluster_name': managed_cluster_name
        })

        self.cmd('aks create -g {rg} -n {managed_cluster_name} --generate-ssh-keys')
        self.cmd('aks get-credentials -g {rg} -n {managed_cluster_name} -f {kubeconfig}')

        self.cmd('connectedk8s connect -g {rg} -n {name} -l eastus --tags foo=doo --kube-config {kubeconfig} --kube-context {managed_cluster_name}', checks=[
            self.check('tags.foo', 'doo'),
            self.check('name', '{name}')
        ])
        self.cmd('connectedk8s show -g {rg} -n {name}', checks=[
            self.check('name', '{name}'),
            self.check('resourceGroup', '{rg}'),
            self.check('tags.foo', 'doo')
        ])

        os.environ.setdefault('KUBECONFIG', kubeconfig)
        helm_client_location = install_helm_client()
        cmd = [helm_client_location, 'get', 'values', 'azure-arc', "--namespace", "azure-arc-release", "-ojson"]

        # scenario - auto-upgrade is true , so implicit upgrade commands dont work
        self.cmd('connectedk8s update -n {name} -g {rg} --auto-upgrade true --kube-config {kubeconfig} --kube-context {managed_cluster_name}')
        cmd_output1 = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE)
        _, error_helm_delete = cmd_output1.communicate()
        assert(cmd_output1.returncode == 0)
        changed_cmd1 = json.loads(cmd_output1.communicate()[0].strip())
        assert(changed_cmd1["systemDefaultValues"]['azureArcAgents']['autoUpdate'] == bool(1))

        with self.assertRaisesRegexp(CLIError, "az connectedk8s upgrade to manually upgrade agents and extensions is only supported when auto-upgrade is set to false"):
            self.cmd('connectedk8s upgrade -g {rg} -n {name} --kube-config {kubeconfig} --kube-context {managed_cluster_name}')

        # scenario - auto upgrade is off , changing agent version to 1.6.19(older) ,then updating version to latest
        self.cmd('connectedk8s update -n {name} -g {rg} --auto-upgrade false --kube-config {kubeconfig} --kube-context {managed_cluster_name}')
        cmd_output1 = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE)
        _, error_helm_delete = cmd_output1.communicate()
        assert(cmd_output1.returncode == 0)
        changed_cmd1 = json.loads(cmd_output1.communicate()[0].strip())
        assert(changed_cmd1["systemDefaultValues"]['azureArcAgents']['autoUpdate'] == bool(0))

        # self.cmd('connectedk8s upgrade -g {rg} -n {name} --kube-config {kubeconfig} --kube-context {managed_cluster_name} --agent-version 1.6.19')
        # self.cmd('connectedk8s show -g {rg} -n {name}', checks=[
        #     self.check('agentVersion', '1.6.19')
        # ])

        self.cmd('connectedk8s upgrade -g {rg} -n {name} --kube-config {kubeconfig} --kube-context {managed_cluster_name}')
        response= requests.post('https://eastus.dp.kubernetesconfiguration.azure.com/azure-arc-k8sagents/GetLatestHelmPackagePath?api-version=2019-11-01-preview&releaseTrain=stable')
        jsonData = json.loads(response.text)
        repo_path=jsonData['repositoryPath']
        index_value = 0
        for ind in range (0,len(repo_path)):
            if  repo_path[ind]==':':
                break
            index_value += 1

        self.cmd('connectedk8s show -g {rg} -n {name}', checks=[
            self.check('agentVersion', jsonData['repositoryPath'][index_value+1:]),
        ])

        # scenario : testing the onboarding timeout change
        self.cmd('connectedk8s upgrade -g {rg} -n {name} --upgrade-timeout 650 --kube-config {kubeconfig} --kube-context {managed_cluster_name}')

        self.cmd('connectedk8s delete -g {rg} -n {name} --kube-config {kubeconfig} --kube-context {managed_cluster_name} -y')
        self.cmd('aks delete -g {rg} -n {managed_cluster_name} -y')

        # delete the kube config
        os.remove("%s" % (_get_test_data_file(managed_cluster_name + '-config.yaml')))


    @live_only()
    @ResourceGroupPreparer(name_prefix='conk8stest', location='eastus2euap', random_name_length=16)
    def test_update(self,resource_group):
        managed_cluster_name = self.create_random_name(prefix='test-update', length=24)
        kubeconfig="%s" % (_get_test_data_file(managed_cluster_name + '-config.yaml')) 
        # kubeconfigpls="%s" % (_get_test_data_file(managed_cluster_name + '-plsconfig.yaml')) 
        self.kwargs.update({
            'name': self.create_random_name(prefix='cc-', length=12),
            'kubeconfig': kubeconfig,
            'rg':resource_group,
            # 'kubeconfigpls': kubeconfigpls,
            'managed_cluster_name': managed_cluster_name
        })

        self.cmd('aks create -g {rg} -n {managed_cluster_name} --generate-ssh-keys')
        self.cmd('aks get-credentials -g {rg} -n {managed_cluster_name} -f {kubeconfig}')
        self.cmd('connectedk8s connect -g {rg} -n {name} -l eastus --tags foo=doo --kube-config {kubeconfig} --kube-context {managed_cluster_name}', checks=[
            self.check('tags.foo', 'doo'),
            self.check('name', '{name}')
        ])
        self.cmd('connectedk8s show -g {rg} -n {name}', checks=[
            self.check('name', '{name}'),
            self.check('resourceGroup', '{rg}'),
            self.check('tags.foo', 'doo')
        ])

        os.environ.setdefault('KUBECONFIG', kubeconfig)
        helm_client_location = install_helm_client()
        cmd = [helm_client_location, 'get', 'values', 'azure-arc', "--namespace", "azure-arc-release", "-ojson"]

        # scenario - auto-upgrade is turned on
        self.cmd('connectedk8s update -n {name} -g {rg} --auto-upgrade true --kube-config {kubeconfig} --kube-context {managed_cluster_name}')
        cmd_output1 = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE)
        _, error_helm_delete = cmd_output1.communicate()
        assert(cmd_output1.returncode == 0)
        changed_cmd1 = json.loads(cmd_output1.communicate()[0].strip())
        assert(changed_cmd1["systemDefaultValues"]['azureArcAgents']['autoUpdate'] == bool(1))

        # scenario - auto-upgrade is turned off
        self.cmd('connectedk8s update -n {name} -g {rg} --auto-upgrade false --kube-config {kubeconfig} --kube-context {managed_cluster_name}')
        cmd_output1 = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE)
        _, error_helm_delete = cmd_output1.communicate()
        assert(cmd_output1.returncode == 0)
        changed_cmd1 = json.loads(cmd_output1.communicate()[0].strip())
        assert(changed_cmd1["systemDefaultValues"]['azureArcAgents']['autoUpdate'] == bool(0))

        #scenario - updating the tags
        self.cmd('connectedk8s update -n {name} -g {rg} --kube-config {kubeconfig} --kube-context {managed_cluster_name} --tags foo=moo')
        self.cmd('connectedk8s show -g {rg} -n {name}', checks=[
            self.check('name', '{name}'),
            self.check('resourceGroup', '{rg}'),
            self.check('tags.foo', 'moo')
        ])

        self.cmd('connectedk8s delete -g {rg} -n {name} --kube-config {kubeconfig} --kube-context {managed_cluster_name} -y')
        self.cmd('aks delete -g {rg} -n {managed_cluster_name} -y')

        # delete the kube config
        os.remove("%s" % (_get_test_data_file(managed_cluster_name + '-config.yaml')))
        # os.remove("%s" % (_get_test_data_file(managed_cluster_name + '-plsconfig.yaml')))


    @live_only()
    @ResourceGroupPreparer(name_prefix='conk8stest', location='eastus2euap', random_name_length=16)
    def test_troubleshoot(self,resource_group):
        managed_cluster_name = self.create_random_name(prefix='test-troubleshoot', length=24)
        kubeconfig="%s" % (_get_test_data_file(managed_cluster_name + '-config.yaml')) 
        # kubeconfigpls="%s" % (_get_test_data_file(managed_cluster_name + '-plsconfig.yaml')) 
        self.kwargs.update({
            'name': self.create_random_name(prefix='cc-', length=12),
            'kubeconfig': kubeconfig,
            'rg':resource_group,
            # 'kubeconfigpls': kubeconfigpls,
            'managed_cluster_name': managed_cluster_name
        })

        self.cmd('aks create -g {rg} -n {managed_cluster_name} --generate-ssh-keys')
        self.cmd('aks get-credentials -g {rg} -n {managed_cluster_name} -f {kubeconfig}')
        self.cmd('connectedk8s connect -g {rg} -n {name} -l eastus --tags foo=doo --kube-config {kubeconfig} --kube-context {managed_cluster_name}', checks=[
            self.check('tags.foo', 'doo'),
            self.check('name', '{name}')
        ])
        self.cmd('connectedk8s show -g {rg} -n {name}', checks=[
            self.check('name', '{name}'),
            self.check('resourceGroup', '{rg}'),
            self.check('tags.foo', 'doo')
        ])

        self.cmd('connectedk8s troubleshoot -g {rg} -n {name} --kube-config {kubeconfig} --kube-context {managed_cluster_name}')

        self.cmd('connectedk8s delete -g {rg} -n {name} --kube-config {kubeconfig} --kube-context {managed_cluster_name} -y')
        self.cmd('aks delete -g {rg} -n {managed_cluster_name} -y')

        # delete the kube config
        os.remove("%s" % (_get_test_data_file(managed_cluster_name + '-config.yaml')))
