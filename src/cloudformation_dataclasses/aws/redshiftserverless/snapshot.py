"""PropertyTypes for AWS::RedshiftServerless::Snapshot."""

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

