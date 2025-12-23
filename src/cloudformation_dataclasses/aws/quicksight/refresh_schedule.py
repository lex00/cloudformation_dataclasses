"""PropertyTypes for AWS::QuickSight::RefreshSchedule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class RefreshOnDay(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "day_of_week": "DayOfWeek",
        "day_of_month": "DayOfMonth",
    }

    day_of_week: Optional[Union[str, Ref, GetAtt, Sub]] = None
    day_of_month: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RefreshScheduleMap(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "start_after_date_time": "StartAfterDateTime",
        "schedule_id": "ScheduleId",
        "schedule_frequency": "ScheduleFrequency",
        "refresh_type": "RefreshType",
    }

    start_after_date_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schedule_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schedule_frequency: Optional[ScheduleFrequency] = None
    refresh_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScheduleFrequency(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "time_zone": "TimeZone",
        "refresh_on_day": "RefreshOnDay",
        "time_of_the_day": "TimeOfTheDay",
        "interval": "Interval",
    }

    time_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    refresh_on_day: Optional[RefreshOnDay] = None
    time_of_the_day: Optional[Union[str, Ref, GetAtt, Sub]] = None
    interval: Optional[Union[str, Ref, GetAtt, Sub]] = None

