"""PropertyTypes for AWS::ServiceDiscovery::PublicDnsNamespace."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class CustomHealthStatus:
    """CustomHealthStatus enum values."""

    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"


class FilterCondition:
    """FilterCondition enum values."""

    EQ = "EQ"
    IN = "IN"
    BETWEEN = "BETWEEN"
    BEGINS_WITH = "BEGINS_WITH"


class HealthCheckType:
    """HealthCheckType enum values."""

    HTTP = "HTTP"
    HTTPS = "HTTPS"
    TCP = "TCP"


class HealthStatus:
    """HealthStatus enum values."""

    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"
    UNKNOWN = "UNKNOWN"


class HealthStatusFilter:
    """HealthStatusFilter enum values."""

    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"
    ALL = "ALL"
    HEALTHY_OR_ELSE_ALL = "HEALTHY_OR_ELSE_ALL"


class NamespaceFilterName:
    """NamespaceFilterName enum values."""

    TYPE = "TYPE"
    NAME = "NAME"
    HTTP_NAME = "HTTP_NAME"
    RESOURCE_OWNER = "RESOURCE_OWNER"


class NamespaceType:
    """NamespaceType enum values."""

    DNS_PUBLIC = "DNS_PUBLIC"
    DNS_PRIVATE = "DNS_PRIVATE"
    HTTP = "HTTP"


class OperationFilterName:
    """OperationFilterName enum values."""

    NAMESPACE_ID = "NAMESPACE_ID"
    SERVICE_ID = "SERVICE_ID"
    STATUS = "STATUS"
    TYPE = "TYPE"
    UPDATE_DATE = "UPDATE_DATE"


class OperationStatus:
    """OperationStatus enum values."""

    SUBMITTED = "SUBMITTED"
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"


class OperationTargetType:
    """OperationTargetType enum values."""

    NAMESPACE = "NAMESPACE"
    SERVICE = "SERVICE"
    INSTANCE = "INSTANCE"


class OperationType:
    """OperationType enum values."""

    CREATE_NAMESPACE = "CREATE_NAMESPACE"
    DELETE_NAMESPACE = "DELETE_NAMESPACE"
    UPDATE_NAMESPACE = "UPDATE_NAMESPACE"
    UPDATE_SERVICE = "UPDATE_SERVICE"
    REGISTER_INSTANCE = "REGISTER_INSTANCE"
    DEREGISTER_INSTANCE = "DEREGISTER_INSTANCE"


class RecordType:
    """RecordType enum values."""

    SRV = "SRV"
    A = "A"
    AAAA = "AAAA"
    CNAME = "CNAME"


class RoutingPolicy:
    """RoutingPolicy enum values."""

    MULTIVALUE = "MULTIVALUE"
    WEIGHTED = "WEIGHTED"


class ServiceFilterName:
    """ServiceFilterName enum values."""

    NAMESPACE_ID = "NAMESPACE_ID"
    RESOURCE_OWNER = "RESOURCE_OWNER"


class ServiceType:
    """ServiceType enum values."""

    HTTP = "HTTP"
    DNS_HTTP = "DNS_HTTP"
    DNS = "DNS"


class ServiceTypeOption:
    """ServiceTypeOption enum values."""

    HTTP = "HTTP"


@dataclass
class Properties(PropertyType):
    DNS_PROPERTIES = "DnsProperties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dns_properties": "DnsProperties",
    }

    dns_properties: Optional[PublicDnsPropertiesMutable] = None


@dataclass
class PublicDnsPropertiesMutable(PropertyType):
    SOA = "SOA"

    _property_mappings: ClassVar[dict[str, str]] = {
        "soa": "SOA",
    }

    soa: Optional[SOA] = None


@dataclass
class SOA(PropertyType):
    TTL = "TTL"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ttl": "TTL",
    }

    ttl: Optional[Union[float, Ref, GetAtt, Sub]] = None

