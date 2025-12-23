"""PropertyTypes for AWS::DirectoryService::MicrosoftAD."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class VpcSettings(PropertyType):
    SUBNET_IDS = "SubnetIds"
    VPC_ID = "VpcId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subnet_ids": "SubnetIds",
        "vpc_id": "VpcId",
    }

    subnet_ids: Optional[Union[list[str], Ref]] = None
    vpc_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

