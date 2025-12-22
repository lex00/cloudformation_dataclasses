"""PropertyTypes for AWS::SSMContacts::Contact."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AcceptCodeValidation:
    """AcceptCodeValidation enum values."""

    IGNORE = "IGNORE"
    ENFORCE = "ENFORCE"


class AcceptType:
    """AcceptType enum values."""

    DELIVERED = "DELIVERED"
    READ = "READ"


class ActivationStatus:
    """ActivationStatus enum values."""

    ACTIVATED = "ACTIVATED"
    NOT_ACTIVATED = "NOT_ACTIVATED"


class ChannelType:
    """ChannelType enum values."""

    SMS = "SMS"
    VOICE = "VOICE"
    EMAIL = "EMAIL"


class ContactType:
    """ContactType enum values."""

    PERSONAL = "PERSONAL"
    ESCALATION = "ESCALATION"
    ONCALL_SCHEDULE = "ONCALL_SCHEDULE"


class DayOfWeek:
    """DayOfWeek enum values."""

    MON = "MON"
    TUE = "TUE"
    WED = "WED"
    THU = "THU"
    FRI = "FRI"
    SAT = "SAT"
    SUN = "SUN"


class ReceiptType:
    """ReceiptType enum values."""

    DELIVERED = "DELIVERED"
    ERROR = "ERROR"
    READ = "READ"
    SENT = "SENT"
    STOP = "STOP"


class ShiftType:
    """ShiftType enum values."""

    REGULAR = "REGULAR"
    OVERRIDDEN = "OVERRIDDEN"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWN_OPERATION = "UNKNOWN_OPERATION"
    CANNOT_PARSE = "CANNOT_PARSE"
    FIELD_VALIDATION_FAILED = "FIELD_VALIDATION_FAILED"
    OTHER = "OTHER"


@dataclass
class ChannelTargetInfo(PropertyType):
    RETRY_INTERVAL_IN_MINUTES = "RetryIntervalInMinutes"
    CHANNEL_ID = "ChannelId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "retry_interval_in_minutes": "RetryIntervalInMinutes",
        "channel_id": "ChannelId",
    }

    retry_interval_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    channel_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ContactTargetInfo(PropertyType):
    CONTACT_ID = "ContactId"
    IS_ESSENTIAL = "IsEssential"

    _property_mappings: ClassVar[dict[str, str]] = {
        "contact_id": "ContactId",
        "is_essential": "IsEssential",
    }

    contact_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_essential: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Stage(PropertyType):
    DURATION_IN_MINUTES = "DurationInMinutes"
    ROTATION_IDS = "RotationIds"
    TARGETS = "Targets"

    _property_mappings: ClassVar[dict[str, str]] = {
        "duration_in_minutes": "DurationInMinutes",
        "rotation_ids": "RotationIds",
        "targets": "Targets",
    }

    duration_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rotation_ids: Optional[Union[list[str], Ref]] = None
    targets: Optional[list[Targets]] = None


@dataclass
class Targets(PropertyType):
    CHANNEL_TARGET_INFO = "ChannelTargetInfo"
    CONTACT_TARGET_INFO = "ContactTargetInfo"

    _property_mappings: ClassVar[dict[str, str]] = {
        "channel_target_info": "ChannelTargetInfo",
        "contact_target_info": "ContactTargetInfo",
    }

    channel_target_info: Optional[ChannelTargetInfo] = None
    contact_target_info: Optional[ContactTargetInfo] = None

