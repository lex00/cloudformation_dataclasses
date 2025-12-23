"""PropertyTypes for AWS::EC2::Subnet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BlockPublicAccessStates(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "internet_gateway_block_mode": "InternetGatewayBlockMode",
    }

    internet_gateway_block_mode: Optional[Union[str, BlockPublicAccessMode, Ref, GetAtt, Sub]] = None


@dataclass
class PrivateDnsNameOptionsOnLaunch(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_resource_name_dns_a_record": "EnableResourceNameDnsARecord",
        "hostname_type": "HostnameType",
        "enable_resource_name_dns_aaaa_record": "EnableResourceNameDnsAAAARecord",
    }

    enable_resource_name_dns_a_record: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    hostname_type: Optional[Union[str, HostnameType, Ref, GetAtt, Sub]] = None
    enable_resource_name_dns_aaaa_record: Optional[Union[bool, Ref, GetAtt, Sub]] = None

