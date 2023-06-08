# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from ._utils import (_get_or_add_extension, _get_azext_module, GA_CONTAINERAPP_EXTENSION_NAME)


def load_arguments(self, _):
    if not _get_or_add_extension(self, GA_CONTAINERAPP_EXTENSION_NAME):
        return
    azext_params = _get_azext_module(
        GA_CONTAINERAPP_EXTENSION_NAME, "azext_containerapp._params")
    azext_params.load_arguments(self, _)