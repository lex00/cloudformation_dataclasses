"""PropertyTypes for AWS::MediaConvert::JobTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccelerationSettings(PropertyType):
    MODE = "Mode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
    }

    mode: Optional[Union[str, AccelerationMode, Ref, GetAtt, Sub]] = None


@dataclass
class HopDestination(PropertyType):
    WAIT_MINUTES = "WaitMinutes"
    PRIORITY = "Priority"
    QUEUE = "Queue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "wait_minutes": "WaitMinutes",
        "priority": "Priority",
        "queue": "Queue",
    }

    wait_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None
    queue: Optional[Union[str, Ref, GetAtt, Sub]] = None

