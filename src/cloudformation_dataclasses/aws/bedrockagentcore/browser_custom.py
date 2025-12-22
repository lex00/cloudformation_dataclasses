"""PropertyTypes for AWS::BedrockAgentCore::BrowserCustom."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BrowserNetworkConfiguration(PropertyType):
    VPC_CONFIG = "VpcConfig"
    NETWORK_MODE = "NetworkMode"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_config": "VpcConfig",
        "network_mode": "NetworkMode",
    }

    vpc_config: Optional[VpcConfig] = None
    network_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BrowserSigning(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class RecordingConfig(PropertyType):
    ENABLED = "Enabled"
    S3_LOCATION = "S3Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "s3_location": "S3Location",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    s3_location: Optional[S3Location] = None


@dataclass
class S3Location(PropertyType):
    BUCKET = "Bucket"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "prefix": "Prefix",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


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

