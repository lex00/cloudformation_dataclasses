"""PropertyTypes for AWS::SecurityHub::Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class StandardsControl(PropertyType):
    STANDARDS_CONTROL_ARN = "StandardsControlArn"
    REASON = "Reason"

    _property_mappings: ClassVar[dict[str, str]] = {
        "standards_control_arn": "StandardsControlArn",
        "reason": "Reason",
    }

    standards_control_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    reason: Optional[Union[str, Ref, GetAtt, Sub]] = None

