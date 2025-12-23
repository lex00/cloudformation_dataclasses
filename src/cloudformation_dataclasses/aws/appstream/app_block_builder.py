"""PropertyTypes for AWS::AppStream::AppBlockBuilder."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccessEndpoint(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint_type": "EndpointType",
        "vpce_id": "VpceId",
    }

    endpoint_type: Optional[Union[str, AccessEndpointType, Ref, GetAtt, Sub]] = None
    vpce_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "security_group_ids": "SecurityGroupIds",
        "subnet_ids": "SubnetIds",
    }

    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None

