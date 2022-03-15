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

import json


def desktopvirtualization_workspace_list(client,
                                         resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def desktopvirtualization_workspace_show(client,
                                         resource_group_name,
                                         workspace_name):
    return client.get(resource_group_name=resource_group_name,
                      workspace_name=workspace_name)


def desktopvirtualization_workspace_create(client,
                                           resource_group_name,
                                           workspace_name,
                                           location=None,
                                           tags=None,
                                           description=None,
                                           friendly_name=None,
                                           application_group_references=None):
    workspace = {}
    if location is not None:
        workspace['location'] = location
    if tags is not None:
        workspace['tags'] = tags
    if description is not None:
        workspace['description'] = description
    if friendly_name is not None:
        workspace['friendly_name'] = friendly_name
    if application_group_references is not None:
        workspace['application_group_references'] = application_group_references
    return client.create_or_update(resource_group_name=resource_group_name,
                                   workspace_name=workspace_name,
                                   workspace=workspace)


def desktopvirtualization_workspace_update(client,
                                           resource_group_name,
                                           workspace_name,
                                           tags=None,
                                           description=None,
                                           friendly_name=None,
                                           application_group_references=None):
    workspace = {}
    if tags is not None:
        workspace['tags'] = tags
    if description is not None:
        workspace['description'] = description
    if friendly_name is not None:
        workspace['friendly_name'] = friendly_name
    if application_group_references is not None:
        workspace['application_group_references'] = application_group_references
    return client.update(resource_group_name=resource_group_name,
                         workspace_name=workspace_name,
                         workspace=workspace)


def desktopvirtualization_workspace_delete(client,
                                           resource_group_name,
                                           workspace_name):
    return client.delete(resource_group_name=resource_group_name,
                         workspace_name=workspace_name)


def desktopvirtualization_applicationgroup_list(client,
                                                resource_group_name=None,
                                                filter=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name,
                                             filter=filter)
    return client.list_by_subscription(filter=filter)


def desktopvirtualization_applicationgroup_show(client,
                                                resource_group_name,
                                                application_group_name):
    return client.get(resource_group_name=resource_group_name,
                      application_group_name=application_group_name)


def desktopvirtualization_applicationgroup_create(client,
                                                  resource_group_name,
                                                  application_group_name,
                                                  host_pool_arm_path,
                                                  application_group_type,
                                                  location=None,
                                                  tags=None,
                                                  description=None,
                                                  friendly_name=None):
    application_group = {}
    if location is not None:
        application_group['location'] = location
    if tags is not None:
        application_group['tags'] = tags
    if description is not None:
        application_group['description'] = description
    if friendly_name is not None:
        application_group['friendly_name'] = friendly_name
    application_group['host_pool_arm_path'] = host_pool_arm_path
    application_group['application_group_type'] = application_group_type
    return client.create_or_update(resource_group_name=resource_group_name,
                                   application_group_name=application_group_name,
                                   application_group=application_group)


def desktopvirtualization_applicationgroup_update(client,
                                                  resource_group_name,
                                                  application_group_name,
                                                  tags=None,
                                                  description=None,
                                                  friendly_name=None):
    application_group = {}
    if tags is not None:
        application_group['tags'] = tags
    if description is not None:
        application_group['description'] = description
    if friendly_name is not None:
        application_group['friendly_name'] = friendly_name
    return client.update(resource_group_name=resource_group_name,
                         application_group_name=application_group_name,
                         application_group=application_group)


def desktopvirtualization_applicationgroup_delete(client,
                                                  resource_group_name,
                                                  application_group_name):
    return client.delete(resource_group_name=resource_group_name,
                         application_group_name=application_group_name)


def desktopvirtualization_hostpool_list(client,
                                        resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list()


def desktopvirtualization_hostpool_show(client,
                                        resource_group_name,
                                        host_pool_name):
    return client.get(resource_group_name=resource_group_name,
                      host_pool_name=host_pool_name)


def desktopvirtualization_hostpool_create(client,
                                          resource_group_name,
                                          host_pool_name,
                                          host_pool_type,
                                          load_balancer_type,
                                          preferred_app_group_type,
                                          location=None,
                                          tags=None,
                                          friendly_name=None,
                                          description=None,
                                          personal_desktop_assignment_type=None,
                                          custom_rdp_property=None,
                                          max_session_limit=None,
                                          ring=None,
                                          validation_environment=None,
                                          registration_info=None,
                                          vm_template=None,
                                          ssoadfs_authority=None,
                                          sso_client_id=None,
                                          sso_client_secret_key_vault_path=None,
                                          sso_secret_type=None,
                                          start_vm_on_connect=None):
    host_pool = {}
	host_pool['host_pool_type'] = host_pool_type
	host_pool['load_balancer_type'] = load_balancer_type
	host_pool['preferred_app_group_type'] = preferred_app_group_type
    if location is not None:
        host_pool['location'] = location
    if tags is not None:
        host_pool['tags'] = tags
    if friendly_name is not None:
        host_pool['friendly_name'] = friendly_name
    if description is not None:
        host_pool['description'] = description
    if personal_desktop_assignment_type is not None:
        host_pool['personal_desktop_assignment_type'] = personal_desktop_assignment_type
    if custom_rdp_property is not None:
        host_pool['custom_rdp_property'] = custom_rdp_property
    if max_session_limit is not None:
        host_pool['max_session_limit'] = max_session_limit
    if ring is not None:
        host_pool['ring'] = ring
    if validation_environment is not None:
        host_pool['validation_environment'] = validation_environment
    if registration_info is not None:
        host_pool['registration_info'] = registration_info
    if vm_template is not None:
        host_pool['vm_template'] = vm_template
    if ssoadfs_authority is not None:
        host_pool['ssoadfs_authority'] = ssoadfs_authority
    if sso_client_id is not None:
        host_pool['sso_client_id'] = sso_client_id
    if sso_client_secret_key_vault_path is not None:
        host_pool['sso_client_secret_key_vault_path'] = sso_client_secret_key_vault_path
    if sso_secret_type is not None:
        host_pool['sso_secret_type'] = sso_secret_type
    if start_vm_on_connect is not None:
        host_pool['start_vm_on_connect'] = start_vm_on_connect
    return client.create_or_update(resource_group_name=resource_group_name,
                                   host_pool_name=host_pool_name,
                                   host_pool=host_pool)


def desktopvirtualization_hostpool_update(client,
                                          resource_group_name,
                                          host_pool_name,
                                          tags=None,
                                          friendly_name=None,
                                          description=None,
                                          custom_rdp_property=None,
                                          max_session_limit=None,
                                          personal_desktop_assignment_type=None,
                                          load_balancer_type=None,
                                          ring=None,
                                          validation_environment=None,
                                          registration_info=None,
                                          vm_template=None,
                                          ssoadfs_authority=None,
                                          sso_client_id=None,
                                          sso_client_secret_key_vault_path=None,
                                          sso_secret_type=None,
                                          preferred_app_group_type=None,
                                          start_vm_on_connect=None):
    host_pool = {}
    if tags is not None:
        host_pool['tags'] = tags
    if friendly_name is not None:
        host_pool['friendly_name'] = friendly_name
    if description is not None:
        host_pool['description'] = description
    if custom_rdp_property is not None:
        host_pool['custom_rdp_property'] = custom_rdp_property
    if max_session_limit is not None:
        host_pool['max_session_limit'] = max_session_limit
    if personal_desktop_assignment_type is not None:
        host_pool['personal_desktop_assignment_type'] = personal_desktop_assignment_type
    if load_balancer_type is not None:
        host_pool['load_balancer_type'] = load_balancer_type
    if ring is not None:
        host_pool['ring'] = ring
    if validation_environment is not None:
        host_pool['validation_environment'] = validation_environment
    if registration_info is not None:
        host_pool['registration_info'] = registration_info
    if vm_template is not None:
        host_pool['vm_template'] = vm_template
    if ssoadfs_authority is not None:
        host_pool['ssoadfs_authority'] = ssoadfs_authority
    if sso_client_id is not None:
        host_pool['sso_client_id'] = sso_client_id
    if sso_client_secret_key_vault_path is not None:
        host_pool['sso_client_secret_key_vault_path'] = sso_client_secret_key_vault_path
    if sso_secret_type is not None:
        host_pool['sso_secret_type'] = sso_secret_type
    if preferred_app_group_type is not None:
        host_pool['preferred_app_group_type'] = preferred_app_group_type
    if start_vm_on_connect is not None:
        host_pool['start_vm_on_connect'] = start_vm_on_connect
    return client.update(resource_group_name=resource_group_name,
                         host_pool_name=host_pool_name,
                         host_pool=host_pool)


def desktopvirtualization_hostpool_delete(client,
                                          resource_group_name,
                                          host_pool_name,
                                          force=None):
    return client.delete(resource_group_name=resource_group_name,
                         host_pool_name=host_pool_name,
                         force=force)


def desktopvirtualization_hostpool_retrieve_registration_token(client,
                                                               resource_group_name,
                                                               host_pool_name):
    return client.retrieve_registration_token(resource_group_name=resource_group_name,
                                              host_pool_name=host_pool_name)
