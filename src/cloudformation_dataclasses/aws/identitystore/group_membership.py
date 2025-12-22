"""PropertyTypes for AWS::IdentityStore::GroupMembership."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccessDeniedExceptionReason:
    """AccessDeniedExceptionReason enum values."""

    KMS_ACCESS_DENIED = "KMS_ACCESS_DENIED"


class ConflictExceptionReason:
    """ConflictExceptionReason enum values."""

    UNIQUENESS_CONSTRAINT_VIOLATION = "UNIQUENESS_CONSTRAINT_VIOLATION"
    CONCURRENT_MODIFICATION = "CONCURRENT_MODIFICATION"


class ResourceNotFoundExceptionReason:
    """ResourceNotFoundExceptionReason enum values."""

    KMS_KEY_NOT_FOUND = "KMS_KEY_NOT_FOUND"


class ResourceType:
    """ResourceType enum values."""

    GROUP = "GROUP"
    USER = "USER"
    IDENTITY_STORE = "IDENTITY_STORE"
    GROUP_MEMBERSHIP = "GROUP_MEMBERSHIP"
    RESOURCE_POLICY = "RESOURCE_POLICY"


class ThrottlingExceptionReason:
    """ThrottlingExceptionReason enum values."""

    KMS_THROTTLING = "KMS_THROTTLING"


class UserStatus:
    """UserStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    KMS_INVALID_ARN = "KMS_INVALID_ARN"
    KMS_INVALID_KEY_USAGE = "KMS_INVALID_KEY_USAGE"
    KMS_INVALID_STATE = "KMS_INVALID_STATE"
    KMS_DISABLED = "KMS_DISABLED"


@dataclass
class MemberId(PropertyType):
    USER_ID = "UserId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "user_id": "UserId",
    }

    user_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

