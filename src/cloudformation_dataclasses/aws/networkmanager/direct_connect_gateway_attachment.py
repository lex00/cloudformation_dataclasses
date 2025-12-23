"""PropertyTypes for AWS::NetworkManager::DirectConnectGatewayAttachment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ProposedNetworkFunctionGroupChange(PropertyType):
    TAGS = "Tags"
    NETWORK_FUNCTION_GROUP_NAME = "NetworkFunctionGroupName"
    ATTACHMENT_POLICY_RULE_NUMBER = "AttachmentPolicyRuleNumber"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tags": "Tags",
        "network_function_group_name": "NetworkFunctionGroupName",
        "attachment_policy_rule_number": "AttachmentPolicyRuleNumber",
    }

    tags: Optional[list[Tag]] = None
    network_function_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attachment_policy_rule_number: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ProposedSegmentChange(PropertyType):
    SEGMENT_NAME = "SegmentName"
    TAGS = "Tags"
    ATTACHMENT_POLICY_RULE_NUMBER = "AttachmentPolicyRuleNumber"

    _property_mappings: ClassVar[dict[str, str]] = {
        "segment_name": "SegmentName",
        "tags": "Tags",
        "attachment_policy_rule_number": "AttachmentPolicyRuleNumber",
    }

    segment_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None
    attachment_policy_rule_number: Optional[Union[int, Ref, GetAtt, Sub]] = None

