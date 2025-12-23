"""PropertyTypes for AWS::ElasticLoadBalancingV2::TargetGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Matcher(PropertyType):
    GRPC_CODE = "GrpcCode"
    HTTP_CODE = "HttpCode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "grpc_code": "GrpcCode",
        "http_code": "HttpCode",
    }

    grpc_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    http_code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetDescription(PropertyType):
    QUIC_SERVER_ID = "QuicServerId"
    PORT = "Port"
    AVAILABILITY_ZONE = "AvailabilityZone"
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "quic_server_id": "QuicServerId",
        "port": "Port",
        "availability_zone": "AvailabilityZone",
        "id": "Id",
    }

    quic_server_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetGroupAttribute(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

