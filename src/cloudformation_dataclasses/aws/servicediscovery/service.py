"""PropertyTypes for AWS::ServiceDiscovery::Service."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DnsConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dns_records": "DnsRecords",
        "routing_policy": "RoutingPolicy",
        "namespace_id": "NamespaceId",
    }

    dns_records: Optional[list[DnsRecord]] = None
    routing_policy: Optional[Union[str, RoutingPolicy, Ref, GetAtt, Sub]] = None
    namespace_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DnsRecord(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "ttl": "TTL",
    }

    type_: Optional[Union[str, RecordType, Ref, GetAtt, Sub]] = None
    ttl: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class HealthCheckConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "resource_path": "ResourcePath",
        "failure_threshold": "FailureThreshold",
    }

    type_: Optional[Union[str, HealthCheckType, Ref, GetAtt, Sub]] = None
    resource_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    failure_threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class HealthCheckCustomConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "failure_threshold": "FailureThreshold",
    }

    failure_threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None

