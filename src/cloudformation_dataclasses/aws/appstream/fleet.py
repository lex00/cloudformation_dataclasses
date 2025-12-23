"""PropertyTypes for AWS::AppStream::Fleet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ComputeCapacity(PropertyType):
    DESIRED_INSTANCES = "DesiredInstances"
    DESIRED_SESSIONS = "DesiredSessions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "desired_instances": "DesiredInstances",
        "desired_sessions": "DesiredSessions",
    }

    desired_instances: Optional[Union[int, Ref, GetAtt, Sub]] = None
    desired_sessions: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DomainJoinInfo(PropertyType):
    ORGANIZATIONAL_UNIT_DISTINGUISHED_NAME = "OrganizationalUnitDistinguishedName"
    DIRECTORY_NAME = "DirectoryName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "organizational_unit_distinguished_name": "OrganizationalUnitDistinguishedName",
        "directory_name": "DirectoryName",
    }

    organizational_unit_distinguished_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    directory_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Location(PropertyType):
    S3_BUCKET = "S3Bucket"
    S3_KEY = "S3Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_bucket": "S3Bucket",
        "s3_key": "S3Key",
    }

    s3_bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConfig(PropertyType):
    SUBNET_IDS = "SubnetIds"
    SECURITY_GROUP_IDS = "SecurityGroupIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subnet_ids": "SubnetIds",
        "security_group_ids": "SecurityGroupIds",
    }

    subnet_ids: Optional[Union[list[str], Ref]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None

