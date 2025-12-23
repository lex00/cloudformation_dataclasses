"""PropertyTypes for AWS::Batch::ServiceEnvironment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CapacityLimit(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_unit": "CapacityUnit",
        "max_capacity": "MaxCapacity",
    }

    capacity_unit: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None

