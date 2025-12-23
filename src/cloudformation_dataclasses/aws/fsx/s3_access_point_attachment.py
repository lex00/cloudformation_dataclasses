"""PropertyTypes for AWS::FSx::S3AccessPointAttachment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FileSystemGID(PropertyType):
    GID = "Gid"

    _property_mappings: ClassVar[dict[str, str]] = {
        "gid": "Gid",
    }

    gid: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class OntapFileSystemIdentity(PropertyType):
    TYPE = "Type"
    UNIX_USER = "UnixUser"
    WINDOWS_USER = "WindowsUser"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "unix_user": "UnixUser",
        "windows_user": "WindowsUser",
    }

    type_: Optional[Union[str, OntapFileSystemUserType, Ref, GetAtt, Sub]] = None
    unix_user: Optional[OntapUnixFileSystemUser] = None
    windows_user: Optional[OntapWindowsFileSystemUser] = None


@dataclass
class OntapUnixFileSystemUser(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OntapWindowsFileSystemUser(PropertyType):
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "Name",
    }

    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OpenZFSFileSystemIdentity(PropertyType):
    TYPE = "Type"
    POSIX_USER = "PosixUser"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "posix_user": "PosixUser",
    }

    type_: Optional[Union[str, OpenZFSFileSystemUserType, Ref, GetAtt, Sub]] = None
    posix_user: Optional[OpenZFSPosixFileSystemUser] = None


@dataclass
class OpenZFSPosixFileSystemUser(PropertyType):
    UID = "Uid"
    SECONDARY_GIDS = "SecondaryGids"
    GID = "Gid"

    _property_mappings: ClassVar[dict[str, str]] = {
        "uid": "Uid",
        "secondary_gids": "SecondaryGids",
        "gid": "Gid",
    }

    uid: Optional[Union[float, Ref, GetAtt, Sub]] = None
    secondary_gids: Optional[list[FileSystemGID]] = None
    gid: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class S3AccessPoint(PropertyType):
    POLICY = "Policy"
    RESOURCE_ARN = "ResourceARN"
    ALIAS = "Alias"
    VPC_CONFIGURATION = "VpcConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "policy": "Policy",
        "resource_arn": "ResourceARN",
        "alias": "Alias",
        "vpc_configuration": "VpcConfiguration",
    }

    policy: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    alias: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpc_configuration: Optional[S3AccessPointVpcConfiguration] = None


@dataclass
class S3AccessPointOntapConfiguration(PropertyType):
    VOLUME_ID = "VolumeId"
    FILE_SYSTEM_IDENTITY = "FileSystemIdentity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "volume_id": "VolumeId",
        "file_system_identity": "FileSystemIdentity",
    }

    volume_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_system_identity: Optional[OntapFileSystemIdentity] = None


@dataclass
class S3AccessPointOpenZFSConfiguration(PropertyType):
    VOLUME_ID = "VolumeId"
    FILE_SYSTEM_IDENTITY = "FileSystemIdentity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "volume_id": "VolumeId",
        "file_system_identity": "FileSystemIdentity",
    }

    volume_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_system_identity: Optional[OpenZFSFileSystemIdentity] = None


@dataclass
class S3AccessPointVpcConfiguration(PropertyType):
    VPC_ID = "VpcId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_id": "VpcId",
    }

    vpc_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

