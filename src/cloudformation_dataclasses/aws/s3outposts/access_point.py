"""PropertyTypes for AWS::S3Outposts::AccessPoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class VpcConfiguration(PropertyType):
    VPC_ID = "VpcId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_id": "VpcId",
    }

    vpc_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

