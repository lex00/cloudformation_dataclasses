"""PropertyTypes for AWS::AppSync::Api."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AuthMode(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_type": "AuthType",
    }

    auth_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AuthProvider(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "open_id_connect_config": "OpenIDConnectConfig",
        "cognito_config": "CognitoConfig",
        "lambda_authorizer_config": "LambdaAuthorizerConfig",
        "auth_type": "AuthType",
    }

    open_id_connect_config: Optional[OpenIDConnectConfig] = None
    cognito_config: Optional[CognitoConfig] = None
    lambda_authorizer_config: Optional[LambdaAuthorizerConfig] = None
    auth_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CognitoConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "app_id_client_regex": "AppIdClientRegex",
        "user_pool_id": "UserPoolId",
        "aws_region": "AwsRegion",
    }

    app_id_client_regex: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_pool_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aws_region: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DnsMap(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "http": "Http",
        "realtime": "Realtime",
    }

    http: Optional[Union[str, Ref, GetAtt, Sub]] = None
    realtime: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EventConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_providers": "AuthProviders",
        "connection_auth_modes": "ConnectionAuthModes",
        "default_publish_auth_modes": "DefaultPublishAuthModes",
        "default_subscribe_auth_modes": "DefaultSubscribeAuthModes",
        "log_config": "LogConfig",
    }

    auth_providers: Optional[list[AuthProvider]] = None
    connection_auth_modes: Optional[list[AuthMode]] = None
    default_publish_auth_modes: Optional[list[AuthMode]] = None
    default_subscribe_auth_modes: Optional[list[AuthMode]] = None
    log_config: Optional[EventLogConfig] = None


@dataclass
class EventLogConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_logs_role_arn": "CloudWatchLogsRoleArn",
        "log_level": "LogLevel",
    }

    cloud_watch_logs_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_level: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LambdaAuthorizerConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "identity_validation_expression": "IdentityValidationExpression",
        "authorizer_uri": "AuthorizerUri",
        "authorizer_result_ttl_in_seconds": "AuthorizerResultTtlInSeconds",
    }

    identity_validation_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authorizer_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authorizer_result_ttl_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class OpenIDConnectConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "issuer": "Issuer",
        "client_id": "ClientId",
        "auth_ttl": "AuthTTL",
        "iat_ttl": "IatTTL",
    }

    issuer: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_ttl: Optional[Union[float, Ref, GetAtt, Sub]] = None
    iat_ttl: Optional[Union[float, Ref, GetAtt, Sub]] = None

