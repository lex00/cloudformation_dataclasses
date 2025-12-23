"""PropertyTypes for AWS::AmplifyUIBuilder::Theme."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ThemeValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "children": "Children",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    children: Optional[list[ThemeValues]] = None


@dataclass
class ThemeValues(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[ThemeValue] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

