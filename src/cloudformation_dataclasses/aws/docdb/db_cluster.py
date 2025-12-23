"""PropertyTypes for AWS::DocDB::DBCluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ServerlessV2ScalingConfiguration(PropertyType):
    MIN_CAPACITY = "MinCapacity"
    MAX_CAPACITY = "MaxCapacity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min_capacity": "MinCapacity",
        "max_capacity": "MaxCapacity",
    }

    min_capacity: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max_capacity: Optional[Union[float, Ref, GetAtt, Sub]] = None

