"""PropertyTypes for AWS::ElastiCache::ServerlessCache."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AZMode:
    """AZMode enum values."""

    SINGLE_AZ = "single-az"
    CROSS_AZ = "cross-az"


class AuthTokenUpdateStatus:
    """AuthTokenUpdateStatus enum values."""

    SETTING = "SETTING"
    ROTATING = "ROTATING"


class AuthTokenUpdateStrategyType:
    """AuthTokenUpdateStrategyType enum values."""

    SET = "SET"
    ROTATE = "ROTATE"
    DELETE = "DELETE"


class AuthenticationType:
    """AuthenticationType enum values."""

    PASSWORD = "password"
    NO_PASSWORD = "no-password"
    IAM = "iam"


class AutomaticFailoverStatus:
    """AutomaticFailoverStatus enum values."""

    ENABLED = "enabled"
    DISABLED = "disabled"
    ENABLING = "enabling"
    DISABLING = "disabling"


class ChangeType:
    """ChangeType enum values."""

    IMMEDIATE = "immediate"
    REQUIRES_REBOOT = "requires-reboot"


class ClusterMode:
    """ClusterMode enum values."""

    ENABLED = "enabled"
    DISABLED = "disabled"
    COMPATIBLE = "compatible"


class DataStorageUnit:
    """DataStorageUnit enum values."""

    GB = "GB"


class DataTieringStatus:
    """DataTieringStatus enum values."""

    ENABLED = "enabled"
    DISABLED = "disabled"


class DestinationType:
    """DestinationType enum values."""

    CLOUDWATCH_LOGS = "cloudwatch-logs"
    KINESIS_FIREHOSE = "kinesis-firehose"


class InputAuthenticationType:
    """InputAuthenticationType enum values."""

    PASSWORD = "password"
    NO_PASSWORD_REQUIRED = "no-password-required"
    IAM = "iam"


class IpDiscovery:
    """IpDiscovery enum values."""

    IPV4 = "ipv4"
    IPV6 = "ipv6"


class LogDeliveryConfigurationStatus:
    """LogDeliveryConfigurationStatus enum values."""

    ACTIVE = "active"
    ENABLING = "enabling"
    MODIFYING = "modifying"
    DISABLING = "disabling"
    ERROR = "error"


class LogFormat:
    """LogFormat enum values."""

    TEXT = "text"
    JSON = "json"


class LogType:
    """LogType enum values."""

    SLOW_LOG = "slow-log"
    ENGINE_LOG = "engine-log"


class MultiAZStatus:
    """MultiAZStatus enum values."""

    ENABLED = "enabled"
    DISABLED = "disabled"


class NetworkType:
    """NetworkType enum values."""

    IPV4 = "ipv4"
    IPV6 = "ipv6"
    DUAL_STACK = "dual_stack"


class NodeUpdateInitiatedBy:
    """NodeUpdateInitiatedBy enum values."""

    SYSTEM = "system"
    CUSTOMER = "customer"


class NodeUpdateStatus:
    """NodeUpdateStatus enum values."""

    NOT_APPLIED = "not-applied"
    WAITING_TO_START = "waiting-to-start"
    IN_PROGRESS = "in-progress"
    STOPPING = "stopping"
    STOPPED = "stopped"
    COMPLETE = "complete"


class OutpostMode:
    """OutpostMode enum values."""

    SINGLE_OUTPOST = "single-outpost"
    CROSS_OUTPOST = "cross-outpost"


class PendingAutomaticFailoverStatus:
    """PendingAutomaticFailoverStatus enum values."""

    ENABLED = "enabled"
    DISABLED = "disabled"


class ServiceUpdateSeverity:
    """ServiceUpdateSeverity enum values."""

    CRITICAL = "critical"
    IMPORTANT = "important"
    MEDIUM = "medium"
    LOW = "low"


class ServiceUpdateStatus:
    """ServiceUpdateStatus enum values."""

    AVAILABLE = "available"
    CANCELLED = "cancelled"
    EXPIRED = "expired"


class ServiceUpdateType:
    """ServiceUpdateType enum values."""

    SECURITY_UPDATE = "security-update"


class SlaMet:
    """SlaMet enum values."""

    YES = "yes"
    NO = "no"
    N_A = "n/a"


class SourceType:
    """SourceType enum values."""

    CACHE_CLUSTER = "cache-cluster"
    CACHE_PARAMETER_GROUP = "cache-parameter-group"
    CACHE_SECURITY_GROUP = "cache-security-group"
    CACHE_SUBNET_GROUP = "cache-subnet-group"
    REPLICATION_GROUP = "replication-group"
    SERVERLESS_CACHE = "serverless-cache"
    SERVERLESS_CACHE_SNAPSHOT = "serverless-cache-snapshot"
    USER = "user"
    USER_GROUP = "user-group"


class TransitEncryptionMode:
    """TransitEncryptionMode enum values."""

    PREFERRED = "preferred"
    REQUIRED = "required"


class UpdateActionStatus:
    """UpdateActionStatus enum values."""

    NOT_APPLIED = "not-applied"
    WAITING_TO_START = "waiting-to-start"
    IN_PROGRESS = "in-progress"
    STOPPING = "stopping"
    STOPPED = "stopped"
    COMPLETE = "complete"
    SCHEDULING = "scheduling"
    SCHEDULED = "scheduled"
    NOT_APPLICABLE = "not-applicable"


@dataclass
class CacheUsageLimits(PropertyType):
    DATA_STORAGE = "DataStorage"
    ECPU_PER_SECOND = "ECPUPerSecond"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_storage": "DataStorage",
        "ecpu_per_second": "ECPUPerSecond",
    }

    data_storage: Optional[DataStorage] = None
    ecpu_per_second: Optional[ECPUPerSecond] = None


@dataclass
class DataStorage(PropertyType):
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "minimum": "Minimum",
        "maximum": "Maximum",
        "unit": "Unit",
    }

    minimum: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, DataStorageUnit, Ref, GetAtt, Sub]] = None


@dataclass
class ECPUPerSecond(PropertyType):
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"

    _property_mappings: ClassVar[dict[str, str]] = {
        "minimum": "Minimum",
        "maximum": "Maximum",
    }

    minimum: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Endpoint(PropertyType):
    ADDRESS = "Address"
    PORT = "Port"

    _property_mappings: ClassVar[dict[str, str]] = {
        "address": "Address",
        "port": "Port",
    }

    address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[str, Ref, GetAtt, Sub]] = None

