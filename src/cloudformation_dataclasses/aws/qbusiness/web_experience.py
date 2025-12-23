"""PropertyTypes for AWS::QBusiness::WebExperience."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BrowserExtensionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled_browser_extensions": "EnabledBrowserExtensions",
    }

    enabled_browser_extensions: Optional[Union[list[str], Ref]] = None


@dataclass
class CustomizationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "favicon_url": "FaviconUrl",
        "font_url": "FontUrl",
        "custom_css_url": "CustomCSSUrl",
        "logo_url": "LogoUrl",
    }

    favicon_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    font_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_css_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    logo_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IdentityProviderConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "open_id_connect_configuration": "OpenIDConnectConfiguration",
        "saml_configuration": "SamlConfiguration",
    }

    open_id_connect_configuration: Optional[OpenIDConnectProviderConfiguration] = None
    saml_configuration: Optional[SamlProviderConfiguration] = None


@dataclass
class OpenIDConnectProviderConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secrets_arn": "SecretsArn",
        "secrets_role": "SecretsRole",
    }

    secrets_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_role: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SamlProviderConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "authentication_url": "AuthenticationUrl",
    }

    authentication_url: Optional[Union[str, Ref, GetAtt, Sub]] = None

