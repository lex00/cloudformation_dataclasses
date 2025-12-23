"""PropertyTypes for AWS::SES::MailManagerIngressPoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IngressPointConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "smtp_password": "SmtpPassword",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    smtp_password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NetworkConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "public_network_configuration": "PublicNetworkConfiguration",
        "private_network_configuration": "PrivateNetworkConfiguration",
    }

    public_network_configuration: Optional[PublicNetworkConfiguration] = None
    private_network_configuration: Optional[PrivateNetworkConfiguration] = None


@dataclass
class PrivateNetworkConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_endpoint_id": "VpcEndpointId",
    }

    vpc_endpoint_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PublicNetworkConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_type": "IpType",
    }

    ip_type: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None

