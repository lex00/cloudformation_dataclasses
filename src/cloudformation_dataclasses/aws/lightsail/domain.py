"""PropertyTypes for AWS::Lightsail::Domain."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DomainEntry(PropertyType):
    TARGET = "Target"
    TYPE = "Type"
    ID = "Id"
    IS_ALIAS = "IsAlias"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target": "Target",
        "type_": "Type",
        "id": "Id",
        "is_alias": "IsAlias",
        "name": "Name",
    }

    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_alias: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Location(PropertyType):
    REGION_NAME = "RegionName"
    AVAILABILITY_ZONE = "AvailabilityZone"

    _property_mappings: ClassVar[dict[str, str]] = {
        "region_name": "RegionName",
        "availability_zone": "AvailabilityZone",
    }

    region_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None

