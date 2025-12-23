"""PropertyTypes for AWS::DataSync::LocationObjectStorage."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CmkSecretConfig(PropertyType):
    SECRET_ARN = "SecretArn"
    KMS_KEY_ARN = "KmsKeyArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "kms_key_arn": "KmsKeyArn",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomSecretConfig(PropertyType):
    SECRET_ARN = "SecretArn"
    SECRET_ACCESS_ROLE_ARN = "SecretAccessRoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "secret_access_role_arn": "SecretAccessRoleArn",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secret_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ManagedSecretConfig(PropertyType):
    SECRET_ARN = "SecretArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

