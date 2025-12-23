"""PropertyTypes for AWS::CleanRoomsML::TrainingDataset."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ColumnSchema(PropertyType):
    COLUMN_NAME = "ColumnName"
    COLUMN_TYPES = "ColumnTypes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_name": "ColumnName",
        "column_types": "ColumnTypes",
    }

    column_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    column_types: Optional[Union[list[str], Ref]] = None


@dataclass
class DataSource(PropertyType):
    GLUE_DATA_SOURCE = "GlueDataSource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "glue_data_source": "GlueDataSource",
    }

    glue_data_source: Optional[GlueDataSource] = None


@dataclass
class Dataset(PropertyType):
    TYPE = "Type"
    INPUT_CONFIG = "InputConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "input_config": "InputConfig",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    input_config: Optional[DatasetInputConfig] = None


@dataclass
class DatasetInputConfig(PropertyType):
    SCHEMA = "Schema"
    DATA_SOURCE = "DataSource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "schema": "Schema",
        "data_source": "DataSource",
    }

    schema: Optional[list[ColumnSchema]] = None
    data_source: Optional[DataSource] = None


@dataclass
class GlueDataSource(PropertyType):
    TABLE_NAME = "TableName"
    DATABASE_NAME = "DatabaseName"
    CATALOG_ID = "CatalogId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "table_name": "TableName",
        "database_name": "DatabaseName",
        "catalog_id": "CatalogId",
    }

    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    database_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    catalog_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

