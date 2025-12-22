"""PropertyTypes for AWS::FSx::FileSystem."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ActiveDirectoryErrorType:
    """ActiveDirectoryErrorType enum values."""

    DOMAIN_NOT_FOUND = "DOMAIN_NOT_FOUND"
    INCOMPATIBLE_DOMAIN_MODE = "INCOMPATIBLE_DOMAIN_MODE"
    WRONG_VPC = "WRONG_VPC"
    INVALID_NETWORK_TYPE = "INVALID_NETWORK_TYPE"
    INVALID_DOMAIN_STAGE = "INVALID_DOMAIN_STAGE"


class AdministrativeActionType:
    """AdministrativeActionType enum values."""

    FILE_SYSTEM_UPDATE = "FILE_SYSTEM_UPDATE"
    STORAGE_OPTIMIZATION = "STORAGE_OPTIMIZATION"
    FILE_SYSTEM_ALIAS_ASSOCIATION = "FILE_SYSTEM_ALIAS_ASSOCIATION"
    FILE_SYSTEM_ALIAS_DISASSOCIATION = "FILE_SYSTEM_ALIAS_DISASSOCIATION"
    VOLUME_UPDATE = "VOLUME_UPDATE"
    SNAPSHOT_UPDATE = "SNAPSHOT_UPDATE"
    RELEASE_NFS_V3_LOCKS = "RELEASE_NFS_V3_LOCKS"
    VOLUME_RESTORE = "VOLUME_RESTORE"
    THROUGHPUT_OPTIMIZATION = "THROUGHPUT_OPTIMIZATION"
    IOPS_OPTIMIZATION = "IOPS_OPTIMIZATION"
    STORAGE_TYPE_OPTIMIZATION = "STORAGE_TYPE_OPTIMIZATION"
    MISCONFIGURED_STATE_RECOVERY = "MISCONFIGURED_STATE_RECOVERY"
    VOLUME_UPDATE_WITH_SNAPSHOT = "VOLUME_UPDATE_WITH_SNAPSHOT"
    VOLUME_INITIALIZE_WITH_SNAPSHOT = "VOLUME_INITIALIZE_WITH_SNAPSHOT"
    DOWNLOAD_DATA_FROM_BACKUP = "DOWNLOAD_DATA_FROM_BACKUP"


class AliasLifecycle:
    """AliasLifecycle enum values."""

    AVAILABLE = "AVAILABLE"
    CREATING = "CREATING"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_FAILED = "DELETE_FAILED"


class AutoImportPolicyType:
    """AutoImportPolicyType enum values."""

    NONE = "NONE"
    NEW = "NEW"
    NEW_CHANGED = "NEW_CHANGED"
    NEW_CHANGED_DELETED = "NEW_CHANGED_DELETED"


class AutocommitPeriodType:
    """AutocommitPeriodType enum values."""

    MINUTES = "MINUTES"
    HOURS = "HOURS"
    DAYS = "DAYS"
    MONTHS = "MONTHS"
    YEARS = "YEARS"
    NONE = "NONE"


class BackupLifecycle:
    """BackupLifecycle enum values."""

    AVAILABLE = "AVAILABLE"
    CREATING = "CREATING"
    TRANSFERRING = "TRANSFERRING"
    DELETED = "DELETED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    COPYING = "COPYING"


class BackupType:
    """BackupType enum values."""

    AUTOMATIC = "AUTOMATIC"
    USER_INITIATED = "USER_INITIATED"
    AWS_BACKUP = "AWS_BACKUP"


class DataCompressionType:
    """DataCompressionType enum values."""

    NONE = "NONE"
    LZ4 = "LZ4"


class DataRepositoryLifecycle:
    """DataRepositoryLifecycle enum values."""

    CREATING = "CREATING"
    AVAILABLE = "AVAILABLE"
    MISCONFIGURED = "MISCONFIGURED"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    FAILED = "FAILED"


class DataRepositoryTaskFilterName:
    """DataRepositoryTaskFilterName enum values."""

    FILE_SYSTEM_ID = "file-system-id"
    TASK_LIFECYCLE = "task-lifecycle"
    DATA_REPOSITORY_ASSOCIATION_ID = "data-repository-association-id"
    FILE_CACHE_ID = "file-cache-id"


class DataRepositoryTaskLifecycle:
    """DataRepositoryTaskLifecycle enum values."""

    PENDING = "PENDING"
    EXECUTING = "EXECUTING"
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"
    CANCELED = "CANCELED"
    CANCELING = "CANCELING"


class DataRepositoryTaskType:
    """DataRepositoryTaskType enum values."""

    EXPORT_TO_REPOSITORY = "EXPORT_TO_REPOSITORY"
    IMPORT_METADATA_FROM_REPOSITORY = "IMPORT_METADATA_FROM_REPOSITORY"
    RELEASE_DATA_FROM_FILESYSTEM = "RELEASE_DATA_FROM_FILESYSTEM"
    AUTO_RELEASE_DATA = "AUTO_RELEASE_DATA"


class DeleteFileSystemOpenZFSOption:
    """DeleteFileSystemOpenZFSOption enum values."""

    DELETE_CHILD_VOLUMES_AND_SNAPSHOTS = "DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"


class DeleteOpenZFSVolumeOption:
    """DeleteOpenZFSVolumeOption enum values."""

    DELETE_CHILD_VOLUMES_AND_SNAPSHOTS = "DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"


class DiskIopsConfigurationMode:
    """DiskIopsConfigurationMode enum values."""

    AUTOMATIC = "AUTOMATIC"
    USER_PROVISIONED = "USER_PROVISIONED"


class DriveCacheType:
    """DriveCacheType enum values."""

    NONE = "NONE"
    READ = "READ"


class EventType:
    """EventType enum values."""

    NEW = "NEW"
    CHANGED = "CHANGED"
    DELETED = "DELETED"


class FileCacheLifecycle:
    """FileCacheLifecycle enum values."""

    AVAILABLE = "AVAILABLE"
    CREATING = "CREATING"
    DELETING = "DELETING"
    UPDATING = "UPDATING"
    FAILED = "FAILED"


class FileCacheLustreDeploymentType:
    """FileCacheLustreDeploymentType enum values."""

    CACHE_1 = "CACHE_1"


class FileCacheType:
    """FileCacheType enum values."""

    LUSTRE = "LUSTRE"


class FileSystemLifecycle:
    """FileSystemLifecycle enum values."""

    AVAILABLE = "AVAILABLE"
    CREATING = "CREATING"
    FAILED = "FAILED"
    DELETING = "DELETING"
    MISCONFIGURED = "MISCONFIGURED"
    UPDATING = "UPDATING"
    MISCONFIGURED_UNAVAILABLE = "MISCONFIGURED_UNAVAILABLE"


class FileSystemMaintenanceOperation:
    """FileSystemMaintenanceOperation enum values."""

    PATCHING = "PATCHING"
    BACKING_UP = "BACKING_UP"


class FileSystemType:
    """FileSystemType enum values."""

    WINDOWS = "WINDOWS"
    LUSTRE = "LUSTRE"
    ONTAP = "ONTAP"
    OPENZFS = "OPENZFS"


class FilterName:
    """FilterName enum values."""

    FILE_SYSTEM_ID = "file-system-id"
    BACKUP_TYPE = "backup-type"
    FILE_SYSTEM_TYPE = "file-system-type"
    VOLUME_ID = "volume-id"
    DATA_REPOSITORY_TYPE = "data-repository-type"
    FILE_CACHE_ID = "file-cache-id"
    FILE_CACHE_TYPE = "file-cache-type"


class FlexCacheEndpointType:
    """FlexCacheEndpointType enum values."""

    NONE = "NONE"
    ORIGIN = "ORIGIN"
    CACHE = "CACHE"


class InputOntapVolumeType:
    """InputOntapVolumeType enum values."""

    RW = "RW"
    DP = "DP"


class LustreAccessAuditLogLevel:
    """LustreAccessAuditLogLevel enum values."""

    DISABLED = "DISABLED"
    WARN_ONLY = "WARN_ONLY"
    ERROR_ONLY = "ERROR_ONLY"
    WARN_ERROR = "WARN_ERROR"


class LustreDeploymentType:
    """LustreDeploymentType enum values."""

    SCRATCH_1 = "SCRATCH_1"
    SCRATCH_2 = "SCRATCH_2"
    PERSISTENT_1 = "PERSISTENT_1"
    PERSISTENT_2 = "PERSISTENT_2"


class LustreReadCacheSizingMode:
    """LustreReadCacheSizingMode enum values."""

    NO_CACHE = "NO_CACHE"
    USER_PROVISIONED = "USER_PROVISIONED"
    PROPORTIONAL_TO_THROUGHPUT_CAPACITY = "PROPORTIONAL_TO_THROUGHPUT_CAPACITY"


class MetadataConfigurationMode:
    """MetadataConfigurationMode enum values."""

    AUTOMATIC = "AUTOMATIC"
    USER_PROVISIONED = "USER_PROVISIONED"


class NetworkType:
    """NetworkType enum values."""

    IPV4 = "IPV4"
    DUAL = "DUAL"


class NfsVersion:
    """NfsVersion enum values."""

    NFS3 = "NFS3"


class OntapDeploymentType:
    """OntapDeploymentType enum values."""

    MULTI_AZ_1 = "MULTI_AZ_1"
    SINGLE_AZ_1 = "SINGLE_AZ_1"
    SINGLE_AZ_2 = "SINGLE_AZ_2"
    MULTI_AZ_2 = "MULTI_AZ_2"


class OntapFileSystemUserType:
    """OntapFileSystemUserType enum values."""

    UNIX = "UNIX"
    WINDOWS = "WINDOWS"


class OntapVolumeType:
    """OntapVolumeType enum values."""

    RW = "RW"
    DP = "DP"
    LS = "LS"


class OpenZFSCopyStrategy:
    """OpenZFSCopyStrategy enum values."""

    CLONE = "CLONE"
    FULL_COPY = "FULL_COPY"
    INCREMENTAL_COPY = "INCREMENTAL_COPY"


class OpenZFSDataCompressionType:
    """OpenZFSDataCompressionType enum values."""

    NONE = "NONE"
    ZSTD = "ZSTD"
    LZ4 = "LZ4"


class OpenZFSDeploymentType:
    """OpenZFSDeploymentType enum values."""

    SINGLE_AZ_1 = "SINGLE_AZ_1"
    SINGLE_AZ_2 = "SINGLE_AZ_2"
    SINGLE_AZ_HA_1 = "SINGLE_AZ_HA_1"
    SINGLE_AZ_HA_2 = "SINGLE_AZ_HA_2"
    MULTI_AZ_1 = "MULTI_AZ_1"


class OpenZFSFileSystemUserType:
    """OpenZFSFileSystemUserType enum values."""

    POSIX = "POSIX"


class OpenZFSQuotaType:
    """OpenZFSQuotaType enum values."""

    USER = "USER"
    GROUP = "GROUP"


class OpenZFSReadCacheSizingMode:
    """OpenZFSReadCacheSizingMode enum values."""

    NO_CACHE = "NO_CACHE"
    USER_PROVISIONED = "USER_PROVISIONED"
    PROPORTIONAL_TO_THROUGHPUT_CAPACITY = "PROPORTIONAL_TO_THROUGHPUT_CAPACITY"


class PrivilegedDelete:
    """PrivilegedDelete enum values."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    PERMANENTLY_DISABLED = "PERMANENTLY_DISABLED"


class ReportFormat:
    """ReportFormat enum values."""

    REPORT_CSV_20191124 = "REPORT_CSV_20191124"


class ReportScope:
    """ReportScope enum values."""

    FAILED_FILES_ONLY = "FAILED_FILES_ONLY"


class ResourceType:
    """ResourceType enum values."""

    FILE_SYSTEM = "FILE_SYSTEM"
    VOLUME = "VOLUME"


class RestoreOpenZFSVolumeOption:
    """RestoreOpenZFSVolumeOption enum values."""

    DELETE_INTERMEDIATE_SNAPSHOTS = "DELETE_INTERMEDIATE_SNAPSHOTS"
    DELETE_CLONED_VOLUMES = "DELETE_CLONED_VOLUMES"


class RetentionPeriodType:
    """RetentionPeriodType enum values."""

    SECONDS = "SECONDS"
    MINUTES = "MINUTES"
    HOURS = "HOURS"
    DAYS = "DAYS"
    MONTHS = "MONTHS"
    YEARS = "YEARS"
    INFINITE = "INFINITE"
    UNSPECIFIED = "UNSPECIFIED"


class S3AccessPointAttachmentLifecycle:
    """S3AccessPointAttachmentLifecycle enum values."""

    AVAILABLE = "AVAILABLE"
    CREATING = "CREATING"
    DELETING = "DELETING"
    UPDATING = "UPDATING"
    FAILED = "FAILED"
    MISCONFIGURED = "MISCONFIGURED"


class S3AccessPointAttachmentType:
    """S3AccessPointAttachmentType enum values."""

    OPENZFS = "OPENZFS"
    ONTAP = "ONTAP"


class S3AccessPointAttachmentsFilterName:
    """S3AccessPointAttachmentsFilterName enum values."""

    FILE_SYSTEM_ID = "file-system-id"
    VOLUME_ID = "volume-id"
    TYPE = "type"


class SecurityStyle:
    """SecurityStyle enum values."""

    UNIX = "UNIX"
    NTFS = "NTFS"
    MIXED = "MIXED"


class ServiceLimit:
    """ServiceLimit enum values."""

    FILE_SYSTEM_COUNT = "FILE_SYSTEM_COUNT"
    TOTAL_THROUGHPUT_CAPACITY = "TOTAL_THROUGHPUT_CAPACITY"
    TOTAL_STORAGE = "TOTAL_STORAGE"
    TOTAL_USER_INITIATED_BACKUPS = "TOTAL_USER_INITIATED_BACKUPS"
    TOTAL_USER_TAGS = "TOTAL_USER_TAGS"
    TOTAL_IN_PROGRESS_COPY_BACKUPS = "TOTAL_IN_PROGRESS_COPY_BACKUPS"
    STORAGE_VIRTUAL_MACHINES_PER_FILE_SYSTEM = "STORAGE_VIRTUAL_MACHINES_PER_FILE_SYSTEM"
    VOLUMES_PER_FILE_SYSTEM = "VOLUMES_PER_FILE_SYSTEM"
    TOTAL_SSD_IOPS = "TOTAL_SSD_IOPS"
    FILE_CACHE_COUNT = "FILE_CACHE_COUNT"


class SnaplockType:
    """SnaplockType enum values."""

    COMPLIANCE = "COMPLIANCE"
    ENTERPRISE = "ENTERPRISE"


class SnapshotFilterName:
    """SnapshotFilterName enum values."""

    FILE_SYSTEM_ID = "file-system-id"
    VOLUME_ID = "volume-id"


class SnapshotLifecycle:
    """SnapshotLifecycle enum values."""

    PENDING = "PENDING"
    CREATING = "CREATING"
    DELETING = "DELETING"
    AVAILABLE = "AVAILABLE"


class Status:
    """Status enum values."""

    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    UPDATED_OPTIMIZING = "UPDATED_OPTIMIZING"
    OPTIMIZING = "OPTIMIZING"
    PAUSED = "PAUSED"
    CANCELLED = "CANCELLED"


class StorageType:
    """StorageType enum values."""

    SSD = "SSD"
    HDD = "HDD"
    INTELLIGENT_TIERING = "INTELLIGENT_TIERING"


class StorageVirtualMachineFilterName:
    """StorageVirtualMachineFilterName enum values."""

    FILE_SYSTEM_ID = "file-system-id"


class StorageVirtualMachineLifecycle:
    """StorageVirtualMachineLifecycle enum values."""

    CREATED = "CREATED"
    CREATING = "CREATING"
    DELETING = "DELETING"
    FAILED = "FAILED"
    MISCONFIGURED = "MISCONFIGURED"
    PENDING = "PENDING"


class StorageVirtualMachineRootVolumeSecurityStyle:
    """StorageVirtualMachineRootVolumeSecurityStyle enum values."""

    UNIX = "UNIX"
    NTFS = "NTFS"
    MIXED = "MIXED"


class StorageVirtualMachineSubtype:
    """StorageVirtualMachineSubtype enum values."""

    DEFAULT = "DEFAULT"
    DP_DESTINATION = "DP_DESTINATION"
    SYNC_DESTINATION = "SYNC_DESTINATION"
    SYNC_SOURCE = "SYNC_SOURCE"


class TieringPolicyName:
    """TieringPolicyName enum values."""

    SNAPSHOT_ONLY = "SNAPSHOT_ONLY"
    AUTO = "AUTO"
    ALL = "ALL"
    NONE = "NONE"


class Unit:
    """Unit enum values."""

    DAYS = "DAYS"


class UpdateOpenZFSVolumeOption:
    """UpdateOpenZFSVolumeOption enum values."""

    DELETE_INTERMEDIATE_SNAPSHOTS = "DELETE_INTERMEDIATE_SNAPSHOTS"
    DELETE_CLONED_VOLUMES = "DELETE_CLONED_VOLUMES"
    DELETE_INTERMEDIATE_DATA = "DELETE_INTERMEDIATE_DATA"


class VolumeFilterName:
    """VolumeFilterName enum values."""

    FILE_SYSTEM_ID = "file-system-id"
    STORAGE_VIRTUAL_MACHINE_ID = "storage-virtual-machine-id"


class VolumeLifecycle:
    """VolumeLifecycle enum values."""

    CREATING = "CREATING"
    CREATED = "CREATED"
    DELETING = "DELETING"
    FAILED = "FAILED"
    MISCONFIGURED = "MISCONFIGURED"
    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"


class VolumeStyle:
    """VolumeStyle enum values."""

    FLEXVOL = "FLEXVOL"
    FLEXGROUP = "FLEXGROUP"


class VolumeType:
    """VolumeType enum values."""

    ONTAP = "ONTAP"
    OPENZFS = "OPENZFS"


class WindowsAccessAuditLogLevel:
    """WindowsAccessAuditLogLevel enum values."""

    DISABLED = "DISABLED"
    SUCCESS_ONLY = "SUCCESS_ONLY"
    FAILURE_ONLY = "FAILURE_ONLY"
    SUCCESS_AND_FAILURE = "SUCCESS_AND_FAILURE"


class WindowsDeploymentType:
    """WindowsDeploymentType enum values."""

    MULTI_AZ_1 = "MULTI_AZ_1"
    SINGLE_AZ_1 = "SINGLE_AZ_1"
    SINGLE_AZ_2 = "SINGLE_AZ_2"


@dataclass
class AuditLogConfiguration(PropertyType):
    FILE_ACCESS_AUDIT_LOG_LEVEL = "FileAccessAuditLogLevel"
    FILE_SHARE_ACCESS_AUDIT_LOG_LEVEL = "FileShareAccessAuditLogLevel"
    AUDIT_LOG_DESTINATION = "AuditLogDestination"

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
    OPTIONS = "Options"
    CLIENTS = "Clients"

    _property_mappings: ClassVar[dict[str, str]] = {
        "options": "Options",
        "clients": "Clients",
    }

    options: Optional[Union[list[str], Ref]] = None
    clients: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataReadCacheConfiguration(PropertyType):
    SIZING_MODE = "SizingMode"
    SIZE_GI_B = "SizeGiB"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sizing_mode": "SizingMode",
        "size_gi_b": "SizeGiB",
    }

    sizing_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    size_gi_b: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DiskIopsConfiguration(PropertyType):
    MODE = "Mode"
    IOPS = "Iops"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
        "iops": "Iops",
    }

    mode: Optional[Union[str, DiskIopsConfigurationMode, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class LustreConfiguration(PropertyType):
    DRIVE_CACHE_TYPE = "DriveCacheType"
    AUTO_IMPORT_POLICY = "AutoImportPolicy"
    EFA_ENABLED = "EfaEnabled"
    IMPORTED_FILE_CHUNK_SIZE = "ImportedFileChunkSize"
    DEPLOYMENT_TYPE = "DeploymentType"
    THROUGHPUT_CAPACITY = "ThroughputCapacity"
    DATA_COMPRESSION_TYPE = "DataCompressionType"
    DATA_READ_CACHE_CONFIGURATION = "DataReadCacheConfiguration"
    IMPORT_PATH = "ImportPath"
    WEEKLY_MAINTENANCE_START_TIME = "WeeklyMaintenanceStartTime"
    METADATA_CONFIGURATION = "MetadataConfiguration"
    DAILY_AUTOMATIC_BACKUP_START_TIME = "DailyAutomaticBackupStartTime"
    COPY_TAGS_TO_BACKUPS = "CopyTagsToBackups"
    EXPORT_PATH = "ExportPath"
    PER_UNIT_STORAGE_THROUGHPUT = "PerUnitStorageThroughput"
    AUTOMATIC_BACKUP_RETENTION_DAYS = "AutomaticBackupRetentionDays"

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
    MODE = "Mode"
    IOPS = "Iops"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
        "iops": "Iops",
    }

    mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NfsExports(PropertyType):
    CLIENT_CONFIGURATIONS = "ClientConfigurations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "client_configurations": "ClientConfigurations",
    }

    client_configurations: Optional[list[ClientConfigurations]] = None


@dataclass
class OntapConfiguration(PropertyType):
    HA_PAIRS = "HAPairs"
    FSX_ADMIN_PASSWORD = "FsxAdminPassword"
    THROUGHPUT_CAPACITY_PER_HA_PAIR = "ThroughputCapacityPerHAPair"
    DEPLOYMENT_TYPE = "DeploymentType"
    THROUGHPUT_CAPACITY = "ThroughputCapacity"
    ENDPOINT_IP_ADDRESS_RANGE = "EndpointIpAddressRange"
    ROUTE_TABLE_IDS = "RouteTableIds"
    WEEKLY_MAINTENANCE_START_TIME = "WeeklyMaintenanceStartTime"
    DISK_IOPS_CONFIGURATION = "DiskIopsConfiguration"
    DAILY_AUTOMATIC_BACKUP_START_TIME = "DailyAutomaticBackupStartTime"
    AUTOMATIC_BACKUP_RETENTION_DAYS = "AutomaticBackupRetentionDays"
    ENDPOINT_IPV6_ADDRESS_RANGE = "EndpointIpv6AddressRange"
    PREFERRED_SUBNET_ID = "PreferredSubnetId"

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
    OPTIONS = "Options"
    COPY_TAGS_TO_VOLUMES = "CopyTagsToVolumes"
    DEPLOYMENT_TYPE = "DeploymentType"
    THROUGHPUT_CAPACITY = "ThroughputCapacity"
    ROOT_VOLUME_CONFIGURATION = "RootVolumeConfiguration"
    ENDPOINT_IP_ADDRESS_RANGE = "EndpointIpAddressRange"
    READ_CACHE_CONFIGURATION = "ReadCacheConfiguration"
    ROUTE_TABLE_IDS = "RouteTableIds"
    WEEKLY_MAINTENANCE_START_TIME = "WeeklyMaintenanceStartTime"
    DISK_IOPS_CONFIGURATION = "DiskIopsConfiguration"
    DAILY_AUTOMATIC_BACKUP_START_TIME = "DailyAutomaticBackupStartTime"
    COPY_TAGS_TO_BACKUPS = "CopyTagsToBackups"
    AUTOMATIC_BACKUP_RETENTION_DAYS = "AutomaticBackupRetentionDays"
    ENDPOINT_IPV6_ADDRESS_RANGE = "EndpointIpv6AddressRange"
    PREFERRED_SUBNET_ID = "PreferredSubnetId"

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
    SIZING_MODE = "SizingMode"
    SIZE_GI_B = "SizeGiB"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sizing_mode": "SizingMode",
        "size_gi_b": "SizeGiB",
    }

    sizing_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    size_gi_b: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RootVolumeConfiguration(PropertyType):
    READ_ONLY = "ReadOnly"
    DATA_COMPRESSION_TYPE = "DataCompressionType"
    NFS_EXPORTS = "NfsExports"
    COPY_TAGS_TO_SNAPSHOTS = "CopyTagsToSnapshots"
    RECORD_SIZE_KI_B = "RecordSizeKiB"
    USER_AND_GROUP_QUOTAS = "UserAndGroupQuotas"

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
    FILE_SYSTEM_ADMINISTRATORS_GROUP = "FileSystemAdministratorsGroup"
    USER_NAME = "UserName"
    DOMAIN_NAME = "DomainName"
    ORGANIZATIONAL_UNIT_DISTINGUISHED_NAME = "OrganizationalUnitDistinguishedName"
    DOMAIN_JOIN_SERVICE_ACCOUNT_SECRET = "DomainJoinServiceAccountSecret"
    DNS_IPS = "DnsIps"
    PASSWORD = "Password"

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


@dataclass
class WindowsConfiguration(PropertyType):
    SELF_MANAGED_ACTIVE_DIRECTORY_CONFIGURATION = "SelfManagedActiveDirectoryConfiguration"
    AUDIT_LOG_CONFIGURATION = "AuditLogConfiguration"
    WEEKLY_MAINTENANCE_START_TIME = "WeeklyMaintenanceStartTime"
    ACTIVE_DIRECTORY_ID = "ActiveDirectoryId"
    DISK_IOPS_CONFIGURATION = "DiskIopsConfiguration"
    DEPLOYMENT_TYPE = "DeploymentType"
    ALIASES = "Aliases"
    THROUGHPUT_CAPACITY = "ThroughputCapacity"
    COPY_TAGS_TO_BACKUPS = "CopyTagsToBackups"
    DAILY_AUTOMATIC_BACKUP_START_TIME = "DailyAutomaticBackupStartTime"
    AUTOMATIC_BACKUP_RETENTION_DAYS = "AutomaticBackupRetentionDays"
    PREFERRED_SUBNET_ID = "PreferredSubnetId"

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

