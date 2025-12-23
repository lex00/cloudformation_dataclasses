"""PropertyTypes for AWS::RDS::DBSecurityGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Ingress(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cidrip": "CIDRIP",
        "ec2_security_group_id": "EC2SecurityGroupId",
        "ec2_security_group_name": "EC2SecurityGroupName",
        "ec2_security_group_owner_id": "EC2SecurityGroupOwnerId",
    }

    cidrip: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ec2_security_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ec2_security_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ec2_security_group_owner_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

