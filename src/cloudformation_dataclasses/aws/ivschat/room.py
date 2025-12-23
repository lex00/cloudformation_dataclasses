"""PropertyTypes for AWS::IVSChat::Room."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MessageReviewHandler(PropertyType):
    FALLBACK_RESULT = "FallbackResult"
    URI = "Uri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "fallback_result": "FallbackResult",
        "uri": "Uri",
    }

    fallback_result: Optional[Union[str, Ref, GetAtt, Sub]] = None
    uri: Optional[Union[str, Ref, GetAtt, Sub]] = None

