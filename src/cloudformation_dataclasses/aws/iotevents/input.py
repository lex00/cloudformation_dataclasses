"""PropertyTypes for AWS::IoTEvents::Input."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Attribute(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "json_path": "JsonPath",
    }

    json_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "attributes": "Attributes",
    }

    attributes: Optional[list[Attribute]] = None

