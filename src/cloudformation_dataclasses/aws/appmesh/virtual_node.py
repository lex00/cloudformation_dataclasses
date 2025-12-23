"""PropertyTypes for AWS::AppMesh::VirtualNode."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccessLog(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "file": "File",
    }

    file: Optional[FileAccessLog] = None


@dataclass
class AwsCloudMapInstanceAttribute(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AwsCloudMapServiceDiscovery(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "virtual_service": "VirtualService",
    }

    virtual_service: Optional[VirtualServiceBackend] = None


@dataclass
class BackendDefaults(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "client_policy": "ClientPolicy",
    }

    client_policy: Optional[ClientPolicy] = None


@dataclass
class ClientPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tls": "TLS",
    }

    tls: Optional[ClientPolicyTls] = None


@dataclass
class ClientPolicyTls(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "sds": "SDS",
        "file": "File",
    }

    sds: Optional[ListenerTlsSdsCertificate] = None
    file: Optional[ListenerTlsFileCertificate] = None


@dataclass
class DnsServiceDiscovery(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FileAccessLog(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "format": "Format",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    format: Optional[LoggingFormat] = None


@dataclass
class GrpcTimeout(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "per_request": "PerRequest",
        "idle": "Idle",
    }

    per_request: Optional[Duration] = None
    idle: Optional[Duration] = None


@dataclass
class HealthCheck(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "per_request": "PerRequest",
        "idle": "Idle",
    }

    per_request: Optional[Duration] = None
    idle: Optional[Duration] = None


@dataclass
class JsonFormatRef(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Listener(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_arn": "CertificateArn",
    }

    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ListenerTlsCertificate(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "private_key": "PrivateKey",
        "certificate_chain": "CertificateChain",
    }

    private_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate_chain: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ListenerTlsSdsCertificate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_name": "SecretName",
    }

    secret_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ListenerTlsValidationContext(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subject_alternative_names": "SubjectAlternativeNames",
        "trust": "Trust",
    }

    subject_alternative_names: Optional[SubjectAlternativeNames] = None
    trust: Optional[ListenerTlsValidationContextTrust] = None


@dataclass
class ListenerTlsValidationContextTrust(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sds": "SDS",
        "file": "File",
    }

    sds: Optional[TlsValidationContextSdsTrust] = None
    file: Optional[TlsValidationContextFileTrust] = None


@dataclass
class Logging(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "access_log": "AccessLog",
    }

    access_log: Optional[AccessLog] = None


@dataclass
class LoggingFormat(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text": "Text",
        "json": "Json",
    }

    text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    json: Optional[list[JsonFormatRef]] = None


@dataclass
class OutlierDetection(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "protocol": "Protocol",
    }

    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceDiscovery(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dns": "DNS",
        "aws_cloud_map": "AWSCloudMap",
    }

    dns: Optional[DnsServiceDiscovery] = None
    aws_cloud_map: Optional[AwsCloudMapServiceDiscovery] = None


@dataclass
class SubjectAlternativeNameMatchers(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "exact": "Exact",
    }

    exact: Optional[Union[list[str], Ref]] = None


@dataclass
class SubjectAlternativeNames(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "match": "Match",
    }

    match: Optional[SubjectAlternativeNameMatchers] = None


@dataclass
class TcpTimeout(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "idle": "Idle",
    }

    idle: Optional[Duration] = None


@dataclass
class TlsValidationContext(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subject_alternative_names": "SubjectAlternativeNames",
        "trust": "Trust",
    }

    subject_alternative_names: Optional[SubjectAlternativeNames] = None
    trust: Optional[TlsValidationContextTrust] = None


@dataclass
class TlsValidationContextAcmTrust(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_authority_arns": "CertificateAuthorityArns",
    }

    certificate_authority_arns: Optional[Union[list[str], Ref]] = None


@dataclass
class TlsValidationContextFileTrust(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_chain": "CertificateChain",
    }

    certificate_chain: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TlsValidationContextSdsTrust(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_name": "SecretName",
    }

    secret_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TlsValidationContextTrust(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_requests": "MaxRequests",
    }

    max_requests: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualNodeHttp2ConnectionPool(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_requests": "MaxRequests",
    }

    max_requests: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualNodeHttpConnectionPool(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_connections": "MaxConnections",
        "max_pending_requests": "MaxPendingRequests",
    }

    max_connections: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_pending_requests: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualNodeSpec(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_connections": "MaxConnections",
    }

    max_connections: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualServiceBackend(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "client_policy": "ClientPolicy",
        "virtual_service_name": "VirtualServiceName",
    }

    client_policy: Optional[ClientPolicy] = None
    virtual_service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

