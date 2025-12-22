"""PropertyTypes for AWS::AppSync::DataSource."""

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
class AuthorizationConfig(PropertyType):
    AWS_IAM_CONFIG = "AwsIamConfig"
    AUTHORIZATION_TYPE = "AuthorizationType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_iam_config": "AwsIamConfig",
        "authorization_type": "AuthorizationType",
    }

    aws_iam_config: Optional[AwsIamConfig] = None
    authorization_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AwsIamConfig(PropertyType):
    SIGNING_REGION = "SigningRegion"
    SIGNING_SERVICE_NAME = "SigningServiceName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "signing_region": "SigningRegion",
        "signing_service_name": "SigningServiceName",
    }

    signing_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    signing_service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DeltaSyncConfig(PropertyType):
    BASE_TABLE_TTL = "BaseTableTTL"
    DELTA_SYNC_TABLE_TTL = "DeltaSyncTableTTL"
    DELTA_SYNC_TABLE_NAME = "DeltaSyncTableName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "base_table_ttl": "BaseTableTTL",
        "delta_sync_table_ttl": "DeltaSyncTableTTL",
        "delta_sync_table_name": "DeltaSyncTableName",
    }

    base_table_ttl: Optional[Union[str, Ref, GetAtt, Sub]] = None
    delta_sync_table_ttl: Optional[Union[str, Ref, GetAtt, Sub]] = None
    delta_sync_table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DynamoDBConfig(PropertyType):
    TABLE_NAME = "TableName"
    AWS_REGION = "AwsRegion"
    VERSIONED = "Versioned"
    DELTA_SYNC_CONFIG = "DeltaSyncConfig"
    USE_CALLER_CREDENTIALS = "UseCallerCredentials"

    _property_mappings: ClassVar[dict[str, str]] = {
        "table_name": "TableName",
        "aws_region": "AwsRegion",
        "versioned": "Versioned",
        "delta_sync_config": "DeltaSyncConfig",
        "use_caller_credentials": "UseCallerCredentials",
    }

    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aws_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    versioned: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    delta_sync_config: Optional[DeltaSyncConfig] = None
    use_caller_credentials: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EventBridgeConfig(PropertyType):
    EVENT_BUS_ARN = "EventBusArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "event_bus_arn": "EventBusArn",
    }

    event_bus_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HttpConfig(PropertyType):
    ENDPOINT = "Endpoint"
    AUTHORIZATION_CONFIG = "AuthorizationConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint": "Endpoint",
        "authorization_config": "AuthorizationConfig",
    }

    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    authorization_config: Optional[AuthorizationConfig] = None


@dataclass
class LambdaConfig(PropertyType):
    LAMBDA_FUNCTION_ARN = "LambdaFunctionArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_function_arn": "LambdaFunctionArn",
    }

    lambda_function_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OpenSearchServiceConfig(PropertyType):
    AWS_REGION = "AwsRegion"
    ENDPOINT = "Endpoint"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_region": "AwsRegion",
        "endpoint": "Endpoint",
    }

    aws_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RdsHttpEndpointConfig(PropertyType):
    AWS_REGION = "AwsRegion"
    SCHEMA = "Schema"
    DATABASE_NAME = "DatabaseName"
    DB_CLUSTER_IDENTIFIER = "DbClusterIdentifier"
    AWS_SECRET_STORE_ARN = "AwsSecretStoreArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_region": "AwsRegion",
        "schema": "Schema",
        "database_name": "DatabaseName",
        "db_cluster_identifier": "DbClusterIdentifier",
        "aws_secret_store_arn": "AwsSecretStoreArn",
    }

    aws_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schema: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    db_cluster_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aws_secret_store_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RelationalDatabaseConfig(PropertyType):
    RDS_HTTP_ENDPOINT_CONFIG = "RdsHttpEndpointConfig"
    RELATIONAL_DATABASE_SOURCE_TYPE = "RelationalDatabaseSourceType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rds_http_endpoint_config": "RdsHttpEndpointConfig",
        "relational_database_source_type": "RelationalDatabaseSourceType",
    }

    rds_http_endpoint_config: Optional[RdsHttpEndpointConfig] = None
    relational_database_source_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

