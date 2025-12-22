"""PropertyTypes for AWS::ElastiCache::ReplicationGroup."""

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
class CloudWatchLogsDestinationDetails(PropertyType):
    LOG_GROUP = "LogGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group": "LogGroup",
    }

    log_group: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DestinationDetails(PropertyType):
    CLOUD_WATCH_LOGS_DETAILS = "CloudWatchLogsDetails"
    KINESIS_FIREHOSE_DETAILS = "KinesisFirehoseDetails"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_logs_details": "CloudWatchLogsDetails",
        "kinesis_firehose_details": "KinesisFirehoseDetails",
    }

    cloud_watch_logs_details: Optional[CloudWatchLogsDestinationDetails] = None
    kinesis_firehose_details: Optional[KinesisFirehoseDestinationDetails] = None


@dataclass
class KinesisFirehoseDestinationDetails(PropertyType):
    DELIVERY_STREAM = "DeliveryStream"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delivery_stream": "DeliveryStream",
    }

    delivery_stream: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LogDeliveryConfigurationRequest(PropertyType):
    DESTINATION_DETAILS = "DestinationDetails"
    DESTINATION_TYPE = "DestinationType"
    LOG_FORMAT = "LogFormat"
    LOG_TYPE = "LogType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination_details": "DestinationDetails",
        "destination_type": "DestinationType",
        "log_format": "LogFormat",
        "log_type": "LogType",
    }

    destination_details: Optional[DestinationDetails] = None
    destination_type: Optional[Union[str, DestinationType, Ref, GetAtt, Sub]] = None
    log_format: Optional[Union[str, LogFormat, Ref, GetAtt, Sub]] = None
    log_type: Optional[Union[str, LogType, Ref, GetAtt, Sub]] = None


@dataclass
class NodeGroupConfiguration(PropertyType):
    NODE_GROUP_ID = "NodeGroupId"
    PRIMARY_AVAILABILITY_ZONE = "PrimaryAvailabilityZone"
    REPLICA_AVAILABILITY_ZONES = "ReplicaAvailabilityZones"
    REPLICA_COUNT = "ReplicaCount"
    SLOTS = "Slots"

    _property_mappings: ClassVar[dict[str, str]] = {
        "node_group_id": "NodeGroupId",
        "primary_availability_zone": "PrimaryAvailabilityZone",
        "replica_availability_zones": "ReplicaAvailabilityZones",
        "replica_count": "ReplicaCount",
        "slots": "Slots",
    }

    node_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    primary_availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    replica_availability_zones: Optional[Union[list[str], Ref]] = None
    replica_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    slots: Optional[Union[str, Ref, GetAtt, Sub]] = None

