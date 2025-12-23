"""PropertyTypes for AWS::QBusiness::Permission."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Condition(PropertyType):
    CONDITION_OPERATOR = "ConditionOperator"
    CONDITION_VALUES = "ConditionValues"
    CONDITION_KEY = "ConditionKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "condition_operator": "ConditionOperator",
        "condition_values": "ConditionValues",
        "condition_key": "ConditionKey",
    }

    condition_operator: Optional[Union[str, Ref, GetAtt, Sub]] = None
    condition_values: Optional[Union[list[str], Ref]] = None
    condition_key: Optional[Union[str, Ref, GetAtt, Sub]] = None

