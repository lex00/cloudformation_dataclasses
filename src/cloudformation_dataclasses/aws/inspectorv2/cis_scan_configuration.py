"""PropertyTypes for AWS::InspectorV2::CisScanConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CisTargets(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_resource_tags": "TargetResourceTags",
        "account_ids": "AccountIds",
    }

    target_resource_tags: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    account_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class DailySchedule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "start_time": "StartTime",
    }

    start_time: Optional[Time] = None


@dataclass
class MonthlySchedule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "start_time": "StartTime",
        "day": "Day",
    }

    start_time: Optional[Time] = None
    day: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Schedule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "daily": "Daily",
        "monthly": "Monthly",
        "weekly": "Weekly",
        "one_time": "OneTime",
    }

    daily: Optional[DailySchedule] = None
    monthly: Optional[MonthlySchedule] = None
    weekly: Optional[WeeklySchedule] = None
    one_time: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class Time(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "time_of_day": "TimeOfDay",
        "time_zone": "TimeZone",
    }

    time_of_day: Optional[Union[str, Ref, GetAtt, Sub]] = None
    time_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WeeklySchedule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "days": "Days",
        "start_time": "StartTime",
    }

    days: Optional[Union[list[str], Ref]] = None
    start_time: Optional[Time] = None

