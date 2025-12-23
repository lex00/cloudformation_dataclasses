"""PropertyTypes for AWS::Transfer::Workflow."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CopyStepDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination_file_location": "DestinationFileLocation",
        "source_file_location": "SourceFileLocation",
        "name": "Name",
        "overwrite_existing": "OverwriteExisting",
    }

    destination_file_location: Optional[S3FileLocation] = None
    source_file_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    overwrite_existing: Optional[Union[str, OverwriteExisting, Ref, GetAtt, Sub]] = None


@dataclass
class CustomStepDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "timeout_seconds": "TimeoutSeconds",
        "target": "Target",
        "source_file_location": "SourceFileLocation",
        "name": "Name",
    }

    timeout_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_file_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DecryptStepDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination_file_location": "DestinationFileLocation",
        "type_": "Type",
        "source_file_location": "SourceFileLocation",
        "name": "Name",
        "overwrite_existing": "OverwriteExisting",
    }

    destination_file_location: Optional[InputFileLocation] = None
    type_: Optional[Union[str, EncryptionType, Ref, GetAtt, Sub]] = None
    source_file_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    overwrite_existing: Optional[Union[str, OverwriteExisting, Ref, GetAtt, Sub]] = None


@dataclass
class DeleteStepDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_file_location": "SourceFileLocation",
        "name": "Name",
    }

    source_file_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EfsInputFileLocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "file_system_id": "FileSystemId",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_system_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputFileLocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "efs_file_location": "EfsFileLocation",
        "s3_file_location": "S3FileLocation",
    }

    efs_file_location: Optional[EfsInputFileLocation] = None
    s3_file_location: Optional[S3InputFileLocation] = None


@dataclass
class S3FileLocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_file_location": "S3FileLocation",
    }

    s3_file_location: Optional[S3InputFileLocation] = None


@dataclass
class S3InputFileLocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "key": "Key",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Tag(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TagStepDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_file_location": "SourceFileLocation",
        "tags": "Tags",
        "name": "Name",
    }

    source_file_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[S3Tag]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WorkflowStep(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_step_details": "CustomStepDetails",
        "copy_step_details": "CopyStepDetails",
        "decrypt_step_details": "DecryptStepDetails",
        "type_": "Type",
        "tag_step_details": "TagStepDetails",
        "delete_step_details": "DeleteStepDetails",
    }

    custom_step_details: Optional[CustomStepDetails] = None
    copy_step_details: Optional[CopyStepDetails] = None
    decrypt_step_details: Optional[DecryptStepDetails] = None
    type_: Optional[Union[str, WorkflowStepType, Ref, GetAtt, Sub]] = None
    tag_step_details: Optional[TagStepDetails] = None
    delete_step_details: Optional[DeleteStepDetails] = None

