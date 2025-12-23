"""PropertyTypes for AWS::Pinpoint::Segment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AttributeDimension(PropertyType):
    ATTRIBUTE_TYPE = "AttributeType"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_type": "AttributeType",
        "values": "Values",
    }

    attribute_type: Optional[Union[str, AttributeType, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class Behavior(PropertyType):
    RECENCY = "Recency"

    _property_mappings: ClassVar[dict[str, str]] = {
        "recency": "Recency",
    }

    recency: Optional[Recency] = None


@dataclass
class Coordinates(PropertyType):
    LATITUDE = "Latitude"
    LONGITUDE = "Longitude"

    _property_mappings: ClassVar[dict[str, str]] = {
        "latitude": "Latitude",
        "longitude": "Longitude",
    }

    latitude: Optional[Union[float, Ref, GetAtt, Sub]] = None
    longitude: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class Demographic(PropertyType):
    APP_VERSION = "AppVersion"
    DEVICE_TYPE = "DeviceType"
    PLATFORM = "Platform"
    CHANNEL = "Channel"
    MODEL = "Model"
    MAKE = "Make"

    _property_mappings: ClassVar[dict[str, str]] = {
        "app_version": "AppVersion",
        "device_type": "DeviceType",
        "platform": "Platform",
        "channel": "Channel",
        "model": "Model",
        "make": "Make",
    }

    app_version: Optional[SetDimension] = None
    device_type: Optional[SetDimension] = None
    platform: Optional[SetDimension] = None
    channel: Optional[SetDimension] = None
    model: Optional[SetDimension] = None
    make: Optional[SetDimension] = None


@dataclass
class GPSPoint(PropertyType):
    RANGE_IN_KILOMETERS = "RangeInKilometers"
    COORDINATES = "Coordinates"

    _property_mappings: ClassVar[dict[str, str]] = {
        "range_in_kilometers": "RangeInKilometers",
        "coordinates": "Coordinates",
    }

    range_in_kilometers: Optional[Union[float, Ref, GetAtt, Sub]] = None
    coordinates: Optional[Coordinates] = None


@dataclass
class Groups(PropertyType):
    TYPE = "Type"
    SOURCE_TYPE = "SourceType"
    DIMENSIONS = "Dimensions"
    SOURCE_SEGMENTS = "SourceSegments"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "source_type": "SourceType",
        "dimensions": "Dimensions",
        "source_segments": "SourceSegments",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimensions: Optional[list[SegmentDimensions]] = None
    source_segments: Optional[list[SourceSegments]] = None


@dataclass
class Location(PropertyType):
    GPS_POINT = "GPSPoint"
    COUNTRY = "Country"

    _property_mappings: ClassVar[dict[str, str]] = {
        "gps_point": "GPSPoint",
        "country": "Country",
    }

    gps_point: Optional[GPSPoint] = None
    country: Optional[SetDimension] = None


@dataclass
class Recency(PropertyType):
    DURATION = "Duration"
    RECENCY_TYPE = "RecencyType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "recency_type": "RecencyType",
    }

    duration: Optional[Union[str, Ref, GetAtt, Sub]] = None
    recency_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SegmentDimensions(PropertyType):
    DEMOGRAPHIC = "Demographic"
    METRICS = "Metrics"
    ATTRIBUTES = "Attributes"
    BEHAVIOR = "Behavior"
    USER_ATTRIBUTES = "UserAttributes"
    LOCATION = "Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "demographic": "Demographic",
        "metrics": "Metrics",
        "attributes": "Attributes",
        "behavior": "Behavior",
        "user_attributes": "UserAttributes",
        "location": "Location",
    }

    demographic: Optional[Demographic] = None
    metrics: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    attributes: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    behavior: Optional[Behavior] = None
    user_attributes: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    location: Optional[Location] = None


@dataclass
class SegmentGroups(PropertyType):
    GROUPS = "Groups"
    INCLUDE = "Include"

    _property_mappings: ClassVar[dict[str, str]] = {
        "groups": "Groups",
        "include": "Include",
    }

    groups: Optional[list[Groups]] = None
    include: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SetDimension(PropertyType):
    DIMENSION_TYPE = "DimensionType"
    VALUES = "Values"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dimension_type": "DimensionType",
        "values": "Values",
    }

    dimension_type: Optional[Union[str, DimensionType, Ref, GetAtt, Sub]] = None
    values: Optional[Union[list[str], Ref]] = None


@dataclass
class SourceSegments(PropertyType):
    VERSION = "Version"
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "version": "Version",
        "id": "Id",
    }

    version: Optional[Union[int, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None

