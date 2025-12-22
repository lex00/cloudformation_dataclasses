"""PropertyTypes for AWS::VerifiedPermissions::Policy."""

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
class EntityIdentifier(PropertyType):
    ENTITY_TYPE = "EntityType"
    ENTITY_ID = "EntityId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entity_type": "EntityType",
        "entity_id": "EntityId",
    }

    entity_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    entity_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PolicyDefinition(PropertyType):
    STATIC = "Static"
    TEMPLATE_LINKED = "TemplateLinked"

    _property_mappings: ClassVar[dict[str, str]] = {
        "static": "Static",
        "template_linked": "TemplateLinked",
    }

    static: Optional[StaticPolicyDefinition] = None
    template_linked: Optional[TemplateLinkedPolicyDefinition] = None


@dataclass
class StaticPolicyDefinition(PropertyType):
    DESCRIPTION = "Description"
    STATEMENT = "Statement"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "statement": "Statement",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    statement: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TemplateLinkedPolicyDefinition(PropertyType):
    RESOURCE = "Resource"
    POLICY_TEMPLATE_ID = "PolicyTemplateId"
    PRINCIPAL = "Principal"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource": "Resource",
        "policy_template_id": "PolicyTemplateId",
        "principal": "Principal",
    }

    resource: Optional[EntityIdentifier] = None
    policy_template_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    principal: Optional[EntityIdentifier] = None

