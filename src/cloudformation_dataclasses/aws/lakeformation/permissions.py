"""PropertyTypes for AWS::LakeFormation::Permissions."""

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
class DataLakePrincipal(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_lake_principal_identifier": "DataLakePrincipalIdentifier",
    }

    data_lake_principal_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataLocationResource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_resource": "S3Resource",
        "catalog_id": "CatalogId",
    }

    s3_resource: Optional[Union[str, Ref, GetAtt, Sub]] = None
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
class Resource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "table_resource": "TableResource",
        "database_resource": "DatabaseResource",
        "data_location_resource": "DataLocationResource",
        "table_with_columns_resource": "TableWithColumnsResource",
    }

    table_resource: Optional[TableResource] = None
    database_resource: Optional[DatabaseResource] = None
    data_location_resource: Optional[DataLocationResource] = None
    table_with_columns_resource: Optional[TableWithColumnsResource] = None


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
    table_wildcard: Optional[TableWildcard] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TableWildcard(PropertyType):
    pass


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

