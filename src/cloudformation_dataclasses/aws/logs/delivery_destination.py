"""PropertyTypes for AWS::Logs::DeliveryDestination."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DestinationPolicy(PropertyType):
    DELIVERY_DESTINATION_NAME = "DeliveryDestinationName"
    DELIVERY_DESTINATION_POLICY = "DeliveryDestinationPolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delivery_destination_name": "DeliveryDestinationName",
        "delivery_destination_policy": "DeliveryDestinationPolicy",
    }

    delivery_destination_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    delivery_destination_policy: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None

