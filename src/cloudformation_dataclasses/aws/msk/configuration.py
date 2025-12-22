"""PropertyTypes for AWS::MSK::Configuration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class BrokerAZDistribution:
    """BrokerAZDistribution enum values."""

    DEFAULT = "DEFAULT"


class ClientBroker:
    """ClientBroker enum values."""

    TLS = "TLS"
    TLS_PLAINTEXT = "TLS_PLAINTEXT"
    PLAINTEXT = "PLAINTEXT"


class ClusterState:
    """ClusterState enum values."""

    ACTIVE = "ACTIVE"
    CREATING = "CREATING"
    DELETING = "DELETING"
    FAILED = "FAILED"
    HEALING = "HEALING"
    MAINTENANCE = "MAINTENANCE"
    REBOOTING_BROKER = "REBOOTING_BROKER"
    UPDATING = "UPDATING"


class ClusterType:
    """ClusterType enum values."""

    PROVISIONED = "PROVISIONED"
    SERVERLESS = "SERVERLESS"


class ConfigurationState:
    """ConfigurationState enum values."""

    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"


class CustomerActionStatus:
    """CustomerActionStatus enum values."""

    CRITICAL_ACTION_REQUIRED = "CRITICAL_ACTION_REQUIRED"
    ACTION_RECOMMENDED = "ACTION_RECOMMENDED"
    NONE = "NONE"


class EnhancedMonitoring:
    """EnhancedMonitoring enum values."""

    DEFAULT = "DEFAULT"
    PER_BROKER = "PER_BROKER"
    PER_TOPIC_PER_BROKER = "PER_TOPIC_PER_BROKER"
    PER_TOPIC_PER_PARTITION = "PER_TOPIC_PER_PARTITION"


class KafkaVersionStatus:
    """KafkaVersionStatus enum values."""

    ACTIVE = "ACTIVE"
    DEPRECATED = "DEPRECATED"


class NodeType:
    """NodeType enum values."""

    BROKER = "BROKER"


class RebalancingStatus:
    """RebalancingStatus enum values."""

    PAUSED = "PAUSED"
    ACTIVE = "ACTIVE"


class ReplicationStartingPositionType:
    """ReplicationStartingPositionType enum values."""

    LATEST = "LATEST"
    EARLIEST = "EARLIEST"


class ReplicationTopicNameConfigurationType:
    """ReplicationTopicNameConfigurationType enum values."""

    PREFIXED_WITH_SOURCE_CLUSTER_ALIAS = "PREFIXED_WITH_SOURCE_CLUSTER_ALIAS"
    IDENTICAL = "IDENTICAL"


class ReplicatorState:
    """ReplicatorState enum values."""

    RUNNING = "RUNNING"
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    FAILED = "FAILED"


class StorageMode:
    """StorageMode enum values."""

    LOCAL = "LOCAL"
    TIERED = "TIERED"


class TargetCompressionType:
    """TargetCompressionType enum values."""

    NONE = "NONE"
    GZIP = "GZIP"
    SNAPPY = "SNAPPY"
    LZ4 = "LZ4"
    ZSTD = "ZSTD"


class TopicState:
    """TopicState enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"


class UserIdentityType:
    """UserIdentityType enum values."""

    AWSACCOUNT = "AWSACCOUNT"
    AWSSERVICE = "AWSSERVICE"


class VpcConnectionState:
    """VpcConnectionState enum values."""

    CREATING = "CREATING"
    AVAILABLE = "AVAILABLE"
    INACTIVE = "INACTIVE"
    DEACTIVATING = "DEACTIVATING"
    DELETING = "DELETING"
    FAILED = "FAILED"
    REJECTED = "REJECTED"
    REJECTING = "REJECTING"


@dataclass
class LatestRevision(PropertyType):
    DESCRIPTION = "Description"
    REVISION = "Revision"
    CREATION_TIME = "CreationTime"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "revision": "Revision",
        "creation_time": "CreationTime",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    revision: Optional[Union[int, Ref, GetAtt, Sub]] = None
    creation_time: Optional[Union[str, Ref, GetAtt, Sub]] = None

