"""PropertyTypes for AWS::FSx::StorageVirtualMachine."""

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
class ActiveDirectoryConfiguration(PropertyType):
    SELF_MANAGED_ACTIVE_DIRECTORY_CONFIGURATION = "SelfManagedActiveDirectoryConfiguration"
    NET_BIOS_NAME = "NetBiosName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "self_managed_active_directory_configuration": "SelfManagedActiveDirectoryConfiguration",
        "net_bios_name": "NetBiosName",
    }

    self_managed_active_directory_configuration: Optional[SelfManagedActiveDirectoryConfiguration] = None
    net_bios_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


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

