"""PropertyTypes for AWS::EC2::IPAM."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IpamOperatingRegion(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "region_name": "RegionName",
    }

    region_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IpamOrganizationalUnitExclusion(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "organizations_entity_path": "OrganizationsEntityPath",
    }

    organizations_entity_path: Optional[Union[str, Ref, GetAtt, Sub]] = None

