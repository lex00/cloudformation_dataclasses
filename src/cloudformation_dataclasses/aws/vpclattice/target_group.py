"""PropertyTypes for AWS::VpcLattice::TargetGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class HealthCheckConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "health_check_interval_seconds": "HealthCheckIntervalSeconds",
        "matcher": "Matcher",
        "healthy_threshold_count": "HealthyThresholdCount",
        "port": "Port",
        "enabled": "Enabled",
        "protocol": "Protocol",
        "protocol_version": "ProtocolVersion",
        "unhealthy_threshold_count": "UnhealthyThresholdCount",
        "health_check_timeout_seconds": "HealthCheckTimeoutSeconds",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    health_check_interval_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    matcher: Optional[Matcher] = None
    healthy_threshold_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unhealthy_threshold_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    health_check_timeout_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Matcher(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "http_code": "HttpCode",
    }

    http_code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Target(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "id": "Id",
    }

    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetGroupConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_address_type": "IpAddressType",
        "port": "Port",
        "health_check": "HealthCheck",
        "lambda_event_structure_version": "LambdaEventStructureVersion",
        "vpc_identifier": "VpcIdentifier",
        "protocol": "Protocol",
        "protocol_version": "ProtocolVersion",
    }

    ip_address_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    health_check: Optional[HealthCheckConfig] = None
    lambda_event_structure_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpc_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol_version: Optional[Union[str, Ref, GetAtt, Sub]] = None

