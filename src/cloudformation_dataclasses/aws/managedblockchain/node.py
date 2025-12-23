"""PropertyTypes for AWS::ManagedBlockchain::Node."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class NodeConfiguration(PropertyType):
    AVAILABILITY_ZONE = "AvailabilityZone"
    INSTANCE_TYPE = "InstanceType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_zone": "AvailabilityZone",
        "instance_type": "InstanceType",
    }

    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

