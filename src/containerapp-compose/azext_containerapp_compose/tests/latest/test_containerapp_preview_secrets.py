# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest  # pylint: disable=unused-import

from azure.cli.testsdk import (ResourceGroupPreparer)
from azure.cli.testsdk.decorators import serial_test
from azext_containerapp_compose.tests.latest.common import (ContainerappComposePreviewScenarioTest,  # pylint: disable=unused-import
                                                            write_test_file,
                                                            clean_up_test_file,
                                                            TEST_DIR)


class ContainerappComposePreviewSecretsScenarioTest(ContainerappComposePreviewScenarioTest):
    @serial_test()
    @ResourceGroupPreparer(name_prefix='cli_test_containerapp_preview', location='eastus')
    def test_containerapp_compose_create_with_secrets(self, resource_group):
        compose_text = """
services:
  foo:
    image: mcr.microsoft.com/azuredocs/containerapps-helloworld:latest
    secrets:
      - source: my_secret
        target: redis_secret
        uid: '103'
        gid: '103'
        mode: 0440
secrets:
  my_secret:
    file: ./my_secret.txt
  my_other_secret:
    external: true
"""
        compose_file_name = f"{self._testMethodName}_compose.yml"
        write_test_file(compose_file_name, compose_text)

        secrets_file_name = "./my_secret.txt"
        secrets_text = "Lorem Ipsum\n"
        write_test_file(secrets_file_name, secrets_text)

        self.kwargs.update({
            'environment': self.create_random_name(prefix='containerapp-compose', length=24),
            'workspace': self.create_random_name(prefix='containerapp-compose', length=24),
            'compose': compose_file_name,
        })

        command_string = 'containerapp compose create'
        command_string += ' --compose-file-path {compose}'
        command_string += ' --resource-group {rg}'
        command_string += ' --environment {environment}'
        command_string += ' --logs-workspace {workspace}'

        self.cmd(command_string, checks=[
            self.check('[?name==`foo`].properties.configuration.secrets[0].name', ["redis-secret"]),
            self.check('[?name==`foo`].properties.template.containers[0].env[0].name', ["redis-secret"]),
            self.check('[?name==`foo`].properties.template.containers[0].env[0].secretRef', ["redis-secret"])  # pylint: disable=C0301
        ])

        clean_up_test_file(compose_file_name)
        clean_up_test_file(secrets_file_name)

    @serial_test()
    @ResourceGroupPreparer(name_prefix='cli_test_containerapp_preview', location='eastus')
    def test_containerapp_compose_create_with_secrets_and_existing_environment(self, resource_group):
        compose_text = """
services:
  foo:
    image: mcr.microsoft.com/azuredocs/containerapps-helloworld:latest
    environment:
      database__client: mysql
      database__connection__host: db
      database__connection__user: root
      database__connection__password: example
      database__connection__database: snafu
    secrets:
      - source: my_secret
        target: redis_secret
        uid: '103'
        gid: '103'
        mode: 0440
secrets:
  my_secret:
    file: ./snafu.txt
  my_other_secret:
    external: true
"""
        compose_file_name = f"{self._testMethodName}_compose.yml"
        write_test_file(compose_file_name, compose_text)

        secrets_file_name = "./snafu.txt"
        secrets_text = "Lorem Ipsum\n"
        write_test_file(secrets_file_name, secrets_text)

        self.kwargs.update({
            'environment': self.create_random_name(prefix='containerapp-compose', length=24),
            'workspace': self.create_random_name(prefix='containerapp-compose', length=24),
            'compose': compose_file_name,
        })

        command_string = 'containerapp compose create'
        command_string += ' --compose-file-path {compose}'
        command_string += ' --resource-group {rg}'
        command_string += ' --environment {environment}'
        command_string += ' --logs-workspace {workspace}'

        self.cmd(command_string, checks=[
            self.check('length([?name==`foo`].properties.template.containers[0].env[].name)', 6),
        ])

        clean_up_test_file(compose_file_name)
        clean_up_test_file(secrets_file_name)

    @serial_test()
    @ResourceGroupPreparer(name_prefix='cli_test_containerapp_preview', location='eastus')
    def test_containerapp_compose_create_with_secrets_and_existing_environment_conflict(self, resource_group):
        compose_text = """
services:
  foo:
    image: mcr.microsoft.com/azuredocs/containerapps-helloworld:latest
    environment:
      database--client: mysql
    secrets:
      -  database__client
secrets:
  database__client:
    file: ./database__client.txt
"""
        compose_file_name = f"{self._testMethodName}_compose.yml"
        write_test_file(compose_file_name, compose_text)

        secrets_file_name = "./database__client.txt"
        secrets_text = "Lorem Ipsum\n"
        write_test_file(secrets_file_name, secrets_text)

        self.kwargs.update({
            'environment': self.create_random_name(prefix='containerapp-compose', length=24),
            'workspace': self.create_random_name(prefix='containerapp-compose', length=24),
            'compose': compose_file_name,
        })

        command_string = 'containerapp compose create'
        command_string += ' --compose-file-path {compose}'
        command_string += ' --resource-group {rg}'
        command_string += ' --environment {environment}'
        command_string += ' --logs-workspace {workspace}'

        # This test fails with duplicate environment variable names
        self.cmd(command_string, expect_failure=True)

        clean_up_test_file(compose_file_name)
        clean_up_test_file(secrets_file_name)
