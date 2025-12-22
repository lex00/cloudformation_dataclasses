"""PropertyTypes for AWS::DataSync::Task."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AgentStatus:
    """AgentStatus enum values."""

    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"


class Atime:
    """Atime enum values."""

    NONE = "NONE"
    BEST_EFFORT = "BEST_EFFORT"


class AzureAccessTier:
    """AzureAccessTier enum values."""

    HOT = "HOT"
    COOL = "COOL"
    ARCHIVE = "ARCHIVE"


class AzureBlobAuthenticationType:
    """AzureBlobAuthenticationType enum values."""

    SAS = "SAS"
    NONE = "NONE"


class AzureBlobType:
    """AzureBlobType enum values."""

    BLOCK = "BLOCK"


class EfsInTransitEncryption:
    """EfsInTransitEncryption enum values."""

    NONE = "NONE"
    TLS1_2 = "TLS1_2"


class EndpointType:
    """EndpointType enum values."""

    PUBLIC = "PUBLIC"
    PRIVATE_LINK = "PRIVATE_LINK"
    FIPS = "FIPS"
    FIPS_PRIVATE_LINK = "FIPS_PRIVATE_LINK"


class FilterType:
    """FilterType enum values."""

    SIMPLE_PATTERN = "SIMPLE_PATTERN"


class Gid:
    """Gid enum values."""

    NONE = "NONE"
    INT_VALUE = "INT_VALUE"
    NAME = "NAME"
    BOTH = "BOTH"


class HdfsAuthenticationType:
    """HdfsAuthenticationType enum values."""

    SIMPLE = "SIMPLE"
    KERBEROS = "KERBEROS"


class HdfsDataTransferProtection:
    """HdfsDataTransferProtection enum values."""

    DISABLED = "DISABLED"
    AUTHENTICATION = "AUTHENTICATION"
    INTEGRITY = "INTEGRITY"
    PRIVACY = "PRIVACY"


class HdfsRpcProtection:
    """HdfsRpcProtection enum values."""

    DISABLED = "DISABLED"
    AUTHENTICATION = "AUTHENTICATION"
    INTEGRITY = "INTEGRITY"
    PRIVACY = "PRIVACY"


class LocationFilterName:
    """LocationFilterName enum values."""

    LOCATIONURI = "LocationUri"
    LOCATIONTYPE = "LocationType"
    CREATIONTIME = "CreationTime"


class LogLevel:
    """LogLevel enum values."""

    OFF = "OFF"
    BASIC = "BASIC"
    TRANSFER = "TRANSFER"


class ManifestAction:
    """ManifestAction enum values."""

    TRANSFER = "TRANSFER"


class ManifestFormat:
    """ManifestFormat enum values."""

    CSV = "CSV"


class Mtime:
    """Mtime enum values."""

    NONE = "NONE"
    PRESERVE = "PRESERVE"


class NfsVersion:
    """NfsVersion enum values."""

    AUTOMATIC = "AUTOMATIC"
    NFS3 = "NFS3"
    NFS4_0 = "NFS4_0"
    NFS4_1 = "NFS4_1"


class ObjectStorageServerProtocol:
    """ObjectStorageServerProtocol enum values."""

    HTTPS = "HTTPS"
    HTTP = "HTTP"


class ObjectTags:
    """ObjectTags enum values."""

    PRESERVE = "PRESERVE"
    NONE = "NONE"


class ObjectVersionIds:
    """ObjectVersionIds enum values."""

    INCLUDE = "INCLUDE"
    NONE = "NONE"


class Operator:
    """Operator enum values."""

    EQUALS = "Equals"
    NOTEQUALS = "NotEquals"
    IN = "In"
    LESSTHANOREQUAL = "LessThanOrEqual"
    LESSTHAN = "LessThan"
    GREATERTHANOREQUAL = "GreaterThanOrEqual"
    GREATERTHAN = "GreaterThan"
    CONTAINS = "Contains"
    NOTCONTAINS = "NotContains"
    BEGINSWITH = "BeginsWith"


class OverwriteMode:
    """OverwriteMode enum values."""

    ALWAYS = "ALWAYS"
    NEVER = "NEVER"


class PhaseStatus:
    """PhaseStatus enum values."""

    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"


class PosixPermissions:
    """PosixPermissions enum values."""

    NONE = "NONE"
    PRESERVE = "PRESERVE"


class PreserveDeletedFiles:
    """PreserveDeletedFiles enum values."""

    PRESERVE = "PRESERVE"
    REMOVE = "REMOVE"


class PreserveDevices:
    """PreserveDevices enum values."""

    NONE = "NONE"
    PRESERVE = "PRESERVE"


class ReportLevel:
    """ReportLevel enum values."""

    ERRORS_ONLY = "ERRORS_ONLY"
    SUCCESSES_AND_ERRORS = "SUCCESSES_AND_ERRORS"


class ReportOutputType:
    """ReportOutputType enum values."""

    SUMMARY_ONLY = "SUMMARY_ONLY"
    STANDARD = "STANDARD"


class S3StorageClass:
    """S3StorageClass enum values."""

    STANDARD = "STANDARD"
    STANDARD_IA = "STANDARD_IA"
    ONEZONE_IA = "ONEZONE_IA"
    INTELLIGENT_TIERING = "INTELLIGENT_TIERING"
    GLACIER = "GLACIER"
    DEEP_ARCHIVE = "DEEP_ARCHIVE"
    OUTPOSTS = "OUTPOSTS"
    GLACIER_INSTANT_RETRIEVAL = "GLACIER_INSTANT_RETRIEVAL"


class ScheduleDisabledBy:
    """ScheduleDisabledBy enum values."""

    USER = "USER"
    SERVICE = "SERVICE"


class ScheduleStatus:
    """ScheduleStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class SmbAuthenticationType:
    """SmbAuthenticationType enum values."""

    NTLM = "NTLM"
    KERBEROS = "KERBEROS"


class SmbSecurityDescriptorCopyFlags:
    """SmbSecurityDescriptorCopyFlags enum values."""

    NONE = "NONE"
    OWNER_DACL = "OWNER_DACL"
    OWNER_DACL_SACL = "OWNER_DACL_SACL"


class SmbVersion:
    """SmbVersion enum values."""

    AUTOMATIC = "AUTOMATIC"
    SMB2 = "SMB2"
    SMB3 = "SMB3"
    SMB1 = "SMB1"
    SMB2_0 = "SMB2_0"


class TaskExecutionStatus:
    """TaskExecutionStatus enum values."""

    QUEUED = "QUEUED"
    CANCELLING = "CANCELLING"
    LAUNCHING = "LAUNCHING"
    PREPARING = "PREPARING"
    TRANSFERRING = "TRANSFERRING"
    VERIFYING = "VERIFYING"
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"


class TaskFilterName:
    """TaskFilterName enum values."""

    LOCATIONID = "LocationId"
    CREATIONTIME = "CreationTime"


class TaskMode:
    """TaskMode enum values."""

    BASIC = "BASIC"
    ENHANCED = "ENHANCED"


class TaskQueueing:
    """TaskQueueing enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class TaskStatus:
    """TaskStatus enum values."""

    AVAILABLE = "AVAILABLE"
    CREATING = "CREATING"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    UNAVAILABLE = "UNAVAILABLE"


class TransferMode:
    """TransferMode enum values."""

    CHANGED = "CHANGED"
    ALL = "ALL"


class Uid:
    """Uid enum values."""

    NONE = "NONE"
    INT_VALUE = "INT_VALUE"
    NAME = "NAME"
    BOTH = "BOTH"


class VerifyMode:
    """VerifyMode enum values."""

    POINT_IN_TIME_CONSISTENT = "POINT_IN_TIME_CONSISTENT"
    ONLY_FILES_TRANSFERRED = "ONLY_FILES_TRANSFERRED"
    NONE = "NONE"


@dataclass
class Deleted(PropertyType):
    REPORT_LEVEL = "ReportLevel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "report_level": "ReportLevel",
    }

    report_level: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Destination(PropertyType):
    S3 = "S3"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
    }

    s3: Optional[TaskReportConfigDestinationS3] = None


@dataclass
class FilterRule(PropertyType):
    FILTER_TYPE = "FilterType"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_type": "FilterType",
        "value": "Value",
    }

    filter_type: Optional[Union[str, FilterType, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ManifestConfig(PropertyType):
    ACTION = "Action"
    FORMAT = "Format"
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "format": "Format",
        "source": "Source",
    }

    action: Optional[Union[str, ManifestAction, Ref, GetAtt, Sub]] = None
    format: Optional[Union[str, ManifestFormat, Ref, GetAtt, Sub]] = None
    source: Optional[Source] = None


@dataclass
class ManifestConfigSourceS3(PropertyType):
    S3_BUCKET_ARN = "S3BucketArn"
    BUCKET_ACCESS_ROLE_ARN = "BucketAccessRoleArn"
    MANIFEST_OBJECT_VERSION_ID = "ManifestObjectVersionId"
    MANIFEST_OBJECT_PATH = "ManifestObjectPath"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_bucket_arn": "S3BucketArn",
        "bucket_access_role_arn": "BucketAccessRoleArn",
        "manifest_object_version_id": "ManifestObjectVersionId",
        "manifest_object_path": "ManifestObjectPath",
    }

    s3_bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    manifest_object_version_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    manifest_object_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Options(PropertyType):
    VERIFY_MODE = "VerifyMode"
    GID = "Gid"
    ATIME = "Atime"
    OVERWRITE_MODE = "OverwriteMode"
    PRESERVE_DEVICES = "PreserveDevices"
    MTIME = "Mtime"
    TASK_QUEUEING = "TaskQueueing"
    TRANSFER_MODE = "TransferMode"
    LOG_LEVEL = "LogLevel"
    OBJECT_TAGS = "ObjectTags"
    UID = "Uid"
    BYTES_PER_SECOND = "BytesPerSecond"
    POSIX_PERMISSIONS = "PosixPermissions"
    PRESERVE_DELETED_FILES = "PreserveDeletedFiles"
    SECURITY_DESCRIPTOR_COPY_FLAGS = "SecurityDescriptorCopyFlags"

    _property_mappings: ClassVar[dict[str, str]] = {
        "verify_mode": "VerifyMode",
        "gid": "Gid",
        "atime": "Atime",
        "overwrite_mode": "OverwriteMode",
        "preserve_devices": "PreserveDevices",
        "mtime": "Mtime",
        "task_queueing": "TaskQueueing",
        "transfer_mode": "TransferMode",
        "log_level": "LogLevel",
        "object_tags": "ObjectTags",
        "uid": "Uid",
        "bytes_per_second": "BytesPerSecond",
        "posix_permissions": "PosixPermissions",
        "preserve_deleted_files": "PreserveDeletedFiles",
        "security_descriptor_copy_flags": "SecurityDescriptorCopyFlags",
    }

    verify_mode: Optional[Union[str, VerifyMode, Ref, GetAtt, Sub]] = None
    gid: Optional[Union[str, Gid, Ref, GetAtt, Sub]] = None
    atime: Optional[Union[str, Atime, Ref, GetAtt, Sub]] = None
    overwrite_mode: Optional[Union[str, OverwriteMode, Ref, GetAtt, Sub]] = None
    preserve_devices: Optional[Union[str, PreserveDevices, Ref, GetAtt, Sub]] = None
    mtime: Optional[Union[str, Mtime, Ref, GetAtt, Sub]] = None
    task_queueing: Optional[Union[str, TaskQueueing, Ref, GetAtt, Sub]] = None
    transfer_mode: Optional[Union[str, TransferMode, Ref, GetAtt, Sub]] = None
    log_level: Optional[Union[str, LogLevel, Ref, GetAtt, Sub]] = None
    object_tags: Optional[Union[str, ObjectTags, Ref, GetAtt, Sub]] = None
    uid: Optional[Union[str, Uid, Ref, GetAtt, Sub]] = None
    bytes_per_second: Optional[Union[int, Ref, GetAtt, Sub]] = None
    posix_permissions: Optional[Union[str, PosixPermissions, Ref, GetAtt, Sub]] = None
    preserve_deleted_files: Optional[Union[str, PreserveDeletedFiles, Ref, GetAtt, Sub]] = None
    security_descriptor_copy_flags: Optional[Union[str, SmbSecurityDescriptorCopyFlags, Ref, GetAtt, Sub]] = None


@dataclass
class Overrides(PropertyType):
    VERIFIED = "Verified"
    SKIPPED = "Skipped"
    TRANSFERRED = "Transferred"
    DELETED = "Deleted"

    _property_mappings: ClassVar[dict[str, str]] = {
        "verified": "Verified",
        "skipped": "Skipped",
        "transferred": "Transferred",
        "deleted": "Deleted",
    }

    verified: Optional[Verified] = None
    skipped: Optional[Skipped] = None
    transferred: Optional[Transferred] = None
    deleted: Optional[Deleted] = None


@dataclass
class Skipped(PropertyType):
    REPORT_LEVEL = "ReportLevel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "report_level": "ReportLevel",
    }

    report_level: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Source(PropertyType):
    S3 = "S3"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
    }

    s3: Optional[ManifestConfigSourceS3] = None


@dataclass
class TaskReportConfig(PropertyType):
    DESTINATION = "Destination"
    REPORT_LEVEL = "ReportLevel"
    OBJECT_VERSION_IDS = "ObjectVersionIds"
    OVERRIDES = "Overrides"
    OUTPUT_TYPE = "OutputType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "report_level": "ReportLevel",
        "object_version_ids": "ObjectVersionIds",
        "overrides": "Overrides",
        "output_type": "OutputType",
    }

    destination: Optional[Destination] = None
    report_level: Optional[Union[str, ReportLevel, Ref, GetAtt, Sub]] = None
    object_version_ids: Optional[Union[str, ObjectVersionIds, Ref, GetAtt, Sub]] = None
    overrides: Optional[Overrides] = None
    output_type: Optional[Union[str, ReportOutputType, Ref, GetAtt, Sub]] = None


@dataclass
class TaskReportConfigDestinationS3(PropertyType):
    SUBDIRECTORY = "Subdirectory"
    S3_BUCKET_ARN = "S3BucketArn"
    BUCKET_ACCESS_ROLE_ARN = "BucketAccessRoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subdirectory": "Subdirectory",
        "s3_bucket_arn": "S3BucketArn",
        "bucket_access_role_arn": "BucketAccessRoleArn",
    }

    subdirectory: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TaskSchedule(PropertyType):
    STATUS = "Status"
    SCHEDULE_EXPRESSION = "ScheduleExpression"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "schedule_expression": "ScheduleExpression",
    }

    status: Optional[Union[str, ScheduleStatus, Ref, GetAtt, Sub]] = None
    schedule_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Transferred(PropertyType):
    REPORT_LEVEL = "ReportLevel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "report_level": "ReportLevel",
    }

    report_level: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Verified(PropertyType):
    REPORT_LEVEL = "ReportLevel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "report_level": "ReportLevel",
    }

    report_level: Optional[Union[str, Ref, GetAtt, Sub]] = None

