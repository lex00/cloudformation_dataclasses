"""PropertyTypes for AWS::IAM::User."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class LoginProfile(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "password_reset_required": "PasswordResetRequired",
        "password": "Password",
    }

    password_reset_required: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    password: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Policy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "policy_name": "PolicyName",
        "policy_document": "PolicyDocument",
    }

    policy_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    policy_document: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None

