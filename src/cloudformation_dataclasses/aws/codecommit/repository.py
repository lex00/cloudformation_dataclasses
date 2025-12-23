"""PropertyTypes for AWS::CodeCommit::Repository."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Code(PropertyType):
    S3 = "S3"
    BRANCH_NAME = "BranchName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "branch_name": "BranchName",
    }

    s3: Optional[S3] = None
    branch_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RepositoryTrigger(PropertyType):
    EVENTS = "Events"
    BRANCHES = "Branches"
    CUSTOM_DATA = "CustomData"
    DESTINATION_ARN = "DestinationArn"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "events": "Events",
        "branches": "Branches",
        "custom_data": "CustomData",
        "destination_arn": "DestinationArn",
        "name": "Name",
    }

    events: Optional[Union[list[str], Ref]] = None
    branches: Optional[Union[list[str], Ref]] = None
    custom_data: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3(PropertyType):
    OBJECT_VERSION = "ObjectVersion"
    BUCKET = "Bucket"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "object_version": "ObjectVersion",
        "bucket": "Bucket",
        "key": "Key",
    }

    object_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

