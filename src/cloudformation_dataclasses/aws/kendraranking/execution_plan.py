"""PropertyTypes for AWS::KendraRanking::ExecutionPlan."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CapacityUnitsConfiguration(PropertyType):
    RESCORE_CAPACITY_UNITS = "RescoreCapacityUnits"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rescore_capacity_units": "RescoreCapacityUnits",
    }

    rescore_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None

