"""PropertyTypes for AWS::FSx::Volume."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AggregateConfiguration(PropertyType):
    AGGREGATES = "Aggregates"
    CONSTITUENTS_PER_AGGREGATE = "ConstituentsPerAggregate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aggregates": "Aggregates",
        "constituents_per_aggregate": "ConstituentsPerAggregate",
    }

    aggregates: Optional[Union[list[str], Ref]] = None
    constituents_per_aggregate: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AutocommitPeriod(PropertyType):
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, AutocommitPeriodType, Ref, GetAtt, Sub]] = None
    value: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ClientConfigurations(PropertyType):
    OPTIONS = "Options"
    CLIENTS = "Clients"

    _property_mappings: ClassVar[dict[str, str]] = {
        "options": "Options",
        "clients": "Clients",
    }

    options: Optional[Union[list[str], Ref]] = None
    clients: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NfsExports(PropertyType):
    CLIENT_CONFIGURATIONS = "ClientConfigurations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "client_configurations": "ClientConfigurations",
    }

    client_configurations: Optional[list[ClientConfigurations]] = None


@dataclass
class OntapConfiguration(PropertyType):
    JUNCTION_PATH = "JunctionPath"
    STORAGE_VIRTUAL_MACHINE_ID = "StorageVirtualMachineId"
    TIERING_POLICY = "TieringPolicy"
    SIZE_IN_MEGABYTES = "SizeInMegabytes"
    VOLUME_STYLE = "VolumeStyle"
    SIZE_IN_BYTES = "SizeInBytes"
    SECURITY_STYLE = "SecurityStyle"
    SNAPLOCK_CONFIGURATION = "SnaplockConfiguration"
    AGGREGATE_CONFIGURATION = "AggregateConfiguration"
    SNAPSHOT_POLICY = "SnapshotPolicy"
    STORAGE_EFFICIENCY_ENABLED = "StorageEfficiencyEnabled"
    COPY_TAGS_TO_BACKUPS = "CopyTagsToBackups"
    ONTAP_VOLUME_TYPE = "OntapVolumeType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "junction_path": "JunctionPath",
        "storage_virtual_machine_id": "StorageVirtualMachineId",
        "tiering_policy": "TieringPolicy",
        "size_in_megabytes": "SizeInMegabytes",
        "volume_style": "VolumeStyle",
        "size_in_bytes": "SizeInBytes",
        "security_style": "SecurityStyle",
        "snaplock_configuration": "SnaplockConfiguration",
        "aggregate_configuration": "AggregateConfiguration",
        "snapshot_policy": "SnapshotPolicy",
        "storage_efficiency_enabled": "StorageEfficiencyEnabled",
        "copy_tags_to_backups": "CopyTagsToBackups",
        "ontap_volume_type": "OntapVolumeType",
    }

    junction_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    storage_virtual_machine_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tiering_policy: Optional[TieringPolicy] = None
    size_in_megabytes: Optional[Union[str, Ref, GetAtt, Sub]] = None
    volume_style: Optional[Union[str, Ref, GetAtt, Sub]] = None
    size_in_bytes: Optional[Union[str, Ref, GetAtt, Sub]] = None
    security_style: Optional[Union[str, Ref, GetAtt, Sub]] = None
    snaplock_configuration: Optional[SnaplockConfiguration] = None
    aggregate_configuration: Optional[AggregateConfiguration] = None
    snapshot_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    storage_efficiency_enabled: Optional[Union[str, Ref, GetAtt, Sub]] = None
    copy_tags_to_backups: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ontap_volume_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OpenZFSConfiguration(PropertyType):
    READ_ONLY = "ReadOnly"
    OPTIONS = "Options"
    DATA_COMPRESSION_TYPE = "DataCompressionType"
    NFS_EXPORTS = "NfsExports"
    STORAGE_CAPACITY_QUOTA_GI_B = "StorageCapacityQuotaGiB"
    COPY_TAGS_TO_SNAPSHOTS = "CopyTagsToSnapshots"
    PARENT_VOLUME_ID = "ParentVolumeId"
    STORAGE_CAPACITY_RESERVATION_GI_B = "StorageCapacityReservationGiB"
    RECORD_SIZE_KI_B = "RecordSizeKiB"
    ORIGIN_SNAPSHOT = "OriginSnapshot"
    USER_AND_GROUP_QUOTAS = "UserAndGroupQuotas"

    _property_mappings: ClassVar[dict[str, str]] = {
        "read_only": "ReadOnly",
        "options": "Options",
        "data_compression_type": "DataCompressionType",
        "nfs_exports": "NfsExports",
        "storage_capacity_quota_gi_b": "StorageCapacityQuotaGiB",
        "copy_tags_to_snapshots": "CopyTagsToSnapshots",
        "parent_volume_id": "ParentVolumeId",
        "storage_capacity_reservation_gi_b": "StorageCapacityReservationGiB",
        "record_size_ki_b": "RecordSizeKiB",
        "origin_snapshot": "OriginSnapshot",
        "user_and_group_quotas": "UserAndGroupQuotas",
    }

    read_only: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    options: Optional[Union[list[str], Ref]] = None
    data_compression_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    nfs_exports: Optional[list[NfsExports]] = None
    storage_capacity_quota_gi_b: Optional[Union[int, Ref, GetAtt, Sub]] = None
    copy_tags_to_snapshots: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    parent_volume_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    storage_capacity_reservation_gi_b: Optional[Union[int, Ref, GetAtt, Sub]] = None
    record_size_ki_b: Optional[Union[int, Ref, GetAtt, Sub]] = None
    origin_snapshot: Optional[OriginSnapshot] = None
    user_and_group_quotas: Optional[list[UserAndGroupQuotas]] = None


@dataclass
class OriginSnapshot(PropertyType):
    COPY_STRATEGY = "CopyStrategy"
    SNAPSHOT_ARN = "SnapshotARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "copy_strategy": "CopyStrategy",
        "snapshot_arn": "SnapshotARN",
    }

    copy_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    snapshot_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RetentionPeriod(PropertyType):
    TYPE = "Type"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
    }

    type_: Optional[Union[str, RetentionPeriodType, Ref, GetAtt, Sub]] = None
    value: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SnaplockConfiguration(PropertyType):
    AUDIT_LOG_VOLUME = "AuditLogVolume"
    VOLUME_APPEND_MODE_ENABLED = "VolumeAppendModeEnabled"
    AUTOCOMMIT_PERIOD = "AutocommitPeriod"
    RETENTION_PERIOD = "RetentionPeriod"
    PRIVILEGED_DELETE = "PrivilegedDelete"
    SNAPLOCK_TYPE = "SnaplockType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "audit_log_volume": "AuditLogVolume",
        "volume_append_mode_enabled": "VolumeAppendModeEnabled",
        "autocommit_period": "AutocommitPeriod",
        "retention_period": "RetentionPeriod",
        "privileged_delete": "PrivilegedDelete",
        "snaplock_type": "SnaplockType",
    }

    audit_log_volume: Optional[Union[str, Ref, GetAtt, Sub]] = None
    volume_append_mode_enabled: Optional[Union[str, Ref, GetAtt, Sub]] = None
    autocommit_period: Optional[AutocommitPeriod] = None
    retention_period: Optional[SnaplockRetentionPeriod] = None
    privileged_delete: Optional[Union[str, PrivilegedDelete, Ref, GetAtt, Sub]] = None
    snaplock_type: Optional[Union[str, SnaplockType, Ref, GetAtt, Sub]] = None


@dataclass
class SnaplockRetentionPeriod(PropertyType):
    DEFAULT_RETENTION = "DefaultRetention"
    MAXIMUM_RETENTION = "MaximumRetention"
    MINIMUM_RETENTION = "MinimumRetention"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_retention": "DefaultRetention",
        "maximum_retention": "MaximumRetention",
        "minimum_retention": "MinimumRetention",
    }

    default_retention: Optional[RetentionPeriod] = None
    maximum_retention: Optional[RetentionPeriod] = None
    minimum_retention: Optional[RetentionPeriod] = None


@dataclass
class TieringPolicy(PropertyType):
    COOLING_PERIOD = "CoolingPeriod"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cooling_period": "CoolingPeriod",
        "name": "Name",
    }

    cooling_period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, TieringPolicyName, Ref, GetAtt, Sub]] = None


@dataclass
class UserAndGroupQuotas(PropertyType):
    TYPE = "Type"
    ID = "Id"
    STORAGE_CAPACITY_QUOTA_GI_B = "StorageCapacityQuotaGiB"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "id": "Id",
        "storage_capacity_quota_gi_b": "StorageCapacityQuotaGiB",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[int, Ref, GetAtt, Sub]] = None
    storage_capacity_quota_gi_b: Optional[Union[int, Ref, GetAtt, Sub]] = None

