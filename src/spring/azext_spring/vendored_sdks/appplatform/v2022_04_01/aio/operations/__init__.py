# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._services_operations import ServicesOperations
from ._config_servers_operations import ConfigServersOperations
from ._configuration_services_operations import ConfigurationServicesOperations
from ._service_registries_operations import ServiceRegistriesOperations
from ._build_service_operations import BuildServiceOperations
from ._buildpack_binding_operations import BuildpackBindingOperations
from ._build_service_builder_operations import BuildServiceBuilderOperations
from ._build_service_agent_pool_operations import BuildServiceAgentPoolOperations
from ._monitoring_settings_operations import MonitoringSettingsOperations
from ._apps_operations import AppsOperations
from ._bindings_operations import BindingsOperations
from ._certificates_operations import CertificatesOperations
from ._custom_domains_operations import CustomDomainsOperations
from ._deployments_operations import DeploymentsOperations
from ._operations import Operations
from ._runtime_versions_operations import RuntimeVersionsOperations
from ._skus_operations import SkusOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ServicesOperations",
    "ConfigServersOperations",
    "ConfigurationServicesOperations",
    "ServiceRegistriesOperations",
    "BuildServiceOperations",
    "BuildpackBindingOperations",
    "BuildServiceBuilderOperations",
    "BuildServiceAgentPoolOperations",
    "MonitoringSettingsOperations",
    "AppsOperations",
    "BindingsOperations",
    "CertificatesOperations",
    "CustomDomainsOperations",
    "DeploymentsOperations",
    "Operations",
    "RuntimeVersionsOperations",
    "SkusOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
