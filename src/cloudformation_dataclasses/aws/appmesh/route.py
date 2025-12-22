"""PropertyTypes for AWS::AppMesh::Route."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class DefaultGatewayRouteRewrite:
    """DefaultGatewayRouteRewrite enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DnsResponseType:
    """DnsResponseType enum values."""

    LOADBALANCER = "LOADBALANCER"
    ENDPOINTS = "ENDPOINTS"


class DurationUnit:
    """DurationUnit enum values."""

    S = "s"
    MS = "ms"


class EgressFilterType:
    """EgressFilterType enum values."""

    ALLOW_ALL = "ALLOW_ALL"
    DROP_ALL = "DROP_ALL"


class GatewayRouteStatusCode:
    """GatewayRouteStatusCode enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETED = "DELETED"


class GrpcRetryPolicyEvent:
    """GrpcRetryPolicyEvent enum values."""

    CANCELLED = "cancelled"
    DEADLINE_EXCEEDED = "deadline-exceeded"
    INTERNAL = "internal"
    RESOURCE_EXHAUSTED = "resource-exhausted"
    UNAVAILABLE = "unavailable"


class HttpMethod:
    """HttpMethod enum values."""

    GET = "GET"
    HEAD = "HEAD"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    CONNECT = "CONNECT"
    OPTIONS = "OPTIONS"
    TRACE = "TRACE"
    PATCH = "PATCH"


class HttpScheme:
    """HttpScheme enum values."""

    HTTP = "http"
    HTTPS = "https"


class IpPreference:
    """IpPreference enum values."""

    IPV6_PREFERRED = "IPv6_PREFERRED"
    IPV4_PREFERRED = "IPv4_PREFERRED"
    IPV4_ONLY = "IPv4_ONLY"
    IPV6_ONLY = "IPv6_ONLY"


class ListenerTlsMode:
    """ListenerTlsMode enum values."""

    STRICT = "STRICT"
    PERMISSIVE = "PERMISSIVE"
    DISABLED = "DISABLED"


class MeshStatusCode:
    """MeshStatusCode enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETED = "DELETED"


class PortProtocol:
    """PortProtocol enum values."""

    HTTP = "http"
    TCP = "tcp"
    HTTP2 = "http2"
    GRPC = "grpc"


class RouteStatusCode:
    """RouteStatusCode enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETED = "DELETED"


class TcpRetryPolicyEvent:
    """TcpRetryPolicyEvent enum values."""

    CONNECTION_ERROR = "connection-error"


class VirtualGatewayListenerTlsMode:
    """VirtualGatewayListenerTlsMode enum values."""

    STRICT = "STRICT"
    PERMISSIVE = "PERMISSIVE"
    DISABLED = "DISABLED"


class VirtualGatewayPortProtocol:
    """VirtualGatewayPortProtocol enum values."""

    HTTP = "http"
    HTTP2 = "http2"
    GRPC = "grpc"


class VirtualGatewayStatusCode:
    """VirtualGatewayStatusCode enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETED = "DELETED"


class VirtualNodeStatusCode:
    """VirtualNodeStatusCode enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETED = "DELETED"


class VirtualRouterStatusCode:
    """VirtualRouterStatusCode enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETED = "DELETED"


class VirtualServiceStatusCode:
    """VirtualServiceStatusCode enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETED = "DELETED"


@dataclass
class Duration(PropertyType):
    VALUE = "Value"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GrpcRetryPolicy(PropertyType):
    MAX_RETRIES = "MaxRetries"
    PER_RETRY_TIMEOUT = "PerRetryTimeout"
    GRPC_RETRY_EVENTS = "GrpcRetryEvents"
    HTTP_RETRY_EVENTS = "HttpRetryEvents"
    TCP_RETRY_EVENTS = "TcpRetryEvents"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_retries": "MaxRetries",
        "per_retry_timeout": "PerRetryTimeout",
        "grpc_retry_events": "GrpcRetryEvents",
        "http_retry_events": "HttpRetryEvents",
        "tcp_retry_events": "TcpRetryEvents",
    }

    max_retries: Optional[Union[int, Ref, GetAtt, Sub]] = None
    per_retry_timeout: Optional[Duration] = None
    grpc_retry_events: Optional[Union[list[str], Ref]] = None
    http_retry_events: Optional[Union[list[str], Ref]] = None
    tcp_retry_events: Optional[Union[list[str], Ref]] = None


@dataclass
class GrpcRoute(PropertyType):
    ACTION = "Action"
    TIMEOUT = "Timeout"
    RETRY_POLICY = "RetryPolicy"
    MATCH = "Match"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "timeout": "Timeout",
        "retry_policy": "RetryPolicy",
        "match": "Match",
    }

    action: Optional[GrpcRouteAction] = None
    timeout: Optional[GrpcTimeout] = None
    retry_policy: Optional[GrpcRetryPolicy] = None
    match: Optional[GrpcRouteMatch] = None


@dataclass
class GrpcRouteAction(PropertyType):
    WEIGHTED_TARGETS = "WeightedTargets"

    _property_mappings: ClassVar[dict[str, str]] = {
        "weighted_targets": "WeightedTargets",
    }

    weighted_targets: Optional[list[WeightedTarget]] = None


@dataclass
class GrpcRouteMatch(PropertyType):
    SERVICE_NAME = "ServiceName"
    PORT = "Port"
    METADATA = "Metadata"
    METHOD_NAME = "MethodName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service_name": "ServiceName",
        "port": "Port",
        "metadata": "Metadata",
        "method_name": "MethodName",
    }

    service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    metadata: Optional[list[GrpcRouteMetadata]] = None
    method_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GrpcRouteMetadata(PropertyType):
    INVERT = "Invert"
    NAME = "Name"
    MATCH = "Match"

    _property_mappings: ClassVar[dict[str, str]] = {
        "invert": "Invert",
        "name": "Name",
        "match": "Match",
    }

    invert: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    match: Optional[GrpcRouteMetadataMatchMethod] = None


@dataclass
class GrpcRouteMetadataMatchMethod(PropertyType):
    SUFFIX = "Suffix"
    REGEX = "Regex"
    EXACT = "Exact"
    PREFIX = "Prefix"
    RANGE = "Range"

    _property_mappings: ClassVar[dict[str, str]] = {
        "suffix": "Suffix",
        "regex": "Regex",
        "exact": "Exact",
        "prefix": "Prefix",
        "range": "Range",
    }

    suffix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    regex: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exact: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    range: Optional[MatchRange] = None


@dataclass
class GrpcTimeout(PropertyType):
    PER_REQUEST = "PerRequest"
    IDLE = "Idle"

    _property_mappings: ClassVar[dict[str, str]] = {
        "per_request": "PerRequest",
        "idle": "Idle",
    }

    per_request: Optional[Duration] = None
    idle: Optional[Duration] = None


@dataclass
class HeaderMatchMethod(PropertyType):
    SUFFIX = "Suffix"
    REGEX = "Regex"
    EXACT = "Exact"
    PREFIX = "Prefix"
    RANGE = "Range"

    _property_mappings: ClassVar[dict[str, str]] = {
        "suffix": "Suffix",
        "regex": "Regex",
        "exact": "Exact",
        "prefix": "Prefix",
        "range": "Range",
    }

    suffix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    regex: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exact: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    range: Optional[MatchRange] = None


@dataclass
class HttpPathMatch(PropertyType):
    REGEX = "Regex"
    EXACT = "Exact"

    _property_mappings: ClassVar[dict[str, str]] = {
        "regex": "Regex",
        "exact": "Exact",
    }

    regex: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exact: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HttpQueryParameterMatch(PropertyType):
    EXACT = "Exact"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exact": "Exact",
    }

    exact: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HttpRetryPolicy(PropertyType):
    MAX_RETRIES = "MaxRetries"
    PER_RETRY_TIMEOUT = "PerRetryTimeout"
    HTTP_RETRY_EVENTS = "HttpRetryEvents"
    TCP_RETRY_EVENTS = "TcpRetryEvents"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_retries": "MaxRetries",
        "per_retry_timeout": "PerRetryTimeout",
        "http_retry_events": "HttpRetryEvents",
        "tcp_retry_events": "TcpRetryEvents",
    }

    max_retries: Optional[Union[int, Ref, GetAtt, Sub]] = None
    per_retry_timeout: Optional[Duration] = None
    http_retry_events: Optional[Union[list[str], Ref]] = None
    tcp_retry_events: Optional[Union[list[str], Ref]] = None


@dataclass
class HttpRoute(PropertyType):
    ACTION = "Action"
    TIMEOUT = "Timeout"
    RETRY_POLICY = "RetryPolicy"
    MATCH = "Match"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "timeout": "Timeout",
        "retry_policy": "RetryPolicy",
        "match": "Match",
    }

    action: Optional[HttpRouteAction] = None
    timeout: Optional[HttpTimeout] = None
    retry_policy: Optional[HttpRetryPolicy] = None
    match: Optional[HttpRouteMatch] = None


@dataclass
class HttpRouteAction(PropertyType):
    WEIGHTED_TARGETS = "WeightedTargets"

    _property_mappings: ClassVar[dict[str, str]] = {
        "weighted_targets": "WeightedTargets",
    }

    weighted_targets: Optional[list[WeightedTarget]] = None


@dataclass
class HttpRouteHeader(PropertyType):
    INVERT = "Invert"
    NAME = "Name"
    MATCH = "Match"

    _property_mappings: ClassVar[dict[str, str]] = {
        "invert": "Invert",
        "name": "Name",
        "match": "Match",
    }

    invert: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    match: Optional[HeaderMatchMethod] = None


@dataclass
class HttpRouteMatch(PropertyType):
    PATH = "Path"
    SCHEME = "Scheme"
    HEADERS = "Headers"
    PORT = "Port"
    PREFIX = "Prefix"
    METHOD = "Method"
    QUERY_PARAMETERS = "QueryParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "scheme": "Scheme",
        "headers": "Headers",
        "port": "Port",
        "prefix": "Prefix",
        "method": "Method",
        "query_parameters": "QueryParameters",
    }

    path: Optional[HttpPathMatch] = None
    scheme: Optional[Union[str, Ref, GetAtt, Sub]] = None
    headers: Optional[list[HttpRouteHeader]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    method: Optional[Union[str, Ref, GetAtt, Sub]] = None
    query_parameters: Optional[list[QueryParameter]] = None


@dataclass
class HttpTimeout(PropertyType):
    PER_REQUEST = "PerRequest"
    IDLE = "Idle"

    _property_mappings: ClassVar[dict[str, str]] = {
        "per_request": "PerRequest",
        "idle": "Idle",
    }

    per_request: Optional[Duration] = None
    idle: Optional[Duration] = None


@dataclass
class MatchRange(PropertyType):
    START = "Start"
    END = "End"

    _property_mappings: ClassVar[dict[str, str]] = {
        "start": "Start",
        "end": "End",
    }

    start: Optional[Union[int, Ref, GetAtt, Sub]] = None
    end: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class QueryParameter(PropertyType):
    NAME = "Name"
    MATCH = "Match"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
        "match": "Match",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    match: Optional[HttpQueryParameterMatch] = None


@dataclass
class RouteSpec(PropertyType):
    HTTP_ROUTE = "HttpRoute"
    PRIORITY = "Priority"
    HTTP2_ROUTE = "Http2Route"
    GRPC_ROUTE = "GrpcRoute"
    TCP_ROUTE = "TcpRoute"

    _property_mappings: ClassVar[dict[str, str]] = {
        "http_route": "HttpRoute",
        "priority": "Priority",
        "http2_route": "Http2Route",
        "grpc_route": "GrpcRoute",
        "tcp_route": "TcpRoute",
    }

    http_route: Optional[HttpRoute] = None
    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None
    http2_route: Optional[HttpRoute] = None
    grpc_route: Optional[GrpcRoute] = None
    tcp_route: Optional[TcpRoute] = None


@dataclass
class TcpRoute(PropertyType):
    ACTION = "Action"
    TIMEOUT = "Timeout"
    MATCH = "Match"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "timeout": "Timeout",
        "match": "Match",
    }

    action: Optional[TcpRouteAction] = None
    timeout: Optional[TcpTimeout] = None
    match: Optional[TcpRouteMatch] = None


@dataclass
class TcpRouteAction(PropertyType):
    WEIGHTED_TARGETS = "WeightedTargets"

    _property_mappings: ClassVar[dict[str, str]] = {
        "weighted_targets": "WeightedTargets",
    }

    weighted_targets: Optional[list[WeightedTarget]] = None


@dataclass
class TcpRouteMatch(PropertyType):
    PORT = "Port"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
    }

    port: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TcpTimeout(PropertyType):
    IDLE = "Idle"

    _property_mappings: ClassVar[dict[str, str]] = {
        "idle": "Idle",
    }

    idle: Optional[Duration] = None


@dataclass
class WeightedTarget(PropertyType):
    VIRTUAL_NODE = "VirtualNode"
    PORT = "Port"
    WEIGHT = "Weight"

    _property_mappings: ClassVar[dict[str, str]] = {
        "virtual_node": "VirtualNode",
        "port": "Port",
        "weight": "Weight",
    }

    virtual_node: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    weight: Optional[Union[int, Ref, GetAtt, Sub]] = None

