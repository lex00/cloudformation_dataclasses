"""PropertyTypes for AWS::VerifiedPermissions::PolicyStore."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class BatchGetPolicyErrorCode:
    """BatchGetPolicyErrorCode enum values."""

    POLICY_STORE_NOT_FOUND = "POLICY_STORE_NOT_FOUND"
    POLICY_NOT_FOUND = "POLICY_NOT_FOUND"


class CedarVersion:
    """CedarVersion enum values."""

    CEDAR_2 = "CEDAR_2"
    CEDAR_4 = "CEDAR_4"


class Decision:
    """Decision enum values."""

    ALLOW = "ALLOW"
    DENY = "DENY"


class DeletionProtection:
    """DeletionProtection enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class OpenIdIssuer:
    """OpenIdIssuer enum values."""

    COGNITO = "COGNITO"


class PolicyEffect:
    """PolicyEffect enum values."""

    PERMIT = "Permit"
    FORBID = "Forbid"


class PolicyType:
    """PolicyType enum values."""

    STATIC = "STATIC"
    TEMPLATE_LINKED = "TEMPLATE_LINKED"


class ResourceType:
    """ResourceType enum values."""

    IDENTITY_SOURCE = "IDENTITY_SOURCE"
    POLICY_STORE = "POLICY_STORE"
    POLICY = "POLICY"
    POLICY_TEMPLATE = "POLICY_TEMPLATE"
    SCHEMA = "SCHEMA"


class ValidationMode:
    """ValidationMode enum values."""

    OFF = "OFF"
    STRICT = "STRICT"


@dataclass
class DeletionProtection(PropertyType):
    MODE = "Mode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
    }

    mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SchemaDefinition(PropertyType):
    CEDAR_JSON = "CedarJson"
    CEDAR_FORMAT = "CedarFormat"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cedar_json": "CedarJson",
        "cedar_format": "CedarFormat",
    }

    cedar_json: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cedar_format: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ValidationSettings(PropertyType):
    MODE = "Mode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
    }

    mode: Optional[Union[str, Ref, GetAtt, Sub]] = None

