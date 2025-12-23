"""PropertyTypes for AWS::BillingConductor::PricingRule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FreeTier(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "activated": "Activated",
    }

    activated: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Tiering(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "free_tier": "FreeTier",
    }

    free_tier: Optional[FreeTier] = None

