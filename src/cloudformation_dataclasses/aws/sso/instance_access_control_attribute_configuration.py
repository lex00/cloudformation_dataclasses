"""PropertyTypes for AWS::SSO::InstanceAccessControlAttributeConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccessControlAttribute(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[AccessControlAttributeValue] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AccessControlAttributeValue(PropertyType):
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source": "Source",
    }

    source: Optional[Union[list[str], Ref]] = None

