"""PropertyTypes for AWS::ApiGatewayV2::ApiGatewayManagedOverrides."""

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
class AccessLogSettings(PropertyType):
    FORMAT = "Format"
    DESTINATION_ARN = "DestinationArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "format": "Format",
        "destination_arn": "DestinationArn",
    }

    format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IntegrationOverrides(PropertyType):
    DESCRIPTION = "Description"
    PAYLOAD_FORMAT_VERSION = "PayloadFormatVersion"
    TIMEOUT_IN_MILLIS = "TimeoutInMillis"
    INTEGRATION_METHOD = "IntegrationMethod"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "payload_format_version": "PayloadFormatVersion",
        "timeout_in_millis": "TimeoutInMillis",
        "integration_method": "IntegrationMethod",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload_format_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timeout_in_millis: Optional[Union[int, Ref, GetAtt, Sub]] = None
    integration_method: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RouteOverrides(PropertyType):
    TARGET = "Target"
    AUTHORIZER_ID = "AuthorizerId"
    OPERATION_NAME = "OperationName"
    AUTHORIZATION_SCOPES = "AuthorizationScopes"
    AUTHORIZATION_TYPE = "AuthorizationType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target": "Target",
        "authorizer_id": "AuthorizerId",
        "operation_name": "OperationName",
        "authorization_scopes": "AuthorizationScopes",
        "authorization_type": "AuthorizationType",
    }

    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authorizer_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    operation_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authorization_scopes: Optional[Union[list[str], Ref]] = None
    authorization_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RouteSettings(PropertyType):
    LOGGING_LEVEL = "LoggingLevel"
    DATA_TRACE_ENABLED = "DataTraceEnabled"
    THROTTLING_BURST_LIMIT = "ThrottlingBurstLimit"
    DETAILED_METRICS_ENABLED = "DetailedMetricsEnabled"
    THROTTLING_RATE_LIMIT = "ThrottlingRateLimit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "logging_level": "LoggingLevel",
        "data_trace_enabled": "DataTraceEnabled",
        "throttling_burst_limit": "ThrottlingBurstLimit",
        "detailed_metrics_enabled": "DetailedMetricsEnabled",
        "throttling_rate_limit": "ThrottlingRateLimit",
    }

    logging_level: Optional[Union[str, LoggingLevel, Ref, GetAtt, Sub]] = None
    data_trace_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    throttling_burst_limit: Optional[Union[int, Ref, GetAtt, Sub]] = None
    detailed_metrics_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    throttling_rate_limit: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class StageOverrides(PropertyType):
    DESCRIPTION = "Description"
    ACCESS_LOG_SETTINGS = "AccessLogSettings"
    AUTO_DEPLOY = "AutoDeploy"
    ROUTE_SETTINGS = "RouteSettings"
    STAGE_VARIABLES = "StageVariables"
    DEFAULT_ROUTE_SETTINGS = "DefaultRouteSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "access_log_settings": "AccessLogSettings",
        "auto_deploy": "AutoDeploy",
        "route_settings": "RouteSettings",
        "stage_variables": "StageVariables",
        "default_route_settings": "DefaultRouteSettings",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    access_log_settings: Optional[AccessLogSettings] = None
    auto_deploy: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    route_settings: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    stage_variables: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    default_route_settings: Optional[RouteSettings] = None

