"""PropertyTypes for AWS::ECS::ClusterCapacityProviderAssociations."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CapacityProviderStrategy(PropertyType):
    CAPACITY_PROVIDER = "CapacityProvider"
    BASE = "Base"
    WEIGHT = "Weight"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_provider": "CapacityProvider",
        "base": "Base",
        "weight": "Weight",
    }

    capacity_provider: Optional[Union[str, Ref, GetAtt, Sub]] = None
    base: Optional[Union[int, Ref, GetAtt, Sub]] = None
    weight: Optional[Union[int, Ref, GetAtt, Sub]] = None

