"""PropertyTypes for AWS::ApiGateway::UsagePlan."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ApiStage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "stage": "Stage",
        "api_id": "ApiId",
        "throttle": "Throttle",
    }

    stage: Optional[Union[str, Ref, GetAtt, Sub]] = None
    api_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    throttle: Optional[dict[str, Any]] = None


@dataclass
class QuotaSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "period": "Period",
        "limit": "Limit",
        "offset": "Offset",
    }

    period: Optional[Union[str, Ref, GetAtt, Sub]] = None
    limit: Optional[Union[int, Ref, GetAtt, Sub]] = None
    offset: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ThrottleSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "burst_limit": "BurstLimit",
        "rate_limit": "RateLimit",
    }

    burst_limit: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rate_limit: Optional[Union[float, Ref, GetAtt, Sub]] = None

