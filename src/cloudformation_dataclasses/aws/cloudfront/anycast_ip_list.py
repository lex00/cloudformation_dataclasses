"""PropertyTypes for AWS::CloudFront::AnycastIpList."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AnycastIpList(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_address_type": "IpAddressType",
        "status": "Status",
        "ip_count": "IpCount",
        "anycast_ips": "AnycastIps",
        "last_modified_time": "LastModifiedTime",
        "id": "Id",
        "arn": "Arn",
        "ipam_cidr_config_results": "IpamCidrConfigResults",
        "name": "Name",
    }

    ip_address_type: Optional[Union[str, IpAddressType, Ref, GetAtt, Sub]] = None
    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ip_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    anycast_ips: Optional[Union[list[str], Ref]] = None
    last_modified_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ipam_cidr_config_results: Optional[list[IpamCidrConfigResult]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IpamCidrConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cidr": "Cidr",
        "ipam_pool_arn": "IpamPoolArn",
    }

    cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ipam_pool_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IpamCidrConfigResult(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "anycast_ip": "AnycastIp",
        "cidr": "Cidr",
        "ipam_pool_arn": "IpamPoolArn",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    anycast_ip: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ipam_pool_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Tags(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "items": "Items",
    }

    items: Optional[list[Tag]] = None

