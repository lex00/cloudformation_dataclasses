"""PropertyTypes for AWS::BedrockAgentCore::GatewayTarget."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ApiKeyCredentialProvider(PropertyType):
    PROVIDER_ARN = "ProviderArn"
    CREDENTIAL_LOCATION = "CredentialLocation"
    CREDENTIAL_PREFIX = "CredentialPrefix"
    CREDENTIAL_PARAMETER_NAME = "CredentialParameterName"

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
    S3 = "S3"
    INLINE_PAYLOAD = "InlinePayload"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "inline_payload": "InlinePayload",
    }

    s3: Optional[S3Configuration] = None
    inline_payload: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CredentialProvider(PropertyType):
    OAUTH_CREDENTIAL_PROVIDER = "OauthCredentialProvider"
    API_KEY_CREDENTIAL_PROVIDER = "ApiKeyCredentialProvider"

    _property_mappings: ClassVar[dict[str, str]] = {
        "oauth_credential_provider": "OauthCredentialProvider",
        "api_key_credential_provider": "ApiKeyCredentialProvider",
    }

    oauth_credential_provider: Optional[OAuthCredentialProvider] = None
    api_key_credential_provider: Optional[ApiKeyCredentialProvider] = None


@dataclass
class CredentialProviderConfiguration(PropertyType):
    CREDENTIAL_PROVIDER = "CredentialProvider"
    CREDENTIAL_PROVIDER_TYPE = "CredentialProviderType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "credential_provider": "CredentialProvider",
        "credential_provider_type": "CredentialProviderType",
    }

    credential_provider: Optional[CredentialProvider] = None
    credential_provider_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class McpLambdaTargetConfiguration(PropertyType):
    LAMBDA_ARN = "LambdaArn"
    TOOL_SCHEMA = "ToolSchema"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_arn": "LambdaArn",
        "tool_schema": "ToolSchema",
    }

    lambda_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tool_schema: Optional[ToolSchema] = None


@dataclass
class McpServerTargetConfiguration(PropertyType):
    ENDPOINT = "Endpoint"

    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint": "Endpoint",
    }

    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class McpTargetConfiguration(PropertyType):
    MCP_SERVER = "McpServer"
    OPEN_API_SCHEMA = "OpenApiSchema"
    SMITHY_MODEL = "SmithyModel"
    LAMBDA = "Lambda"

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
    PROVIDER_ARN = "ProviderArn"
    SCOPES = "Scopes"
    CUSTOM_PARAMETERS = "CustomParameters"

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
    BUCKET_OWNER_ACCOUNT_ID = "BucketOwnerAccountId"
    URI = "Uri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_owner_account_id": "BucketOwnerAccountId",
        "uri": "Uri",
    }

    bucket_owner_account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SchemaDefinition(PropertyType):
    TYPE = "Type"
    DESCRIPTION = "Description"
    REQUIRED = "Required"
    ITEMS = "Items"
    PROPERTIES = "Properties"

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
    MCP = "Mcp"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mcp": "Mcp",
    }

    mcp: Optional[McpTargetConfiguration] = None


@dataclass
class ToolDefinition(PropertyType):
    OUTPUT_SCHEMA = "OutputSchema"
    DESCRIPTION = "Description"
    INPUT_SCHEMA = "InputSchema"
    NAME = "Name"

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
    S3 = "S3"
    INLINE_PAYLOAD = "InlinePayload"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "inline_payload": "InlinePayload",
    }

    s3: Optional[S3Configuration] = None
    inline_payload: Optional[list[ToolDefinition]] = None

