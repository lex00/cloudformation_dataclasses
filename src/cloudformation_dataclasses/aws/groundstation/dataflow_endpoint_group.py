"""PropertyTypes for AWS::GroundStation::DataflowEndpointGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AwsGroundStationAgentEndpoint(PropertyType):
    AGENT_STATUS = "AgentStatus"
    INGRESS_ADDRESS = "IngressAddress"
    AUDIT_RESULTS = "AuditResults"
    NAME = "Name"
    EGRESS_ADDRESS = "EgressAddress"

    _property_mappings: ClassVar[dict[str, str]] = {
        "agent_status": "AgentStatus",
        "ingress_address": "IngressAddress",
        "audit_results": "AuditResults",
        "name": "Name",
        "egress_address": "EgressAddress",
    }

    agent_status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ingress_address: Optional[RangedConnectionDetails] = None
    audit_results: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    egress_address: Optional[ConnectionDetails] = None


@dataclass
class ConnectionDetails(PropertyType):
    SOCKET_ADDRESS = "SocketAddress"
    MTU = "Mtu"

    _property_mappings: ClassVar[dict[str, str]] = {
        "socket_address": "SocketAddress",
        "mtu": "Mtu",
    }

    socket_address: Optional[SocketAddress] = None
    mtu: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class DataflowEndpoint(PropertyType):
    ADDRESS = "Address"
    NAME = "Name"
    MTU = "Mtu"

    _property_mappings: ClassVar[dict[str, str]] = {
        "address": "Address",
        "name": "Name",
        "mtu": "Mtu",
    }

    address: Optional[SocketAddress] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mtu: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EndpointDetails(PropertyType):
    ENDPOINT = "Endpoint"
    AWS_GROUND_STATION_AGENT_ENDPOINT = "AwsGroundStationAgentEndpoint"
    SECURITY_DETAILS = "SecurityDetails"

    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint": "Endpoint",
        "aws_ground_station_agent_endpoint": "AwsGroundStationAgentEndpoint",
        "security_details": "SecurityDetails",
    }

    endpoint: Optional[DataflowEndpoint] = None
    aws_ground_station_agent_endpoint: Optional[AwsGroundStationAgentEndpoint] = None
    security_details: Optional[SecurityDetails] = None


@dataclass
class IntegerRange(PropertyType):
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"

    _property_mappings: ClassVar[dict[str, str]] = {
        "minimum": "Minimum",
        "maximum": "Maximum",
    }

    minimum: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RangedConnectionDetails(PropertyType):
    SOCKET_ADDRESS = "SocketAddress"
    MTU = "Mtu"

    _property_mappings: ClassVar[dict[str, str]] = {
        "socket_address": "SocketAddress",
        "mtu": "Mtu",
    }

    socket_address: Optional[RangedSocketAddress] = None
    mtu: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RangedSocketAddress(PropertyType):
    PORT_RANGE = "PortRange"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port_range": "PortRange",
        "name": "Name",
    }

    port_range: Optional[IntegerRange] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SecurityDetails(PropertyType):
    SUBNET_IDS = "SubnetIds"
    SECURITY_GROUP_IDS = "SecurityGroupIds"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subnet_ids": "SubnetIds",
        "security_group_ids": "SecurityGroupIds",
        "role_arn": "RoleArn",
    }

    subnet_ids: Optional[Union[list[str], Ref]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SocketAddress(PropertyType):
    PORT = "Port"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "name": "Name",
    }

    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

