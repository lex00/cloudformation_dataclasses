"""PropertyTypes for AWS::ElasticLoadBalancingV2::LoadBalancer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class LoadBalancerAttribute(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MinimumLoadBalancerCapacity(PropertyType):
    CAPACITY_UNITS = "CapacityUnits"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_units": "CapacityUnits",
    }

    capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SubnetMapping(PropertyType):
    ALLOCATION_ID = "AllocationId"
    I_PV6_ADDRESS = "IPv6Address"
    SUBNET_ID = "SubnetId"
    SOURCE_NAT_IPV6_PREFIX = "SourceNatIpv6Prefix"
    PRIVATE_I_PV4_ADDRESS = "PrivateIPv4Address"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allocation_id": "AllocationId",
        "i_pv6_address": "IPv6Address",
        "subnet_id": "SubnetId",
        "source_nat_ipv6_prefix": "SourceNatIpv6Prefix",
        "private_i_pv4_address": "PrivateIPv4Address",
    }

    allocation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    i_pv6_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_nat_ipv6_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    private_i_pv4_address: Optional[Union[str, Ref, GetAtt, Sub]] = None

