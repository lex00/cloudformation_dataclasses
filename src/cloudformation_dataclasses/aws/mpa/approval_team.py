"""PropertyTypes for AWS::MPA::ApprovalTeam."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ApprovalStrategy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mof_n": "MofN",
    }

    mof_n: Optional[MofNApprovalStrategy] = None


@dataclass
class Approver(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "primary_identity_status": "PrimaryIdentityStatus",
        "primary_identity_source_arn": "PrimaryIdentitySourceArn",
        "approver_id": "ApproverId",
        "primary_identity_id": "PrimaryIdentityId",
        "response_time": "ResponseTime",
    }

    primary_identity_status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    primary_identity_source_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    approver_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    primary_identity_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    response_time: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MofNApprovalStrategy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min_approvals_required": "MinApprovalsRequired",
    }

    min_approvals_required: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Policy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "policy_arn": "PolicyArn",
    }

    policy_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

