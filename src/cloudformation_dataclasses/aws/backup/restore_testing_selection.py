"""PropertyTypes for AWS::Backup::RestoreTestingSelection."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class KeyValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProtectedResourceConditions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "string_equals": "StringEquals",
        "string_not_equals": "StringNotEquals",
    }

    string_equals: Optional[list[KeyValue]] = None
    string_not_equals: Optional[list[KeyValue]] = None

