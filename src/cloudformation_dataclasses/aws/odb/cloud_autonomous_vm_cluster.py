"""PropertyTypes for AWS::ODB::CloudAutonomousVmCluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MaintenanceWindow(PropertyType):
    DAYS_OF_WEEK = "DaysOfWeek"
    PREFERENCE = "Preference"
    LEAD_TIME_IN_WEEKS = "LeadTimeInWeeks"
    MONTHS = "Months"
    WEEKS_OF_MONTH = "WeeksOfMonth"
    HOURS_OF_DAY = "HoursOfDay"

    _property_mappings: ClassVar[dict[str, str]] = {
        "days_of_week": "DaysOfWeek",
        "preference": "Preference",
        "lead_time_in_weeks": "LeadTimeInWeeks",
        "months": "Months",
        "weeks_of_month": "WeeksOfMonth",
        "hours_of_day": "HoursOfDay",
    }

    days_of_week: Optional[Union[list[str], Ref]] = None
    preference: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lead_time_in_weeks: Optional[Union[int, Ref, GetAtt, Sub]] = None
    months: Optional[Union[list[str], Ref]] = None
    weeks_of_month: Optional[Union[list[int], Ref]] = None
    hours_of_day: Optional[Union[list[int], Ref]] = None

