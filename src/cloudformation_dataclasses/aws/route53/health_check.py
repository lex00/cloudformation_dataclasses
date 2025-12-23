"""PropertyTypes for AWS::Route53::HealthCheck."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AlarmIdentifier(PropertyType):
    REGION = "Region"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "region": "Region",
        "name": "Name",
    }

    region: Optional[Union[str, CloudWatchRegion, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HealthCheckConfig(PropertyType):
    ENABLE_SNI = "EnableSNI"
    CHILD_HEALTH_CHECKS = "ChildHealthChecks"
    MEASURE_LATENCY = "MeasureLatency"
    PORT = "Port"
    REGIONS = "Regions"
    INSUFFICIENT_DATA_HEALTH_STATUS = "InsufficientDataHealthStatus"
    SEARCH_STRING = "SearchString"
    TYPE = "Type"
    RESOURCE_PATH = "ResourcePath"
    ROUTING_CONTROL_ARN = "RoutingControlArn"
    FULLY_QUALIFIED_DOMAIN_NAME = "FullyQualifiedDomainName"
    INVERTED = "Inverted"
    HEALTH_THRESHOLD = "HealthThreshold"
    REQUEST_INTERVAL = "RequestInterval"
    ALARM_IDENTIFIER = "AlarmIdentifier"
    FAILURE_THRESHOLD = "FailureThreshold"
    IP_ADDRESS = "IPAddress"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_sni": "EnableSNI",
        "child_health_checks": "ChildHealthChecks",
        "measure_latency": "MeasureLatency",
        "port": "Port",
        "regions": "Regions",
        "insufficient_data_health_status": "InsufficientDataHealthStatus",
        "search_string": "SearchString",
        "type_": "Type",
        "resource_path": "ResourcePath",
        "routing_control_arn": "RoutingControlArn",
        "fully_qualified_domain_name": "FullyQualifiedDomainName",
        "inverted": "Inverted",
        "health_threshold": "HealthThreshold",
        "request_interval": "RequestInterval",
        "alarm_identifier": "AlarmIdentifier",
        "failure_threshold": "FailureThreshold",
        "ip_address": "IPAddress",
    }

    enable_sni: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    child_health_checks: Optional[Union[list[str], Ref]] = None
    measure_latency: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    regions: Optional[Union[list[str], Ref]] = None
    insufficient_data_health_status: Optional[Union[str, InsufficientDataHealthStatus, Ref, GetAtt, Sub]] = None
    search_string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, HealthCheckType, Ref, GetAtt, Sub]] = None
    resource_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    routing_control_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    fully_qualified_domain_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    inverted: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    health_threshold: Optional[Union[int, Ref, GetAtt, Sub]] = None
    request_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    alarm_identifier: Optional[AlarmIdentifier] = None
    failure_threshold: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ip_address: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HealthCheckTag(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

