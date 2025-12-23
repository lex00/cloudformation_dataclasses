"""PropertyTypes for AWS::Athena::CapacityReservation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CapacityAssignment(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "workgroup_names": "WorkgroupNames",
    }

    workgroup_names: Optional[Union[list[str], Ref]] = None


@dataclass
class CapacityAssignmentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_assignments": "CapacityAssignments",
    }

    capacity_assignments: Optional[list[CapacityAssignment]] = None

