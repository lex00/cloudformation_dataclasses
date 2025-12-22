"""PropertyTypes for AWS::Athena::CapacityReservation."""

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
class CapacityAssignment(PropertyType):
    WORKGROUP_NAMES = "WorkgroupNames"

    _property_mappings: ClassVar[dict[str, str]] = {
        "workgroup_names": "WorkgroupNames",
    }

    workgroup_names: Optional[Union[list[str], Ref]] = None


@dataclass
class CapacityAssignmentConfiguration(PropertyType):
    CAPACITY_ASSIGNMENTS = "CapacityAssignments"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_assignments": "CapacityAssignments",
    }

    capacity_assignments: Optional[list[CapacityAssignment]] = None

