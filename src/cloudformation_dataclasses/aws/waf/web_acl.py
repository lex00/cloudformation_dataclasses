"""PropertyTypes for AWS::WAF::WebACL."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ActivatedRule(PropertyType):
    ACTION = "Action"
    PRIORITY = "Priority"
    RULE_ID = "RuleId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "priority": "Priority",
        "rule_id": "RuleId",
    }

    action: Optional[WafAction] = None
    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rule_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WafAction(PropertyType):
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, WafActionType, Ref, GetAtt, Sub]] = None

