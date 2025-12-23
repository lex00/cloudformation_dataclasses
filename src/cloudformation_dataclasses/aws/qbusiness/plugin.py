"""PropertyTypes for AWS::QBusiness::Plugin."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class APISchema(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "payload": "Payload",
    }

    s3: Optional[S3] = None
    payload: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BasicAuthConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "role_arn": "RoleArn",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomPluginConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "api_schema": "ApiSchema",
        "api_schema_type": "ApiSchemaType",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    api_schema: Optional[APISchema] = None
    api_schema_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OAuth2ClientCredentialConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "authorization_url": "AuthorizationUrl",
        "token_url": "TokenUrl",
        "role_arn": "RoleArn",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authorization_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    token_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PluginAuthConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "no_auth_configuration": "NoAuthConfiguration",
        "basic_auth_configuration": "BasicAuthConfiguration",
        "o_auth2_client_credential_configuration": "OAuth2ClientCredentialConfiguration",
    }

    no_auth_configuration: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    basic_auth_configuration: Optional[BasicAuthConfiguration] = None
    o_auth2_client_credential_configuration: Optional[OAuth2ClientCredentialConfiguration] = None


@dataclass
class S3(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "key": "Key",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

