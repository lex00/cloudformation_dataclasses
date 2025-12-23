"""PropertyTypes for AWS::DataZone::UserProfile."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IamUserProfileDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SsoUserProfileDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "username": "Username",
        "first_name": "FirstName",
        "last_name": "LastName",
    }

    username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    first_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    last_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UserProfileDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iam": "Iam",
        "sso": "Sso",
    }

    iam: Optional[IamUserProfileDetails] = None
    sso: Optional[SsoUserProfileDetails] = None

