"""PropertyTypes for AWS::EC2::CapacityReservation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CapacityAllocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allocation_type": "AllocationType",
        "count": "Count",
    }

    allocation_type: Optional[Union[str, AllocationType, Ref, GetAtt, Sub]] = None
    count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CommitmentInfo(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "committed_instance_count": "CommittedInstanceCount",
        "commitment_end_date": "CommitmentEndDate",
    }

    committed_instance_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    commitment_end_date: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TagSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_type": "ResourceType",
        "tags": "Tags",
    }

    resource_type: Optional[Union[str, ResourceType, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None

