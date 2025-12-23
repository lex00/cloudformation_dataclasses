"""PropertyTypes for AWS::MediaConnect::BridgeSource."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BridgeFlowSource(PropertyType):
    FLOW_VPC_INTERFACE_ATTACHMENT = "FlowVpcInterfaceAttachment"
    FLOW_ARN = "FlowArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "flow_vpc_interface_attachment": "FlowVpcInterfaceAttachment",
        "flow_arn": "FlowArn",
    }

    flow_vpc_interface_attachment: Optional[VpcInterfaceAttachment] = None
    flow_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BridgeNetworkSource(PropertyType):
    MULTICAST_SOURCE_SETTINGS = "MulticastSourceSettings"
    NETWORK_NAME = "NetworkName"
    MULTICAST_IP = "MulticastIp"
    PORT = "Port"
    PROTOCOL = "Protocol"

    _property_mappings: ClassVar[dict[str, str]] = {
        "multicast_source_settings": "MulticastSourceSettings",
        "network_name": "NetworkName",
        "multicast_ip": "MulticastIp",
        "port": "Port",
        "protocol": "Protocol",
    }

    multicast_source_settings: Optional[MulticastSourceSettings] = None
    network_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    multicast_ip: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Protocol, Ref, GetAtt, Sub]] = None


@dataclass
class MulticastSourceSettings(PropertyType):
    MULTICAST_SOURCE_IP = "MulticastSourceIp"

    _property_mappings: ClassVar[dict[str, str]] = {
        "multicast_source_ip": "MulticastSourceIp",
    }

    multicast_source_ip: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpcInterfaceAttachment(PropertyType):
    VPC_INTERFACE_NAME = "VpcInterfaceName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_interface_name": "VpcInterfaceName",
    }

    vpc_interface_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

