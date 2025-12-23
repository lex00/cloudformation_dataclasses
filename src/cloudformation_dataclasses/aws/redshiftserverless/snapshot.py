"""PropertyTypes for AWS::RedshiftServerless::Snapshot."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Snapshot(PropertyType):
    STATUS = "Status"
    NAMESPACE_NAME = "NamespaceName"
    ADMIN_USERNAME = "AdminUsername"
    SNAPSHOT_CREATE_TIME = "SnapshotCreateTime"
    NAMESPACE_ARN = "NamespaceArn"
    KMS_KEY_ID = "KmsKeyId"
    SNAPSHOT_ARN = "SnapshotArn"
    OWNER_ACCOUNT = "OwnerAccount"
    RETENTION_PERIOD = "RetentionPeriod"
    SNAPSHOT_NAME = "SnapshotName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "namespace_name": "NamespaceName",
        "admin_username": "AdminUsername",
        "snapshot_create_time": "SnapshotCreateTime",
        "namespace_arn": "NamespaceArn",
        "kms_key_id": "KmsKeyId",
        "snapshot_arn": "SnapshotArn",
        "owner_account": "OwnerAccount",
        "retention_period": "RetentionPeriod",
        "snapshot_name": "SnapshotName",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespace_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    admin_username: Optional[Union[str, Ref, GetAtt, Sub]] = None
    snapshot_create_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespace_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    snapshot_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    owner_account: Optional[Union[str, Ref, GetAtt, Sub]] = None
    retention_period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    snapshot_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

