"""PropertyTypes for AWS::Greengrass::LoggerDefinitionVersion."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Logger(PropertyType):
    SPACE = "Space"
    TYPE = "Type"
    LEVEL = "Level"
    ID = "Id"
    COMPONENT = "Component"

    _property_mappings: ClassVar[dict[str, str]] = {
        "space": "Space",
        "type_": "Type",
        "level": "Level",
        "id": "Id",
        "component": "Component",
    }

    space: Optional[Union[int, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, LoggerType, Ref, GetAtt, Sub]] = None
    level: Optional[Union[str, LoggerLevel, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    component: Optional[Union[str, LoggerComponent, Ref, GetAtt, Sub]] = None

