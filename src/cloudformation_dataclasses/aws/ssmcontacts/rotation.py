"""PropertyTypes for AWS::SSMContacts::Rotation."""

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
class CoverageTime(PropertyType):
    END_TIME = "EndTime"
    START_TIME = "StartTime"

    _property_mappings: ClassVar[dict[str, str]] = {
        "end_time": "EndTime",
        "start_time": "StartTime",
    }

    end_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MonthlySetting(PropertyType):
    DAY_OF_MONTH = "DayOfMonth"
    HAND_OFF_TIME = "HandOffTime"

    _property_mappings: ClassVar[dict[str, str]] = {
        "day_of_month": "DayOfMonth",
        "hand_off_time": "HandOffTime",
    }

    day_of_month: Optional[Union[int, Ref, GetAtt, Sub]] = None
    hand_off_time: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RecurrenceSettings(PropertyType):
    DAILY_SETTINGS = "DailySettings"
    NUMBER_OF_ON_CALLS = "NumberOfOnCalls"
    SHIFT_COVERAGES = "ShiftCoverages"
    WEEKLY_SETTINGS = "WeeklySettings"
    RECURRENCE_MULTIPLIER = "RecurrenceMultiplier"
    MONTHLY_SETTINGS = "MonthlySettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "daily_settings": "DailySettings",
        "number_of_on_calls": "NumberOfOnCalls",
        "shift_coverages": "ShiftCoverages",
        "weekly_settings": "WeeklySettings",
        "recurrence_multiplier": "RecurrenceMultiplier",
        "monthly_settings": "MonthlySettings",
    }

    daily_settings: Optional[Union[list[str], Ref]] = None
    number_of_on_calls: Optional[Union[int, Ref, GetAtt, Sub]] = None
    shift_coverages: Optional[list[ShiftCoverage]] = None
    weekly_settings: Optional[list[WeeklySetting]] = None
    recurrence_multiplier: Optional[Union[int, Ref, GetAtt, Sub]] = None
    monthly_settings: Optional[list[MonthlySetting]] = None


@dataclass
class ShiftCoverage(PropertyType):
    DAY_OF_WEEK = "DayOfWeek"
    COVERAGE_TIMES = "CoverageTimes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "day_of_week": "DayOfWeek",
        "coverage_times": "CoverageTimes",
    }

    day_of_week: Optional[Union[str, Ref, GetAtt, Sub]] = None
    coverage_times: Optional[list[CoverageTime]] = None


@dataclass
class WeeklySetting(PropertyType):
    DAY_OF_WEEK = "DayOfWeek"
    HAND_OFF_TIME = "HandOffTime"

    _property_mappings: ClassVar[dict[str, str]] = {
        "day_of_week": "DayOfWeek",
        "hand_off_time": "HandOffTime",
    }

    day_of_week: Optional[Union[str, DayOfWeek, Ref, GetAtt, Sub]] = None
    hand_off_time: Optional[Union[str, Ref, GetAtt, Sub]] = None

