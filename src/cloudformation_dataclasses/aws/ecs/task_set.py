"""PropertyTypes for AWS::ECS::TaskSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AwsVpcConfiguration(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_vpc_configuration": "AwsVpcConfiguration",
    }

    aws_vpc_configuration: Optional[AwsVpcConfiguration] = None


@dataclass
class Scale(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceRegistry(PropertyType):
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

