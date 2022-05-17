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
# pylint: disable=too-many-statements
# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import (
    resource_group_name_type,
)
from azext_datamigration.action import (
    AddSourceSqlConnection,
    AddTargetSqlConnection
)


def load_arguments(self, _):

    with self.argument_context('datamigration get-assessment') as c:
        c.argument('connection_string', nargs='+', help='SQL Server Connection Strings')
        c.argument('output_folder', type=str, help='Output folder to store assessment report')
        c.argument('config_file_path', type=str, help='Path of the ConfigFile')
        c.argument('overwrite', help='Enable this parameter to overwrite the existing assessment report')

    with self.argument_context('datamigration performance-data-collection') as c:
        c.argument('connection_string', nargs='+', help='SQL Server Connection Strings')
        c.argument('output_folder', type=str, help='Output folder to store performance data')
        c.argument('perf_query_interval', type=int, help='Interval at which to query performance data, in seconds.')
        c.argument('static_query_interval', type=int, help='Interval at which to query and persist static configuration data, in seconds.')
        c.argument('number_of_iteration', type=int, help='Number of iterations of performance data collection to perform before persisting to file. For example, with default values, performance data will be persisted every 30 seconds * 20 iterations = 10 minutes. Minimum: 2.')
        c.argument('config_file_path', type=str, help='Path of the ConfigFile')
        c.argument('time', type=int, help='Time after which the command execution automatically stops, in seconds. If this parameter is not specified manual intervention will be required to stop the command execution.')

    with self.argument_context('datamigration get-sku-recommendation') as c:
        c.argument('output_folder', type=str, help='Output folder where performance data of the SQL Server is stored. The value here must be the same as the one used in PerfDataCollection')
        c.argument('target_platform', type=str, help='Target platform for SKU recommendation: either AzureSqlDatabase, AzureSqlManagedInstance, AzureSqlVirtualMachine, or Any. If Any is selected, then SKU recommendations for all three target platforms will be evaluated, and the best fit will be returned.')
        c.argument('target_sql_instance', type=str, help='Name of the SQL instance for which SKU should be recommendeded. Default: outputFolder will be scanned for files created by the PerfDataCollection action, and recommendations will be provided for every instance found.')
        c.argument('target_percentile', type=int, help='Percentile of data points to be used during aggregation of the performance data. Only used for baseline (non-elastic) strategy.')
        c.argument('scaling_factor', type=int, help='Scaling (comfort) factor used during SKU recommendation. For example, if it is determined that there is a 4 vCore CPU requirement with a scaling factor of 150%, then the true CPU requirement will be 6 vCores.')
        c.argument('start_time', type=str, help='UTC start time of performance data points to consider during aggregation, in YYYY-MM-DD HH:MM format. Only used for baseline (non-elastic) strategy. Default: all data points collected will be considered.')
        c.argument('end_time', type=str, help='UTC end time of performance data points to consider during aggregation, in YYYY-MM-DD HH:MM format. Only used for baseline (non-elastic) strategy. Default: all data points collected will be considered.')
        c.argument('overwrite', help='Whether or not to overwrite any existing SKU recommendation reports. Enable this paramater to overwrite.')
        c.argument('display_result', help='Whether or not to print the SKU recommendation results to the console. Enable this parameter to display result.')
        c.argument('elastic_strategy', help='Whether or not to use the elastic strategy for SKU recommendations based on resource usage profiling. Enable this parameter to use elastic strategy.')
        c.argument('database_allow_list', nargs='+', help='Space separated list of names of databases to be allowed for SKU recommendation consideration while excluding all others. Only set one of the following or neither: databaseAllowList, databaseDenyList. Default: null.')
        c.argument('database_deny_list', nargs='+', help='Space separated list of names of databases to not be considered for SKU recommendation. Only set one of the following or neither: databaseAllowList, databaseDenyList. Default: null.')
        c.argument('config_file_path', type=str, help='Path of the ConfigFile')

    with self.argument_context('datamigration register-integration-runtime') as c:
        c.argument('auth_key', type=str, help='AuthKey of SQL Migration Service')
        c.argument('ir_path', type=str, help='Path of Integration Runtime MSI')
        c.argument('installed_ir_path', type=str, help='Version folder path in the Integration Runtime installed location. This can be provided when IR is installed but the command is failing to read it. Format: "<Parent-folder-path>\\Microsoft Integration Runtime\\<Version>"')

    with self.argument_context('datamigration sql-db create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('sqldb_instance_name', type=str, help='Name of the target SQL Database Server.')
        c.argument('target_db_name', type=str, help='The name of the target database.')
        c.argument('scope', type=str, help='Resource Id of the target resource (SQL VM, SQL Managed Instance or SQL '
                   'DB)')
        c.argument('source_sql_connection', action=AddSourceSqlConnection, nargs='+', help='Source SQL Server '
                   'connection details.')
        c.argument('source_database_name', type=str, help='Name of the source database.')
        c.argument('migration_service', type=str, help='Resource Id of the Migration Service.')
        c.argument('target_db_collation', type=str, help='Database collation to be used for the target database.')
        c.argument('target_sql_connection', action=AddTargetSqlConnection, nargs='+', help='Target SQL DB connection '
                   'details.')
        c.argument('table_list', nargs='+', help='List of tables to copy.')
