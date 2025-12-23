"""PropertyTypes for AWS::BedrockAgentCore::Gateway."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AuthorizerConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_jwt_authorizer": "CustomJWTAuthorizer",
    }

    custom_jwt_authorizer: Optional[CustomJWTAuthorizerConfiguration] = None


@dataclass
class CustomJWTAuthorizerConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "discovery_url": "DiscoveryUrl",
        "allowed_audience": "AllowedAudience",
        "allowed_clients": "AllowedClients",
    }

    discovery_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    allowed_audience: Optional[Union[list[str], Ref]] = None
    allowed_clients: Optional[Union[list[str], Ref]] = None


@dataclass
class GatewayProtocolConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mcp": "Mcp",
    }

    mcp: Optional[MCPGatewayConfiguration] = None


@dataclass
class MCPGatewayConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "supported_versions": "SupportedVersions",
        "instructions": "Instructions",
        "search_type": "SearchType",
    }

    supported_versions: Optional[Union[list[str], Ref]] = None
    instructions: Optional[Union[str, Ref, GetAtt, Sub]] = None
    search_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WorkloadIdentityDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "workload_identity_arn": "WorkloadIdentityArn",
    }

    workload_identity_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

