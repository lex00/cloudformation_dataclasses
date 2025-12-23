"""PropertyTypes for AWS::DAX::Cluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class SSESpecification(PropertyType):
    SSE_ENABLED = "SSEEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sse_enabled": "SSEEnabled",
    }

    sse_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

