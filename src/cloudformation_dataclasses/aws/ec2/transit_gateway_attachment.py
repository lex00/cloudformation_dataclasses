"""PropertyTypes for AWS::EC2::TransitGatewayAttachment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Options(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ipv6_support": "Ipv6Support",
        "appliance_mode_support": "ApplianceModeSupport",
        "security_group_referencing_support": "SecurityGroupReferencingSupport",
        "dns_support": "DnsSupport",
    }

    ipv6_support: Optional[Union[str, Ref, GetAtt, Sub]] = None
    appliance_mode_support: Optional[Union[str, Ref, GetAtt, Sub]] = None
    security_group_referencing_support: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dns_support: Optional[Union[str, Ref, GetAtt, Sub]] = None

