"""PropertyTypes for AWS::Config::RemediationConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ExecutionControls(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ssm_controls": "SsmControls",
    }

    ssm_controls: Optional[SsmControls] = None


@dataclass
class RemediationParameterValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_value": "ResourceValue",
        "static_value": "StaticValue",
    }

    resource_value: Optional[ResourceValue] = None
    static_value: Optional[StaticValue] = None


@dataclass
class ResourceValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[str, ResourceValueType, Ref, GetAtt, Sub]] = None


@dataclass
class SsmControls(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "error_percentage": "ErrorPercentage",
        "concurrent_execution_rate_percentage": "ConcurrentExecutionRatePercentage",
    }

    error_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    concurrent_execution_rate_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class StaticValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
    }

    values: Optional[Union[list[str], Ref]] = None

