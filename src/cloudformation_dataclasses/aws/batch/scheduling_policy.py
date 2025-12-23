"""PropertyTypes for AWS::Batch::SchedulingPolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FairsharePolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "share_distribution": "ShareDistribution",
        "share_decay_seconds": "ShareDecaySeconds",
        "compute_reservation": "ComputeReservation",
    }

    share_distribution: Optional[list[ShareAttributes]] = None
    share_decay_seconds: Optional[Union[float, Ref, GetAtt, Sub]] = None
    compute_reservation: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ShareAttributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "weight_factor": "WeightFactor",
        "share_identifier": "ShareIdentifier",
    }

    weight_factor: Optional[Union[float, Ref, GetAtt, Sub]] = None
    share_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None

