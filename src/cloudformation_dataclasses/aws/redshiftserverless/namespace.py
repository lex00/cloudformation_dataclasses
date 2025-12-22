"""PropertyTypes for AWS::RedshiftServerless::Namespace."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class LakehouseIdcRegistration:
    """LakehouseIdcRegistration enum values."""

    ASSOCIATE = "Associate"
    DISASSOCIATE = "Disassociate"


class LakehouseRegistration:
    """LakehouseRegistration enum values."""

    REGISTER = "Register"
    DEREGISTER = "Deregister"


class LogExport:
    """LogExport enum values."""

    USERACTIVITYLOG = "useractivitylog"
    USERLOG = "userlog"
    CONNECTIONLOG = "connectionlog"


class ManagedWorkgroupStatus:
    """ManagedWorkgroupStatus enum values."""

    CREATING = "CREATING"
    DELETING = "DELETING"
    MODIFYING = "MODIFYING"
    AVAILABLE = "AVAILABLE"
    NOT_AVAILABLE = "NOT_AVAILABLE"


class NamespaceStatus:
    """NamespaceStatus enum values."""

    AVAILABLE = "AVAILABLE"
    MODIFYING = "MODIFYING"
    DELETING = "DELETING"


class OfferingType:
    """OfferingType enum values."""

    ALL_UPFRONT = "ALL_UPFRONT"
    NO_UPFRONT = "NO_UPFRONT"


class PerformanceTargetStatus:
    """PerformanceTargetStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class SnapshotStatus:
    """SnapshotStatus enum values."""

    AVAILABLE = "AVAILABLE"
    CREATING = "CREATING"
    DELETED = "DELETED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    COPYING = "COPYING"


class State:
    """State enum values."""

    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"


class UsageLimitBreachAction:
    """UsageLimitBreachAction enum values."""

    LOG = "log"
    EMIT_METRIC = "emit-metric"
    DEACTIVATE = "deactivate"


class UsageLimitPeriod:
    """UsageLimitPeriod enum values."""

    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"


class UsageLimitUsageType:
    """UsageLimitUsageType enum values."""

    SERVERLESS_COMPUTE = "serverless-compute"
    CROSS_REGION_DATASHARING = "cross-region-datasharing"


class WorkgroupStatus:
    """WorkgroupStatus enum values."""

    CREATING = "CREATING"
    AVAILABLE = "AVAILABLE"
    MODIFYING = "MODIFYING"
    DELETING = "DELETING"


@dataclass
class Namespace(PropertyType):
    STATUS = "Status"
    CREATION_DATE = "CreationDate"
    IAM_ROLES = "IamRoles"
    KMS_KEY_ID = "KmsKeyId"
    ADMIN_PASSWORD_SECRET_KMS_KEY_ID = "AdminPasswordSecretKmsKeyId"
    DEFAULT_IAM_ROLE_ARN = "DefaultIamRoleArn"
    ADMIN_PASSWORD_SECRET_ARN = "AdminPasswordSecretArn"
    NAMESPACE_NAME = "NamespaceName"
    ADMIN_USERNAME = "AdminUsername"
    NAMESPACE_ARN = "NamespaceArn"
    DB_NAME = "DbName"
    NAMESPACE_ID = "NamespaceId"
    LOG_EXPORTS = "LogExports"

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
    SNAPSHOT_RETENTION_PERIOD = "SnapshotRetentionPeriod"
    DESTINATION_KMS_KEY_ID = "DestinationKmsKeyId"
    DESTINATION_REGION = "DestinationRegion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "snapshot_retention_period": "SnapshotRetentionPeriod",
        "destination_kms_key_id": "DestinationKmsKeyId",
        "destination_region": "DestinationRegion",
    }

    snapshot_retention_period: Optional[Union[int, Ref, GetAtt, Sub]] = None
    destination_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_region: Optional[Union[str, Ref, GetAtt, Sub]] = None

