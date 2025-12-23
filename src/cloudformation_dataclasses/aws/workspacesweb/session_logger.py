"""PropertyTypes for AWS::WorkSpacesWeb::SessionLogger."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EventFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "all": "All",
        "include": "Include",
    }

    all: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    include: Optional[Union[list[str], Ref]] = None


@dataclass
class LogConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
    }

    s3: Optional[S3LogConfiguration] = None


@dataclass
class S3LogConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "folder_structure": "FolderStructure",
        "log_file_format": "LogFileFormat",
        "bucket_owner": "BucketOwner",
        "key_prefix": "KeyPrefix",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    folder_structure: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_file_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_owner: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None

