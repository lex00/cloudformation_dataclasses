"""PropertyTypes for AWS::Lambda::Alias."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AliasRoutingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "additional_version_weights": "AdditionalVersionWeights",
    }

    additional_version_weights: Optional[list[VersionWeight]] = None


@dataclass
class ProvisionedConcurrencyConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "provisioned_concurrent_executions": "ProvisionedConcurrentExecutions",
    }

    provisioned_concurrent_executions: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VersionWeight(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "function_version": "FunctionVersion",
        "function_weight": "FunctionWeight",
    }

    function_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    function_weight: Optional[Union[float, Ref, GetAtt, Sub]] = None

