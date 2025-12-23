"""PropertyTypes for AWS::Route53::RecordSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AliasTarget(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dns_name": "DNSName",
        "evaluate_target_health": "EvaluateTargetHealth",
        "hosted_zone_id": "HostedZoneId",
    }

    dns_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    evaluate_target_health: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    hosted_zone_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CidrRoutingConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "collection_id": "CollectionId",
        "location_name": "LocationName",
    }

    collection_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    location_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Coordinates(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "latitude": "Latitude",
        "longitude": "Longitude",
    }

    latitude: Optional[Union[str, Ref, GetAtt, Sub]] = None
    longitude: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GeoLocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "continent_code": "ContinentCode",
        "country_code": "CountryCode",
        "subdivision_code": "SubdivisionCode",
    }

    continent_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    country_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subdivision_code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GeoProximityLocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_region": "AWSRegion",
        "bias": "Bias",
        "coordinates": "Coordinates",
        "local_zone_group": "LocalZoneGroup",
    }

    aws_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bias: Optional[Union[int, Ref, GetAtt, Sub]] = None
    coordinates: Optional[Coordinates] = None
    local_zone_group: Optional[Union[str, Ref, GetAtt, Sub]] = None

