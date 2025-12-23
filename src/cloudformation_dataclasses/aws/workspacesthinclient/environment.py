"""PropertyTypes for AWS::WorkSpacesThinClient::Environment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MaintenanceWindow(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "end_time_minute": "EndTimeMinute",
        "type_": "Type",
        "days_of_the_week": "DaysOfTheWeek",
        "apply_time_of": "ApplyTimeOf",
        "start_time_minute": "StartTimeMinute",
        "start_time_hour": "StartTimeHour",
        "end_time_hour": "EndTimeHour",
    }

    end_time_minute: Optional[Union[int, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    days_of_the_week: Optional[Union[list[str], Ref]] = None
    apply_time_of: Optional[Union[str, Ref, GetAtt, Sub]] = None
    start_time_minute: Optional[Union[int, Ref, GetAtt, Sub]] = None
    start_time_hour: Optional[Union[int, Ref, GetAtt, Sub]] = None
    end_time_hour: Optional[Union[int, Ref, GetAtt, Sub]] = None

