"""PropertyTypes for AWS::RedshiftServerless::Namespace."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Namespace(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "creation_date": "CreationDate",
        "iam_roles": "IamRoles",
        "kms_key_id": "KmsKeyId",
        "admin_password_secret_kms_key_id": "AdminPasswordSecretKmsKeyId",
        "default_iam_role_arn": "DefaultIamRoleArn",
        "admin_password_secret_arn": "AdminPasswordSecretArn",
        "namespace_name": "NamespaceName",
        "admin_username": "AdminUsername",
        "namespace_arn": "NamespaceArn",
        "db_name": "DbName",
        "namespace_id": "NamespaceId",
        "log_exports": "LogExports",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    creation_date: Optional[Union[str, Ref, GetAtt, Sub]] = None
    iam_roles: Optional[Union[list[str], Ref]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    admin_password_secret_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default_iam_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    admin_password_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespace_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    admin_username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespace_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    db_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespace_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_exports: Optional[Union[list[str], Ref]] = None


@dataclass
class SnapshotCopyConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "snapshot_retention_period": "SnapshotRetentionPeriod",
        "destination_kms_key_id": "DestinationKmsKeyId",
        "destination_region": "DestinationRegion",
    }

    snapshot_retention_period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    destination_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_region: Optional[Union[str, Ref, GetAtt, Sub]] = None

