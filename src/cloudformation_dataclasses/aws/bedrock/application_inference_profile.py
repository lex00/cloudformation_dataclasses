"""PropertyTypes for AWS::Bedrock::ApplicationInferenceProfile."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class InferenceProfileModel(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "model_arn": "ModelArn",
    }

    model_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InferenceProfileModelSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "copy_from": "CopyFrom",
    }

    copy_from: Optional[Union[str, Ref, GetAtt, Sub]] = None

