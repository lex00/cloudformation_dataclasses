"""PropertyTypes for AWS::CloudTrail::Channel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Destination(PropertyType):
    TYPE = "Type"
    LOCATION = "Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "location": "Location",
    }

    type_: Optional[Union[str, DestinationType, Ref, GetAtt, Sub]] = None
    location: Optional[Union[str, Ref, GetAtt, Sub]] = None

