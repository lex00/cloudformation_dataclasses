"""PropertyTypes for AWS::NetworkFirewall::VpcEndpointAssociation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class SubnetMapping(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_address_type": "IPAddressType",
        "subnet_id": "SubnetId",
    }

    ip_address_type: Optional[Union[str, IPAddressType, Ref, GetAtt, Sub]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

