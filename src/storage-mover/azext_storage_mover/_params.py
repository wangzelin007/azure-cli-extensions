# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=too-many-statements
# pylint: disable=line-too-long
from azure.cli.core.commands.parameters import (get_enum_type)


def load_arguments(self, _):  # pylint: disable=unused-argument

    with self.argument_context('storage-mover endpoint') as c:
        c.argument('endpoint_name', options_list=('--endpoint-name', '--name', '-n'), required=True,
                   help='The name of the endpoint resource.')
        c.argument('resource_group', options_list=('--resource-group', '-g'), required=True,
                   help='Name of resource group. You can configure the default group using '
                        '`az configure --defaults group=<name>`.')
        c.argument('storage_mover_name', options_list=('--storage-mover-name'), required=True,
                   help='The name of the Storage Mover resource.')
        c.argument('description', help='A description for the Endpoint.')

    for command in ['create-for-storage-container', 'update-for-storage-container']:
        with self.argument_context('storage-mover endpoint ' + command) as c:
            c.argument('blob_container_name', options_list=('--container-name'), required=True,
                       help='The name of the Storage blob container that is the target destination.')
            c.argument('storage_account_resource_id', options_list=('--storage-account-id'), required=True,
                       help=' The Azure Resource ID of the storage account that is the target destination.')

    for command in ['create-for-nfs', 'update-for-nfs']:
        with self.argument_context('storage-mover endpoint ' + command) as c:
            c.argument('export', required=True, help='The directory being exported from the server.')
            c.argument('host', required=True, help='The host name or IP address of the server exporting the file system.')
            c.argument('nfs_version', arg_type=get_enum_type(['NFSauto', 'NFSv3', 'NFSv4']),
                       help='The NFS protocol version.')

    for command in ['create-for-storage-smb-file-share', 'update-for-storage-smb-file-share']:
        with self.argument_context('storage-mover endpoint ' + command) as c:
            c.argument('file_share_name', required=True, help='The name of the Azure Storage file share.')
            c.argument('storage_account_resource_id', options_list=('--storage-account-id'), required=True,
                       help='The Azure Resource ID of the storage account that is the target destination.')

    for command in ['create-for-smb', 'update-for-smb']:
        with self.argument_context('storage-mover endpoint ' + command) as c:
            c.argument('host', required=True, help='The host name or IP address of the server exporting the file system.')
            c.argument('share_name', required=True, help='The name of the SMB share being exported from the server.')
            c.argument('password_uri', help='The Azure Key Vault secret URI which stores the password. Use empty string to clean-up existing value.')
            c.argument('username_uri', help='The Azure Key Vault secret URI which stores the username. Use empty string to clean-up existing value.')
