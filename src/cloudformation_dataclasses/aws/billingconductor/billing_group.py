"""PropertyTypes for AWS::BillingConductor::BillingGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccountGrouping(PropertyType):
    RESPONSIBILITY_TRANSFER_ARN = "ResponsibilityTransferArn"
    LINKED_ACCOUNT_IDS = "LinkedAccountIds"
    AUTO_ASSOCIATE = "AutoAssociate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "responsibility_transfer_arn": "ResponsibilityTransferArn",
        "linked_account_ids": "LinkedAccountIds",
        "auto_associate": "AutoAssociate",
    }

    responsibility_transfer_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    linked_account_ids: Optional[Union[list[str], Ref]] = None
    auto_associate: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ComputationPreference(PropertyType):
    PRICING_PLAN_ARN = "PricingPlanArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pricing_plan_arn": "PricingPlanArn",
    }

    pricing_plan_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

