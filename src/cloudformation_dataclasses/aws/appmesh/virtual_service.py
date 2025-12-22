"""PropertyTypes for AWS::AppMesh::VirtualService."""

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
class VirtualNodeServiceProvider(PropertyType):
    VIRTUAL_NODE_NAME = "VirtualNodeName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "virtual_node_name": "VirtualNodeName",
    }

    virtual_node_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualRouterServiceProvider(PropertyType):
    VIRTUAL_ROUTER_NAME = "VirtualRouterName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "virtual_router_name": "VirtualRouterName",
    }

    virtual_router_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualServiceProvider(PropertyType):
    VIRTUAL_NODE = "VirtualNode"
    VIRTUAL_ROUTER = "VirtualRouter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "virtual_node": "VirtualNode",
        "virtual_router": "VirtualRouter",
    }

    virtual_node: Optional[VirtualNodeServiceProvider] = None
    virtual_router: Optional[VirtualRouterServiceProvider] = None


@dataclass
class VirtualServiceSpec(PropertyType):
    PROVIDER = "Provider"

    _property_mappings: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Optional[VirtualServiceProvider] = None

