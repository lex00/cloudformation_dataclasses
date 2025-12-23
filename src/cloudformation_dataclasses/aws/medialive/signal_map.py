"""PropertyTypes for AWS::MediaLive::SignalMap."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MediaResource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destinations": "Destinations",
        "sources": "Sources",
        "name": "Name",
    }

    destinations: Optional[list[MediaResourceNeighbor]] = None
    sources: Optional[list[MediaResourceNeighbor]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MediaResourceNeighbor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
        "name": "Name",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MonitorDeployment(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "details_uri": "DetailsUri",
        "status": "Status",
        "error_message": "ErrorMessage",
    }

    details_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    status: Optional[Union[str, SignalMapMonitorDeploymentStatus, Ref, GetAtt, Sub]] = None
    error_message: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SuccessfulMonitorDeployment(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "details_uri": "DetailsUri",
        "status": "Status",
    }

    details_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    status: Optional[Union[str, SignalMapMonitorDeploymentStatus, Ref, GetAtt, Sub]] = None

