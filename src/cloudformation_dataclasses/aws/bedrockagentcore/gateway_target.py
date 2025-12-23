"""PropertyTypes for AWS::BedrockAgentCore::GatewayTarget."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ApiKeyCredentialProvider(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "provider_arn": "ProviderArn",
        "credential_location": "CredentialLocation",
        "credential_prefix": "CredentialPrefix",
        "credential_parameter_name": "CredentialParameterName",
    }

    provider_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credential_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credential_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    credential_parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ApiSchemaConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "inline_payload": "InlinePayload",
    }

    s3: Optional[S3Configuration] = None
    inline_payload: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CredentialProvider(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "oauth_credential_provider": "OauthCredentialProvider",
        "api_key_credential_provider": "ApiKeyCredentialProvider",
    }

    oauth_credential_provider: Optional[OAuthCredentialProvider] = None
    api_key_credential_provider: Optional[ApiKeyCredentialProvider] = None


@dataclass
class CredentialProviderConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "credential_provider": "CredentialProvider",
        "credential_provider_type": "CredentialProviderType",
    }

    credential_provider: Optional[CredentialProvider] = None
    credential_provider_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class McpLambdaTargetConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_arn": "LambdaArn",
        "tool_schema": "ToolSchema",
    }

    lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tool_schema: Optional[ToolSchema] = None


@dataclass
class McpServerTargetConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint": "Endpoint",
    }

    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class McpTargetConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mcp_server": "McpServer",
        "open_api_schema": "OpenApiSchema",
        "smithy_model": "SmithyModel",
        "lambda_": "Lambda",
    }

    mcp_server: Optional[McpServerTargetConfiguration] = None
    open_api_schema: Optional[ApiSchemaConfiguration] = None
    smithy_model: Optional[ApiSchemaConfiguration] = None
    lambda_: Optional[McpLambdaTargetConfiguration] = None


@dataclass
class OAuthCredentialProvider(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "provider_arn": "ProviderArn",
        "scopes": "Scopes",
        "custom_parameters": "CustomParameters",
    }

    provider_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scopes: Optional[Union[list[str], Ref]] = None
    custom_parameters: Optional[dict[str, str]] = None


@dataclass
class S3Configuration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_owner_account_id": "BucketOwnerAccountId",
        "uri": "Uri",
    }

    bucket_owner_account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SchemaDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "description": "Description",
        "required": "Required",
        "items": "Items",
        "properties": "Properties",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    required: Optional[Union[list[str], Ref]] = None
    items: Optional[SchemaDefinition] = None
    properties: Optional[dict[str, Any]] = None


@dataclass
class TargetConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mcp": "Mcp",
    }

    mcp: Optional[McpTargetConfiguration] = None


@dataclass
class ToolDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "output_schema": "OutputSchema",
        "description": "Description",
        "input_schema": "InputSchema",
        "name": "Name",
    }

    output_schema: Optional[SchemaDefinition] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_schema: Optional[SchemaDefinition] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ToolSchema(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "inline_payload": "InlinePayload",
    }

    s3: Optional[S3Configuration] = None
    inline_payload: Optional[list[ToolDefinition]] = None

