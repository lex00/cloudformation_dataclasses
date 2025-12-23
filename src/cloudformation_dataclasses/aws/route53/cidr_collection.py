"""PropertyTypes for AWS::Route53::CidrCollection."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Location(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cidr_list": "CidrList",
        "location_name": "LocationName",
    }

    cidr_list: Optional[Union[list[str], Ref]] = None
    location_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

