"""PropertyTypes for AWS::AppSync::DataSource."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

