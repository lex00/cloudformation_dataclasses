"""PropertyTypes for AWS::CleanRooms::PrivacyBudgetTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BudgetParameter(PropertyType):
    TYPE = "Type"
    BUDGET = "Budget"
    AUTO_REFRESH = "AutoRefresh"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "budget": "Budget",
        "auto_refresh": "AutoRefresh",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    budget: Optional[Union[int, Ref, GetAtt, Sub]] = None
    auto_refresh: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Parameters(PropertyType):
    RESOURCE_ARN = "ResourceArn"
    BUDGET_PARAMETERS = "BudgetParameters"
    EPSILON = "Epsilon"
    USERS_NOISE_PER_QUERY = "UsersNoisePerQuery"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceArn",
        "budget_parameters": "BudgetParameters",
        "epsilon": "Epsilon",
        "users_noise_per_query": "UsersNoisePerQuery",
    }

    resource_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    budget_parameters: Optional[list[BudgetParameter]] = None
    epsilon: Optional[Union[int, Ref, GetAtt, Sub]] = None
    users_noise_per_query: Optional[Union[int, Ref, GetAtt, Sub]] = None

