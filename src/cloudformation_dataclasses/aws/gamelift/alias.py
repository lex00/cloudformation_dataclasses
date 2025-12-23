"""PropertyTypes for AWS::GameLift::Alias."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class RoutingStrategy(PropertyType):
    TYPE = "Type"
    MESSAGE = "Message"
    FLEET_ID = "FleetId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "message": "Message",
        "fleet_id": "FleetId",
    }

    type_: Optional[Union[str, RoutingStrategyType, Ref, GetAtt, Sub]] = None
    message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    fleet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

