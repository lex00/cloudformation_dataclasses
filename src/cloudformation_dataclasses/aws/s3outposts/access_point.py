"""PropertyTypes for AWS::S3Outposts::AccessPoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class EndpointAccessType:
    """EndpointAccessType enum values."""

    PRIVATE = "Private"
    CUSTOMEROWNEDIP = "CustomerOwnedIp"


class EndpointStatus:
    """EndpointStatus enum values."""

    PENDING = "Pending"
    AVAILABLE = "Available"
    DELETING = "Deleting"
    CREATE_FAILED = "Create_Failed"
    DELETE_FAILED = "Delete_Failed"


@dataclass
class VpcConfiguration(PropertyType):
    VPC_ID = "VpcId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_id": "VpcId",
    }

    vpc_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

