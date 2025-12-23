"""PropertyTypes for AWS::WAFRegional::WebACL."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Action(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Rule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "priority": "Priority",
        "rule_id": "RuleId",
    }

    action: Optional[Action] = None
    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rule_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

