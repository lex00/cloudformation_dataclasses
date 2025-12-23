"""PropertyTypes for AWS::AppSync::GraphQLApi."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AdditionalAuthenticationProvider(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "open_id_connect_config": "OpenIDConnectConfig",
        "lambda_authorizer_config": "LambdaAuthorizerConfig",
        "user_pool_config": "UserPoolConfig",
        "authentication_type": "AuthenticationType",
    }

    open_id_connect_config: Optional[OpenIDConnectConfig] = None
    lambda_authorizer_config: Optional[LambdaAuthorizerConfig] = None
    user_pool_config: Optional[CognitoUserPoolConfig] = None
    authentication_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CognitoUserPoolConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "app_id_client_regex": "AppIdClientRegex",
        "user_pool_id": "UserPoolId",
        "aws_region": "AwsRegion",
    }

    app_id_client_regex: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_pool_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aws_region: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EnhancedMetricsConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "operation_level_metrics_config": "OperationLevelMetricsConfig",
        "resolver_level_metrics_behavior": "ResolverLevelMetricsBehavior",
        "data_source_level_metrics_behavior": "DataSourceLevelMetricsBehavior",
    }

    operation_level_metrics_config: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resolver_level_metrics_behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_source_level_metrics_behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LambdaAuthorizerConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "identity_validation_expression": "IdentityValidationExpression",
        "authorizer_uri": "AuthorizerUri",
        "authorizer_result_ttl_in_seconds": "AuthorizerResultTtlInSeconds",
    }

    identity_validation_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authorizer_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authorizer_result_ttl_in_seconds: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class LogConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_logs_role_arn": "CloudWatchLogsRoleArn",
        "exclude_verbose_content": "ExcludeVerboseContent",
        "field_log_level": "FieldLogLevel",
    }

    cloud_watch_logs_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exclude_verbose_content: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    field_log_level: Optional[Union[str, Ref, GetAtt, Sub]] = None


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


@dataclass
class UserPoolConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "app_id_client_regex": "AppIdClientRegex",
        "user_pool_id": "UserPoolId",
        "aws_region": "AwsRegion",
        "default_action": "DefaultAction",
    }

    app_id_client_regex: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_pool_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aws_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default_action: Optional[Union[str, Ref, GetAtt, Sub]] = None

