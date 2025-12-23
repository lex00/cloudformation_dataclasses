"""PropertyTypes for AWS::LakeFormation::TagAssociation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DatabaseResource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "catalog_id": "CatalogId",
        "name": "Name",
    }

    catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LFTagPair(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tag_key": "TagKey",
        "catalog_id": "CatalogId",
        "tag_values": "TagValues",
    }

    tag_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_values: Optional[Union[list[str], Ref]] = None


@dataclass
class Resource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "table": "Table",
        "table_with_columns": "TableWithColumns",
        "database": "Database",
        "catalog": "Catalog",
    }

    table: Optional[TableResource] = None
    table_with_columns: Optional[TableWithColumnsResource] = None
    database: Optional[DatabaseResource] = None
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
    }

    column_names: Optional[Union[list[str], Ref]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

