"""PropertyTypes for AWS::AppIntegrations::Application."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ApplicationConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "contact_handling": "ContactHandling",
    }

    contact_handling: Optional[ContactHandling] = None


@dataclass
class ApplicationSourceConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "external_url_config": "ExternalUrlConfig",
    }

    external_url_config: Optional[ExternalUrlConfig] = None


@dataclass
class ContactHandling(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scope": "Scope",
    }

    scope: Optional[Union[str, ContactHandlingScope, Ref, GetAtt, Sub]] = None


@dataclass
class ExternalUrlConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "approved_origins": "ApprovedOrigins",
        "access_url": "AccessUrl",
    }

    approved_origins: Optional[Union[list[str], Ref]] = None
    access_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IframeConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allow": "Allow",
        "sandbox": "Sandbox",
    }

    allow: Optional[Union[list[str], Ref]] = None
    sandbox: Optional[Union[list[str], Ref]] = None

