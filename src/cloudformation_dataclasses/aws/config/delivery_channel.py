"""PropertyTypes for AWS::Config::DeliveryChannel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConfigSnapshotDeliveryProperties(PropertyType):
    DELIVERY_FREQUENCY = "DeliveryFrequency"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delivery_frequency": "DeliveryFrequency",
    }

    delivery_frequency: Optional[Union[str, Ref, GetAtt, Sub]] = None

