"""PropertyTypes for AWS::DataSync::LocationFSxOpenZFS."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MountOptions(PropertyType):
    VERSION = "Version"

    _property_mappings: ClassVar[dict[str, str]] = {
        "version": "Version",
    }

    version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NFS(PropertyType):
    MOUNT_OPTIONS = "MountOptions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mount_options": "MountOptions",
    }

    mount_options: Optional[MountOptions] = None


@dataclass
class Protocol(PropertyType):
    NFS = "NFS"

    _property_mappings: ClassVar[dict[str, str]] = {
        "nfs": "NFS",
    }

    nfs: Optional[NFS] = None

