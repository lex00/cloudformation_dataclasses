"""PropertyTypes for AWS::ODB::CloudExadataInfrastructure."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CustomerContact(PropertyType):
    EMAIL = "Email"

    _property_mappings: ClassVar[dict[str, str]] = {
        "email": "Email",
    }

    email: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MaintenanceWindow(PropertyType):
    CUSTOM_ACTION_TIMEOUT_IN_MINS = "CustomActionTimeoutInMins"
    DAYS_OF_WEEK = "DaysOfWeek"
    PREFERENCE = "Preference"
    LEAD_TIME_IN_WEEKS = "LeadTimeInWeeks"
    MONTHS = "Months"
    PATCHING_MODE = "PatchingMode"
    WEEKS_OF_MONTH = "WeeksOfMonth"
    IS_CUSTOM_ACTION_TIMEOUT_ENABLED = "IsCustomActionTimeoutEnabled"
    HOURS_OF_DAY = "HoursOfDay"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_action_timeout_in_mins": "CustomActionTimeoutInMins",
        "days_of_week": "DaysOfWeek",
        "preference": "Preference",
        "lead_time_in_weeks": "LeadTimeInWeeks",
        "months": "Months",
        "patching_mode": "PatchingMode",
        "weeks_of_month": "WeeksOfMonth",
        "is_custom_action_timeout_enabled": "IsCustomActionTimeoutEnabled",
        "hours_of_day": "HoursOfDay",
    }

    custom_action_timeout_in_mins: Optional[Union[int, Ref, GetAtt, Sub]] = None
    days_of_week: Optional[Union[list[str], Ref]] = None
    preference: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lead_time_in_weeks: Optional[Union[int, Ref, GetAtt, Sub]] = None
    months: Optional[Union[list[str], Ref]] = None
    patching_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    weeks_of_month: Optional[Union[list[int], Ref]] = None
    is_custom_action_timeout_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    hours_of_day: Optional[Union[list[int], Ref]] = None

