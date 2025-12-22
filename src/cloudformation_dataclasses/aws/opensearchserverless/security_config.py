"""PropertyTypes for AWS::OpenSearchServerless::SecurityConfig."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccessPolicyType:
    """AccessPolicyType enum values."""

    DATA = "data"


class CollectionStatus:
    """CollectionStatus enum values."""

    CREATING = "CREATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"


class CollectionType:
    """CollectionType enum values."""

    SEARCH = "SEARCH"
    TIMESERIES = "TIMESERIES"
    VECTORSEARCH = "VECTORSEARCH"


class IamIdentityCenterGroupAttribute:
    """IamIdentityCenterGroupAttribute enum values."""

    GROUPID = "GroupId"
    GROUPNAME = "GroupName"


class IamIdentityCenterUserAttribute:
    """IamIdentityCenterUserAttribute enum values."""

    USERID = "UserId"
    USERNAME = "UserName"
    EMAIL = "Email"


class LifecyclePolicyType:
    """LifecyclePolicyType enum values."""

    RETENTION = "retention"


class ResourceType:
    """ResourceType enum values."""

    INDEX = "index"


class SecurityConfigType:
    """SecurityConfigType enum values."""

    SAML = "saml"
    IAMIDENTITYCENTER = "iamidentitycenter"
    IAMFEDERATION = "iamfederation"


class SecurityPolicyType:
    """SecurityPolicyType enum values."""

    ENCRYPTION = "encryption"
    NETWORK = "network"


class ServerlessVectorAccelerationStatus:
    """ServerlessVectorAccelerationStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    ALLOWED = "ALLOWED"


class StandbyReplicas:
    """StandbyReplicas enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class VpcEndpointStatus:
    """VpcEndpointStatus enum values."""

    PENDING = "PENDING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"


@dataclass
class IamFederationConfigOptions(PropertyType):
    USER_ATTRIBUTE = "UserAttribute"
    GROUP_ATTRIBUTE = "GroupAttribute"

    _property_mappings: ClassVar[dict[str, str]] = {
        "user_attribute": "UserAttribute",
        "group_attribute": "GroupAttribute",
    }

    user_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IamIdentityCenterConfigOptions(PropertyType):
    APPLICATION_ARN = "ApplicationArn"
    APPLICATION_NAME = "ApplicationName"
    USER_ATTRIBUTE = "UserAttribute"
    INSTANCE_ARN = "InstanceArn"
    APPLICATION_DESCRIPTION = "ApplicationDescription"
    GROUP_ATTRIBUTE = "GroupAttribute"

    _property_mappings: ClassVar[dict[str, str]] = {
        "application_arn": "ApplicationArn",
        "application_name": "ApplicationName",
        "user_attribute": "UserAttribute",
        "instance_arn": "InstanceArn",
        "application_description": "ApplicationDescription",
        "group_attribute": "GroupAttribute",
    }

    application_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    application_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    application_description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SamlConfigOptions(PropertyType):
    SESSION_TIMEOUT = "SessionTimeout"
    OPEN_SEARCH_SERVERLESS_ENTITY_ID = "OpenSearchServerlessEntityId"
    USER_ATTRIBUTE = "UserAttribute"
    METADATA = "Metadata"
    GROUP_ATTRIBUTE = "GroupAttribute"

    _property_mappings: ClassVar[dict[str, str]] = {
        "session_timeout": "SessionTimeout",
        "open_search_serverless_entity_id": "OpenSearchServerlessEntityId",
        "user_attribute": "UserAttribute",
        "metadata": "Metadata",
        "group_attribute": "GroupAttribute",
    }

    session_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    open_search_serverless_entity_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metadata: Optional[Union[str, Ref, GetAtt, Sub]] = None
    group_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None

