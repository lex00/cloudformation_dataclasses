"""PropertyTypes for AWS::SSM::Document."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AttachmentsSource(PropertyType):
    VALUES = "Values"
    KEY = "Key"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "key": "Key",
        "name": "Name",
    }

    values: Optional[Union[list[str], Ref]] = None
    key: Optional[Union[str, AttachmentsSourceKey, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DocumentRequires(PropertyType):
    VERSION = "Version"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "version": "Version",
        "name": "Name",
    }

    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

