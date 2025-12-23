"""PropertyTypes for AWS::LakeFormation::PrincipalPermissions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ColumnWildcard(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "excluded_column_names": "ExcludedColumnNames",
    }

    excluded_column_names: Optional[Union[list[str], Ref]] = None


@dataclass
class DataCellsFilterResource(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_lake_principal_identifier": "DataLakePrincipalIdentifier",
    }

    data_lake_principal_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataLocationResource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceArn",
        "catalog_id": "CatalogId",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatabaseResource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "catalog_id": "CatalogId",
        "name": "Name",
    }

    catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LFTag(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tag_key": "TagKey",
        "tag_values": "TagValues",
    }

    tag_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_values: Optional[Union[list[str], Ref]] = None


@dataclass
class LFTagKeyResource(PropertyType):
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

