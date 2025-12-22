"""PropertyTypes for AWS::EventSchemas::Registry."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class CodeGenerationStatus:
    """CodeGenerationStatus enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    CREATE_FAILED = "CREATE_FAILED"


class DiscovererState:
    """DiscovererState enum values."""

    STARTED = "STARTED"
    STOPPED = "STOPPED"


class Type:
    """Type enum values."""

    OPENAPI3 = "OpenApi3"
    JSONSCHEMADRAFT4 = "JSONSchemaDraft4"


@dataclass
class TagsEntry(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

