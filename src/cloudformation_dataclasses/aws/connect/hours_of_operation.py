"""PropertyTypes for AWS::Connect::HoursOfOperation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class HoursOfOperationConfig(PropertyType):
    END_TIME = "EndTime"
    START_TIME = "StartTime"
    DAY = "Day"

    _property_mappings: ClassVar[dict[str, str]] = {
        "end_time": "EndTime",
        "start_time": "StartTime",
        "day": "Day",
    }

    end_time: Optional[HoursOfOperationTimeSlice] = None
    start_time: Optional[HoursOfOperationTimeSlice] = None
    day: Optional[Union[str, HoursOfOperationDays, Ref, GetAtt, Sub]] = None


@dataclass
class HoursOfOperationOverride(PropertyType):
    HOURS_OF_OPERATION_OVERRIDE_ID = "HoursOfOperationOverrideId"
    OVERRIDE_CONFIG = "OverrideConfig"
    EFFECTIVE_FROM = "EffectiveFrom"
    OVERRIDE_NAME = "OverrideName"
    OVERRIDE_DESCRIPTION = "OverrideDescription"
    EFFECTIVE_TILL = "EffectiveTill"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hours_of_operation_override_id": "HoursOfOperationOverrideId",
        "override_config": "OverrideConfig",
        "effective_from": "EffectiveFrom",
        "override_name": "OverrideName",
        "override_description": "OverrideDescription",
        "effective_till": "EffectiveTill",
    }

    hours_of_operation_override_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    override_config: Optional[list[HoursOfOperationOverrideConfig]] = None
    effective_from: Optional[Union[str, Ref, GetAtt, Sub]] = None
    override_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    override_description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    effective_till: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HoursOfOperationOverrideConfig(PropertyType):
    END_TIME = "EndTime"
    START_TIME = "StartTime"
    DAY = "Day"

    _property_mappings: ClassVar[dict[str, str]] = {
        "end_time": "EndTime",
        "start_time": "StartTime",
        "day": "Day",
    }

    end_time: Optional[OverrideTimeSlice] = None
    start_time: Optional[OverrideTimeSlice] = None
    day: Optional[Union[str, OverrideDays, Ref, GetAtt, Sub]] = None


@dataclass
class HoursOfOperationTimeSlice(PropertyType):
    HOURS = "Hours"
    MINUTES = "Minutes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hours": "Hours",
        "minutes": "Minutes",
    }

    hours: Optional[Union[int, Ref, GetAtt, Sub]] = None
    minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class OverrideTimeSlice(PropertyType):
    HOURS = "Hours"
    MINUTES = "Minutes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hours": "Hours",
        "minutes": "Minutes",
    }

    hours: Optional[Union[int, Ref, GetAtt, Sub]] = None
    minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None

