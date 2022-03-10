# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
# pylint: disable=bad-continuation
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType
from azext_desktopvirtualization.generated._client_factory import (
    cf_workspace,
    cf_scaling_plan,
    cf_application_group,
    cf_host_pool,
    cf_msix_package,
    cf_msix_image,
)


desktopvirtualization_application_group = CliCommandType(
    operations_tmpl='azext_desktopvirtualization.vendored_sdks.desktopvirtualization.operations._application_groups_operations#ApplicationGroupsOperations.{}',
    client_factory=cf_application_group,
)


desktopvirtualization_host_pool = CliCommandType(
    operations_tmpl='azext_desktopvirtualization.vendored_sdks.desktopvirtualization.operations._host_pools_operations#HostPoolsOperations.{}',
    client_factory=cf_host_pool,
)


desktopvirtualization_msix_image = CliCommandType(
    operations_tmpl='azext_desktopvirtualization.vendored_sdks.desktopvirtualization.operations._msix_images_operations#MsixImagesOperations.{}',
    client_factory=cf_msix_image,
)


desktopvirtualization_msix_package = CliCommandType(
    operations_tmpl='azext_desktopvirtualization.vendored_sdks.desktopvirtualization.operations._msix_packages_operations#MsixPackagesOperations.{}',
    client_factory=cf_msix_package,
)


desktopvirtualization_scaling_plan = CliCommandType(
    operations_tmpl='azext_desktopvirtualization.vendored_sdks.desktopvirtualization.operations._scaling_plans_operations#ScalingPlansOperations.{}',
    client_factory=cf_scaling_plan,
)


desktopvirtualization_workspace = CliCommandType(
    operations_tmpl='azext_desktopvirtualization.vendored_sdks.desktopvirtualization.operations._workspaces_operations#WorkspacesOperations.{}',
    client_factory=cf_workspace,
)


def load_command_table(self, _):

    with self.command_group(
        'desktopvirtualization applicationgroup',
        desktopvirtualization_application_group,
        client_factory=cf_application_group,
    ) as g:
        g.custom_command('list', 'desktopvirtualization_applicationgroup_list')
        g.custom_show_command('show', 'desktopvirtualization_applicationgroup_show')
        g.custom_command('create', 'desktopvirtualization_applicationgroup_create')
        g.custom_command('update', 'desktopvirtualization_applicationgroup_update')
        g.custom_command('delete', 'desktopvirtualization_applicationgroup_delete', confirmation=True)

    with self.command_group(
        'desktopvirtualization hostpool', desktopvirtualization_host_pool, client_factory=cf_host_pool
    ) as g:
        g.custom_command('list', 'desktopvirtualization_hostpool_list')
        g.custom_show_command('show', 'desktopvirtualization_hostpool_show')
        g.custom_command('create', 'desktopvirtualization_hostpool_create')
        g.custom_command('update', 'desktopvirtualization_hostpool_update')
        g.custom_command('delete', 'desktopvirtualization_hostpool_delete', confirmation=True)
        g.custom_command('retrieve-registration-token', 'desktopvirtualization_hostpool_retrieve_registration_token')

    with self.command_group(
        'desktopvirtualization msix-image', desktopvirtualization_msix_image, client_factory=cf_msix_image
    ) as g:
        g.custom_command('expand', 'desktopvirtualization_msix_image_expand')

    with self.command_group(
        'desktopvirtualization msix-package', desktopvirtualization_msix_package, client_factory=cf_msix_package
    ) as g:
        g.custom_command('list', 'desktopvirtualization_msix_package_list')
        g.custom_show_command('show', 'desktopvirtualization_msix_package_show')
        g.custom_command('create', 'desktopvirtualization_msix_package_create')
        g.custom_command('update', 'desktopvirtualization_msix_package_update')
        g.custom_command('delete', 'desktopvirtualization_msix_package_delete', confirmation=True)

    with self.command_group(
        'desktopvirtualization scaling-plan', desktopvirtualization_scaling_plan, client_factory=cf_scaling_plan
    ) as g:
        g.custom_command('list', 'desktopvirtualization_scaling_plan_list')
        g.custom_show_command('show', 'desktopvirtualization_scaling_plan_show')
        g.custom_command('create', 'desktopvirtualization_scaling_plan_create')
        g.custom_command('update', 'desktopvirtualization_scaling_plan_update')
        g.custom_command('delete', 'desktopvirtualization_scaling_plan_delete', confirmation=True)

    with self.command_group(
        'desktopvirtualization workspace', desktopvirtualization_workspace, client_factory=cf_workspace
    ) as g:
        g.custom_command('list', 'desktopvirtualization_workspace_list')
        g.custom_show_command('show', 'desktopvirtualization_workspace_show')
        g.custom_command('create', 'desktopvirtualization_workspace_create')
        g.custom_command('update', 'desktopvirtualization_workspace_update')
        g.custom_command('delete', 'desktopvirtualization_workspace_delete', confirmation=True)

    with self.command_group('desktopvirtualization', is_experimental=True):
        pass
