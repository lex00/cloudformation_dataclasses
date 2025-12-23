"""PropertyTypes for AWS::IoT::ProvisioningTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ProvisioningHook(PropertyType):
    TARGET_ARN = "TargetArn"
    PAYLOAD_VERSION = "PayloadVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_arn": "TargetArn",
        "payload_version": "PayloadVersion",
    }

    target_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload_version: Optional[Union[str, Ref, GetAtt, Sub]] = None

