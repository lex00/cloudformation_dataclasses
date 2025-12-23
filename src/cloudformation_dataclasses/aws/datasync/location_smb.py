"""PropertyTypes for AWS::DataSync::LocationSMB."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CmkSecretConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "kms_key_arn": "KmsKeyArn",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomSecretConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "secret_access_role_arn": "SecretAccessRoleArn",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secret_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ManagedSecretConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MountOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "version": "Version",
    }

    version: Optional[Union[str, Ref, GetAtt, Sub]] = None

