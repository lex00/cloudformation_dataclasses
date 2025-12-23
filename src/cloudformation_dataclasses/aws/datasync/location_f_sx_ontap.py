"""PropertyTypes for AWS::DataSync::LocationFSxONTAP."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class NFS(PropertyType):
    MOUNT_OPTIONS = "MountOptions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mount_options": "MountOptions",
    }

    mount_options: Optional[NfsMountOptions] = None


@dataclass
class NfsMountOptions(PropertyType):
    VERSION = "Version"

    _property_mappings: ClassVar[dict[str, str]] = {
        "version": "Version",
    }

    version: Optional[Union[str, NfsVersion, Ref, GetAtt, Sub]] = None


@dataclass
class Protocol(PropertyType):
    SMB = "SMB"
    NFS = "NFS"

    _property_mappings: ClassVar[dict[str, str]] = {
        "smb": "SMB",
        "nfs": "NFS",
    }

    smb: Optional[SMB] = None
    nfs: Optional[NFS] = None


@dataclass
class SMB(PropertyType):
    USER = "User"
    DOMAIN = "Domain"
    MOUNT_OPTIONS = "MountOptions"
    PASSWORD = "Password"

    _property_mappings: ClassVar[dict[str, str]] = {
        "user": "User",
        "domain": "Domain",
        "mount_options": "MountOptions",
        "password": "Password",
    }

    user: Optional[Union[str, Ref, GetAtt, Sub]] = None
    domain: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mount_options: Optional[SmbMountOptions] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SmbMountOptions(PropertyType):
    VERSION = "Version"

    _property_mappings: ClassVar[dict[str, str]] = {
        "version": "Version",
    }

    version: Optional[Union[str, SmbVersion, Ref, GetAtt, Sub]] = None

