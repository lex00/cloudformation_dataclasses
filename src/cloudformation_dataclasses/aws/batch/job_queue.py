"""PropertyTypes for AWS::Batch::JobQueue."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ComputeEnvironmentOrder(PropertyType):
    COMPUTE_ENVIRONMENT = "ComputeEnvironment"
    ORDER = "Order"

    _property_mappings: ClassVar[dict[str, str]] = {
        "compute_environment": "ComputeEnvironment",
        "order": "Order",
    }

    compute_environment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    order: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class JobStateTimeLimitAction(PropertyType):
    ACTION = "Action"
    MAX_TIME_SECONDS = "MaxTimeSeconds"
    STATE = "State"
    REASON = "Reason"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "max_time_seconds": "MaxTimeSeconds",
        "state": "State",
        "reason": "Reason",
    }

    action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_time_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    reason: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceEnvironmentOrder(PropertyType):
    ORDER = "Order"
    SERVICE_ENVIRONMENT = "ServiceEnvironment"

    _property_mappings: ClassVar[dict[str, str]] = {
        "order": "Order",
        "service_environment": "ServiceEnvironment",
    }

    order: Optional[Union[int, Ref, GetAtt, Sub]] = None
    service_environment: Optional[Union[str, Ref, GetAtt, Sub]] = None

