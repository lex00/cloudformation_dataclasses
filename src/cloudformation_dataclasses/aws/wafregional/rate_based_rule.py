"""PropertyTypes for AWS::WAFRegional::RateBasedRule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Predicate(PropertyType):
    TYPE = "Type"
    DATA_ID = "DataId"
    NEGATED = "Negated"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "data_id": "DataId",
        "negated": "Negated",
    }

    type_: Optional[Union[str, PredicateType, Ref, GetAtt, Sub]] = None
    data_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    negated: Optional[Union[bool, Ref, GetAtt, Sub]] = None

