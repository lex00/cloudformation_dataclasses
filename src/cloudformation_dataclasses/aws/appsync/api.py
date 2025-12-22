"""PropertyTypes for AWS::AppSync::Api."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ApiCacheStatus:
    """ApiCacheStatus enum values."""

    AVAILABLE = "AVAILABLE"
    CREATING = "CREATING"
    DELETING = "DELETING"
    MODIFYING = "MODIFYING"
    FAILED = "FAILED"


class ApiCacheType:
    """ApiCacheType enum values."""

    T2_SMALL = "T2_SMALL"
    T2_MEDIUM = "T2_MEDIUM"
    R4_LARGE = "R4_LARGE"
    R4_XLARGE = "R4_XLARGE"
    R4_2XLARGE = "R4_2XLARGE"
    R4_4XLARGE = "R4_4XLARGE"
    R4_8XLARGE = "R4_8XLARGE"
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"
    XLARGE = "XLARGE"
    LARGE_2X = "LARGE_2X"
    LARGE_4X = "LARGE_4X"
    LARGE_8X = "LARGE_8X"
    LARGE_12X = "LARGE_12X"


class ApiCachingBehavior:
    """ApiCachingBehavior enum values."""

    FULL_REQUEST_CACHING = "FULL_REQUEST_CACHING"
    PER_RESOLVER_CACHING = "PER_RESOLVER_CACHING"
    OPERATION_LEVEL_CACHING = "OPERATION_LEVEL_CACHING"


class AssociationStatus:
    """AssociationStatus enum values."""

    PROCESSING = "PROCESSING"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"


class AuthenticationType:
    """AuthenticationType enum values."""

    API_KEY = "API_KEY"
    AWS_IAM = "AWS_IAM"
    AMAZON_COGNITO_USER_POOLS = "AMAZON_COGNITO_USER_POOLS"
    OPENID_CONNECT = "OPENID_CONNECT"
    AWS_LAMBDA = "AWS_LAMBDA"


class AuthorizationType:
    """AuthorizationType enum values."""

    AWS_IAM = "AWS_IAM"


class BadRequestReason:
    """BadRequestReason enum values."""

    CODE_ERROR = "CODE_ERROR"


class CacheHealthMetricsConfig:
    """CacheHealthMetricsConfig enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ConflictDetectionType:
    """ConflictDetectionType enum values."""

    VERSION = "VERSION"
    NONE = "NONE"


class ConflictHandlerType:
    """ConflictHandlerType enum values."""

    OPTIMISTIC_CONCURRENCY = "OPTIMISTIC_CONCURRENCY"
    LAMBDA = "LAMBDA"
    AUTOMERGE = "AUTOMERGE"
    NONE = "NONE"


class DataSourceIntrospectionStatus:
    """DataSourceIntrospectionStatus enum values."""

    PROCESSING = "PROCESSING"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"


class DataSourceLevelMetricsBehavior:
    """DataSourceLevelMetricsBehavior enum values."""

    FULL_REQUEST_DATA_SOURCE_METRICS = "FULL_REQUEST_DATA_SOURCE_METRICS"
    PER_DATA_SOURCE_METRICS = "PER_DATA_SOURCE_METRICS"


class DataSourceLevelMetricsConfig:
    """DataSourceLevelMetricsConfig enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DataSourceType:
    """DataSourceType enum values."""

    AWS_LAMBDA = "AWS_LAMBDA"
    AMAZON_DYNAMODB = "AMAZON_DYNAMODB"
    AMAZON_ELASTICSEARCH = "AMAZON_ELASTICSEARCH"
    NONE = "NONE"
    HTTP = "HTTP"
    RELATIONAL_DATABASE = "RELATIONAL_DATABASE"
    AMAZON_OPENSEARCH_SERVICE = "AMAZON_OPENSEARCH_SERVICE"
    AMAZON_EVENTBRIDGE = "AMAZON_EVENTBRIDGE"
    AMAZON_BEDROCK_RUNTIME = "AMAZON_BEDROCK_RUNTIME"


class DefaultAction:
    """DefaultAction enum values."""

    ALLOW = "ALLOW"
    DENY = "DENY"


class EventLogLevel:
    """EventLogLevel enum values."""

    NONE = "NONE"
    ERROR = "ERROR"
    ALL = "ALL"
    INFO = "INFO"
    DEBUG = "DEBUG"


class FieldLogLevel:
    """FieldLogLevel enum values."""

    NONE = "NONE"
    ERROR = "ERROR"
    ALL = "ALL"
    INFO = "INFO"
    DEBUG = "DEBUG"


class GraphQLApiIntrospectionConfig:
    """GraphQLApiIntrospectionConfig enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class GraphQLApiType:
    """GraphQLApiType enum values."""

    GRAPHQL = "GRAPHQL"
    MERGED = "MERGED"


class GraphQLApiVisibility:
    """GraphQLApiVisibility enum values."""

    GLOBAL = "GLOBAL"
    PRIVATE = "PRIVATE"


class HandlerBehavior:
    """HandlerBehavior enum values."""

    CODE = "CODE"
    DIRECT = "DIRECT"


class InvokeType:
    """InvokeType enum values."""

    REQUEST_RESPONSE = "REQUEST_RESPONSE"
    EVENT = "EVENT"


class MergeType:
    """MergeType enum values."""

    MANUAL_MERGE = "MANUAL_MERGE"
    AUTO_MERGE = "AUTO_MERGE"


class OperationLevelMetricsConfig:
    """OperationLevelMetricsConfig enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class OutputType:
    """OutputType enum values."""

    SDL = "SDL"
    JSON = "JSON"


class Ownership:
    """Ownership enum values."""

    CURRENT_ACCOUNT = "CURRENT_ACCOUNT"
    OTHER_ACCOUNTS = "OTHER_ACCOUNTS"


class RelationalDatabaseSourceType:
    """RelationalDatabaseSourceType enum values."""

    RDS_HTTP_ENDPOINT = "RDS_HTTP_ENDPOINT"


class ResolverKind:
    """ResolverKind enum values."""

    UNIT = "UNIT"
    PIPELINE = "PIPELINE"


class ResolverLevelMetricsBehavior:
    """ResolverLevelMetricsBehavior enum values."""

    FULL_REQUEST_RESOLVER_METRICS = "FULL_REQUEST_RESOLVER_METRICS"
    PER_RESOLVER_METRICS = "PER_RESOLVER_METRICS"


class ResolverLevelMetricsConfig:
    """ResolverLevelMetricsConfig enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class RuntimeName:
    """RuntimeName enum values."""

    APPSYNC_JS = "APPSYNC_JS"


class SchemaStatus:
    """SchemaStatus enum values."""

    PROCESSING = "PROCESSING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class SourceApiAssociationStatus:
    """SourceApiAssociationStatus enum values."""

    MERGE_SCHEDULED = "MERGE_SCHEDULED"
    MERGE_FAILED = "MERGE_FAILED"
    MERGE_SUCCESS = "MERGE_SUCCESS"
    MERGE_IN_PROGRESS = "MERGE_IN_PROGRESS"
    AUTO_MERGE_SCHEDULE_FAILED = "AUTO_MERGE_SCHEDULE_FAILED"
    DELETION_SCHEDULED = "DELETION_SCHEDULED"
    DELETION_IN_PROGRESS = "DELETION_IN_PROGRESS"
    DELETION_FAILED = "DELETION_FAILED"


class TypeDefinitionFormat:
    """TypeDefinitionFormat enum values."""

    SDL = "SDL"
    JSON = "JSON"


@dataclass
class AuthMode(PropertyType):
    AUTH_TYPE = "AuthType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_type": "AuthType",
    }

    auth_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AuthProvider(PropertyType):
    OPEN_ID_CONNECT_CONFIG = "OpenIDConnectConfig"
    COGNITO_CONFIG = "CognitoConfig"
    LAMBDA_AUTHORIZER_CONFIG = "LambdaAuthorizerConfig"
    AUTH_TYPE = "AuthType"

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
    APP_ID_CLIENT_REGEX = "AppIdClientRegex"
    USER_POOL_ID = "UserPoolId"
    AWS_REGION = "AwsRegion"

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
    HTTP = "Http"
    REALTIME = "Realtime"

    _property_mappings: ClassVar[dict[str, str]] = {
        "http": "Http",
        "realtime": "Realtime",
    }

    http: Optional[Union[str, Ref, GetAtt, Sub]] = None
    realtime: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EventConfig(PropertyType):
    AUTH_PROVIDERS = "AuthProviders"
    CONNECTION_AUTH_MODES = "ConnectionAuthModes"
    DEFAULT_PUBLISH_AUTH_MODES = "DefaultPublishAuthModes"
    DEFAULT_SUBSCRIBE_AUTH_MODES = "DefaultSubscribeAuthModes"
    LOG_CONFIG = "LogConfig"

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
    CLOUD_WATCH_LOGS_ROLE_ARN = "CloudWatchLogsRoleArn"
    LOG_LEVEL = "LogLevel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_logs_role_arn": "CloudWatchLogsRoleArn",
        "log_level": "LogLevel",
    }

    cloud_watch_logs_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_level: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LambdaAuthorizerConfig(PropertyType):
    IDENTITY_VALIDATION_EXPRESSION = "IdentityValidationExpression"
    AUTHORIZER_URI = "AuthorizerUri"
    AUTHORIZER_RESULT_TTL_IN_SECONDS = "AuthorizerResultTtlInSeconds"

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
    ISSUER = "Issuer"
    CLIENT_ID = "ClientId"
    AUTH_TTL = "AuthTTL"
    IAT_TTL = "IatTTL"

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

