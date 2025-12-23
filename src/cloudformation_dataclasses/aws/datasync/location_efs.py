"""PropertyTypes for AWS::DataSync::LocationEFS."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Ec2Config(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "subnet_arn": "SubnetArn",
        "security_group_arns": "SecurityGroupArns",
    }

    subnet_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    security_group_arns: Optional[Union[list[str], Ref]] = None

