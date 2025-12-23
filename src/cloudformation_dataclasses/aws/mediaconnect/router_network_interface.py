"""PropertyTypes for AWS::MediaConnect::RouterNetworkInterface."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class PublicRouterNetworkInterfaceConfiguration(PropertyType):
    ALLOW_RULES = "AllowRules"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allow_rules": "AllowRules",
    }

    allow_rules: Optional[list[PublicRouterNetworkInterfaceRule]] = None


@dataclass
class PublicRouterNetworkInterfaceRule(PropertyType):
    CIDR = "Cidr"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cidr": "Cidr",
    }

    cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RouterNetworkInterfaceConfiguration(PropertyType):
    VPC = "Vpc"
    PUBLIC = "Public"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc": "Vpc",
        "public": "Public",
    }

    vpc: Optional[VpcRouterNetworkInterfaceConfiguration] = None
    public: Optional[PublicRouterNetworkInterfaceConfiguration] = None


@dataclass
class VpcRouterNetworkInterfaceConfiguration(PropertyType):
    SUBNET_ID = "SubnetId"
    SECURITY_GROUP_IDS = "SecurityGroupIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subnet_id": "SubnetId",
        "security_group_ids": "SecurityGroupIds",
    }

    subnet_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None

