"""PropertyTypes for AWS::DataSync::LocationAzureBlob."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AzureBlobSasConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "azure_blob_sas_token": "AzureBlobSasToken",
    }

    azure_blob_sas_token: Optional[Union[str, Ref, GetAtt, Sub]] = None


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

