"""PropertyTypes for AWS::Glue::SecurityConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CloudWatchEncryption(PropertyType):
    KMS_KEY_ARN = "KmsKeyArn"
    CLOUD_WATCH_ENCRYPTION_MODE = "CloudWatchEncryptionMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
        "cloud_watch_encryption_mode": "CloudWatchEncryptionMode",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cloud_watch_encryption_mode: Optional[Union[str, CloudWatchEncryptionMode, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionConfiguration(PropertyType):
    S3_ENCRYPTIONS = "S3Encryptions"
    CLOUD_WATCH_ENCRYPTION = "CloudWatchEncryption"
    JOB_BOOKMARKS_ENCRYPTION = "JobBookmarksEncryption"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_encryptions": "S3Encryptions",
        "cloud_watch_encryption": "CloudWatchEncryption",
        "job_bookmarks_encryption": "JobBookmarksEncryption",
    }

    s3_encryptions: Optional[S3Encryptions] = None
    cloud_watch_encryption: Optional[CloudWatchEncryption] = None
    job_bookmarks_encryption: Optional[JobBookmarksEncryption] = None


@dataclass
class JobBookmarksEncryption(PropertyType):
    KMS_KEY_ARN = "KmsKeyArn"
    JOB_BOOKMARKS_ENCRYPTION_MODE = "JobBookmarksEncryptionMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
        "job_bookmarks_encryption_mode": "JobBookmarksEncryptionMode",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    job_bookmarks_encryption_mode: Optional[Union[str, JobBookmarksEncryptionMode, Ref, GetAtt, Sub]] = None


@dataclass
class S3Encryption(PropertyType):
    KMS_KEY_ARN = "KmsKeyArn"
    S3_ENCRYPTION_MODE = "S3EncryptionMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
        "s3_encryption_mode": "S3EncryptionMode",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_encryption_mode: Optional[Union[str, S3EncryptionMode, Ref, GetAtt, Sub]] = None


@dataclass
class S3Encryptions(PropertyType):
    pass

