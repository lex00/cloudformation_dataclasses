"""PropertyTypes for AWS::LakeFormation::DataCellsFilter."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ApplicationStatus:
    """ApplicationStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ComparisonOperator:
    """ComparisonOperator enum values."""

    EQ = "EQ"
    NE = "NE"
    LE = "LE"
    LT = "LT"
    GE = "GE"
    GT = "GT"
    CONTAINS = "CONTAINS"
    NOT_CONTAINS = "NOT_CONTAINS"
    BEGINS_WITH = "BEGINS_WITH"
    IN = "IN"
    BETWEEN = "BETWEEN"


class DataLakeResourceType:
    """DataLakeResourceType enum values."""

    CATALOG = "CATALOG"
    DATABASE = "DATABASE"
    TABLE = "TABLE"
    DATA_LOCATION = "DATA_LOCATION"
    LF_TAG = "LF_TAG"
    LF_TAG_POLICY = "LF_TAG_POLICY"
    LF_TAG_POLICY_DATABASE = "LF_TAG_POLICY_DATABASE"
    LF_TAG_POLICY_TABLE = "LF_TAG_POLICY_TABLE"
    LF_NAMED_TAG_EXPRESSION = "LF_NAMED_TAG_EXPRESSION"


class EnableStatus:
    """EnableStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class FieldNameString:
    """FieldNameString enum values."""

    RESOURCE_ARN = "RESOURCE_ARN"
    ROLE_ARN = "ROLE_ARN"
    LAST_MODIFIED = "LAST_MODIFIED"


class OptimizerType:
    """OptimizerType enum values."""

    COMPACTION = "COMPACTION"
    GARBAGE_COLLECTION = "GARBAGE_COLLECTION"
    ALL = "ALL"


class Permission:
    """Permission enum values."""

    ALL = "ALL"
    SELECT = "SELECT"
    ALTER = "ALTER"
    DROP = "DROP"
    DELETE = "DELETE"
    INSERT = "INSERT"
    DESCRIBE = "DESCRIBE"
    CREATE_DATABASE = "CREATE_DATABASE"
    CREATE_TABLE = "CREATE_TABLE"
    DATA_LOCATION_ACCESS = "DATA_LOCATION_ACCESS"
    CREATE_LF_TAG = "CREATE_LF_TAG"
    ASSOCIATE = "ASSOCIATE"
    GRANT_WITH_LF_TAG_EXPRESSION = "GRANT_WITH_LF_TAG_EXPRESSION"
    CREATE_LF_TAG_EXPRESSION = "CREATE_LF_TAG_EXPRESSION"
    CREATE_CATALOG = "CREATE_CATALOG"
    SUPER_USER = "SUPER_USER"


class PermissionType:
    """PermissionType enum values."""

    COLUMN_PERMISSION = "COLUMN_PERMISSION"
    CELL_FILTER_PERMISSION = "CELL_FILTER_PERMISSION"
    NESTED_PERMISSION = "NESTED_PERMISSION"
    NESTED_CELL_PERMISSION = "NESTED_CELL_PERMISSION"


class QueryStateString:
    """QueryStateString enum values."""

    PENDING = "PENDING"
    WORKUNITS_AVAILABLE = "WORKUNITS_AVAILABLE"
    ERROR = "ERROR"
    FINISHED = "FINISHED"
    EXPIRED = "EXPIRED"


class ResourceShareType:
    """ResourceShareType enum values."""

    FOREIGN = "FOREIGN"
    ALL = "ALL"


class ResourceType:
    """ResourceType enum values."""

    DATABASE = "DATABASE"
    TABLE = "TABLE"


class ServiceAuthorization:
    """ServiceAuthorization enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class TransactionStatus:
    """TransactionStatus enum values."""

    ACTIVE = "ACTIVE"
    COMMITTED = "COMMITTED"
    ABORTED = "ABORTED"
    COMMIT_IN_PROGRESS = "COMMIT_IN_PROGRESS"


class TransactionStatusFilter:
    """TransactionStatusFilter enum values."""

    ALL = "ALL"
    COMPLETED = "COMPLETED"
    ACTIVE = "ACTIVE"
    COMMITTED = "COMMITTED"
    ABORTED = "ABORTED"


class TransactionType:
    """TransactionType enum values."""

    READ_AND_WRITE = "READ_AND_WRITE"
    READ_ONLY = "READ_ONLY"


@dataclass
class ColumnWildcard(PropertyType):
    EXCLUDED_COLUMN_NAMES = "ExcludedColumnNames"

    _property_mappings: ClassVar[dict[str, str]] = {
        "excluded_column_names": "ExcludedColumnNames",
    }

    excluded_column_names: Optional[Union[list[str], Ref]] = None


@dataclass
class RowFilter(PropertyType):
    ALL_ROWS_WILDCARD = "AllRowsWildcard"
    FILTER_EXPRESSION = "FilterExpression"

    _property_mappings: ClassVar[dict[str, str]] = {
        "all_rows_wildcard": "AllRowsWildcard",
        "filter_expression": "FilterExpression",
    }

    all_rows_wildcard: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    filter_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None

