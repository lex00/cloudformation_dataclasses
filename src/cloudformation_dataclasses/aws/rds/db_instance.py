"""PropertyTypes for AWS::RDS::DBInstance."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ActivityStreamMode:
    """ActivityStreamMode enum values."""

    SYNC = "sync"
    ASYNC = "async"


class ActivityStreamPolicyStatus:
    """ActivityStreamPolicyStatus enum values."""

    LOCKED = "locked"
    UNLOCKED = "unlocked"
    LOCKING_POLICY = "locking-policy"
    UNLOCKING_POLICY = "unlocking-policy"


class ActivityStreamStatus:
    """ActivityStreamStatus enum values."""

    STOPPED = "stopped"
    STARTING = "starting"
    STARTED = "started"
    STOPPING = "stopping"


class ApplyMethod:
    """ApplyMethod enum values."""

    IMMEDIATE = "immediate"
    PENDING_REBOOT = "pending-reboot"


class AuditPolicyState:
    """AuditPolicyState enum values."""

    LOCKED = "locked"
    UNLOCKED = "unlocked"


class AuthScheme:
    """AuthScheme enum values."""

    SECRETS = "SECRETS"


class AutomationMode:
    """AutomationMode enum values."""

    FULL = "full"
    ALL_PAUSED = "all-paused"


class ClientPasswordAuthType:
    """ClientPasswordAuthType enum values."""

    MYSQL_NATIVE_PASSWORD = "MYSQL_NATIVE_PASSWORD"
    MYSQL_CACHING_SHA2_PASSWORD = "MYSQL_CACHING_SHA2_PASSWORD"
    POSTGRES_SCRAM_SHA_256 = "POSTGRES_SCRAM_SHA_256"
    POSTGRES_MD5 = "POSTGRES_MD5"
    SQL_SERVER_AUTHENTICATION = "SQL_SERVER_AUTHENTICATION"


class ClusterScalabilityType:
    """ClusterScalabilityType enum values."""

    STANDARD = "standard"
    LIMITLESS = "limitless"


class CustomEngineVersionStatus:
    """CustomEngineVersionStatus enum values."""

    AVAILABLE = "available"
    INACTIVE = "inactive"
    INACTIVE_EXCEPT_RESTORE = "inactive-except-restore"


class DBProxyEndpointStatus:
    """DBProxyEndpointStatus enum values."""

    AVAILABLE = "available"
    MODIFYING = "modifying"
    INCOMPATIBLE_NETWORK = "incompatible-network"
    INSUFFICIENT_RESOURCE_LIMITS = "insufficient-resource-limits"
    CREATING = "creating"
    DELETING = "deleting"


class DBProxyEndpointTargetRole:
    """DBProxyEndpointTargetRole enum values."""

    READ_WRITE = "READ_WRITE"
    READ_ONLY = "READ_ONLY"


class DBProxyStatus:
    """DBProxyStatus enum values."""

    AVAILABLE = "available"
    MODIFYING = "modifying"
    INCOMPATIBLE_NETWORK = "incompatible-network"
    INSUFFICIENT_RESOURCE_LIMITS = "insufficient-resource-limits"
    CREATING = "creating"
    DELETING = "deleting"
    SUSPENDED = "suspended"
    SUSPENDING = "suspending"
    REACTIVATING = "reactivating"


class DatabaseInsightsMode:
    """DatabaseInsightsMode enum values."""

    STANDARD = "standard"
    ADVANCED = "advanced"


class DefaultAuthScheme:
    """DefaultAuthScheme enum values."""

    IAM_AUTH = "IAM_AUTH"
    NONE = "NONE"


class EndpointNetworkType:
    """EndpointNetworkType enum values."""

    IPV4 = "IPV4"
    IPV6 = "IPV6"
    DUAL = "DUAL"


class EngineFamily:
    """EngineFamily enum values."""

    MYSQL = "MYSQL"
    POSTGRESQL = "POSTGRESQL"
    SQLSERVER = "SQLSERVER"


class ExportSourceType:
    """ExportSourceType enum values."""

    SNAPSHOT = "SNAPSHOT"
    CLUSTER = "CLUSTER"


class FailoverStatus:
    """FailoverStatus enum values."""

    PENDING = "pending"
    FAILING_OVER = "failing-over"
    CANCELLING = "cancelling"


class GlobalClusterMemberSynchronizationStatus:
    """GlobalClusterMemberSynchronizationStatus enum values."""

    CONNECTED = "connected"
    PENDING_RESYNC = "pending-resync"


class IAMAuthMode:
    """IAMAuthMode enum values."""

    DISABLED = "DISABLED"
    REQUIRED = "REQUIRED"
    ENABLED = "ENABLED"


class IntegrationStatus:
    """IntegrationStatus enum values."""

    CREATING = "creating"
    ACTIVE = "active"
    MODIFYING = "modifying"
    FAILED = "failed"
    DELETING = "deleting"
    SYNCING = "syncing"
    NEEDS_ATTENTION = "needs_attention"


class LifecycleSupportName:
    """LifecycleSupportName enum values."""

    OPEN_SOURCE_RDS_STANDARD_SUPPORT = "open-source-rds-standard-support"
    OPEN_SOURCE_RDS_EXTENDED_SUPPORT = "open-source-rds-extended-support"


class LimitlessDatabaseStatus:
    """LimitlessDatabaseStatus enum values."""

    ACTIVE = "active"
    NOT_IN_USE = "not-in-use"
    ENABLED = "enabled"
    DISABLED = "disabled"
    ENABLING = "enabling"
    DISABLING = "disabling"
    MODIFYING_MAX_CAPACITY = "modifying-max-capacity"
    ERROR = "error"


class LocalWriteForwardingStatus:
    """LocalWriteForwardingStatus enum values."""

    ENABLED = "enabled"
    DISABLED = "disabled"
    ENABLING = "enabling"
    DISABLING = "disabling"
    REQUESTED = "requested"


class MasterUserAuthenticationType:
    """MasterUserAuthenticationType enum values."""

    PASSWORD = "password"
    IAM_DB_AUTH = "iam-db-auth"


class ReplicaMode:
    """ReplicaMode enum values."""

    OPEN_READ_ONLY = "open-read-only"
    MOUNTED = "mounted"


class SourceType:
    """SourceType enum values."""

    DB_INSTANCE = "db-instance"
    DB_PARAMETER_GROUP = "db-parameter-group"
    DB_SECURITY_GROUP = "db-security-group"
    DB_SNAPSHOT = "db-snapshot"
    DB_CLUSTER = "db-cluster"
    DB_CLUSTER_SNAPSHOT = "db-cluster-snapshot"
    CUSTOM_ENGINE_VERSION = "custom-engine-version"
    DB_PROXY = "db-proxy"
    BLUE_GREEN_DEPLOYMENT = "blue-green-deployment"
    DB_SHARD_GROUP = "db-shard-group"
    ZERO_ETL = "zero-etl"


class TargetConnectionNetworkType:
    """TargetConnectionNetworkType enum values."""

    IPV4 = "IPV4"
    IPV6 = "IPV6"


class TargetHealthReason:
    """TargetHealthReason enum values."""

    UNREACHABLE = "UNREACHABLE"
    CONNECTION_FAILED = "CONNECTION_FAILED"
    AUTH_FAILURE = "AUTH_FAILURE"
    PENDING_PROXY_CAPACITY = "PENDING_PROXY_CAPACITY"
    INVALID_REPLICATION_STATE = "INVALID_REPLICATION_STATE"
    PROMOTED = "PROMOTED"


class TargetRole:
    """TargetRole enum values."""

    READ_WRITE = "READ_WRITE"
    READ_ONLY = "READ_ONLY"
    UNKNOWN = "UNKNOWN"


class TargetState:
    """TargetState enum values."""

    REGISTERING = "REGISTERING"
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"
    UNUSED = "UNUSED"


class TargetType:
    """TargetType enum values."""

    RDS_INSTANCE = "RDS_INSTANCE"
    RDS_SERVERLESS_ENDPOINT = "RDS_SERVERLESS_ENDPOINT"
    TRACKED_CLUSTER = "TRACKED_CLUSTER"


class UpgradeRolloutOrder:
    """UpgradeRolloutOrder enum values."""

    FIRST = "first"
    SECOND = "second"
    LAST = "last"


class WriteForwardingStatus:
    """WriteForwardingStatus enum values."""

    ENABLED = "enabled"
    DISABLED = "disabled"
    ENABLING = "enabling"
    DISABLING = "disabling"
    UNKNOWN = "unknown"


@dataclass
class CertificateDetails(PropertyType):
    VALID_TILL = "ValidTill"
    CA_IDENTIFIER = "CAIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "valid_till": "ValidTill",
        "ca_identifier": "CAIdentifier",
    }

    valid_till: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ca_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DBInstanceRole(PropertyType):
    ROLE_ARN = "RoleArn"
    FEATURE_NAME = "FeatureName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleArn",
        "feature_name": "FeatureName",
    }

    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    feature_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DBInstanceStatusInfo(PropertyType):
    STATUS = "Status"
    MESSAGE = "Message"
    STATUS_TYPE = "StatusType"
    NORMAL = "Normal"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "message": "Message",
        "status_type": "StatusType",
        "normal": "Normal",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    status_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    normal: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Endpoint(PropertyType):
    ADDRESS = "Address"
    PORT = "Port"
    HOSTED_ZONE_ID = "HostedZoneId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "address": "Address",
        "port": "Port",
        "hosted_zone_id": "HostedZoneId",
    }

    address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hosted_zone_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MasterUserSecret(PropertyType):
    SECRET_ARN = "SecretArn"
    KMS_KEY_ID = "KmsKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "kms_key_id": "KmsKeyId",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProcessorFeature(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

