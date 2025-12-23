"""PropertyTypes for AWS::Redshift::EndpointAccess."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class NetworkInterface(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "private_ip_address": "PrivateIpAddress",
        "availability_zone": "AvailabilityZone",
        "subnet_id": "SubnetId",
        "network_interface_id": "NetworkInterfaceId",
    }

    private_ip_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    network_interface_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpcEndpoint(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_id": "VpcId",
        "network_interfaces": "NetworkInterfaces",
        "vpc_endpoint_id": "VpcEndpointId",
    }

    vpc_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    network_interfaces: Optional[list[NetworkInterface]] = None
    vpc_endpoint_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpcSecurityGroup(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "vpc_security_group_id": "VpcSecurityGroupId",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpc_security_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

