"""PropertyTypes for AWS::EC2::IPAMPool."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ProvisionedCidr(PropertyType):
    CIDR = "Cidr"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cidr": "Cidr",
    }

    cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourceResource(PropertyType):
    RESOURCE_REGION = "ResourceRegion"
    RESOURCE_ID = "ResourceId"
    RESOURCE_OWNER = "ResourceOwner"
    RESOURCE_TYPE = "ResourceType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_region": "ResourceRegion",
        "resource_id": "ResourceId",
        "resource_owner": "ResourceOwner",
        "resource_type": "ResourceType",
    }

    resource_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_owner: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

