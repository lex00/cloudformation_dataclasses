"""PropertyTypes for AWS::AppMesh::GatewayRoute."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class GatewayRouteHostnameMatch(PropertyType):
    SUFFIX = "Suffix"
    EXACT = "Exact"

    _property_mappings: ClassVar[dict[str, str]] = {
        "suffix": "Suffix",
        "exact": "Exact",
    }

    suffix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exact: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GatewayRouteHostnameRewrite(PropertyType):
    DEFAULT_TARGET_HOSTNAME = "DefaultTargetHostname"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_target_hostname": "DefaultTargetHostname",
    }

    default_target_hostname: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GatewayRouteMetadataMatch(PropertyType):
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
    range: Optional[GatewayRouteRangeMatch] = None


@dataclass
class GatewayRouteRangeMatch(PropertyType):
    START = "Start"
    END = "End"

    _property_mappings: ClassVar[dict[str, str]] = {
        "start": "Start",
        "end": "End",
    }

    start: Optional[Union[int, Ref, GetAtt, Sub]] = None
    end: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class GatewayRouteSpec(PropertyType):
    HTTP_ROUTE = "HttpRoute"
    PRIORITY = "Priority"
    HTTP2_ROUTE = "Http2Route"
    GRPC_ROUTE = "GrpcRoute"

    _property_mappings: ClassVar[dict[str, str]] = {
        "http_route": "HttpRoute",
        "priority": "Priority",
        "http2_route": "Http2Route",
        "grpc_route": "GrpcRoute",
    }

    http_route: Optional[HttpGatewayRoute] = None
    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None
    http2_route: Optional[HttpGatewayRoute] = None
    grpc_route: Optional[GrpcGatewayRoute] = None


@dataclass
class GatewayRouteTarget(PropertyType):
    PORT = "Port"
    VIRTUAL_SERVICE = "VirtualService"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "virtual_service": "VirtualService",
    }

    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    virtual_service: Optional[GatewayRouteVirtualService] = None


@dataclass
class GatewayRouteVirtualService(PropertyType):
    VIRTUAL_SERVICE_NAME = "VirtualServiceName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "virtual_service_name": "VirtualServiceName",
    }

    virtual_service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GrpcGatewayRoute(PropertyType):
    ACTION = "Action"
    MATCH = "Match"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "match": "Match",
    }

    action: Optional[GrpcGatewayRouteAction] = None
    match: Optional[GrpcGatewayRouteMatch] = None


@dataclass
class GrpcGatewayRouteAction(PropertyType):
    TARGET = "Target"
    REWRITE = "Rewrite"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target": "Target",
        "rewrite": "Rewrite",
    }

    target: Optional[GatewayRouteTarget] = None
    rewrite: Optional[GrpcGatewayRouteRewrite] = None


@dataclass
class GrpcGatewayRouteMatch(PropertyType):
    SERVICE_NAME = "ServiceName"
    PORT = "Port"
    HOSTNAME = "Hostname"
    METADATA = "Metadata"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service_name": "ServiceName",
        "port": "Port",
        "hostname": "Hostname",
        "metadata": "Metadata",
    }

    service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    hostname: Optional[GatewayRouteHostnameMatch] = None
    metadata: Optional[list[GrpcGatewayRouteMetadata]] = None


@dataclass
class GrpcGatewayRouteMetadata(PropertyType):
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
    match: Optional[GatewayRouteMetadataMatch] = None


@dataclass
class GrpcGatewayRouteRewrite(PropertyType):
    HOSTNAME = "Hostname"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hostname": "Hostname",
    }

    hostname: Optional[GatewayRouteHostnameRewrite] = None


@dataclass
class HttpGatewayRoute(PropertyType):
    ACTION = "Action"
    MATCH = "Match"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "match": "Match",
    }

    action: Optional[HttpGatewayRouteAction] = None
    match: Optional[HttpGatewayRouteMatch] = None


@dataclass
class HttpGatewayRouteAction(PropertyType):
    TARGET = "Target"
    REWRITE = "Rewrite"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target": "Target",
        "rewrite": "Rewrite",
    }

    target: Optional[GatewayRouteTarget] = None
    rewrite: Optional[HttpGatewayRouteRewrite] = None


@dataclass
class HttpGatewayRouteHeader(PropertyType):
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
    match: Optional[HttpGatewayRouteHeaderMatch] = None


@dataclass
class HttpGatewayRouteHeaderMatch(PropertyType):
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
    range: Optional[GatewayRouteRangeMatch] = None


@dataclass
class HttpGatewayRouteMatch(PropertyType):
    PATH = "Path"
    HEADERS = "Headers"
    PORT = "Port"
    HOSTNAME = "Hostname"
    PREFIX = "Prefix"
    METHOD = "Method"
    QUERY_PARAMETERS = "QueryParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "headers": "Headers",
        "port": "Port",
        "hostname": "Hostname",
        "prefix": "Prefix",
        "method": "Method",
        "query_parameters": "QueryParameters",
    }

    path: Optional[HttpPathMatch] = None
    headers: Optional[list[HttpGatewayRouteHeader]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    hostname: Optional[GatewayRouteHostnameMatch] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    method: Optional[Union[str, Ref, GetAtt, Sub]] = None
    query_parameters: Optional[list[QueryParameter]] = None


@dataclass
class HttpGatewayRoutePathRewrite(PropertyType):
    EXACT = "Exact"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exact": "Exact",
    }

    exact: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HttpGatewayRoutePrefixRewrite(PropertyType):
    VALUE = "Value"
    DEFAULT_PREFIX = "DefaultPrefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "default_prefix": "DefaultPrefix",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HttpGatewayRouteRewrite(PropertyType):
    PATH = "Path"
    HOSTNAME = "Hostname"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "hostname": "Hostname",
        "prefix": "Prefix",
    }

    path: Optional[HttpGatewayRoutePathRewrite] = None
    hostname: Optional[GatewayRouteHostnameRewrite] = None
    prefix: Optional[HttpGatewayRoutePrefixRewrite] = None


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
class QueryParameter(PropertyType):
    NAME = "Name"
    MATCH = "Match"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
        "match": "Match",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    match: Optional[HttpQueryParameterMatch] = None

