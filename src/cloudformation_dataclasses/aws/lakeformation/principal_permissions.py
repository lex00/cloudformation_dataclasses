"""PropertyTypes for AWS::LakeFormation::PrincipalPermissions."""

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
class DataCellsFilterResource(PropertyType):
    TABLE_NAME = "TableName"
    DATABASE_NAME = "DatabaseName"
    TABLE_CATALOG_ID = "TableCatalogId"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "table_name": "TableName",
        "database_name": "DatabaseName",
        "table_catalog_id": "TableCatalogId",
        "name": "Name",
    }

    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataLakePrincipal(PropertyType):
    DATA_LAKE_PRINCIPAL_IDENTIFIER = "DataLakePrincipalIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_lake_principal_identifier": "DataLakePrincipalIdentifier",
    }

    data_lake_principal_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataLocationResource(PropertyType):
    RESOURCE_ARN = "ResourceArn"
    CATALOG_ID = "CatalogId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceArn",
        "catalog_id": "CatalogId",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatabaseResource(PropertyType):
    CATALOG_ID = "CatalogId"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "catalog_id": "CatalogId",
        "name": "Name",
    }

    catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LFTag(PropertyType):
    TAG_KEY = "TagKey"
    TAG_VALUES = "TagValues"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tag_key": "TagKey",
        "tag_values": "TagValues",
    }

    tag_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_values: Optional[Union[list[str], Ref]] = None


@dataclass
class LFTagKeyResource(PropertyType):
    TAG_KEY = "TagKey"
    CATALOG_ID = "CatalogId"
    TAG_VALUES = "TagValues"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tag_key": "TagKey",
        "catalog_id": "CatalogId",
        "tag_values": "TagValues",
    }

    tag_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_values: Optional[Union[list[str], Ref]] = None


@dataclass
class LFTagPolicyResource(PropertyType):
    EXPRESSION = "Expression"
    RESOURCE_TYPE = "ResourceType"
    CATALOG_ID = "CatalogId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "expression": "Expression",
        "resource_type": "ResourceType",
        "catalog_id": "CatalogId",
    }

    expression: Optional[list[LFTag]] = None
    resource_type: Optional[Union[str, ResourceType, Ref, GetAtt, Sub]] = None
    catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Resource(PropertyType):
    LF_TAG = "LFTag"
    TABLE = "Table"
    DATA_CELLS_FILTER = "DataCellsFilter"
    TABLE_WITH_COLUMNS = "TableWithColumns"
    LF_TAG_POLICY = "LFTagPolicy"
    DATABASE = "Database"
    DATA_LOCATION = "DataLocation"
    CATALOG = "Catalog"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lf_tag": "LFTag",
        "table": "Table",
        "data_cells_filter": "DataCellsFilter",
        "table_with_columns": "TableWithColumns",
        "lf_tag_policy": "LFTagPolicy",
        "database": "Database",
        "data_location": "DataLocation",
        "catalog": "Catalog",
    }

    lf_tag: Optional[LFTagKeyResource] = None
    table: Optional[TableResource] = None
    data_cells_filter: Optional[DataCellsFilterResource] = None
    table_with_columns: Optional[TableWithColumnsResource] = None
    lf_tag_policy: Optional[LFTagPolicyResource] = None
    database: Optional[DatabaseResource] = None
    data_location: Optional[DataLocationResource] = None
    catalog: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class TableResource(PropertyType):
    DATABASE_NAME = "DatabaseName"
    CATALOG_ID = "CatalogId"
    TABLE_WILDCARD = "TableWildcard"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "database_name": "DatabaseName",
        "catalog_id": "CatalogId",
        "table_wildcard": "TableWildcard",
        "name": "Name",
    }

    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_wildcard: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TableWithColumnsResource(PropertyType):
    COLUMN_NAMES = "ColumnNames"
    DATABASE_NAME = "DatabaseName"
    CATALOG_ID = "CatalogId"
    NAME = "Name"
    COLUMN_WILDCARD = "ColumnWildcard"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_names": "ColumnNames",
        "database_name": "DatabaseName",
        "catalog_id": "CatalogId",
        "name": "Name",
        "column_wildcard": "ColumnWildcard",
    }

    column_names: Optional[Union[list[str], Ref]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_wildcard: Optional[ColumnWildcard] = None

