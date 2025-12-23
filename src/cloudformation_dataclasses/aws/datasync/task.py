"""PropertyTypes for AWS::DataSync::Task."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Deleted(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "report_level": "ReportLevel",
    }

    report_level: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Destination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
    }

    s3: Optional[TaskReportConfigDestinationS3] = None


@dataclass
class FilterRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter_type": "FilterType",
        "value": "Value",
    }

    filter_type: Optional[Union[str, FilterType, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ManifestConfig(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "report_level": "ReportLevel",
    }

    report_level: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Source(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
    }

    s3: Optional[ManifestConfigSourceS3] = None


@dataclass
class TaskReportConfig(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "schedule_expression": "ScheduleExpression",
    }

    status: Optional[Union[str, ScheduleStatus, Ref, GetAtt, Sub]] = None
    schedule_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Transferred(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "report_level": "ReportLevel",
    }

    report_level: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Verified(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "report_level": "ReportLevel",
    }

    report_level: Optional[Union[str, Ref, GetAtt, Sub]] = None

