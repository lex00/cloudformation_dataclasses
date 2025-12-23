"""PropertyTypes for AWS::IoTSiteWise::AccessPolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccessPolicyIdentity(PropertyType):
    USER = "User"
    IAM_USER = "IamUser"
    IAM_ROLE = "IamRole"

    _property_mappings: ClassVar[dict[str, str]] = {
        "user": "User",
        "iam_user": "IamUser",
        "iam_role": "IamRole",
    }

    user: Optional[User] = None
    iam_user: Optional[IamUser] = None
    iam_role: Optional[IamRole] = None


@dataclass
class AccessPolicyResource(PropertyType):
    PROJECT = "Project"
    PORTAL = "Portal"

    _property_mappings: ClassVar[dict[str, str]] = {
        "project": "Project",
        "portal": "Portal",
    }

    project: Optional[Project] = None
    portal: Optional[Portal] = None


@dataclass
class IamRole(PropertyType):
    ARN = "arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class IamUser(PropertyType):
    ARN = "arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Portal(PropertyType):
    ID = "id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "id",
    }

    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Project(PropertyType):
    ID = "id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "id",
    }

    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class User(PropertyType):
    ID = "id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "id",
    }

    id: Optional[Union[str, Ref, GetAtt, Sub]] = None

