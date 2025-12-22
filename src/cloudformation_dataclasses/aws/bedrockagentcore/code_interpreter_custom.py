"""PropertyTypes for AWS::BedrockAgentCore::CodeInterpreterCustom."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CodeInterpreterNetworkConfiguration(PropertyType):
    VPC_CONFIG = "VpcConfig"
    NETWORK_MODE = "NetworkMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_config": "VpcConfig",
        "network_mode": "NetworkMode",
    }

    vpc_config: Optional[VpcConfig] = None
    network_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConfig(PropertyType):
    SECURITY_GROUPS = "SecurityGroups"
    SUBNETS = "Subnets"

    _property_mappings: ClassVar[dict[str, str]] = {
        "security_groups": "SecurityGroups",
        "subnets": "Subnets",
    }

    security_groups: Optional[Union[list[str], Ref]] = None
    subnets: Optional[Union[list[str], Ref]] = None

