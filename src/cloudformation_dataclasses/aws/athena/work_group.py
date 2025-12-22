"""PropertyTypes for AWS::Athena::WorkGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AuthenticationType:
    """AuthenticationType enum values."""

    DIRECTORY_IDENTITY = "DIRECTORY_IDENTITY"


class CalculationExecutionState:
    """CalculationExecutionState enum values."""

    CREATING = "CREATING"
    CREATED = "CREATED"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    CANCELING = "CANCELING"
    CANCELED = "CANCELED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class CapacityAllocationStatus:
    """CapacityAllocationStatus enum values."""

    PENDING = "PENDING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class CapacityReservationStatus:
    """CapacityReservationStatus enum values."""

    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    UPDATE_PENDING = "UPDATE_PENDING"


class ColumnNullable:
    """ColumnNullable enum values."""

    NOT_NULL = "NOT_NULL"
    NULLABLE = "NULLABLE"
    UNKNOWN = "UNKNOWN"


class ConnectionType:
    """ConnectionType enum values."""

    DYNAMODB = "DYNAMODB"
    MYSQL = "MYSQL"
    POSTGRESQL = "POSTGRESQL"
    REDSHIFT = "REDSHIFT"
    ORACLE = "ORACLE"
    SYNAPSE = "SYNAPSE"
    SQLSERVER = "SQLSERVER"
    DB2 = "DB2"
    OPENSEARCH = "OPENSEARCH"
    BIGQUERY = "BIGQUERY"
    GOOGLECLOUDSTORAGE = "GOOGLECLOUDSTORAGE"
    HBASE = "HBASE"
    DOCUMENTDB = "DOCUMENTDB"
    CMDB = "CMDB"
    TPCDS = "TPCDS"
    TIMESTREAM = "TIMESTREAM"
    SAPHANA = "SAPHANA"
    SNOWFLAKE = "SNOWFLAKE"
    DATALAKEGEN2 = "DATALAKEGEN2"
    DB2AS400 = "DB2AS400"


class DataCatalogStatus:
    """DataCatalogStatus enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    CREATE_FAILED = "CREATE_FAILED"
    CREATE_FAILED_CLEANUP_IN_PROGRESS = "CREATE_FAILED_CLEANUP_IN_PROGRESS"
    CREATE_FAILED_CLEANUP_COMPLETE = "CREATE_FAILED_CLEANUP_COMPLETE"
    CREATE_FAILED_CLEANUP_FAILED = "CREATE_FAILED_CLEANUP_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_COMPLETE = "DELETE_COMPLETE"
    DELETE_FAILED = "DELETE_FAILED"


class DataCatalogType:
    """DataCatalogType enum values."""

    LAMBDA = "LAMBDA"
    GLUE = "GLUE"
    HIVE = "HIVE"
    FEDERATED = "FEDERATED"


class EncryptionOption:
    """EncryptionOption enum values."""

    SSE_S3 = "SSE_S3"
    SSE_KMS = "SSE_KMS"
    CSE_KMS = "CSE_KMS"


class ExecutorState:
    """ExecutorState enum values."""

    CREATING = "CREATING"
    CREATED = "CREATED"
    REGISTERED = "REGISTERED"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"
    FAILED = "FAILED"


class ExecutorType:
    """ExecutorType enum values."""

    COORDINATOR = "COORDINATOR"
    GATEWAY = "GATEWAY"
    WORKER = "WORKER"


class NotebookType:
    """NotebookType enum values."""

    IPYNB = "IPYNB"


class QueryExecutionState:
    """QueryExecutionState enum values."""

    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


class QueryResultType:
    """QueryResultType enum values."""

    DATA_MANIFEST = "DATA_MANIFEST"
    DATA_ROWS = "DATA_ROWS"


class S3AclOption:
    """S3AclOption enum values."""

    BUCKET_OWNER_FULL_CONTROL = "BUCKET_OWNER_FULL_CONTROL"


class SessionState:
    """SessionState enum values."""

    CREATING = "CREATING"
    CREATED = "CREATED"
    IDLE = "IDLE"
    BUSY = "BUSY"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"
    DEGRADED = "DEGRADED"
    FAILED = "FAILED"


class StatementType:
    """StatementType enum values."""

    DDL = "DDL"
    DML = "DML"
    UTILITY = "UTILITY"


class ThrottleReason:
    """ThrottleReason enum values."""

    CONCURRENT_QUERY_LIMIT_EXCEEDED = "CONCURRENT_QUERY_LIMIT_EXCEEDED"


class WorkGroupState:
    """WorkGroupState enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


@dataclass
class AclConfiguration(PropertyType):
    S3_ACL_OPTION = "S3AclOption"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_acl_option": "S3AclOption",
    }

    s3_acl_option: Optional[Union[str, S3AclOption, Ref, GetAtt, Sub]] = None


@dataclass
class Classification(PropertyType):
    PROPERTIES = "Properties"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "properties": "Properties",
        "name": "Name",
    }

    properties: Optional[dict[str, str]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CloudWatchLoggingConfiguration(PropertyType):
    LOG_GROUP = "LogGroup"
    ENABLED = "Enabled"
    LOG_STREAM_NAME_PREFIX = "LogStreamNamePrefix"
    LOG_TYPES = "LogTypes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group": "LogGroup",
        "enabled": "Enabled",
        "log_stream_name_prefix": "LogStreamNamePrefix",
        "log_types": "LogTypes",
    }

    log_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    log_stream_name_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_types: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class CustomerContentEncryptionConfiguration(PropertyType):
    KMS_KEY = "KmsKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key": "KmsKey",
    }

    kms_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionConfiguration(PropertyType):
    ENCRYPTION_OPTION = "EncryptionOption"
    KMS_KEY = "KmsKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_option": "EncryptionOption",
        "kms_key": "KmsKey",
    }

    encryption_option: Optional[Union[str, EncryptionOption, Ref, GetAtt, Sub]] = None
    kms_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EngineConfiguration(PropertyType):
    SPARK_PROPERTIES = "SparkProperties"
    CLASSIFICATIONS = "Classifications"
    MAX_CONCURRENT_DPUS = "MaxConcurrentDpus"
    COORDINATOR_DPU_SIZE = "CoordinatorDpuSize"
    DEFAULT_EXECUTOR_DPU_SIZE = "DefaultExecutorDpuSize"
    ADDITIONAL_CONFIGS = "AdditionalConfigs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "spark_properties": "SparkProperties",
        "classifications": "Classifications",
        "max_concurrent_dpus": "MaxConcurrentDpus",
        "coordinator_dpu_size": "CoordinatorDpuSize",
        "default_executor_dpu_size": "DefaultExecutorDpuSize",
        "additional_configs": "AdditionalConfigs",
    }

    spark_properties: Optional[dict[str, str]] = None
    classifications: Optional[list[Classification]] = None
    max_concurrent_dpus: Optional[Union[int, Ref, GetAtt, Sub]] = None
    coordinator_dpu_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    default_executor_dpu_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    additional_configs: Optional[dict[str, str]] = None


@dataclass
class EngineVersion(PropertyType):
    SELECTED_ENGINE_VERSION = "SelectedEngineVersion"
    EFFECTIVE_ENGINE_VERSION = "EffectiveEngineVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "selected_engine_version": "SelectedEngineVersion",
        "effective_engine_version": "EffectiveEngineVersion",
    }

    selected_engine_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    effective_engine_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ManagedLoggingConfiguration(PropertyType):
    ENABLED = "Enabled"
    KMS_KEY = "KmsKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "kms_key": "KmsKey",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    kms_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ManagedQueryResultsConfiguration(PropertyType):
    ENCRYPTION_CONFIGURATION = "EncryptionConfiguration"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_configuration": "EncryptionConfiguration",
        "enabled": "Enabled",
    }

    encryption_configuration: Optional[ManagedStorageEncryptionConfiguration] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ManagedStorageEncryptionConfiguration(PropertyType):
    KMS_KEY = "KmsKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key": "KmsKey",
    }

    kms_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MonitoringConfiguration(PropertyType):
    S3_LOGGING_CONFIGURATION = "S3LoggingConfiguration"
    MANAGED_LOGGING_CONFIGURATION = "ManagedLoggingConfiguration"
    CLOUD_WATCH_LOGGING_CONFIGURATION = "CloudWatchLoggingConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_logging_configuration": "S3LoggingConfiguration",
        "managed_logging_configuration": "ManagedLoggingConfiguration",
        "cloud_watch_logging_configuration": "CloudWatchLoggingConfiguration",
    }

    s3_logging_configuration: Optional[S3LoggingConfiguration] = None
    managed_logging_configuration: Optional[ManagedLoggingConfiguration] = None
    cloud_watch_logging_configuration: Optional[CloudWatchLoggingConfiguration] = None


@dataclass
class ResultConfiguration(PropertyType):
    ENCRYPTION_CONFIGURATION = "EncryptionConfiguration"
    OUTPUT_LOCATION = "OutputLocation"
    ACL_CONFIGURATION = "AclConfiguration"
    EXPECTED_BUCKET_OWNER = "ExpectedBucketOwner"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_configuration": "EncryptionConfiguration",
        "output_location": "OutputLocation",
        "acl_configuration": "AclConfiguration",
        "expected_bucket_owner": "ExpectedBucketOwner",
    }

    encryption_configuration: Optional[EncryptionConfiguration] = None
    output_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    acl_configuration: Optional[AclConfiguration] = None
    expected_bucket_owner: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3LoggingConfiguration(PropertyType):
    LOG_LOCATION = "LogLocation"
    ENABLED = "Enabled"
    KMS_KEY = "KmsKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_location": "LogLocation",
        "enabled": "Enabled",
        "kms_key": "KmsKey",
    }

    log_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    kms_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WorkGroupConfiguration(PropertyType):
    ENFORCE_WORK_GROUP_CONFIGURATION = "EnforceWorkGroupConfiguration"
    ENGINE_VERSION = "EngineVersion"
    PUBLISH_CLOUD_WATCH_METRICS_ENABLED = "PublishCloudWatchMetricsEnabled"
    RESULT_CONFIGURATION = "ResultConfiguration"
    ADDITIONAL_CONFIGURATION = "AdditionalConfiguration"
    ENGINE_CONFIGURATION = "EngineConfiguration"
    CUSTOMER_CONTENT_ENCRYPTION_CONFIGURATION = "CustomerContentEncryptionConfiguration"
    BYTES_SCANNED_CUTOFF_PER_QUERY = "BytesScannedCutoffPerQuery"
    MONITORING_CONFIGURATION = "MonitoringConfiguration"
    REQUESTER_PAYS_ENABLED = "RequesterPaysEnabled"
    MANAGED_QUERY_RESULTS_CONFIGURATION = "ManagedQueryResultsConfiguration"
    EXECUTION_ROLE = "ExecutionRole"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enforce_work_group_configuration": "EnforceWorkGroupConfiguration",
        "engine_version": "EngineVersion",
        "publish_cloud_watch_metrics_enabled": "PublishCloudWatchMetricsEnabled",
        "result_configuration": "ResultConfiguration",
        "additional_configuration": "AdditionalConfiguration",
        "engine_configuration": "EngineConfiguration",
        "customer_content_encryption_configuration": "CustomerContentEncryptionConfiguration",
        "bytes_scanned_cutoff_per_query": "BytesScannedCutoffPerQuery",
        "monitoring_configuration": "MonitoringConfiguration",
        "requester_pays_enabled": "RequesterPaysEnabled",
        "managed_query_results_configuration": "ManagedQueryResultsConfiguration",
        "execution_role": "ExecutionRole",
    }

    enforce_work_group_configuration: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    engine_version: Optional[EngineVersion] = None
    publish_cloud_watch_metrics_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    result_configuration: Optional[ResultConfiguration] = None
    additional_configuration: Optional[Union[str, Ref, GetAtt, Sub]] = None
    engine_configuration: Optional[EngineConfiguration] = None
    customer_content_encryption_configuration: Optional[CustomerContentEncryptionConfiguration] = None
    bytes_scanned_cutoff_per_query: Optional[Union[int, Ref, GetAtt, Sub]] = None
    monitoring_configuration: Optional[MonitoringConfiguration] = None
    requester_pays_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    managed_query_results_configuration: Optional[ManagedQueryResultsConfiguration] = None
    execution_role: Optional[Union[str, Ref, GetAtt, Sub]] = None

