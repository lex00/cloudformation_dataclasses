"""PropertyTypes for AWS::BedrockAgentCore::Runtime."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AgentRuntimeArtifact(PropertyType):
    CODE_CONFIGURATION = "CodeConfiguration"
    CONTAINER_CONFIGURATION = "ContainerConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "code_configuration": "CodeConfiguration",
        "container_configuration": "ContainerConfiguration",
    }

    code_configuration: Optional[CodeConfiguration] = None
    container_configuration: Optional[ContainerConfiguration] = None


@dataclass
class AuthorizerConfiguration(PropertyType):
    CUSTOM_JWT_AUTHORIZER = "CustomJWTAuthorizer"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_jwt_authorizer": "CustomJWTAuthorizer",
    }

    custom_jwt_authorizer: Optional[CustomJWTAuthorizerConfiguration] = None


@dataclass
class Code(PropertyType):
    S3 = "S3"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
    }

    s3: Optional[S3Location] = None


@dataclass
class CodeConfiguration(PropertyType):
    RUNTIME = "Runtime"
    ENTRY_POINT = "EntryPoint"
    CODE = "Code"

    _property_mappings: ClassVar[dict[str, str]] = {
        "runtime": "Runtime",
        "entry_point": "EntryPoint",
        "code": "Code",
    }

    runtime: Optional[Union[str, Ref, GetAtt, Sub]] = None
    entry_point: Optional[Union[list[str], Ref]] = None
    code: Optional[Code] = None


@dataclass
class ContainerConfiguration(PropertyType):
    CONTAINER_URI = "ContainerUri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "container_uri": "ContainerUri",
    }

    container_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomJWTAuthorizerConfiguration(PropertyType):
    DISCOVERY_URL = "DiscoveryUrl"
    ALLOWED_AUDIENCE = "AllowedAudience"
    ALLOWED_CLIENTS = "AllowedClients"

    _property_mappings: ClassVar[dict[str, str]] = {
        "discovery_url": "DiscoveryUrl",
        "allowed_audience": "AllowedAudience",
        "allowed_clients": "AllowedClients",
    }

    discovery_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    allowed_audience: Optional[Union[list[str], Ref]] = None
    allowed_clients: Optional[Union[list[str], Ref]] = None


@dataclass
class LifecycleConfiguration(PropertyType):
    MAX_LIFETIME = "MaxLifetime"
    IDLE_RUNTIME_SESSION_TIMEOUT = "IdleRuntimeSessionTimeout"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_lifetime": "MaxLifetime",
        "idle_runtime_session_timeout": "IdleRuntimeSessionTimeout",
    }

    max_lifetime: Optional[Union[int, Ref, GetAtt, Sub]] = None
    idle_runtime_session_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkConfiguration(PropertyType):
    NETWORK_MODE_CONFIG = "NetworkModeConfig"
    NETWORK_MODE = "NetworkMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "network_mode_config": "NetworkModeConfig",
        "network_mode": "NetworkMode",
    }

    network_mode_config: Optional[VpcConfig] = None
    network_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RequestHeaderConfiguration(PropertyType):
    REQUEST_HEADER_ALLOWLIST = "RequestHeaderAllowlist"

    _property_mappings: ClassVar[dict[str, str]] = {
        "request_header_allowlist": "RequestHeaderAllowlist",
    }

    request_header_allowlist: Optional[Union[list[str], Ref]] = None


@dataclass
class S3Location(PropertyType):
    VERSION_ID = "VersionId"
    BUCKET = "Bucket"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "version_id": "VersionId",
        "bucket": "Bucket",
        "prefix": "Prefix",
    }

    version_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConfig(PropertyType):
    SECURITY_GROUPS = "SecurityGroups"
    SUBNETS = "Subnets"

    _property_mappings: ClassVar[dict[str, str]] = {
        "security_groups": "SecurityGroups",
        "subnets": "Subnets",
    }

    security_groups: Optional[Union[list[str], Ref]] = None
    subnets: Optional[Union[list[str], Ref]] = None


@dataclass
class WorkloadIdentityDetails(PropertyType):
    WORKLOAD_IDENTITY_ARN = "WorkloadIdentityArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "workload_identity_arn": "WorkloadIdentityArn",
    }

    workload_identity_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

