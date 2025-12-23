"""PropertyTypes for AWS::AppMesh::Route."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Duration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GrpcRetryPolicy(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "weighted_targets": "WeightedTargets",
    }

    weighted_targets: Optional[list[WeightedTarget]] = None


@dataclass
class GrpcRouteMatch(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "per_request": "PerRequest",
        "idle": "Idle",
    }

    per_request: Optional[Duration] = None
    idle: Optional[Duration] = None


@dataclass
class HeaderMatchMethod(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "regex": "Regex",
        "exact": "Exact",
    }

    regex: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exact: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HttpQueryParameterMatch(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "exact": "Exact",
    }

    exact: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HttpRetryPolicy(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "weighted_targets": "WeightedTargets",
    }

    weighted_targets: Optional[list[WeightedTarget]] = None


@dataclass
class HttpRouteHeader(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "per_request": "PerRequest",
        "idle": "Idle",
    }

    per_request: Optional[Duration] = None
    idle: Optional[Duration] = None


@dataclass
class MatchRange(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "start": "Start",
        "end": "End",
    }

    start: Optional[Union[int, Ref, GetAtt, Sub]] = None
    end: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class QueryParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
        "match": "Match",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    match: Optional[HttpQueryParameterMatch] = None


@dataclass
class RouteSpec(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "weighted_targets": "WeightedTargets",
    }

    weighted_targets: Optional[list[WeightedTarget]] = None


@dataclass
class TcpRouteMatch(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
    }

    port: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TcpTimeout(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "idle": "Idle",
    }

    idle: Optional[Duration] = None


@dataclass
class WeightedTarget(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "virtual_node": "VirtualNode",
        "port": "Port",
        "weight": "Weight",
    }

    virtual_node: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    weight: Optional[Union[int, Ref, GetAtt, Sub]] = None

