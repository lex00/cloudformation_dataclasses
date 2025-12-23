"""PropertyTypes for AWS::MSK::ServerlessCluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ClientAuthentication(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sasl": "Sasl",
    }

    sasl: Optional[Sasl] = None


@dataclass
class Iam(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Sasl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iam": "Iam",
    }

    iam: Optional[Iam] = None


@dataclass
class VpcConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "security_groups": "SecurityGroups",
        "subnet_ids": "SubnetIds",
    }

    security_groups: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None

