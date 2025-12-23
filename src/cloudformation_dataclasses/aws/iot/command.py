"""PropertyTypes for AWS::IoT::Command."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CommandParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "description": "Description",
        "value": "Value",
        "name": "Name",
    }

    default_value: Optional[CommandParameterValue] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[CommandParameterValue] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CommandParameterValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "b": "B",
        "s": "S",
        "d": "D",
        "bin": "BIN",
        "ul": "UL",
        "i": "I",
        "l": "L",
    }

    b: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    s: Optional[Union[str, Ref, GetAtt, Sub]] = None
    d: Optional[Union[float, Ref, GetAtt, Sub]] = None
    bin: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ul: Optional[Union[str, Ref, GetAtt, Sub]] = None
    i: Optional[Union[int, Ref, GetAtt, Sub]] = None
    l: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CommandPayload(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "content_type": "ContentType",
        "content": "Content",
    }

    content_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    content: Optional[Union[str, Ref, GetAtt, Sub]] = None

