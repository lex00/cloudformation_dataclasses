"""PropertyTypes for AWS::Lambda::Version."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FunctionScalingConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min_execution_environments": "MinExecutionEnvironments",
        "max_execution_environments": "MaxExecutionEnvironments",
    }

    min_execution_environments: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_execution_environments: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ProvisionedConcurrencyConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "provisioned_concurrent_executions": "ProvisionedConcurrentExecutions",
    }

    provisioned_concurrent_executions: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RuntimePolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "update_runtime_on": "UpdateRuntimeOn",
        "runtime_version_arn": "RuntimeVersionArn",
    }

    update_runtime_on: Optional[Union[str, Ref, GetAtt, Sub]] = None
    runtime_version_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

