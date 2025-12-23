"""PropertyTypes for AWS::EFS::AccessPoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccessPointTag(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CreationInfo(PropertyType):
    OWNER_GID = "OwnerGid"
    OWNER_UID = "OwnerUid"
    PERMISSIONS = "Permissions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "owner_gid": "OwnerGid",
        "owner_uid": "OwnerUid",
        "permissions": "Permissions",
    }

    owner_gid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    owner_uid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    permissions: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PosixUser(PropertyType):
    UID = "Uid"
    SECONDARY_GIDS = "SecondaryGids"
    GID = "Gid"

    _property_mappings: ClassVar[dict[str, str]] = {
        "uid": "Uid",
        "secondary_gids": "SecondaryGids",
        "gid": "Gid",
    }

    uid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secondary_gids: Optional[Union[list[str], Ref]] = None
    gid: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RootDirectory(PropertyType):
    PATH = "Path"
    CREATION_INFO = "CreationInfo"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "creation_info": "CreationInfo",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    creation_info: Optional[CreationInfo] = None

