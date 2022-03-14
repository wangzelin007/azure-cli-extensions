# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_hostpool_create
from .example_steps import step_hostpool_show
from .example_steps import step_hostpool_list
from .example_steps import step_hostpool_list2
from .example_steps import step_hostpool_update
from .example_steps import step_hostpool_retrieve_registration_token
from .example_steps import step_applicationgroup_create
from .example_steps import step_applicationgroup_show
from .example_steps import step_applicationgroup_list
from .example_steps import step_applicationgroup_list2
from .example_steps import step_applicationgroup_update
from .example_steps import step_applicationgroup_delete
from .example_steps import step_msix_image_expand
from .example_steps import step_msix_package_create
from .example_steps import step_msix_package_show
from .example_steps import step_msix_package_list
from .example_steps import step_msix_package_update
from .example_steps import step_msix_package_delete
from .example_steps import step_scaling_plan_create
from .example_steps import step_scaling_plan_show
from .example_steps import step_scaling_plan_list
from .example_steps import step_scaling_plan_list2
from .example_steps import step_scaling_plan_list3
from .example_steps import step_scaling_plan_update
from .example_steps import step_scaling_plan_delete
from .example_steps import step_hostpool_delete
from .example_steps import step_workspace_create
from .example_steps import step_workspace_show
from .example_steps import step_workspace_list
from .example_steps import step_workspace_list2
from .example_steps import step_workspace_update
from .example_steps import step_workspace_delete
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test):
    setup_scenario(test)

    step_hostpool_create(test, checks=[
        test.check("location", "centralus", case_sensitive=False),
        test.check("description", "des1", case_sensitive=False),
        test.check("friendlyName", "friendly", case_sensitive=False),
        test.check("hostPoolType", "Pooled", case_sensitive=False),
        test.check("loadBalancerType", "BreadthFirst", case_sensitive=False),
        test.check("maxSessionLimit", 999999),
        # test.check("migrationRequest.migrationPath", "TenantGroups/{{defaultV1TenantGroup.Name}}/Tenants/{{defaultV1Ten"
        #            "ant.Name}}/HostPools/{{sessionHostPool.Name}}", case_sensitive=False),
        # test.check("migrationRequest.operation", "Start", case_sensitive=False),
        test.check("personalDesktopAssignmentType", None, case_sensitive=False),
        # test.check("personalDesktopAssignmentType", "Automatic", case_sensitive=False),
        test.check("preferredAppGroupType", "Desktop", case_sensitive=False),
        test.check("ssoClientId", "client", case_sensitive=False),
        test.check("ssoClientSecretKeyVaultPath", "https://keyvault/secret", case_sensitive=False),
        test.check("ssoSecretType", "SharedKey", case_sensitive=False),
        # test.check("ssoadfsAuthority", "https://adfs", case_sensitive=False),
        # test.check("startVMOnConnect", False),
        # test.check("vmTemplate", "{{json:json}}", case_sensitive=False),
        test.check("name", "{myHostPool}", case_sensitive=False),
    ])
    step_hostpool_show(test, checks=[
        test.check("location", "centralus", case_sensitive=False),
        test.check("description", "des1", case_sensitive=False),
        test.check("friendlyName", "friendly", case_sensitive=False),
        test.check("hostPoolType", "Pooled", case_sensitive=False),
        test.check("loadBalancerType", "BreadthFirst", case_sensitive=False),
        test.check("maxSessionLimit", 999999),
        test.check("personalDesktopAssignmentType", None, case_sensitive=False),
        # test.check("personalDesktopAssignmentType", "Automatic", case_sensitive=False),
        test.check("preferredAppGroupType", "Desktop", case_sensitive=False),
        test.check("ssoClientId", "client", case_sensitive=False),
        test.check("ssoClientSecretKeyVaultPath", "https://keyvault/secret", case_sensitive=False),
        test.check("ssoSecretType", "SharedKey", case_sensitive=False),
        # test.check("ssoadfsAuthority", "https://adfs", case_sensitive=False),
        # test.check("startVMOnConnect", False),
        # test.check("vmTemplate", "{{json:json}}", case_sensitive=False),
        test.check("name", "{myHostPool}", case_sensitive=False),
    ])
    step_hostpool_list(test, checks=[
        test.check('length(@)', 1),
    ])
    step_hostpool_list2(test, checks=[
        test.check('length(@)', 1),
    ])
    step_hostpool_update(test, checks=[
        test.check("location", "centralus", case_sensitive=False),
        test.check("description", "des1", case_sensitive=False),
        test.check("friendlyName", "friendly", case_sensitive=False),
        test.check("hostPoolType", "Pooled", case_sensitive=False),
        test.check("loadBalancerType", "BreadthFirst", case_sensitive=False),
        test.check("maxSessionLimit", 999999),
        test.check("personalDesktopAssignmentType", None, case_sensitive=False),
        # test.check("personalDesktopAssignmentType", "Automatic", case_sensitive=False),
        test.check("preferredAppGroupType", "Desktop", case_sensitive=False),
        test.check("ssoClientId", "client", case_sensitive=False),
        test.check("ssoClientSecretKeyVaultPath", "https://keyvault/secret", case_sensitive=False),
        test.check("ssoSecretType", "SharedKey", case_sensitive=False),
        # test.check("ssoadfsAuthority", "https://adfs", case_sensitive=False),
        # test.check("startVMOnConnect", False),
        # test.check("vmTemplate", "{{json:json}}", case_sensitive=False),
        test.check("name", "{myHostPool}", case_sensitive=False),
    ])
    step_hostpool_retrieve_registration_token(test, checks=[])

    step_applicationgroup_create(test, checks=[
        test.check("location", "centralus", case_sensitive=False),
        test.check("description", "des1", case_sensitive=False),
        test.check("applicationGroupType", "RemoteApp", case_sensitive=False),
        test.check("friendlyName", "friendly", case_sensitive=False),
        test.check("hostPoolArmPath", "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Desktop"
                   "Virtualization/hostPools/{myHostPool}", case_sensitive=False),
        # test.check("migrationRequest.migrationPath", "TenantGroups/{{defaultV1TenantGroup.Name}}/Tenants/{{defaultV1Ten"
        #            "ant.Name}}/HostPools/{{sessionHostPool.Name}}", case_sensitive=False),
        # test.check("migrationRequest.operation", "Start", case_sensitive=False),
        test.check("name", "{myApplicationGroup}", case_sensitive=False),
    ])
    step_applicationgroup_show(test, checks=[
        test.check("location", "centralus", case_sensitive=False),
        test.check("description", "des1", case_sensitive=False),
        test.check("applicationGroupType", "RemoteApp", case_sensitive=False),
        test.check("friendlyName", "friendly", case_sensitive=False),
        test.check("hostPoolArmPath", "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Desktop"
                   "Virtualization/hostPools/{myHostPool}", case_sensitive=False),
        test.check("name", "{myApplicationGroup}", case_sensitive=False),
    ])
    step_applicationgroup_list(test, checks=[])
    step_applicationgroup_list2(test, checks=[])
    step_applicationgroup_update(test, checks=[
        test.check("location", "centralus", case_sensitive=False),
        test.check("description", "des1", case_sensitive=False),
        test.check("applicationGroupType", "RemoteApp", case_sensitive=False),
        test.check("friendlyName", "friendly", case_sensitive=False),
        test.check("hostPoolArmPath", "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Desktop"
                   "Virtualization/hostPools/{myHostPool}", case_sensitive=False),
        test.check("name", "{myApplicationGroup}", case_sensitive=False),
    ])
    step_applicationgroup_delete(test, checks=[])

    # Message: ActivityId: e3190f1b-a36e-4ea3-956a-fc14d5371574 Error: No Session Hosts available for operation
    # step_msix_image_expand(test, checks=[])
    # step_msix_package_create(test, checks=[])
    # step_msix_package_show(test, checks=[])
    # step_msix_package_list(test, checks=[])
    # step_msix_package_update(test, checks=[])
    # step_msix_package_delete(test, checks=[])
    # only Pooled Host Pools are supported.Personal Host Pools will be included in a future release.Go to: https://go.microsoft.com/fwlink/?linkid=2146741
    step_scaling_plan_create(test, checks=[
        test.check("location", "centralus", case_sensitive=False),
        test.check("description", "des1", case_sensitive=False),
        test.check("exclusionTag", "value", case_sensitive=False),
        test.check("friendlyName", "friendly", case_sensitive=False),
        test.check("hostPoolType", "Personal", case_sensitive=False),
        test.check("timeZone", "", case_sensitive=False),
        test.check("name", "{myScalingPlan}", case_sensitive=False),
    ])
    step_scaling_plan_show(test, checks=[
        test.check("location", "centralus", case_sensitive=False),
        test.check("description", "des1", case_sensitive=False),
        test.check("exclusionTag", "value", case_sensitive=False),
        test.check("friendlyName", "friendly", case_sensitive=False),
        test.check("hostPoolType", "Personal", case_sensitive=False),
        test.check("timeZone", "UTC", case_sensitive=False),
    ])
    step_scaling_plan_list(test, checks=[
        test.check('length(@)', 1),
    ])
    step_scaling_plan_list2(test, checks=[
        test.check('length(@)', 1),
    ])
    step_scaling_plan_list3(test, checks=[])
    step_scaling_plan_update(test, checks=[
        test.check("location", "centralus", case_sensitive=False),
        test.check("description", "des1", case_sensitive=False),
        test.check("exclusionTag", "value", case_sensitive=False),
        test.check("friendlyName", "friendly", case_sensitive=False),
        test.check("hostPoolType", "Personal", case_sensitive=False),
        test.check("timeZone", "UTC", case_sensitive=False),
        test.check("name", "{myScalingPlan}", case_sensitive=False),
    ])
    step_scaling_plan_delete(test, checks=[])
    step_hostpool_delete(test, checks=[])
    step_workspace_create(test, checks=[
        test.check("location", "centralus", case_sensitive=False),
        test.check("description", "des1", case_sensitive=False),
        test.check("friendlyName", "friendly", case_sensitive=False),
        test.check("name", "{myWorkspace}", case_sensitive=False),
    ])
    step_workspace_show(test, checks=[
        test.check("location", "centralus", case_sensitive=False),
        test.check("description", "des1", case_sensitive=False),
        test.check("friendlyName", "friendly", case_sensitive=False),
        test.check("name", "{myWorkspace}", case_sensitive=False),
    ])
    step_workspace_list(test, checks=[
        test.check('length(@)', 1),
    ])
    step_workspace_list2(test, checks=[
        test.check('length(@)', 1),
    ])
    step_workspace_update(test, checks=[
        test.check("location", "centralus", case_sensitive=False),
        test.check("description", "des1", case_sensitive=False),
        test.check("friendlyName", "friendly", case_sensitive=False),
        test.check("name", "{myWorkspace}", case_sensitive=False),
    ])
    step_workspace_delete(test, checks=[])
    cleanup_scenario(test)


# Test class for Scenario
@try_manual
class DesktopvirtualizationScenarioTest(ScenarioTest):
    def __init__(self, *args, **kwargs):
        super(DesktopvirtualizationScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myWorkspace': 'workspace1',
            'myHostPool': 'hostPool1',
            'myHostPool2': 'hostPool2',
            'myScalingPlan': 'scalingPlan1',
            'myApplicationGroup': 'applicationGroup1',
        })

    @ResourceGroupPreparer(name_prefix='clitestdesktopvirtualization_resourceGroup1'[:7], key='rg',
                           parameter_name='rg', location='centralus')
    def test_desktopvirtualization_Scenario(self, rg):
        call_scenario(self)
        calc_coverage(__file__)
        raise_if()
