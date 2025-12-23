"""PropertyTypes for AWS::Glue::TableOptimizer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IcebergConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "orphan_file_retention_period_in_days": "OrphanFileRetentionPeriodInDays",
        "location": "Location",
    }

    orphan_file_retention_period_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    location: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IcebergRetentionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "clean_expired_files": "CleanExpiredFiles",
        "snapshot_retention_period_in_days": "SnapshotRetentionPeriodInDays",
        "number_of_snapshots_to_retain": "NumberOfSnapshotsToRetain",
    }

    clean_expired_files: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    snapshot_retention_period_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    number_of_snapshots_to_retain: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class OrphanFileDeletionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iceberg_configuration": "IcebergConfiguration",
    }

    iceberg_configuration: Optional[IcebergConfiguration] = None


@dataclass
class RetentionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iceberg_configuration": "IcebergConfiguration",
    }

    iceberg_configuration: Optional[IcebergRetentionConfiguration] = None


@dataclass
class TableOptimizerConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "retention_configuration": "RetentionConfiguration",
        "orphan_file_deletion_configuration": "OrphanFileDeletionConfiguration",
        "enabled": "Enabled",
        "vpc_configuration": "VpcConfiguration",
        "role_arn": "RoleArn",
    }

    retention_configuration: Optional[RetentionConfiguration] = None
    orphan_file_deletion_configuration: Optional[OrphanFileDeletionConfiguration] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    vpc_configuration: Optional[VpcConfiguration] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "glue_connection_name": "GlueConnectionName",
    }

    glue_connection_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

