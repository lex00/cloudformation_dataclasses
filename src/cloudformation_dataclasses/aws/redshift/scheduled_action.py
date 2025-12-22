"""PropertyTypes for AWS::Redshift::ScheduledAction."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ActionType:
    """ActionType enum values."""

    RESTORE_CLUSTER = "restore-cluster"
    RECOMMEND_NODE_CONFIG = "recommend-node-config"
    RESIZE_CLUSTER = "resize-cluster"


class ApplicationType:
    """ApplicationType enum values."""

    NONE = "None"
    LAKEHOUSE = "Lakehouse"


class AquaConfigurationStatus:
    """AquaConfigurationStatus enum values."""

    ENABLED = "enabled"
    DISABLED = "disabled"
    AUTO = "auto"


class AquaStatus:
    """AquaStatus enum values."""

    ENABLED = "enabled"
    DISABLED = "disabled"
    APPLYING = "applying"


class AuthorizationStatus:
    """AuthorizationStatus enum values."""

    AUTHORIZED = "Authorized"
    REVOKING = "Revoking"


class DataShareStatus:
    """DataShareStatus enum values."""

    ACTIVE = "ACTIVE"
    PENDING_AUTHORIZATION = "PENDING_AUTHORIZATION"
    AUTHORIZED = "AUTHORIZED"
    DEAUTHORIZED = "DEAUTHORIZED"
    REJECTED = "REJECTED"
    AVAILABLE = "AVAILABLE"


class DataShareStatusForConsumer:
    """DataShareStatusForConsumer enum values."""

    ACTIVE = "ACTIVE"
    AVAILABLE = "AVAILABLE"


class DataShareStatusForProducer:
    """DataShareStatusForProducer enum values."""

    ACTIVE = "ACTIVE"
    AUTHORIZED = "AUTHORIZED"
    PENDING_AUTHORIZATION = "PENDING_AUTHORIZATION"
    DEAUTHORIZED = "DEAUTHORIZED"
    REJECTED = "REJECTED"


class DataShareType:
    """DataShareType enum values."""

    INTERNAL = "INTERNAL"


class DescribeIntegrationsFilterName:
    """DescribeIntegrationsFilterName enum values."""

    INTEGRATION_ARN = "integration-arn"
    SOURCE_ARN = "source-arn"
    SOURCE_TYPES = "source-types"
    STATUS = "status"


class ImpactRankingType:
    """ImpactRankingType enum values."""

    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class LakehouseIdcRegistration:
    """LakehouseIdcRegistration enum values."""

    ASSOCIATE = "Associate"
    DISASSOCIATE = "Disassociate"


class LakehouseRegistration:
    """LakehouseRegistration enum values."""

    REGISTER = "Register"
    DEREGISTER = "Deregister"


class LogDestinationType:
    """LogDestinationType enum values."""

    S3 = "s3"
    CLOUDWATCH = "cloudwatch"


class Mode:
    """Mode enum values."""

    STANDARD = "standard"
    HIGH_PERFORMANCE = "high-performance"


class NamespaceRegistrationStatus:
    """NamespaceRegistrationStatus enum values."""

    REGISTERING = "Registering"
    DEREGISTERING = "Deregistering"


class NodeConfigurationOptionsFilterName:
    """NodeConfigurationOptionsFilterName enum values."""

    NODETYPE = "NodeType"
    NUMBEROFNODES = "NumberOfNodes"
    ESTIMATEDDISKUTILIZATIONPERCENT = "EstimatedDiskUtilizationPercent"
    MODE = "Mode"


class OperatorType:
    """OperatorType enum values."""

    EQ = "eq"
    LT = "lt"
    GT = "gt"
    LE = "le"
    GE = "ge"
    IN = "in"
    BETWEEN = "between"


class ParameterApplyType:
    """ParameterApplyType enum values."""

    STATIC = "static"
    DYNAMIC = "dynamic"


class PartnerIntegrationStatus:
    """PartnerIntegrationStatus enum values."""

    ACTIVE = "Active"
    INACTIVE = "Inactive"
    RUNTIMEFAILURE = "RuntimeFailure"
    CONNECTIONFAILURE = "ConnectionFailure"


class RecommendedActionType:
    """RecommendedActionType enum values."""

    SQL = "SQL"
    CLI = "CLI"


class ReservedNodeExchangeActionType:
    """ReservedNodeExchangeActionType enum values."""

    RESTORE_CLUSTER = "restore-cluster"
    RESIZE_CLUSTER = "resize-cluster"


class ReservedNodeExchangeStatusType:
    """ReservedNodeExchangeStatusType enum values."""

    REQUESTED = "REQUESTED"
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    RETRYING = "RETRYING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class ReservedNodeOfferingType:
    """ReservedNodeOfferingType enum values."""

    REGULAR = "Regular"
    UPGRADABLE = "Upgradable"


class ScheduleState:
    """ScheduleState enum values."""

    MODIFYING = "MODIFYING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"


class ScheduledActionFilterName:
    """ScheduledActionFilterName enum values."""

    CLUSTER_IDENTIFIER = "cluster-identifier"
    IAM_ROLE = "iam-role"


class ScheduledActionState:
    """ScheduledActionState enum values."""

    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"


class ScheduledActionTypeValues:
    """ScheduledActionTypeValues enum values."""

    RESIZECLUSTER = "ResizeCluster"
    PAUSECLUSTER = "PauseCluster"
    RESUMECLUSTER = "ResumeCluster"


class ServiceAuthorization:
    """ServiceAuthorization enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SnapshotAttributeToSortBy:
    """SnapshotAttributeToSortBy enum values."""

    SOURCE_TYPE = "SOURCE_TYPE"
    TOTAL_SIZE = "TOTAL_SIZE"
    CREATE_TIME = "CREATE_TIME"


class SortByOrder:
    """SortByOrder enum values."""

    ASC = "ASC"
    DESC = "DESC"


class SourceType:
    """SourceType enum values."""

    CLUSTER = "cluster"
    CLUSTER_PARAMETER_GROUP = "cluster-parameter-group"
    CLUSTER_SECURITY_GROUP = "cluster-security-group"
    CLUSTER_SNAPSHOT = "cluster-snapshot"
    SCHEDULED_ACTION = "scheduled-action"


class TableRestoreStatusType:
    """TableRestoreStatusType enum values."""

    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELED = "CANCELED"


class UsageLimitBreachAction:
    """UsageLimitBreachAction enum values."""

    LOG = "log"
    EMIT_METRIC = "emit-metric"
    DISABLE = "disable"


class UsageLimitFeatureType:
    """UsageLimitFeatureType enum values."""

    SPECTRUM = "spectrum"
    CONCURRENCY_SCALING = "concurrency-scaling"
    CROSS_REGION_DATASHARING = "cross-region-datasharing"


class UsageLimitLimitType:
    """UsageLimitLimitType enum values."""

    TIME = "time"
    DATA_SCANNED = "data-scanned"


class UsageLimitPeriod:
    """UsageLimitPeriod enum values."""

    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"


class ZeroETLIntegrationStatus:
    """ZeroETLIntegrationStatus enum values."""

    CREATING = "creating"
    ACTIVE = "active"
    MODIFYING = "modifying"
    FAILED = "failed"
    DELETING = "deleting"
    SYNCING = "syncing"
    NEEDS_ATTENTION = "needs_attention"


@dataclass
class PauseClusterMessage(PropertyType):
    CLUSTER_IDENTIFIER = "ClusterIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_identifier": "ClusterIdentifier",
    }

    cluster_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResizeClusterMessage(PropertyType):
    NODE_TYPE = "NodeType"
    NUMBER_OF_NODES = "NumberOfNodes"
    CLUSTER_TYPE = "ClusterType"
    CLASSIC = "Classic"
    CLUSTER_IDENTIFIER = "ClusterIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "node_type": "NodeType",
        "number_of_nodes": "NumberOfNodes",
        "cluster_type": "ClusterType",
        "classic": "Classic",
        "cluster_identifier": "ClusterIdentifier",
    }

    node_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    number_of_nodes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    cluster_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    classic: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    cluster_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResumeClusterMessage(PropertyType):
    CLUSTER_IDENTIFIER = "ClusterIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_identifier": "ClusterIdentifier",
    }

    cluster_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScheduledActionType(PropertyType):
    PAUSE_CLUSTER = "PauseCluster"
    RESUME_CLUSTER = "ResumeCluster"
    RESIZE_CLUSTER = "ResizeCluster"

    _property_mappings: ClassVar[dict[str, str]] = {
        "pause_cluster": "PauseCluster",
        "resume_cluster": "ResumeCluster",
        "resize_cluster": "ResizeCluster",
    }

    pause_cluster: Optional[PauseClusterMessage] = None
    resume_cluster: Optional[ResumeClusterMessage] = None
    resize_cluster: Optional[ResizeClusterMessage] = None

