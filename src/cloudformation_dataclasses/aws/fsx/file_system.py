"""PropertyTypes for AWS::FSx::FileSystem."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AuditLogConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "file_access_audit_log_level": "FileAccessAuditLogLevel",
        "file_share_access_audit_log_level": "FileShareAccessAuditLogLevel",
        "audit_log_destination": "AuditLogDestination",
    }

    file_access_audit_log_level: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_share_access_audit_log_level: Optional[Union[str, Ref, GetAtt, Sub]] = None
    audit_log_destination: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ClientConfigurations(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "options": "Options",
        "clients": "Clients",
    }

    options: Optional[Union[list[str], Ref]] = None
    clients: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataReadCacheConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sizing_mode": "SizingMode",
        "size_gi_b": "SizeGiB",
    }

    sizing_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    size_gi_b: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DiskIopsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
        "iops": "Iops",
    }

    mode: Optional[Union[str, DiskIopsConfigurationMode, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class LustreConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "drive_cache_type": "DriveCacheType",
        "auto_import_policy": "AutoImportPolicy",
        "efa_enabled": "EfaEnabled",
        "imported_file_chunk_size": "ImportedFileChunkSize",
        "deployment_type": "DeploymentType",
        "throughput_capacity": "ThroughputCapacity",
        "data_compression_type": "DataCompressionType",
        "data_read_cache_configuration": "DataReadCacheConfiguration",
        "import_path": "ImportPath",
        "weekly_maintenance_start_time": "WeeklyMaintenanceStartTime",
        "metadata_configuration": "MetadataConfiguration",
        "daily_automatic_backup_start_time": "DailyAutomaticBackupStartTime",
        "copy_tags_to_backups": "CopyTagsToBackups",
        "export_path": "ExportPath",
        "per_unit_storage_throughput": "PerUnitStorageThroughput",
        "automatic_backup_retention_days": "AutomaticBackupRetentionDays",
    }

    drive_cache_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auto_import_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    efa_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    imported_file_chunk_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    deployment_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    throughput_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    data_compression_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_read_cache_configuration: Optional[DataReadCacheConfiguration] = None
    import_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    weekly_maintenance_start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metadata_configuration: Optional[MetadataConfiguration] = None
    daily_automatic_backup_start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    copy_tags_to_backups: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    export_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    per_unit_storage_throughput: Optional[Union[int, Ref, GetAtt, Sub]] = None
    automatic_backup_retention_days: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class MetadataConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
        "iops": "Iops",
    }

    mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NfsExports(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "client_configurations": "ClientConfigurations",
    }

    client_configurations: Optional[list[ClientConfigurations]] = None


@dataclass
class OntapConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ha_pairs": "HAPairs",
        "fsx_admin_password": "FsxAdminPassword",
        "throughput_capacity_per_ha_pair": "ThroughputCapacityPerHAPair",
        "deployment_type": "DeploymentType",
        "throughput_capacity": "ThroughputCapacity",
        "endpoint_ip_address_range": "EndpointIpAddressRange",
        "route_table_ids": "RouteTableIds",
        "weekly_maintenance_start_time": "WeeklyMaintenanceStartTime",
        "disk_iops_configuration": "DiskIopsConfiguration",
        "daily_automatic_backup_start_time": "DailyAutomaticBackupStartTime",
        "automatic_backup_retention_days": "AutomaticBackupRetentionDays",
        "endpoint_ipv6_address_range": "EndpointIpv6AddressRange",
        "preferred_subnet_id": "PreferredSubnetId",
    }

    ha_pairs: Optional[Union[int, Ref, GetAtt, Sub]] = None
    fsx_admin_password: Optional[Union[str, Ref, GetAtt, Sub]] = None
    throughput_capacity_per_ha_pair: Optional[Union[int, Ref, GetAtt, Sub]] = None
    deployment_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    throughput_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    endpoint_ip_address_range: Optional[Union[str, Ref, GetAtt, Sub]] = None
    route_table_ids: Optional[Union[list[str], Ref]] = None
    weekly_maintenance_start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    disk_iops_configuration: Optional[DiskIopsConfiguration] = None
    daily_automatic_backup_start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    automatic_backup_retention_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    endpoint_ipv6_address_range: Optional[Union[str, Ref, GetAtt, Sub]] = None
    preferred_subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OpenZFSConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "options": "Options",
        "copy_tags_to_volumes": "CopyTagsToVolumes",
        "deployment_type": "DeploymentType",
        "throughput_capacity": "ThroughputCapacity",
        "root_volume_configuration": "RootVolumeConfiguration",
        "endpoint_ip_address_range": "EndpointIpAddressRange",
        "read_cache_configuration": "ReadCacheConfiguration",
        "route_table_ids": "RouteTableIds",
        "weekly_maintenance_start_time": "WeeklyMaintenanceStartTime",
        "disk_iops_configuration": "DiskIopsConfiguration",
        "daily_automatic_backup_start_time": "DailyAutomaticBackupStartTime",
        "copy_tags_to_backups": "CopyTagsToBackups",
        "automatic_backup_retention_days": "AutomaticBackupRetentionDays",
        "endpoint_ipv6_address_range": "EndpointIpv6AddressRange",
        "preferred_subnet_id": "PreferredSubnetId",
    }

    options: Optional[Union[list[str], Ref]] = None
    copy_tags_to_volumes: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    deployment_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    throughput_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    root_volume_configuration: Optional[RootVolumeConfiguration] = None
    endpoint_ip_address_range: Optional[Union[str, Ref, GetAtt, Sub]] = None
    read_cache_configuration: Optional[ReadCacheConfiguration] = None
    route_table_ids: Optional[Union[list[str], Ref]] = None
    weekly_maintenance_start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    disk_iops_configuration: Optional[DiskIopsConfiguration] = None
    daily_automatic_backup_start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    copy_tags_to_backups: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    automatic_backup_retention_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    endpoint_ipv6_address_range: Optional[Union[str, Ref, GetAtt, Sub]] = None
    preferred_subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReadCacheConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sizing_mode": "SizingMode",
        "size_gi_b": "SizeGiB",
    }

    sizing_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    size_gi_b: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RootVolumeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "read_only": "ReadOnly",
        "data_compression_type": "DataCompressionType",
        "nfs_exports": "NfsExports",
        "copy_tags_to_snapshots": "CopyTagsToSnapshots",
        "record_size_ki_b": "RecordSizeKiB",
        "user_and_group_quotas": "UserAndGroupQuotas",
    }

    read_only: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    data_compression_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    nfs_exports: Optional[list[NfsExports]] = None
    copy_tags_to_snapshots: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    record_size_ki_b: Optional[Union[int, Ref, GetAtt, Sub]] = None
    user_and_group_quotas: Optional[list[UserAndGroupQuotas]] = None


@dataclass
class SelfManagedActiveDirectoryConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "file_system_administrators_group": "FileSystemAdministratorsGroup",
        "user_name": "UserName",
        "domain_name": "DomainName",
        "organizational_unit_distinguished_name": "OrganizationalUnitDistinguishedName",
        "domain_join_service_account_secret": "DomainJoinServiceAccountSecret",
        "dns_ips": "DnsIps",
        "password": "Password",
    }

    file_system_administrators_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    organizational_unit_distinguished_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain_join_service_account_secret: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dns_ips: Optional[Union[list[str], Ref]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UserAndGroupQuotas(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "id": "Id",
        "storage_capacity_quota_gi_b": "StorageCapacityQuotaGiB",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[int, Ref, GetAtt, Sub]] = None
    storage_capacity_quota_gi_b: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class WindowsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "self_managed_active_directory_configuration": "SelfManagedActiveDirectoryConfiguration",
        "audit_log_configuration": "AuditLogConfiguration",
        "weekly_maintenance_start_time": "WeeklyMaintenanceStartTime",
        "active_directory_id": "ActiveDirectoryId",
        "disk_iops_configuration": "DiskIopsConfiguration",
        "deployment_type": "DeploymentType",
        "aliases": "Aliases",
        "throughput_capacity": "ThroughputCapacity",
        "copy_tags_to_backups": "CopyTagsToBackups",
        "daily_automatic_backup_start_time": "DailyAutomaticBackupStartTime",
        "automatic_backup_retention_days": "AutomaticBackupRetentionDays",
        "preferred_subnet_id": "PreferredSubnetId",
    }

    self_managed_active_directory_configuration: Optional[SelfManagedActiveDirectoryConfiguration] = None
    audit_log_configuration: Optional[AuditLogConfiguration] = None
    weekly_maintenance_start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    active_directory_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    disk_iops_configuration: Optional[DiskIopsConfiguration] = None
    deployment_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aliases: Optional[Union[list[str], Ref]] = None
    throughput_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    copy_tags_to_backups: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    daily_automatic_backup_start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    automatic_backup_retention_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    preferred_subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

