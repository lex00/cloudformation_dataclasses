"""PropertyTypes for AWS::Transfer::User."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class HomeDirectoryMapEntry(PropertyType):
    ENTRY = "Entry"
    TARGET = "Target"
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entry": "Entry",
        "target": "Target",
        "type_": "Type",
    }

    entry: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, MapType, Ref, GetAtt, Sub]] = None


@dataclass
class PosixProfile(PropertyType):
    UID = "Uid"
    SECONDARY_GIDS = "SecondaryGids"
    GID = "Gid"

    _property_mappings: ClassVar[dict[str, str]] = {
        "uid": "Uid",
        "secondary_gids": "SecondaryGids",
        "gid": "Gid",
    }

    uid: Optional[Union[float, Ref, GetAtt, Sub]] = None
    secondary_gids: Optional[Union[list[float], Ref]] = None
    gid: Optional[Union[float, Ref, GetAtt, Sub]] = None

