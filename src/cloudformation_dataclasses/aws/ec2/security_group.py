"""PropertyTypes for AWS::EC2::SecurityGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Egress(PropertyType):
    CIDR_IP = "CidrIp"
    CIDR_IPV6 = "CidrIpv6"
    DESCRIPTION = "Description"
    FROM_PORT = "FromPort"
    TO_PORT = "ToPort"
    IP_PROTOCOL = "IpProtocol"
    DESTINATION_SECURITY_GROUP_ID = "DestinationSecurityGroupId"
    DESTINATION_PREFIX_LIST_ID = "DestinationPrefixListId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cidr_ip": "CidrIp",
        "cidr_ipv6": "CidrIpv6",
        "description": "Description",
        "from_port": "FromPort",
        "to_port": "ToPort",
        "ip_protocol": "IpProtocol",
        "destination_security_group_id": "DestinationSecurityGroupId",
        "destination_prefix_list_id": "DestinationPrefixListId",
    }

    cidr_ip: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cidr_ipv6: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    from_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    to_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ip_protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_security_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_prefix_list_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Ingress(PropertyType):
    CIDR_IP = "CidrIp"
    CIDR_IPV6 = "CidrIpv6"
    DESCRIPTION = "Description"
    FROM_PORT = "FromPort"
    SOURCE_SECURITY_GROUP_NAME = "SourceSecurityGroupName"
    TO_PORT = "ToPort"
    SOURCE_SECURITY_GROUP_OWNER_ID = "SourceSecurityGroupOwnerId"
    IP_PROTOCOL = "IpProtocol"
    SOURCE_SECURITY_GROUP_ID = "SourceSecurityGroupId"
    SOURCE_PREFIX_LIST_ID = "SourcePrefixListId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cidr_ip": "CidrIp",
        "cidr_ipv6": "CidrIpv6",
        "description": "Description",
        "from_port": "FromPort",
        "source_security_group_name": "SourceSecurityGroupName",
        "to_port": "ToPort",
        "source_security_group_owner_id": "SourceSecurityGroupOwnerId",
        "ip_protocol": "IpProtocol",
        "source_security_group_id": "SourceSecurityGroupId",
        "source_prefix_list_id": "SourcePrefixListId",
    }

    cidr_ip: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cidr_ipv6: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    from_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    source_security_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    to_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    source_security_group_owner_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ip_protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_security_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_prefix_list_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

