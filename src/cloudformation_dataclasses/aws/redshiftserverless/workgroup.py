"""PropertyTypes for AWS::RedshiftServerless::Workgroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConfigParameter(PropertyType):
    PARAMETER_VALUE = "ParameterValue"
    PARAMETER_KEY = "ParameterKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_value": "ParameterValue",
        "parameter_key": "ParameterKey",
    }

    parameter_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameter_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Endpoint(PropertyType):
    ADDRESS = "Address"
    VPC_ENDPOINTS = "VpcEndpoints"
    PORT = "Port"

    _property_mappings: ClassVar[dict[str, str]] = {
        "address": "Address",
        "vpc_endpoints": "VpcEndpoints",
        "port": "Port",
    }

    address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpc_endpoints: Optional[list[VpcEndpoint]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkInterface(PropertyType):
    PRIVATE_IP_ADDRESS = "PrivateIpAddress"
    AVAILABILITY_ZONE = "AvailabilityZone"
    SUBNET_ID = "SubnetId"
    NETWORK_INTERFACE_ID = "NetworkInterfaceId"

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
class PerformanceTarget(PropertyType):
    STATUS = "Status"
    LEVEL = "Level"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "level": "Level",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    level: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VpcEndpoint(PropertyType):
    VPC_ID = "VpcId"
    NETWORK_INTERFACES = "NetworkInterfaces"
    VPC_ENDPOINT_ID = "VpcEndpointId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_id": "VpcId",
        "network_interfaces": "NetworkInterfaces",
        "vpc_endpoint_id": "VpcEndpointId",
    }

    vpc_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    network_interfaces: Optional[list[NetworkInterface]] = None
    vpc_endpoint_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Workgroup(PropertyType):
    STATUS = "Status"
    CREATION_DATE = "CreationDate"
    WORKGROUP_NAME = "WorkgroupName"
    WORKGROUP_ARN = "WorkgroupArn"
    BASE_CAPACITY = "BaseCapacity"
    ENHANCED_VPC_ROUTING = "EnhancedVpcRouting"
    WORKGROUP_ID = "WorkgroupId"
    SECURITY_GROUP_IDS = "SecurityGroupIds"
    SUBNET_IDS = "SubnetIds"
    NAMESPACE_NAME = "NamespaceName"
    ENDPOINT = "Endpoint"
    CONFIG_PARAMETERS = "ConfigParameters"
    TRACK_NAME = "TrackName"
    PUBLICLY_ACCESSIBLE = "PubliclyAccessible"
    PRICE_PERFORMANCE_TARGET = "PricePerformanceTarget"
    MAX_CAPACITY = "MaxCapacity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "creation_date": "CreationDate",
        "workgroup_name": "WorkgroupName",
        "workgroup_arn": "WorkgroupArn",
        "base_capacity": "BaseCapacity",
        "enhanced_vpc_routing": "EnhancedVpcRouting",
        "workgroup_id": "WorkgroupId",
        "security_group_ids": "SecurityGroupIds",
        "subnet_ids": "SubnetIds",
        "namespace_name": "NamespaceName",
        "endpoint": "Endpoint",
        "config_parameters": "ConfigParameters",
        "track_name": "TrackName",
        "publicly_accessible": "PubliclyAccessible",
        "price_performance_target": "PricePerformanceTarget",
        "max_capacity": "MaxCapacity",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    creation_date: Optional[Union[str, Ref, GetAtt, Sub]] = None
    workgroup_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    workgroup_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    base_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    enhanced_vpc_routing: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    workgroup_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None
    namespace_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    endpoint: Optional[Endpoint] = None
    config_parameters: Optional[list[ConfigParameter]] = None
    track_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    publicly_accessible: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    price_performance_target: Optional[PerformanceTarget] = None
    max_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None

