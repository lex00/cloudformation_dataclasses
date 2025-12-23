"""PropertyTypes for AWS::ECS::TaskSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AwsVpcConfiguration(PropertyType):
    SECURITY_GROUPS = "SecurityGroups"
    SUBNETS = "Subnets"
    ASSIGN_PUBLIC_IP = "AssignPublicIp"

    _property_mappings: ClassVar[dict[str, str]] = {
        "security_groups": "SecurityGroups",
        "subnets": "Subnets",
        "assign_public_ip": "AssignPublicIp",
    }

    security_groups: Optional[Union[list[str], Ref]] = None
    subnets: Optional[Union[list[str], Ref]] = None
    assign_public_ip: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CapacityProviderStrategyItem(PropertyType):
    CAPACITY_PROVIDER = "CapacityProvider"
    BASE = "Base"
    WEIGHT = "Weight"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_provider": "CapacityProvider",
        "base": "Base",
        "weight": "Weight",
    }

    capacity_provider: Optional[Union[str, Ref, GetAtt, Sub]] = None
    base: Optional[Union[int, Ref, GetAtt, Sub]] = None
    weight: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class LoadBalancer(PropertyType):
    TARGET_GROUP_ARN = "TargetGroupArn"
    CONTAINER_NAME = "ContainerName"
    CONTAINER_PORT = "ContainerPort"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_group_arn": "TargetGroupArn",
        "container_name": "ContainerName",
        "container_port": "ContainerPort",
    }

    target_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    container_port: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkConfiguration(PropertyType):
    AWS_VPC_CONFIGURATION = "AwsVpcConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_vpc_configuration": "AwsVpcConfiguration",
    }

    aws_vpc_configuration: Optional[AwsVpcConfiguration] = None


@dataclass
class Scale(PropertyType):
    VALUE = "Value"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceRegistry(PropertyType):
    CONTAINER_NAME = "ContainerName"
    PORT = "Port"
    CONTAINER_PORT = "ContainerPort"
    REGISTRY_ARN = "RegistryArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "container_name": "ContainerName",
        "port": "Port",
        "container_port": "ContainerPort",
        "registry_arn": "RegistryArn",
    }

    container_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    container_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    registry_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

