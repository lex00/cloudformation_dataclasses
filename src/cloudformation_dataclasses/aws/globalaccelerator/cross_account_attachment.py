"""PropertyTypes for AWS::GlobalAccelerator::CrossAccountAttachment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Resource(PropertyType):
    CIDR = "Cidr"
    ENDPOINT_ID = "EndpointId"
    REGION = "Region"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cidr": "Cidr",
        "endpoint_id": "EndpointId",
        "region": "Region",
    }

    cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None
    endpoint_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None

