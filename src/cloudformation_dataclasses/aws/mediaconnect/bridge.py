"""PropertyTypes for AWS::MediaConnect::Bridge."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BridgeFlowSource(PropertyType):
    FLOW_VPC_INTERFACE_ATTACHMENT = "FlowVpcInterfaceAttachment"
    FLOW_ARN = "FlowArn"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "flow_vpc_interface_attachment": "FlowVpcInterfaceAttachment",
        "flow_arn": "FlowArn",
        "name": "Name",
    }

    flow_vpc_interface_attachment: Optional[VpcInterfaceAttachment] = None
    flow_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BridgeNetworkOutput(PropertyType):
    NETWORK_NAME = "NetworkName"
    PORT = "Port"
    IP_ADDRESS = "IpAddress"
    PROTOCOL = "Protocol"
    TTL = "Ttl"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "network_name": "NetworkName",
        "port": "Port",
        "ip_address": "IpAddress",
        "protocol": "Protocol",
        "ttl": "Ttl",
        "name": "Name",
    }

    network_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ip_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Protocol, Ref, GetAtt, Sub]] = None
    ttl: Optional[Union[int, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BridgeNetworkSource(PropertyType):
    MULTICAST_SOURCE_SETTINGS = "MulticastSourceSettings"
    NETWORK_NAME = "NetworkName"
    MULTICAST_IP = "MulticastIp"
    PORT = "Port"
    PROTOCOL = "Protocol"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "multicast_source_settings": "MulticastSourceSettings",
        "network_name": "NetworkName",
        "multicast_ip": "MulticastIp",
        "port": "Port",
        "protocol": "Protocol",
        "name": "Name",
    }

    multicast_source_settings: Optional[MulticastSourceSettings] = None
    network_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    multicast_ip: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Protocol, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BridgeOutput(PropertyType):
    NETWORK_OUTPUT = "NetworkOutput"

    _property_mappings: ClassVar[dict[str, str]] = {
        "network_output": "NetworkOutput",
    }

    network_output: Optional[BridgeNetworkOutput] = None


@dataclass
class BridgeSource(PropertyType):
    NETWORK_SOURCE = "NetworkSource"
    FLOW_SOURCE = "FlowSource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "network_source": "NetworkSource",
        "flow_source": "FlowSource",
    }

    network_source: Optional[BridgeNetworkSource] = None
    flow_source: Optional[BridgeFlowSource] = None


@dataclass
class EgressGatewayBridge(PropertyType):
    MAX_BITRATE = "MaxBitrate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_bitrate": "MaxBitrate",
    }

    max_bitrate: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class FailoverConfig(PropertyType):
    STATE = "State"
    SOURCE_PRIORITY = "SourcePriority"
    FAILOVER_MODE = "FailoverMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "state": "State",
        "source_priority": "SourcePriority",
        "failover_mode": "FailoverMode",
    }

    state: Optional[Union[str, State, Ref, GetAtt, Sub]] = None
    source_priority: Optional[SourcePriority] = None
    failover_mode: Optional[Union[str, FailoverMode, Ref, GetAtt, Sub]] = None


@dataclass
class IngressGatewayBridge(PropertyType):
    MAX_OUTPUTS = "MaxOutputs"
    MAX_BITRATE = "MaxBitrate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_outputs": "MaxOutputs",
        "max_bitrate": "MaxBitrate",
    }

    max_outputs: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_bitrate: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class MulticastSourceSettings(PropertyType):
    MULTICAST_SOURCE_IP = "MulticastSourceIp"

    _property_mappings: ClassVar[dict[str, str]] = {
        "multicast_source_ip": "MulticastSourceIp",
    }

    multicast_source_ip: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourcePriority(PropertyType):
    PRIMARY_SOURCE = "PrimarySource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "primary_source": "PrimarySource",
    }

    primary_source: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpcInterfaceAttachment(PropertyType):
    VPC_INTERFACE_NAME = "VpcInterfaceName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_interface_name": "VpcInterfaceName",
    }

    vpc_interface_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

