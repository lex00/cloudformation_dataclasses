"""PropertyTypes for AWS::ResilienceHub::ResiliencyPolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FailurePolicy(PropertyType):
    RPO_IN_SECS = "RpoInSecs"
    RTO_IN_SECS = "RtoInSecs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rpo_in_secs": "RpoInSecs",
        "rto_in_secs": "RtoInSecs",
    }

    rpo_in_secs: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rto_in_secs: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PolicyMap(PropertyType):
    AZ = "AZ"
    REGION = "Region"
    HARDWARE = "Hardware"
    SOFTWARE = "Software"

    _property_mappings: ClassVar[dict[str, str]] = {
        "az": "AZ",
        "region": "Region",
        "hardware": "Hardware",
        "software": "Software",
    }

    az: Optional[FailurePolicy] = None
    region: Optional[FailurePolicy] = None
    hardware: Optional[FailurePolicy] = None
    software: Optional[FailurePolicy] = None

