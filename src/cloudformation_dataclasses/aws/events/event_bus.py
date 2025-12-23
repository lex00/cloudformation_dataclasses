"""PropertyTypes for AWS::Events::EventBus."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DeadLetterConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LogConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "include_detail": "IncludeDetail",
        "level": "Level",
    }

    include_detail: Optional[Union[str, IncludeDetail, Ref, GetAtt, Sub]] = None
    level: Optional[Union[str, Level, Ref, GetAtt, Sub]] = None

