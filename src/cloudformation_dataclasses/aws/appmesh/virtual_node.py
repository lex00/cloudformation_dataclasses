"""PropertyTypes for AWS::AppMesh::VirtualNode."""

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
class AccessLog(PropertyType):
    FILE = "File"

    _property_mappings: ClassVar[dict[str, str]] = {
        "file": "File",
    }

    file: Optional[FileAccessLog] = None


@dataclass
class AwsCloudMapInstanceAttribute(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AwsCloudMapServiceDiscovery(PropertyType):
    NAMESPACE_NAME = "NamespaceName"
    SERVICE_NAME = "ServiceName"
    IP_PREFERENCE = "IpPreference"
    ATTRIBUTES = "Attributes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "namespace_name": "NamespaceName",
        "service_name": "ServiceName",
        "ip_preference": "IpPreference",
        "attributes": "Attributes",
    }

    namespace_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ip_preference: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attributes: Optional[list[AwsCloudMapInstanceAttribute]] = None


@dataclass
class Backend(PropertyType):
    VIRTUAL_SERVICE = "VirtualService"

    _property_mappings: ClassVar[dict[str, str]] = {
        "virtual_service": "VirtualService",
    }

    virtual_service: Optional[VirtualServiceBackend] = None


@dataclass
class BackendDefaults(PropertyType):
    CLIENT_POLICY = "ClientPolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "client_policy": "ClientPolicy",
    }

    client_policy: Optional[ClientPolicy] = None


@dataclass
class ClientPolicy(PropertyType):
    TLS = "TLS"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tls": "TLS",
    }

    tls: Optional[ClientPolicyTls] = None


@dataclass
class ClientPolicyTls(PropertyType):
    VALIDATION = "Validation"
    ENFORCE = "Enforce"
    PORTS = "Ports"
    CERTIFICATE = "Certificate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "validation": "Validation",
        "enforce": "Enforce",
        "ports": "Ports",
        "certificate": "Certificate",
    }

    validation: Optional[TlsValidationContext] = None
    enforce: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ports: Optional[Union[list[int], Ref]] = None
    certificate: Optional[ClientTlsCertificate] = None


@dataclass
class ClientTlsCertificate(PropertyType):
    SDS = "SDS"
    FILE = "File"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sds": "SDS",
        "file": "File",
    }

    sds: Optional[ListenerTlsSdsCertificate] = None
    file: Optional[ListenerTlsFileCertificate] = None


@dataclass
class DnsServiceDiscovery(PropertyType):
    IP_PREFERENCE = "IpPreference"
    HOSTNAME = "Hostname"
    RESPONSE_TYPE = "ResponseType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_preference": "IpPreference",
        "hostname": "Hostname",
        "response_type": "ResponseType",
    }

    ip_preference: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hostname: Optional[Union[str, Ref, GetAtt, Sub]] = None
    response_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class FileAccessLog(PropertyType):
    PATH = "Path"
    FORMAT = "Format"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "format": "Format",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    format: Optional[LoggingFormat] = None


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
class HealthCheck(PropertyType):
    PATH = "Path"
    UNHEALTHY_THRESHOLD = "UnhealthyThreshold"
    PORT = "Port"
    HEALTHY_THRESHOLD = "HealthyThreshold"
    TIMEOUT_MILLIS = "TimeoutMillis"
    PROTOCOL = "Protocol"
    INTERVAL_MILLIS = "IntervalMillis"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "unhealthy_threshold": "UnhealthyThreshold",
        "port": "Port",
        "healthy_threshold": "HealthyThreshold",
        "timeout_millis": "TimeoutMillis",
        "protocol": "Protocol",
        "interval_millis": "IntervalMillis",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unhealthy_threshold: Optional[Union[int, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    healthy_threshold: Optional[Union[int, Ref, GetAtt, Sub]] = None
    timeout_millis: Optional[Union[int, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    interval_millis: Optional[Union[int, Ref, GetAtt, Sub]] = None


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
class JsonFormatRef(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Listener(PropertyType):
    CONNECTION_POOL = "ConnectionPool"
    TIMEOUT = "Timeout"
    HEALTH_CHECK = "HealthCheck"
    TLS = "TLS"
    PORT_MAPPING = "PortMapping"
    OUTLIER_DETECTION = "OutlierDetection"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connection_pool": "ConnectionPool",
        "timeout": "Timeout",
        "health_check": "HealthCheck",
        "tls": "TLS",
        "port_mapping": "PortMapping",
        "outlier_detection": "OutlierDetection",
    }

    connection_pool: Optional[VirtualNodeConnectionPool] = None
    timeout: Optional[ListenerTimeout] = None
    health_check: Optional[HealthCheck] = None
    tls: Optional[ListenerTls] = None
    port_mapping: Optional[PortMapping] = None
    outlier_detection: Optional[OutlierDetection] = None


@dataclass
class ListenerTimeout(PropertyType):
    TCP = "TCP"
    HTTP2 = "HTTP2"
    HTTP = "HTTP"
    GRPC = "GRPC"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tcp": "TCP",
        "http2": "HTTP2",
        "http": "HTTP",
        "grpc": "GRPC",
    }

    tcp: Optional[TcpTimeout] = None
    http2: Optional[HttpTimeout] = None
    http: Optional[HttpTimeout] = None
    grpc: Optional[GrpcTimeout] = None


@dataclass
class ListenerTls(PropertyType):
    VALIDATION = "Validation"
    MODE = "Mode"
    CERTIFICATE = "Certificate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "validation": "Validation",
        "mode": "Mode",
        "certificate": "Certificate",
    }

    validation: Optional[ListenerTlsValidationContext] = None
    mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate: Optional[ListenerTlsCertificate] = None


@dataclass
class ListenerTlsAcmCertificate(PropertyType):
    CERTIFICATE_ARN = "CertificateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_arn": "CertificateArn",
    }

    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ListenerTlsCertificate(PropertyType):
    SDS = "SDS"
    ACM = "ACM"
    FILE = "File"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sds": "SDS",
        "acm": "ACM",
        "file": "File",
    }

    sds: Optional[ListenerTlsSdsCertificate] = None
    acm: Optional[ListenerTlsAcmCertificate] = None
    file: Optional[ListenerTlsFileCertificate] = None


@dataclass
class ListenerTlsFileCertificate(PropertyType):
    PRIVATE_KEY = "PrivateKey"
    CERTIFICATE_CHAIN = "CertificateChain"

    _property_mappings: ClassVar[dict[str, str]] = {
        "private_key": "PrivateKey",
        "certificate_chain": "CertificateChain",
    }

    private_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate_chain: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ListenerTlsSdsCertificate(PropertyType):
    SECRET_NAME = "SecretName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_name": "SecretName",
    }

    secret_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ListenerTlsValidationContext(PropertyType):
    SUBJECT_ALTERNATIVE_NAMES = "SubjectAlternativeNames"
    TRUST = "Trust"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subject_alternative_names": "SubjectAlternativeNames",
        "trust": "Trust",
    }

    subject_alternative_names: Optional[SubjectAlternativeNames] = None
    trust: Optional[ListenerTlsValidationContextTrust] = None


@dataclass
class ListenerTlsValidationContextTrust(PropertyType):
    SDS = "SDS"
    FILE = "File"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sds": "SDS",
        "file": "File",
    }

    sds: Optional[TlsValidationContextSdsTrust] = None
    file: Optional[TlsValidationContextFileTrust] = None


@dataclass
class Logging(PropertyType):
    ACCESS_LOG = "AccessLog"

    _property_mappings: ClassVar[dict[str, str]] = {
        "access_log": "AccessLog",
    }

    access_log: Optional[AccessLog] = None


@dataclass
class LoggingFormat(PropertyType):
    TEXT = "Text"
    JSON = "Json"

    _property_mappings: ClassVar[dict[str, str]] = {
        "text": "Text",
        "json": "Json",
    }

    text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    json: Optional[list[JsonFormatRef]] = None


@dataclass
class OutlierDetection(PropertyType):
    MAX_EJECTION_PERCENT = "MaxEjectionPercent"
    BASE_EJECTION_DURATION = "BaseEjectionDuration"
    MAX_SERVER_ERRORS = "MaxServerErrors"
    INTERVAL = "Interval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_ejection_percent": "MaxEjectionPercent",
        "base_ejection_duration": "BaseEjectionDuration",
        "max_server_errors": "MaxServerErrors",
        "interval": "Interval",
    }

    max_ejection_percent: Optional[Union[int, Ref, GetAtt, Sub]] = None
    base_ejection_duration: Optional[Duration] = None
    max_server_errors: Optional[Union[int, Ref, GetAtt, Sub]] = None
    interval: Optional[Duration] = None


@dataclass
class PortMapping(PropertyType):
    PORT = "Port"
    PROTOCOL = "Protocol"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "protocol": "Protocol",
    }

    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceDiscovery(PropertyType):
    DNS = "DNS"
    AWS_CLOUD_MAP = "AWSCloudMap"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dns": "DNS",
        "aws_cloud_map": "AWSCloudMap",
    }

    dns: Optional[DnsServiceDiscovery] = None
    aws_cloud_map: Optional[AwsCloudMapServiceDiscovery] = None


@dataclass
class SubjectAlternativeNameMatchers(PropertyType):
    EXACT = "Exact"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exact": "Exact",
    }

    exact: Optional[Union[list[str], Ref]] = None


@dataclass
class SubjectAlternativeNames(PropertyType):
    MATCH = "Match"

    _property_mappings: ClassVar[dict[str, str]] = {
        "match": "Match",
    }

    match: Optional[SubjectAlternativeNameMatchers] = None


@dataclass
class TcpTimeout(PropertyType):
    IDLE = "Idle"

    _property_mappings: ClassVar[dict[str, str]] = {
        "idle": "Idle",
    }

    idle: Optional[Duration] = None


@dataclass
class TlsValidationContext(PropertyType):
    SUBJECT_ALTERNATIVE_NAMES = "SubjectAlternativeNames"
    TRUST = "Trust"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subject_alternative_names": "SubjectAlternativeNames",
        "trust": "Trust",
    }

    subject_alternative_names: Optional[SubjectAlternativeNames] = None
    trust: Optional[TlsValidationContextTrust] = None


@dataclass
class TlsValidationContextAcmTrust(PropertyType):
    CERTIFICATE_AUTHORITY_ARNS = "CertificateAuthorityArns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_authority_arns": "CertificateAuthorityArns",
    }

    certificate_authority_arns: Optional[Union[list[str], Ref]] = None


@dataclass
class TlsValidationContextFileTrust(PropertyType):
    CERTIFICATE_CHAIN = "CertificateChain"

    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_chain": "CertificateChain",
    }

    certificate_chain: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TlsValidationContextSdsTrust(PropertyType):
    SECRET_NAME = "SecretName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_name": "SecretName",
    }

    secret_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TlsValidationContextTrust(PropertyType):
    SDS = "SDS"
    ACM = "ACM"
    FILE = "File"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sds": "SDS",
        "acm": "ACM",
        "file": "File",
    }

    sds: Optional[TlsValidationContextSdsTrust] = None
    acm: Optional[TlsValidationContextAcmTrust] = None
    file: Optional[TlsValidationContextFileTrust] = None


@dataclass
class VirtualNodeConnectionPool(PropertyType):
    TCP = "TCP"
    HTTP2 = "HTTP2"
    HTTP = "HTTP"
    GRPC = "GRPC"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tcp": "TCP",
        "http2": "HTTP2",
        "http": "HTTP",
        "grpc": "GRPC",
    }

    tcp: Optional[VirtualNodeTcpConnectionPool] = None
    http2: Optional[VirtualNodeHttp2ConnectionPool] = None
    http: Optional[VirtualNodeHttpConnectionPool] = None
    grpc: Optional[VirtualNodeGrpcConnectionPool] = None


@dataclass
class VirtualNodeGrpcConnectionPool(PropertyType):
    MAX_REQUESTS = "MaxRequests"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_requests": "MaxRequests",
    }

    max_requests: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualNodeHttp2ConnectionPool(PropertyType):
    MAX_REQUESTS = "MaxRequests"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_requests": "MaxRequests",
    }

    max_requests: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualNodeHttpConnectionPool(PropertyType):
    MAX_CONNECTIONS = "MaxConnections"
    MAX_PENDING_REQUESTS = "MaxPendingRequests"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_connections": "MaxConnections",
        "max_pending_requests": "MaxPendingRequests",
    }

    max_connections: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_pending_requests: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualNodeSpec(PropertyType):
    LOGGING = "Logging"
    BACKENDS = "Backends"
    LISTENERS = "Listeners"
    BACKEND_DEFAULTS = "BackendDefaults"
    SERVICE_DISCOVERY = "ServiceDiscovery"

    _property_mappings: ClassVar[dict[str, str]] = {
        "logging": "Logging",
        "backends": "Backends",
        "listeners": "Listeners",
        "backend_defaults": "BackendDefaults",
        "service_discovery": "ServiceDiscovery",
    }

    logging: Optional[Logging] = None
    backends: Optional[list[Backend]] = None
    listeners: Optional[list[Listener]] = None
    backend_defaults: Optional[BackendDefaults] = None
    service_discovery: Optional[ServiceDiscovery] = None


@dataclass
class VirtualNodeTcpConnectionPool(PropertyType):
    MAX_CONNECTIONS = "MaxConnections"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_connections": "MaxConnections",
    }

    max_connections: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualServiceBackend(PropertyType):
    CLIENT_POLICY = "ClientPolicy"
    VIRTUAL_SERVICE_NAME = "VirtualServiceName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "client_policy": "ClientPolicy",
        "virtual_service_name": "VirtualServiceName",
    }

    client_policy: Optional[ClientPolicy] = None
    virtual_service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

