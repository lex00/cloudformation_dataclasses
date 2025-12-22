"""PropertyTypes for AWS::MSK::ServerlessCluster."""

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
class ClientAuthentication(PropertyType):
    SASL = "Sasl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sasl": "Sasl",
    }

    sasl: Optional[Sasl] = None


@dataclass
class Iam(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Sasl(PropertyType):
    IAM = "Iam"

    _property_mappings: ClassVar[dict[str, str]] = {
        "iam": "Iam",
    }

    iam: Optional[Iam] = None


@dataclass
class VpcConfig(PropertyType):
    SECURITY_GROUPS = "SecurityGroups"
    SUBNET_IDS = "SubnetIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "security_groups": "SecurityGroups",
        "subnet_ids": "SubnetIds",
    }

    security_groups: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None

