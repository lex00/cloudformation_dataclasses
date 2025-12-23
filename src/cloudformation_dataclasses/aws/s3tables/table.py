"""PropertyTypes for AWS::S3Tables::Table."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Compaction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "target_file_size_mb": "TargetFileSizeMB",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_file_size_mb: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class IcebergMetadata(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iceberg_schema": "IcebergSchema",
    }

    iceberg_schema: Optional[IcebergSchema] = None


@dataclass
class IcebergSchema(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "schema_field_list": "SchemaFieldList",
    }

    schema_field_list: Optional[list[SchemaField]] = None


@dataclass
class SchemaField(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "required": "Required",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    required: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SnapshotManagement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "min_snapshots_to_keep": "MinSnapshotsToKeep",
        "max_snapshot_age_hours": "MaxSnapshotAgeHours",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    min_snapshots_to_keep: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_snapshot_age_hours: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class StorageClassConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_class": "StorageClass",
    }

    storage_class: Optional[Union[str, Ref, GetAtt, Sub]] = None

