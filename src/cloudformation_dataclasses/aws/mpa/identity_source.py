"""PropertyTypes for AWS::MPA::IdentitySource."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IamIdentityCenter(PropertyType):
    APPROVAL_PORTAL_URL = "ApprovalPortalUrl"
    INSTANCE_ARN = "InstanceArn"
    REGION = "Region"

    _property_mappings: ClassVar[dict[str, str]] = {
        "approval_portal_url": "ApprovalPortalUrl",
        "instance_arn": "InstanceArn",
        "region": "Region",
    }

    approval_portal_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IdentitySourceParameters(PropertyType):
    IAM_IDENTITY_CENTER = "IamIdentityCenter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "iam_identity_center": "IamIdentityCenter",
    }

    iam_identity_center: Optional[IamIdentityCenter] = None

