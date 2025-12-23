"""PropertyTypes for AWS::IoTThingsGraph::FlowTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DefinitionDocument(PropertyType):
    LANGUAGE = "Language"
    TEXT = "Text"

    _property_mappings: ClassVar[dict[str, str]] = {
        "language": "Language",
        "text": "Text",
    }

    language: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None

