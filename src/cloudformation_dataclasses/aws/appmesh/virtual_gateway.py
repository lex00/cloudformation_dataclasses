"""PropertyTypes for AWS::AppMesh::VirtualGateway."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class JsonFormatRef(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LoggingFormat(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "text": "Text",
        "json": "Json",
    }

    text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    json: Optional[list[JsonFormatRef]] = None


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
class VirtualGatewayAccessLog(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "file": "File",
    }

    file: Optional[VirtualGatewayFileAccessLog] = None


@dataclass
class VirtualGatewayBackendDefaults(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "client_policy": "ClientPolicy",
    }

    client_policy: Optional[VirtualGatewayClientPolicy] = None


@dataclass
class VirtualGatewayClientPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tls": "TLS",
    }

    tls: Optional[VirtualGatewayClientPolicyTls] = None


@dataclass
class VirtualGatewayClientPolicyTls(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "validation": "Validation",
        "enforce": "Enforce",
        "ports": "Ports",
        "certificate": "Certificate",
    }

    validation: Optional[VirtualGatewayTlsValidationContext] = None
    enforce: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ports: Optional[Union[list[int], Ref]] = None
    certificate: Optional[VirtualGatewayClientTlsCertificate] = None


@dataclass
class VirtualGatewayClientTlsCertificate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sds": "SDS",
        "file": "File",
    }

    sds: Optional[VirtualGatewayListenerTlsSdsCertificate] = None
    file: Optional[VirtualGatewayListenerTlsFileCertificate] = None


@dataclass
class VirtualGatewayConnectionPool(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "http2": "HTTP2",
        "http": "HTTP",
        "grpc": "GRPC",
    }

    http2: Optional[VirtualGatewayHttp2ConnectionPool] = None
    http: Optional[VirtualGatewayHttpConnectionPool] = None
    grpc: Optional[VirtualGatewayGrpcConnectionPool] = None


@dataclass
class VirtualGatewayFileAccessLog(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "format": "Format",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    format: Optional[LoggingFormat] = None


@dataclass
class VirtualGatewayGrpcConnectionPool(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_requests": "MaxRequests",
    }

    max_requests: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualGatewayHealthCheckPolicy(PropertyType):
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
class VirtualGatewayHttp2ConnectionPool(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_requests": "MaxRequests",
    }

    max_requests: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualGatewayHttpConnectionPool(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_connections": "MaxConnections",
        "max_pending_requests": "MaxPendingRequests",
    }

    max_connections: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_pending_requests: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualGatewayListener(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "connection_pool": "ConnectionPool",
        "health_check": "HealthCheck",
        "tls": "TLS",
        "port_mapping": "PortMapping",
    }

    connection_pool: Optional[VirtualGatewayConnectionPool] = None
    health_check: Optional[VirtualGatewayHealthCheckPolicy] = None
    tls: Optional[VirtualGatewayListenerTls] = None
    port_mapping: Optional[VirtualGatewayPortMapping] = None


@dataclass
class VirtualGatewayListenerTls(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "validation": "Validation",
        "mode": "Mode",
        "certificate": "Certificate",
    }

    validation: Optional[VirtualGatewayListenerTlsValidationContext] = None
    mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate: Optional[VirtualGatewayListenerTlsCertificate] = None


@dataclass
class VirtualGatewayListenerTlsAcmCertificate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_arn": "CertificateArn",
    }

    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualGatewayListenerTlsCertificate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sds": "SDS",
        "acm": "ACM",
        "file": "File",
    }

    sds: Optional[VirtualGatewayListenerTlsSdsCertificate] = None
    acm: Optional[VirtualGatewayListenerTlsAcmCertificate] = None
    file: Optional[VirtualGatewayListenerTlsFileCertificate] = None


@dataclass
class VirtualGatewayListenerTlsFileCertificate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "private_key": "PrivateKey",
        "certificate_chain": "CertificateChain",
    }

    private_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate_chain: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualGatewayListenerTlsSdsCertificate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_name": "SecretName",
    }

    secret_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualGatewayListenerTlsValidationContext(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subject_alternative_names": "SubjectAlternativeNames",
        "trust": "Trust",
    }

    subject_alternative_names: Optional[SubjectAlternativeNames] = None
    trust: Optional[VirtualGatewayListenerTlsValidationContextTrust] = None


@dataclass
class VirtualGatewayListenerTlsValidationContextTrust(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sds": "SDS",
        "file": "File",
    }

    sds: Optional[VirtualGatewayTlsValidationContextSdsTrust] = None
    file: Optional[VirtualGatewayTlsValidationContextFileTrust] = None


@dataclass
class VirtualGatewayLogging(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "access_log": "AccessLog",
    }

    access_log: Optional[VirtualGatewayAccessLog] = None


@dataclass
class VirtualGatewayPortMapping(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "protocol": "Protocol",
    }

    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualGatewaySpec(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "logging": "Logging",
        "listeners": "Listeners",
        "backend_defaults": "BackendDefaults",
    }

    logging: Optional[VirtualGatewayLogging] = None
    listeners: Optional[list[VirtualGatewayListener]] = None
    backend_defaults: Optional[VirtualGatewayBackendDefaults] = None


@dataclass
class VirtualGatewayTlsValidationContext(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subject_alternative_names": "SubjectAlternativeNames",
        "trust": "Trust",
    }

    subject_alternative_names: Optional[SubjectAlternativeNames] = None
    trust: Optional[VirtualGatewayTlsValidationContextTrust] = None


@dataclass
class VirtualGatewayTlsValidationContextAcmTrust(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_authority_arns": "CertificateAuthorityArns",
    }

    certificate_authority_arns: Optional[Union[list[str], Ref]] = None


@dataclass
class VirtualGatewayTlsValidationContextFileTrust(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_chain": "CertificateChain",
    }

    certificate_chain: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualGatewayTlsValidationContextSdsTrust(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_name": "SecretName",
    }

    secret_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VirtualGatewayTlsValidationContextTrust(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sds": "SDS",
        "acm": "ACM",
        "file": "File",
    }

    sds: Optional[VirtualGatewayTlsValidationContextSdsTrust] = None
    acm: Optional[VirtualGatewayTlsValidationContextAcmTrust] = None
    file: Optional[VirtualGatewayTlsValidationContextFileTrust] = None

