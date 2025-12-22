"""PropertyTypes for AWS::IVSChat::Room."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ChatTokenCapability:
    """ChatTokenCapability enum values."""

    SEND_MESSAGE = "SEND_MESSAGE"
    DISCONNECT_USER = "DISCONNECT_USER"
    DELETE_MESSAGE = "DELETE_MESSAGE"


class CreateLoggingConfigurationState:
    """CreateLoggingConfigurationState enum values."""

    ACTIVE = "ACTIVE"


class FallbackResult:
    """FallbackResult enum values."""

    ALLOW = "ALLOW"
    DENY = "DENY"


class LoggingConfigurationState:
    """LoggingConfigurationState enum values."""

    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"
    UPDATING = "UPDATING"
    UPDATE_FAILED = "UPDATE_FAILED"
    ACTIVE = "ACTIVE"


class ResourceType:
    """ResourceType enum values."""

    ROOM = "ROOM"


class UpdateLoggingConfigurationState:
    """UpdateLoggingConfigurationState enum values."""

    ACTIVE = "ACTIVE"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWN_OPERATION = "UNKNOWN_OPERATION"
    FIELD_VALIDATION_FAILED = "FIELD_VALIDATION_FAILED"
    OTHER = "OTHER"


@dataclass
class MessageReviewHandler(PropertyType):
    FALLBACK_RESULT = "FallbackResult"
    URI = "Uri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fallback_result": "FallbackResult",
        "uri": "Uri",
    }

    fallback_result: Optional[Union[str, Ref, GetAtt, Sub]] = None
    uri: Optional[Union[str, Ref, GetAtt, Sub]] = None

