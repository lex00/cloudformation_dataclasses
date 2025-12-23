"""PropertyTypes for AWS::IoT::TopicRuleDestination."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class HttpUrlDestinationSummary(PropertyType):
    CONFIRMATION_URL = "ConfirmationUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "confirmation_url": "ConfirmationUrl",
    }

    confirmation_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class VpcDestinationProperties(PropertyType):
    SECURITY_GROUPS = "SecurityGroups"
    VPC_ID = "VpcId"
    SUBNET_IDS = "SubnetIds"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "security_groups": "SecurityGroups",
        "vpc_id": "VpcId",
        "subnet_ids": "SubnetIds",
        "role_arn": "RoleArn",
    }

    security_groups: Optional[Union[list[str], Ref]] = None
    vpc_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

