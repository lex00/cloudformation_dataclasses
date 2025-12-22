"""PropertyTypes for AWS::ApiGatewayV2::Api."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AuthorizationType:
    """AuthorizationType enum values."""

    NONE = "NONE"
    AWS_IAM = "AWS_IAM"
    CUSTOM = "CUSTOM"
    JWT = "JWT"


class AuthorizerType:
    """AuthorizerType enum values."""

    REQUEST = "REQUEST"
    JWT = "JWT"


class ConnectionType:
    """ConnectionType enum values."""

    INTERNET = "INTERNET"
    VPC_LINK = "VPC_LINK"


class ContentHandlingStrategy:
    """ContentHandlingStrategy enum values."""

    CONVERT_TO_BINARY = "CONVERT_TO_BINARY"
    CONVERT_TO_TEXT = "CONVERT_TO_TEXT"


class DeploymentStatus:
    """DeploymentStatus enum values."""

    PENDING = "PENDING"
    FAILED = "FAILED"
    DEPLOYED = "DEPLOYED"


class DomainNameStatus:
    """DomainNameStatus enum values."""

    AVAILABLE = "AVAILABLE"
    UPDATING = "UPDATING"
    PENDING_CERTIFICATE_REIMPORT = "PENDING_CERTIFICATE_REIMPORT"
    PENDING_OWNERSHIP_VERIFICATION = "PENDING_OWNERSHIP_VERIFICATION"


class EndpointType:
    """EndpointType enum values."""

    REGIONAL = "REGIONAL"
    EDGE = "EDGE"


class IntegrationType:
    """IntegrationType enum values."""

    AWS = "AWS"
    HTTP = "HTTP"
    MOCK = "MOCK"
    HTTP_PROXY = "HTTP_PROXY"
    AWS_PROXY = "AWS_PROXY"


class IpAddressType:
    """IpAddressType enum values."""

    IPV4 = "ipv4"
    DUALSTACK = "dualstack"


class LoggingLevel:
    """LoggingLevel enum values."""

    ERROR = "ERROR"
    INFO = "INFO"
    OFF = "OFF"


class PassthroughBehavior:
    """PassthroughBehavior enum values."""

    WHEN_NO_MATCH = "WHEN_NO_MATCH"
    NEVER = "NEVER"
    WHEN_NO_TEMPLATES = "WHEN_NO_TEMPLATES"


class PreviewStatus:
    """PreviewStatus enum values."""

    PREVIEW_IN_PROGRESS = "PREVIEW_IN_PROGRESS"
    PREVIEW_FAILED = "PREVIEW_FAILED"
    PREVIEW_READY = "PREVIEW_READY"


class ProtocolType:
    """ProtocolType enum values."""

    WEBSOCKET = "WEBSOCKET"
    HTTP = "HTTP"


class PublishStatus:
    """PublishStatus enum values."""

    PUBLISHED = "PUBLISHED"
    PUBLISH_IN_PROGRESS = "PUBLISH_IN_PROGRESS"
    PUBLISH_FAILED = "PUBLISH_FAILED"
    DISABLED = "DISABLED"


class RoutingMode:
    """RoutingMode enum values."""

    API_MAPPING_ONLY = "API_MAPPING_ONLY"
    ROUTING_RULE_ONLY = "ROUTING_RULE_ONLY"
    ROUTING_RULE_THEN_API_MAPPING = "ROUTING_RULE_THEN_API_MAPPING"


class SecurityPolicy:
    """SecurityPolicy enum values."""

    TLS_1_0 = "TLS_1_0"
    TLS_1_2 = "TLS_1_2"


class Status:
    """Status enum values."""

    AVAILABLE = "AVAILABLE"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"


class TryItState:
    """TryItState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class VpcLinkStatus:
    """VpcLinkStatus enum values."""

    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"
    FAILED = "FAILED"
    INACTIVE = "INACTIVE"


class VpcLinkVersion:
    """VpcLinkVersion enum values."""

    V2 = "V2"


@dataclass
class BodyS3Location(PropertyType):
    ETAG = "Etag"
    BUCKET = "Bucket"
    VERSION = "Version"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "etag": "Etag",
        "bucket": "Bucket",
        "version": "Version",
        "key": "Key",
    }

    etag: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Cors(PropertyType):
    ALLOW_ORIGINS = "AllowOrigins"
    ALLOW_CREDENTIALS = "AllowCredentials"
    EXPOSE_HEADERS = "ExposeHeaders"
    ALLOW_HEADERS = "AllowHeaders"
    MAX_AGE = "MaxAge"
    ALLOW_METHODS = "AllowMethods"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allow_origins": "AllowOrigins",
        "allow_credentials": "AllowCredentials",
        "expose_headers": "ExposeHeaders",
        "allow_headers": "AllowHeaders",
        "max_age": "MaxAge",
        "allow_methods": "AllowMethods",
    }

    allow_origins: Optional[Union[list[str], Ref]] = None
    allow_credentials: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    expose_headers: Optional[Union[list[str], Ref]] = None
    allow_headers: Optional[Union[list[str], Ref]] = None
    max_age: Optional[Union[int, Ref, GetAtt, Sub]] = None
    allow_methods: Optional[Union[list[str], Ref]] = None

