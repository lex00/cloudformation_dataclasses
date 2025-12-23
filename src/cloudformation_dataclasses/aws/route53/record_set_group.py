"""PropertyTypes for AWS::Route53::RecordSetGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AliasTarget(PropertyType):
    DNS_NAME = "DNSName"
    EVALUATE_TARGET_HEALTH = "EvaluateTargetHealth"
    HOSTED_ZONE_ID = "HostedZoneId"

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
    COLLECTION_ID = "CollectionId"
    LOCATION_NAME = "LocationName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "collection_id": "CollectionId",
        "location_name": "LocationName",
    }

    collection_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    location_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Coordinates(PropertyType):
    LATITUDE = "Latitude"
    LONGITUDE = "Longitude"

    _property_mappings: ClassVar[dict[str, str]] = {
        "latitude": "Latitude",
        "longitude": "Longitude",
    }

    latitude: Optional[Union[str, Ref, GetAtt, Sub]] = None
    longitude: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GeoLocation(PropertyType):
    CONTINENT_CODE = "ContinentCode"
    COUNTRY_CODE = "CountryCode"
    SUBDIVISION_CODE = "SubdivisionCode"

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
    AWS_REGION = "AWSRegion"
    BIAS = "Bias"
    COORDINATES = "Coordinates"
    LOCAL_ZONE_GROUP = "LocalZoneGroup"

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


@dataclass
class RecordSet(PropertyType):
    ALIAS_TARGET = "AliasTarget"
    CIDR_ROUTING_CONFIG = "CidrRoutingConfig"
    FAILOVER = "Failover"
    GEO_LOCATION = "GeoLocation"
    GEO_PROXIMITY_LOCATION = "GeoProximityLocation"
    HEALTH_CHECK_ID = "HealthCheckId"
    HOSTED_ZONE_ID = "HostedZoneId"
    HOSTED_ZONE_NAME = "HostedZoneName"
    MULTI_VALUE_ANSWER = "MultiValueAnswer"
    NAME = "Name"
    REGION = "Region"
    RESOURCE_RECORDS = "ResourceRecords"
    SET_IDENTIFIER = "SetIdentifier"
    TTL = "TTL"
    TYPE = "Type"
    WEIGHT = "Weight"

    _property_mappings: ClassVar[dict[str, str]] = {
        "alias_target": "AliasTarget",
        "cidr_routing_config": "CidrRoutingConfig",
        "failover": "Failover",
        "geo_location": "GeoLocation",
        "geo_proximity_location": "GeoProximityLocation",
        "health_check_id": "HealthCheckId",
        "hosted_zone_id": "HostedZoneId",
        "hosted_zone_name": "HostedZoneName",
        "multi_value_answer": "MultiValueAnswer",
        "name": "Name",
        "region": "Region",
        "resource_records": "ResourceRecords",
        "set_identifier": "SetIdentifier",
        "ttl": "TTL",
        "type_": "Type",
        "weight": "Weight",
    }

    alias_target: Optional[AliasTarget] = None
    cidr_routing_config: Optional[CidrRoutingConfig] = None
    failover: Optional[Union[str, Ref, GetAtt, Sub]] = None
    geo_location: Optional[GeoLocation] = None
    geo_proximity_location: Optional[GeoProximityLocation] = None
    health_check_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hosted_zone_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hosted_zone_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    multi_value_answer: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_records: Optional[Union[list[str], Ref]] = None
    set_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ttl: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    weight: Optional[Union[int, Ref, GetAtt, Sub]] = None

