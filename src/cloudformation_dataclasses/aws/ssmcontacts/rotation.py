"""PropertyTypes for AWS::SSMContacts::Rotation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CoverageTime(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "end_time": "EndTime",
        "start_time": "StartTime",
    }

    end_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MonthlySetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "day_of_month": "DayOfMonth",
        "hand_off_time": "HandOffTime",
    }

    day_of_month: Optional[Union[int, Ref, GetAtt, Sub]] = None
    hand_off_time: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RecurrenceSettings(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "day_of_week": "DayOfWeek",
        "coverage_times": "CoverageTimes",
    }

    day_of_week: Optional[Union[str, Ref, GetAtt, Sub]] = None
    coverage_times: Optional[list[CoverageTime]] = None


@dataclass
class WeeklySetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "day_of_week": "DayOfWeek",
        "hand_off_time": "HandOffTime",
    }

    day_of_week: Optional[Union[str, DayOfWeek, Ref, GetAtt, Sub]] = None
    hand_off_time: Optional[Union[str, Ref, GetAtt, Sub]] = None

