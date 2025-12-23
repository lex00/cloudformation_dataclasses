"""PropertyTypes for AWS::MediaConnect::FlowSource."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Encryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "key_type": "KeyType",
        "resource_id": "ResourceId",
        "device_id": "DeviceId",
        "region": "Region",
        "constant_initialization_vector": "ConstantInitializationVector",
        "algorithm": "Algorithm",
        "role_arn": "RoleArn",
        "url": "Url",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key_type: Optional[Union[str, KeyType, Ref, GetAtt, Sub]] = None
    resource_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    constant_initialization_vector: Optional[Union[str, Ref, GetAtt, Sub]] = None
    algorithm: Optional[Union[str, Algorithm, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GatewayBridgeSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bridge_arn": "BridgeArn",
        "vpc_interface_attachment": "VpcInterfaceAttachment",
    }

    bridge_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpc_interface_attachment: Optional[VpcInterfaceAttachment] = None


@dataclass
class VpcInterfaceAttachment(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_interface_name": "VpcInterfaceName",
    }

    vpc_interface_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

