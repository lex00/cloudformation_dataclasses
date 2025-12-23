"""PropertyTypes for AWS::ApiGatewayV2::RouteResponse."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ParameterConstraints(PropertyType):
    REQUIRED = "Required"

    _property_mappings: ClassVar[dict[str, str]] = {
        "required": "Required",
    }

    required: Optional[Union[bool, Ref, GetAtt, Sub]] = None

