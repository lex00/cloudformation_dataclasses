"""PropertyTypes for AWS::RDS::DBProxy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AuthFormat(PropertyType):
    SECRET_ARN = "SecretArn"
    DESCRIPTION = "Description"
    IAM_AUTH = "IAMAuth"
    CLIENT_PASSWORD_AUTH_TYPE = "ClientPasswordAuthType"
    AUTH_SCHEME = "AuthScheme"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "description": "Description",
        "iam_auth": "IAMAuth",
        "client_password_auth_type": "ClientPasswordAuthType",
        "auth_scheme": "AuthScheme",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    iam_auth: Optional[Union[str, Ref, GetAtt, Sub]] = None
    client_password_auth_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    auth_scheme: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TagFormat(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

