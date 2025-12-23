"""PropertyTypes for AWS::IoT::BillingGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BillingGroupProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "billing_group_description": "BillingGroupDescription",
    }

    billing_group_description: Optional[Union[str, Ref, GetAtt, Sub]] = None

