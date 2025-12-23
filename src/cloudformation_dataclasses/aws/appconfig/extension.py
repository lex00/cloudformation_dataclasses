"""PropertyTypes for AWS::AppConfig::Extension."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Parameter(PropertyType):
    DYNAMIC = "Dynamic"
    DESCRIPTION = "Description"
    REQUIRED = "Required"

    _property_mappings: ClassVar[dict[str, str]] = {
        "dynamic": "Dynamic",
        "description": "Description",
        "required": "Required",
    }

    dynamic: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    required: Optional[Union[bool, Ref, GetAtt, Sub]] = None

