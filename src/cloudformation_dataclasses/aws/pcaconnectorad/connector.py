"""PropertyTypes for AWS::PCAConnectorAD::Connector."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class VpcInformation(PropertyType):
    IP_ADDRESS_TYPE = "IpAddressType"
    SECURITY_GROUP_IDS = "SecurityGroupIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_address_type": "IpAddressType",
        "security_group_ids": "SecurityGroupIds",
    }

    ip_address_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None

