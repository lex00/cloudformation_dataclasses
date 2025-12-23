"""PropertyTypes for AWS::Deadline::Queue."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class JobAttachmentSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "root_prefix": "RootPrefix",
        "s3_bucket_name": "S3BucketName",
    }

    root_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class JobRunAsUser(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "run_as": "RunAs",
        "posix": "Posix",
        "windows": "Windows",
    }

    run_as: Optional[Union[str, Ref, GetAtt, Sub]] = None
    posix: Optional[PosixUser] = None
    windows: Optional[WindowsUser] = None


@dataclass
class PosixUser(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "group": "Group",
        "user": "User",
    }

    group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    user: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WindowsUser(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "user": "User",
        "password_arn": "PasswordArn",
    }

    user: Optional[Union[str, Ref, GetAtt, Sub]] = None
    password_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

