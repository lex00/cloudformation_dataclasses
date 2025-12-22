"""PropertyTypes for AWS::ARCZonalShift::ZonalAutoshiftConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ControlCondition(PropertyType):
    TYPE = "Type"
    ALARM_IDENTIFIER = "AlarmIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "alarm_identifier": "AlarmIdentifier",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    alarm_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PracticeRunConfiguration(PropertyType):
    BLOCKED_DATES = "BlockedDates"
    OUTCOME_ALARMS = "OutcomeAlarms"
    BLOCKING_ALARMS = "BlockingAlarms"
    BLOCKED_WINDOWS = "BlockedWindows"

    _property_mappings: ClassVar[dict[str, str]] = {
        "blocked_dates": "BlockedDates",
        "outcome_alarms": "OutcomeAlarms",
        "blocking_alarms": "BlockingAlarms",
        "blocked_windows": "BlockedWindows",
    }

    blocked_dates: Optional[Union[list[str], Ref]] = None
    outcome_alarms: Optional[list[ControlCondition]] = None
    blocking_alarms: Optional[list[ControlCondition]] = None
    blocked_windows: Optional[Union[list[str], Ref]] = None

