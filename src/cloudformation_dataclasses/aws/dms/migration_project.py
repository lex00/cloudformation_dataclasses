"""PropertyTypes for AWS::DMS::MigrationProject."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DataProviderDescriptor(PropertyType):
    DATA_PROVIDER_NAME = "DataProviderName"
    DATA_PROVIDER_ARN = "DataProviderArn"
    SECRETS_MANAGER_SECRET_ID = "SecretsManagerSecretId"
    SECRETS_MANAGER_ACCESS_ROLE_ARN = "SecretsManagerAccessRoleArn"
    DATA_PROVIDER_IDENTIFIER = "DataProviderIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_provider_name": "DataProviderName",
        "data_provider_arn": "DataProviderArn",
        "secrets_manager_secret_id": "SecretsManagerSecretId",
        "secrets_manager_access_role_arn": "SecretsManagerAccessRoleArn",
        "data_provider_identifier": "DataProviderIdentifier",
    }

    data_provider_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_provider_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_manager_secret_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    secrets_manager_access_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_provider_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SchemaConversionApplicationAttributes(PropertyType):
    S3_BUCKET_PATH = "S3BucketPath"
    S3_BUCKET_ROLE_ARN = "S3BucketRoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_bucket_path": "S3BucketPath",
        "s3_bucket_role_arn": "S3BucketRoleArn",
    }

    s3_bucket_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_bucket_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

