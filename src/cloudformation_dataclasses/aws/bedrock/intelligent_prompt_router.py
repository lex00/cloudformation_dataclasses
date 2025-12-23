"""PropertyTypes for AWS::Bedrock::IntelligentPromptRouter."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class PromptRouterTargetModel(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "model_arn": "ModelArn",
    }

    model_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RoutingCriteria(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "response_quality_difference": "ResponseQualityDifference",
    }

    response_quality_difference: Optional[Union[float, Ref, GetAtt, Sub]] = None

