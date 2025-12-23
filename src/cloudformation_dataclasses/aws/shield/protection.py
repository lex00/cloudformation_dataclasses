"""PropertyTypes for AWS::Shield::Protection."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Action(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "block": "Block",
        "count": "Count",
    }

    block: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    count: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class ApplicationLayerAutomaticResponseConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "action": "Action",
    }

    status: Optional[Union[str, ApplicationLayerAutomaticResponseStatus, Ref, GetAtt, Sub]] = None
    action: Optional[Action] = None

