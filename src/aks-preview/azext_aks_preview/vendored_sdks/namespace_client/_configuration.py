# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.8.4, generator: @autorest/python@5.16.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

    from azure.core.credentials import TokenCredential

VERSION = "unknown"

class NamespaceClientConfiguration(Configuration):  # pylint: disable=too-many-instance-attributes
    """Configuration for NamespaceClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g.
     00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :keyword api_version: Api Version. Default value is "2021-12-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        super(NamespaceClientConfiguration, self).__init__(**kwargs)
        api_version = kwargs.pop('api_version', "2021-12-01-preview")  # type: str

        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")

        self.credential = credential
        self.subscription_id = subscription_id
        self.api_version = api_version
        self.credential_scopes = kwargs.pop('credential_scopes', [])
        kwargs.setdefault('sdk_moniker', 'namespaceclient/{}'.format(VERSION))
        self._configure(**kwargs)

    def _configure(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        self.user_agent_policy = kwargs.get('user_agent_policy') or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get('headers_policy') or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get('proxy_policy') or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get('logging_policy') or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get('http_logging_policy') or policies.HttpLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get('retry_policy') or policies.RetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get('custom_hook_policy') or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get('redirect_policy') or policies.RedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get('authentication_policy')
        if not self.credential_scopes and not self.authentication_policy:
            raise ValueError("You must provide either credential_scopes or authentication_policy as kwargs")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = policies.BearerTokenCredentialPolicy(self.credential, *self.credential_scopes, **kwargs)
