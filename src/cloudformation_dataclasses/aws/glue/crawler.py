"""PropertyTypes for AWS::Glue::Crawler."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CatalogTarget(PropertyType):
    CONNECTION_NAME = "ConnectionName"
    DATABASE_NAME = "DatabaseName"
    DLQ_EVENT_QUEUE_ARN = "DlqEventQueueArn"
    TABLES = "Tables"
    EVENT_QUEUE_ARN = "EventQueueArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connection_name": "ConnectionName",
        "database_name": "DatabaseName",
        "dlq_event_queue_arn": "DlqEventQueueArn",
        "tables": "Tables",
        "event_queue_arn": "EventQueueArn",
    }

    connection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dlq_event_queue_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tables: Optional[Union[list[str], Ref]] = None
    event_queue_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DeltaTarget(PropertyType):
    CONNECTION_NAME = "ConnectionName"
    CREATE_NATIVE_DELTA_TABLE = "CreateNativeDeltaTable"
    WRITE_MANIFEST = "WriteManifest"
    DELTA_TABLES = "DeltaTables"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connection_name": "ConnectionName",
        "create_native_delta_table": "CreateNativeDeltaTable",
        "write_manifest": "WriteManifest",
        "delta_tables": "DeltaTables",
    }

    connection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    create_native_delta_table: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    write_manifest: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    delta_tables: Optional[Union[list[str], Ref]] = None


@dataclass
class DynamoDBTarget(PropertyType):
    PATH = "Path"
    SCAN_RATE = "ScanRate"
    SCAN_ALL = "ScanAll"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "scan_rate": "ScanRate",
        "scan_all": "ScanAll",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    scan_rate: Optional[Union[float, Ref, GetAtt, Sub]] = None
    scan_all: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class HudiTarget(PropertyType):
    CONNECTION_NAME = "ConnectionName"
    EXCLUSIONS = "Exclusions"
    PATHS = "Paths"
    MAXIMUM_TRAVERSAL_DEPTH = "MaximumTraversalDepth"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connection_name": "ConnectionName",
        "exclusions": "Exclusions",
        "paths": "Paths",
        "maximum_traversal_depth": "MaximumTraversalDepth",
    }

    connection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exclusions: Optional[Union[list[str], Ref]] = None
    paths: Optional[Union[list[str], Ref]] = None
    maximum_traversal_depth: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class IcebergTarget(PropertyType):
    CONNECTION_NAME = "ConnectionName"
    EXCLUSIONS = "Exclusions"
    PATHS = "Paths"
    MAXIMUM_TRAVERSAL_DEPTH = "MaximumTraversalDepth"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connection_name": "ConnectionName",
        "exclusions": "Exclusions",
        "paths": "Paths",
        "maximum_traversal_depth": "MaximumTraversalDepth",
    }

    connection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exclusions: Optional[Union[list[str], Ref]] = None
    paths: Optional[Union[list[str], Ref]] = None
    maximum_traversal_depth: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class JdbcTarget(PropertyType):
    CONNECTION_NAME = "ConnectionName"
    PATH = "Path"
    EXCLUSIONS = "Exclusions"
    ENABLE_ADDITIONAL_METADATA = "EnableAdditionalMetadata"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connection_name": "ConnectionName",
        "path": "Path",
        "exclusions": "Exclusions",
        "enable_additional_metadata": "EnableAdditionalMetadata",
    }

    connection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exclusions: Optional[Union[list[str], Ref]] = None
    enable_additional_metadata: Optional[Union[list[str], Ref]] = None


@dataclass
class LakeFormationConfiguration(PropertyType):
    ACCOUNT_ID = "AccountId"
    USE_LAKE_FORMATION_CREDENTIALS = "UseLakeFormationCredentials"

    _property_mappings: ClassVar[dict[str, str]] = {
        "account_id": "AccountId",
        "use_lake_formation_credentials": "UseLakeFormationCredentials",
    }

    account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    use_lake_formation_credentials: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MongoDBTarget(PropertyType):
    CONNECTION_NAME = "ConnectionName"
    PATH = "Path"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connection_name": "ConnectionName",
        "path": "Path",
    }

    connection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RecrawlPolicy(PropertyType):
    RECRAWL_BEHAVIOR = "RecrawlBehavior"

    _property_mappings: ClassVar[dict[str, str]] = {
        "recrawl_behavior": "RecrawlBehavior",
    }

    recrawl_behavior: Optional[Union[str, RecrawlBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class S3Target(PropertyType):
    CONNECTION_NAME = "ConnectionName"
    PATH = "Path"
    SAMPLE_SIZE = "SampleSize"
    EXCLUSIONS = "Exclusions"
    DLQ_EVENT_QUEUE_ARN = "DlqEventQueueArn"
    EVENT_QUEUE_ARN = "EventQueueArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connection_name": "ConnectionName",
        "path": "Path",
        "sample_size": "SampleSize",
        "exclusions": "Exclusions",
        "dlq_event_queue_arn": "DlqEventQueueArn",
        "event_queue_arn": "EventQueueArn",
    }

    connection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sample_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    exclusions: Optional[Union[list[str], Ref]] = None
    dlq_event_queue_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    event_queue_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Schedule(PropertyType):
    SCHEDULE_EXPRESSION = "ScheduleExpression"

    _property_mappings: ClassVar[dict[str, str]] = {
        "schedule_expression": "ScheduleExpression",
    }

    schedule_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SchemaChangePolicy(PropertyType):
    UPDATE_BEHAVIOR = "UpdateBehavior"
    DELETE_BEHAVIOR = "DeleteBehavior"

    _property_mappings: ClassVar[dict[str, str]] = {
        "update_behavior": "UpdateBehavior",
        "delete_behavior": "DeleteBehavior",
    }

    update_behavior: Optional[Union[str, UpdateBehavior, Ref, GetAtt, Sub]] = None
    delete_behavior: Optional[Union[str, DeleteBehavior, Ref, GetAtt, Sub]] = None


@dataclass
class Targets(PropertyType):
    HUDI_TARGETS = "HudiTargets"
    S3_TARGETS = "S3Targets"
    CATALOG_TARGETS = "CatalogTargets"
    DELTA_TARGETS = "DeltaTargets"
    MONGO_DB_TARGETS = "MongoDBTargets"
    JDBC_TARGETS = "JdbcTargets"
    DYNAMO_DB_TARGETS = "DynamoDBTargets"
    ICEBERG_TARGETS = "IcebergTargets"

    _property_mappings: ClassVar[dict[str, str]] = {
        "hudi_targets": "HudiTargets",
        "s3_targets": "S3Targets",
        "catalog_targets": "CatalogTargets",
        "delta_targets": "DeltaTargets",
        "mongo_db_targets": "MongoDBTargets",
        "jdbc_targets": "JdbcTargets",
        "dynamo_db_targets": "DynamoDBTargets",
        "iceberg_targets": "IcebergTargets",
    }

    hudi_targets: Optional[list[HudiTarget]] = None
    s3_targets: Optional[list[S3Target]] = None
    catalog_targets: Optional[list[CatalogTarget]] = None
    delta_targets: Optional[list[DeltaTarget]] = None
    mongo_db_targets: Optional[list[MongoDBTarget]] = None
    jdbc_targets: Optional[list[JdbcTarget]] = None
    dynamo_db_targets: Optional[list[DynamoDBTarget]] = None
    iceberg_targets: Optional[list[IcebergTarget]] = None

