"""PropertyTypes for AWS::AppIntegrations::Application."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ApplicationType:
    """ApplicationType enum values."""

    STANDARD = "STANDARD"
    SERVICE = "SERVICE"
    MCP_SERVER = "MCP_SERVER"


class ContactHandlingScope:
    """ContactHandlingScope enum values."""

    CROSS_CONTACTS = "CROSS_CONTACTS"
    PER_CONTACT = "PER_CONTACT"


class ExecutionMode:
    """ExecutionMode enum values."""

    ON_DEMAND = "ON_DEMAND"
    SCHEDULED = "SCHEDULED"


class ExecutionStatus:
    """ExecutionStatus enum values."""

    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"


@dataclass
class ApplicationConfig(PropertyType):
    CONTACT_HANDLING = "ContactHandling"

    _property_mappings: ClassVar[dict[str, str]] = {
        "contact_handling": "ContactHandling",
    }

    contact_handling: Optional[ContactHandling] = None


@dataclass
class ApplicationSourceConfig(PropertyType):
    EXTERNAL_URL_CONFIG = "ExternalUrlConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "external_url_config": "ExternalUrlConfig",
    }

    external_url_config: Optional[ExternalUrlConfig] = None


@dataclass
class ContactHandling(PropertyType):
    SCOPE = "Scope"

    _property_mappings: ClassVar[dict[str, str]] = {
        "scope": "Scope",
    }

    scope: Optional[Union[str, ContactHandlingScope, Ref, GetAtt, Sub]] = None


@dataclass
class ExternalUrlConfig(PropertyType):
    APPROVED_ORIGINS = "ApprovedOrigins"
    ACCESS_URL = "AccessUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "approved_origins": "ApprovedOrigins",
        "access_url": "AccessUrl",
    }

    approved_origins: Optional[Union[list[str], Ref]] = None
    access_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IframeConfig(PropertyType):
    ALLOW = "Allow"
    SANDBOX = "Sandbox"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allow": "Allow",
        "sandbox": "Sandbox",
    }

    allow: Optional[Union[list[str], Ref]] = None
    sandbox: Optional[Union[list[str], Ref]] = None

