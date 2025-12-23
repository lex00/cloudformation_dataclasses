"""PropertyTypes for AWS::ServiceCatalog::CloudFormationProvisionedProduct."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ProvisioningParameter(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProvisioningPreferences(PropertyType):
    STACK_SET_ACCOUNTS = "StackSetAccounts"
    STACK_SET_FAILURE_TOLERANCE_COUNT = "StackSetFailureToleranceCount"
    STACK_SET_MAX_CONCURRENCY_PERCENTAGE = "StackSetMaxConcurrencyPercentage"
    STACK_SET_MAX_CONCURRENCY_COUNT = "StackSetMaxConcurrencyCount"
    STACK_SET_REGIONS = "StackSetRegions"
    STACK_SET_OPERATION_TYPE = "StackSetOperationType"
    STACK_SET_FAILURE_TOLERANCE_PERCENTAGE = "StackSetFailureTolerancePercentage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stack_set_accounts": "StackSetAccounts",
        "stack_set_failure_tolerance_count": "StackSetFailureToleranceCount",
        "stack_set_max_concurrency_percentage": "StackSetMaxConcurrencyPercentage",
        "stack_set_max_concurrency_count": "StackSetMaxConcurrencyCount",
        "stack_set_regions": "StackSetRegions",
        "stack_set_operation_type": "StackSetOperationType",
        "stack_set_failure_tolerance_percentage": "StackSetFailureTolerancePercentage",
    }

    stack_set_accounts: Optional[Union[list[str], Ref]] = None
    stack_set_failure_tolerance_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    stack_set_max_concurrency_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    stack_set_max_concurrency_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    stack_set_regions: Optional[Union[list[str], Ref]] = None
    stack_set_operation_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stack_set_failure_tolerance_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None

