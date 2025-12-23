"""PropertyTypes for AWS::EC2::NetworkInsightsAnalysis."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AdditionalDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "service_name": "ServiceName",
        "additional_detail_type": "AdditionalDetailType",
        "load_balancers": "LoadBalancers",
        "component": "Component",
    }

    service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    additional_detail_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    load_balancers: Optional[list[AnalysisComponent]] = None
    component: Optional[AnalysisComponent] = None


@dataclass
class AlternatePathHint(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "component_arn": "ComponentArn",
        "component_id": "ComponentId",
    }

    component_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    component_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AnalysisAclRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "port_range": "PortRange",
        "cidr": "Cidr",
        "rule_action": "RuleAction",
        "egress": "Egress",
        "rule_number": "RuleNumber",
        "protocol": "Protocol",
    }

    port_range: Optional[PortRange] = None
    cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rule_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    egress: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    rule_number: Optional[Union[int, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AnalysisComponent(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "Id",
        "arn": "Arn",
    }

    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AnalysisLoadBalancerListener(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_port": "InstancePort",
        "load_balancer_port": "LoadBalancerPort",
    }

    instance_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    load_balancer_port: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AnalysisLoadBalancerTarget(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "address": "Address",
        "instance": "Instance",
        "port": "Port",
        "availability_zone": "AvailabilityZone",
    }

    address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance: Optional[AnalysisComponent] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AnalysisPacketHeader(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination_port_ranges": "DestinationPortRanges",
        "source_port_ranges": "SourcePortRanges",
        "destination_addresses": "DestinationAddresses",
        "protocol": "Protocol",
        "source_addresses": "SourceAddresses",
    }

    destination_port_ranges: Optional[list[PortRange]] = None
    source_port_ranges: Optional[list[PortRange]] = None
    destination_addresses: Optional[Union[list[str], Ref]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_addresses: Optional[Union[list[str], Ref]] = None


@dataclass
class AnalysisRouteTableRoute(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "origin": "Origin",
        "destination_prefix_list_id": "destinationPrefixListId",
        "transit_gateway_id": "TransitGatewayId",
        "vpc_peering_connection_id": "VpcPeeringConnectionId",
        "instance_id": "instanceId",
        "state": "State",
        "egress_only_internet_gateway_id": "egressOnlyInternetGatewayId",
        "destination_cidr": "destinationCidr",
        "network_interface_id": "NetworkInterfaceId",
        "nat_gateway_id": "NatGatewayId",
        "gateway_id": "gatewayId",
    }

    origin: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_prefix_list_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    transit_gateway_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpc_peering_connection_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    egress_only_internet_gateway_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None
    network_interface_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    nat_gateway_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    gateway_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AnalysisSecurityGroupRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "port_range": "PortRange",
        "cidr": "Cidr",
        "prefix_list_id": "PrefixListId",
        "security_group_id": "SecurityGroupId",
        "protocol": "Protocol",
        "direction": "Direction",
    }

    port_range: Optional[PortRange] = None
    cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix_list_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    security_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    direction: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Explanation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "vpn_gateway": "VpnGateway",
        "packet_field": "PacketField",
        "transit_gateway_attachment": "TransitGatewayAttachment",
        "protocols": "Protocols",
        "ingress_route_table": "IngressRouteTable",
        "classic_load_balancer_listener": "ClassicLoadBalancerListener",
        "vpc_peering_connection": "VpcPeeringConnection",
        "address": "Address",
        "port": "Port",
        "addresses": "Addresses",
        "elastic_load_balancer_listener": "ElasticLoadBalancerListener",
        "transit_gateway_route_table": "TransitGatewayRouteTable",
        "explanation_code": "ExplanationCode",
        "internet_gateway": "InternetGateway",
        "source_vpc": "SourceVpc",
        "attached_to": "AttachedTo",
        "prefix_list": "PrefixList",
        "transit_gateway_route_table_route": "TransitGatewayRouteTableRoute",
        "component_region": "ComponentRegion",
        "load_balancer_target_group": "LoadBalancerTargetGroup",
        "network_interface": "NetworkInterface",
        "customer_gateway": "CustomerGateway",
        "destination_vpc": "DestinationVpc",
        "security_group": "SecurityGroup",
        "transit_gateway": "TransitGateway",
        "route_table": "RouteTable",
        "state": "State",
        "load_balancer_listener_port": "LoadBalancerListenerPort",
        "vpc_endpoint": "vpcEndpoint",
        "subnet": "Subnet",
        "cidrs": "Cidrs",
        "destination": "Destination",
        "security_groups": "SecurityGroups",
        "component_account": "ComponentAccount",
        "vpn_connection": "VpnConnection",
        "vpc": "Vpc",
        "nat_gateway": "NatGateway",
        "direction": "Direction",
        "load_balancer_target_port": "LoadBalancerTargetPort",
        "load_balancer_target": "LoadBalancerTarget",
        "load_balancer_target_groups": "LoadBalancerTargetGroups",
        "component": "Component",
        "missing_component": "MissingComponent",
        "route_table_route": "RouteTableRoute",
        "availability_zones": "AvailabilityZones",
        "port_ranges": "PortRanges",
        "acl": "Acl",
        "security_group_rule": "SecurityGroupRule",
        "subnet_route_table": "SubnetRouteTable",
        "load_balancer_arn": "LoadBalancerArn",
        "acl_rule": "AclRule",
    }

    vpn_gateway: Optional[AnalysisComponent] = None
    packet_field: Optional[Union[str, Ref, GetAtt, Sub]] = None
    transit_gateway_attachment: Optional[AnalysisComponent] = None
    protocols: Optional[Union[list[str], Ref]] = None
    ingress_route_table: Optional[AnalysisComponent] = None
    classic_load_balancer_listener: Optional[AnalysisLoadBalancerListener] = None
    vpc_peering_connection: Optional[AnalysisComponent] = None
    address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    addresses: Optional[Union[list[str], Ref]] = None
    elastic_load_balancer_listener: Optional[AnalysisComponent] = None
    transit_gateway_route_table: Optional[AnalysisComponent] = None
    explanation_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    internet_gateway: Optional[AnalysisComponent] = None
    source_vpc: Optional[AnalysisComponent] = None
    attached_to: Optional[AnalysisComponent] = None
    prefix_list: Optional[AnalysisComponent] = None
    transit_gateway_route_table_route: Optional[TransitGatewayRouteTableRoute] = None
    component_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    load_balancer_target_group: Optional[AnalysisComponent] = None
    network_interface: Optional[AnalysisComponent] = None
    customer_gateway: Optional[AnalysisComponent] = None
    destination_vpc: Optional[AnalysisComponent] = None
    security_group: Optional[AnalysisComponent] = None
    transit_gateway: Optional[AnalysisComponent] = None
    route_table: Optional[AnalysisComponent] = None
    state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    load_balancer_listener_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    vpc_endpoint: Optional[AnalysisComponent] = None
    subnet: Optional[AnalysisComponent] = None
    cidrs: Optional[Union[list[str], Ref]] = None
    destination: Optional[AnalysisComponent] = None
    security_groups: Optional[list[AnalysisComponent]] = None
    component_account: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpn_connection: Optional[AnalysisComponent] = None
    vpc: Optional[AnalysisComponent] = None
    nat_gateway: Optional[AnalysisComponent] = None
    direction: Optional[Union[str, Ref, GetAtt, Sub]] = None
    load_balancer_target_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    load_balancer_target: Optional[AnalysisLoadBalancerTarget] = None
    load_balancer_target_groups: Optional[list[AnalysisComponent]] = None
    component: Optional[AnalysisComponent] = None
    missing_component: Optional[Union[str, Ref, GetAtt, Sub]] = None
    route_table_route: Optional[AnalysisRouteTableRoute] = None
    availability_zones: Optional[Union[list[str], Ref]] = None
    port_ranges: Optional[list[PortRange]] = None
    acl: Optional[AnalysisComponent] = None
    security_group_rule: Optional[AnalysisSecurityGroupRule] = None
    subnet_route_table: Optional[AnalysisComponent] = None
    load_balancer_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    acl_rule: Optional[AnalysisAclRule] = None


@dataclass
class PathComponent(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "additional_details": "AdditionalDetails",
        "inbound_header": "InboundHeader",
        "vpc": "Vpc",
        "destination_vpc": "DestinationVpc",
        "security_group_rule": "SecurityGroupRule",
        "transit_gateway": "TransitGateway",
        "elastic_load_balancer_listener": "ElasticLoadBalancerListener",
        "explanations": "Explanations",
        "service_name": "ServiceName",
        "sequence_number": "SequenceNumber",
        "source_vpc": "SourceVpc",
        "outbound_header": "OutboundHeader",
        "acl_rule": "AclRule",
        "transit_gateway_route_table_route": "TransitGatewayRouteTableRoute",
        "component": "Component",
        "subnet": "Subnet",
        "route_table_route": "RouteTableRoute",
    }

    additional_details: Optional[list[AdditionalDetail]] = None
    inbound_header: Optional[AnalysisPacketHeader] = None
    vpc: Optional[AnalysisComponent] = None
    destination_vpc: Optional[AnalysisComponent] = None
    security_group_rule: Optional[AnalysisSecurityGroupRule] = None
    transit_gateway: Optional[AnalysisComponent] = None
    elastic_load_balancer_listener: Optional[AnalysisComponent] = None
    explanations: Optional[list[Explanation]] = None
    service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sequence_number: Optional[Union[int, Ref, GetAtt, Sub]] = None
    source_vpc: Optional[AnalysisComponent] = None
    outbound_header: Optional[AnalysisPacketHeader] = None
    acl_rule: Optional[AnalysisAclRule] = None
    transit_gateway_route_table_route: Optional[TransitGatewayRouteTableRoute] = None
    component: Optional[AnalysisComponent] = None
    subnet: Optional[AnalysisComponent] = None
    route_table_route: Optional[AnalysisRouteTableRoute] = None


@dataclass
class PortRange(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
    }

    from_: Optional[Union[int, Ref, GetAtt, Sub]] = None
    to: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TransitGatewayRouteTableRoute(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "prefix_list_id": "PrefixListId",
        "resource_id": "ResourceId",
        "state": "State",
        "resource_type": "ResourceType",
        "route_origin": "RouteOrigin",
        "destination_cidr": "DestinationCidr",
        "attachment_id": "AttachmentId",
    }

    prefix_list_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    route_origin: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attachment_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

