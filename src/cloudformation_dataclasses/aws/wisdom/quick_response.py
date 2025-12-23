"""PropertyTypes for AWS::Wisdom::QuickResponse."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class GroupingConfiguration(PropertyType):
    VALUES = "Values"
    CRITERIA = "Criteria"

    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "criteria": "Criteria",
    }

    values: Optional[Union[list[str], Ref]] = None
    criteria: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QuickResponseContentProvider(PropertyType):
    CONTENT = "Content"

    _property_mappings: ClassVar[dict[str, str]] = {
        "content": "Content",
    }

    content: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QuickResponseContents(PropertyType):
    PLAIN_TEXT = "PlainText"
    MARKDOWN = "Markdown"

    _property_mappings: ClassVar[dict[str, str]] = {
        "plain_text": "PlainText",
        "markdown": "Markdown",
    }

    plain_text: Optional[QuickResponseContentProvider] = None
    markdown: Optional[QuickResponseContentProvider] = None

