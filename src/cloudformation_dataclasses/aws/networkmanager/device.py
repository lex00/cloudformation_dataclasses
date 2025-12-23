"""PropertyTypes for AWS::NetworkManager::Device."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AWSLocation(PropertyType):
    ZONE = "Zone"
    SUBNET_ARN = "SubnetArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "zone": "Zone",
        "subnet_arn": "SubnetArn",
    }

    zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subnet_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Location(PropertyType):
    ADDRESS = "Address"
    LATITUDE = "Latitude"
    LONGITUDE = "Longitude"

    _property_mappings: ClassVar[dict[str, str]] = {
        "address": "Address",
        "latitude": "Latitude",
        "longitude": "Longitude",
    }

    address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    latitude: Optional[Union[str, Ref, GetAtt, Sub]] = None
    longitude: Optional[Union[str, Ref, GetAtt, Sub]] = None

