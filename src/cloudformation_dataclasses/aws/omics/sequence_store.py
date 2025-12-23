"""PropertyTypes for AWS::Omics::SequenceStore."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class SseConfig(PropertyType):
    TYPE = "Type"
    KEY_ARN = "KeyArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "key_arn": "KeyArn",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

