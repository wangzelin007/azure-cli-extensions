# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from argcomplete.completers import FilesCompleter
from azure.cli.core import AzCommandsLoader
from knack.arguments import CLIArgumentType


def load_arguments(self: AzCommandsLoader, _):

    from azure.cli.core.commands.parameters import file_type, get_enum_type, get_three_state_flag

    definition_type = get_enum_type(["vnf", "cnf", "nsd"])

    # Set the argument context so these options are only available when this specific command
    # is called.
    with self.argument_context('aosm definition') as c:
        c.argument(
            'definition_type',
            arg_type=definition_type,
            help='Type of AOSM definition to generate.'
        )
        c.argument(
            'config_file',
            options_list=["--config-file", "-f"],
            type=file_type,
            completer=FilesCompleter(allowednames="*.json"),
            help='The path to the configuration file.'
        )
        c.argument('publish', arg_type=get_three_state_flag(), help='Publishes generated AOSM definition.')

    with self.argument_context('aosm generate-config') as c:
        c.argument('definition_type', arg_type=definition_type, help='Type of AOSM definition config to generate.')
