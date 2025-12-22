"""PropertyTypes for AWS::EMR::Step."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ActionOnFailure:
    """ActionOnFailure enum values."""

    TERMINATE_JOB_FLOW = "TERMINATE_JOB_FLOW"
    TERMINATE_CLUSTER = "TERMINATE_CLUSTER"
    CANCEL_AND_WAIT = "CANCEL_AND_WAIT"
    CONTINUE = "CONTINUE"


class AdjustmentType:
    """AdjustmentType enum values."""

    CHANGE_IN_CAPACITY = "CHANGE_IN_CAPACITY"
    PERCENT_CHANGE_IN_CAPACITY = "PERCENT_CHANGE_IN_CAPACITY"
    EXACT_CAPACITY = "EXACT_CAPACITY"


class AuthMode:
    """AuthMode enum values."""

    SSO = "SSO"
    IAM = "IAM"


class AutoScalingPolicyState:
    """AutoScalingPolicyState enum values."""

    PENDING = "PENDING"
    ATTACHING = "ATTACHING"
    ATTACHED = "ATTACHED"
    DETACHING = "DETACHING"
    DETACHED = "DETACHED"
    FAILED = "FAILED"


class AutoScalingPolicyStateChangeReasonCode:
    """AutoScalingPolicyStateChangeReasonCode enum values."""

    USER_REQUEST = "USER_REQUEST"
    PROVISION_FAILURE = "PROVISION_FAILURE"
    CLEANUP_FAILURE = "CLEANUP_FAILURE"


class CancelStepsRequestStatus:
    """CancelStepsRequestStatus enum values."""

    SUBMITTED = "SUBMITTED"
    FAILED = "FAILED"


class ClusterState:
    """ClusterState enum values."""

    STARTING = "STARTING"
    BOOTSTRAPPING = "BOOTSTRAPPING"
    RUNNING = "RUNNING"
    WAITING = "WAITING"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"
    TERMINATED_WITH_ERRORS = "TERMINATED_WITH_ERRORS"


class ClusterStateChangeReasonCode:
    """ClusterStateChangeReasonCode enum values."""

    INTERNAL_ERROR = "INTERNAL_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    INSTANCE_FAILURE = "INSTANCE_FAILURE"
    INSTANCE_FLEET_TIMEOUT = "INSTANCE_FLEET_TIMEOUT"
    BOOTSTRAP_FAILURE = "BOOTSTRAP_FAILURE"
    USER_REQUEST = "USER_REQUEST"
    STEP_FAILURE = "STEP_FAILURE"
    ALL_STEPS_COMPLETED = "ALL_STEPS_COMPLETED"


class ComparisonOperator:
    """ComparisonOperator enum values."""

    GREATER_THAN_OR_EQUAL = "GREATER_THAN_OR_EQUAL"
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL = "LESS_THAN_OR_EQUAL"


class ComputeLimitsUnitType:
    """ComputeLimitsUnitType enum values."""

    INSTANCEFLEETUNITS = "InstanceFleetUnits"
    INSTANCES = "Instances"
    VCPU = "VCPU"


class ExecutionEngineType:
    """ExecutionEngineType enum values."""

    EMR = "EMR"


class IdcUserAssignment:
    """IdcUserAssignment enum values."""

    REQUIRED = "REQUIRED"
    OPTIONAL = "OPTIONAL"


class IdentityType:
    """IdentityType enum values."""

    USER = "USER"
    GROUP = "GROUP"


class InstanceCollectionType:
    """InstanceCollectionType enum values."""

    INSTANCE_FLEET = "INSTANCE_FLEET"
    INSTANCE_GROUP = "INSTANCE_GROUP"


class InstanceFleetState:
    """InstanceFleetState enum values."""

    PROVISIONING = "PROVISIONING"
    BOOTSTRAPPING = "BOOTSTRAPPING"
    RUNNING = "RUNNING"
    RESIZING = "RESIZING"
    RECONFIGURING = "RECONFIGURING"
    SUSPENDED = "SUSPENDED"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"


class InstanceFleetStateChangeReasonCode:
    """InstanceFleetStateChangeReasonCode enum values."""

    INTERNAL_ERROR = "INTERNAL_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    INSTANCE_FAILURE = "INSTANCE_FAILURE"
    CLUSTER_TERMINATED = "CLUSTER_TERMINATED"


class InstanceFleetType:
    """InstanceFleetType enum values."""

    MASTER = "MASTER"
    CORE = "CORE"
    TASK = "TASK"


class InstanceGroupState:
    """InstanceGroupState enum values."""

    PROVISIONING = "PROVISIONING"
    BOOTSTRAPPING = "BOOTSTRAPPING"
    RUNNING = "RUNNING"
    RECONFIGURING = "RECONFIGURING"
    RESIZING = "RESIZING"
    SUSPENDED = "SUSPENDED"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"
    ARRESTED = "ARRESTED"
    SHUTTING_DOWN = "SHUTTING_DOWN"
    ENDED = "ENDED"


class InstanceGroupStateChangeReasonCode:
    """InstanceGroupStateChangeReasonCode enum values."""

    INTERNAL_ERROR = "INTERNAL_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    INSTANCE_FAILURE = "INSTANCE_FAILURE"
    CLUSTER_TERMINATED = "CLUSTER_TERMINATED"


class InstanceGroupType:
    """InstanceGroupType enum values."""

    MASTER = "MASTER"
    CORE = "CORE"
    TASK = "TASK"


class InstanceRoleType:
    """InstanceRoleType enum values."""

    MASTER = "MASTER"
    CORE = "CORE"
    TASK = "TASK"


class InstanceState:
    """InstanceState enum values."""

    AWAITING_FULFILLMENT = "AWAITING_FULFILLMENT"
    PROVISIONING = "PROVISIONING"
    BOOTSTRAPPING = "BOOTSTRAPPING"
    RUNNING = "RUNNING"
    TERMINATED = "TERMINATED"


class InstanceStateChangeReasonCode:
    """InstanceStateChangeReasonCode enum values."""

    INTERNAL_ERROR = "INTERNAL_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    INSTANCE_FAILURE = "INSTANCE_FAILURE"
    BOOTSTRAP_FAILURE = "BOOTSTRAP_FAILURE"
    CLUSTER_TERMINATED = "CLUSTER_TERMINATED"


class JobFlowExecutionState:
    """JobFlowExecutionState enum values."""

    STARTING = "STARTING"
    BOOTSTRAPPING = "BOOTSTRAPPING"
    RUNNING = "RUNNING"
    WAITING = "WAITING"
    SHUTTING_DOWN = "SHUTTING_DOWN"
    TERMINATED = "TERMINATED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class MarketType:
    """MarketType enum values."""

    ON_DEMAND = "ON_DEMAND"
    SPOT = "SPOT"


class NotebookExecutionStatus:
    """NotebookExecutionStatus enum values."""

    START_PENDING = "START_PENDING"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    FINISHING = "FINISHING"
    FINISHED = "FINISHED"
    FAILING = "FAILING"
    FAILED = "FAILED"
    STOP_PENDING = "STOP_PENDING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class OnClusterAppUIType:
    """OnClusterAppUIType enum values."""

    SPARKHISTORYSERVER = "SparkHistoryServer"
    YARNTIMELINESERVICE = "YarnTimelineService"
    TEZUI = "TezUI"
    APPLICATIONMASTER = "ApplicationMaster"
    JOBHISTORYSERVER = "JobHistoryServer"
    RESOURCEMANAGER = "ResourceManager"


class OnDemandCapacityReservationPreference:
    """OnDemandCapacityReservationPreference enum values."""

    OPEN = "open"
    NONE = "none"


class OnDemandCapacityReservationUsageStrategy:
    """OnDemandCapacityReservationUsageStrategy enum values."""

    USE_CAPACITY_RESERVATIONS_FIRST = "use-capacity-reservations-first"


class OnDemandProvisioningAllocationStrategy:
    """OnDemandProvisioningAllocationStrategy enum values."""

    LOWEST_PRICE = "lowest-price"
    PRIORITIZED = "prioritized"


class OutputNotebookFormat:
    """OutputNotebookFormat enum values."""

    HTML = "HTML"


class PersistentAppUIType:
    """PersistentAppUIType enum values."""

    SHS = "SHS"
    TEZ = "TEZ"
    YTS = "YTS"


class PlacementGroupStrategy:
    """PlacementGroupStrategy enum values."""

    SPREAD = "SPREAD"
    PARTITION = "PARTITION"
    CLUSTER = "CLUSTER"
    NONE = "NONE"


class ProfilerType:
    """ProfilerType enum values."""

    SHS = "SHS"
    TEZUI = "TEZUI"
    YTS = "YTS"


class ReconfigurationType:
    """ReconfigurationType enum values."""

    OVERWRITE = "OVERWRITE"
    MERGE = "MERGE"


class RepoUpgradeOnBoot:
    """RepoUpgradeOnBoot enum values."""

    SECURITY = "SECURITY"
    NONE = "NONE"


class ScaleDownBehavior:
    """ScaleDownBehavior enum values."""

    TERMINATE_AT_INSTANCE_HOUR = "TERMINATE_AT_INSTANCE_HOUR"
    TERMINATE_AT_TASK_COMPLETION = "TERMINATE_AT_TASK_COMPLETION"


class ScalingStrategy:
    """ScalingStrategy enum values."""

    DEFAULT = "DEFAULT"
    ADVANCED = "ADVANCED"


class SpotProvisioningAllocationStrategy:
    """SpotProvisioningAllocationStrategy enum values."""

    CAPACITY_OPTIMIZED = "capacity-optimized"
    PRICE_CAPACITY_OPTIMIZED = "price-capacity-optimized"
    LOWEST_PRICE = "lowest-price"
    DIVERSIFIED = "diversified"
    CAPACITY_OPTIMIZED_PRIORITIZED = "capacity-optimized-prioritized"


class SpotProvisioningTimeoutAction:
    """SpotProvisioningTimeoutAction enum values."""

    SWITCH_TO_ON_DEMAND = "SWITCH_TO_ON_DEMAND"
    TERMINATE_CLUSTER = "TERMINATE_CLUSTER"


class Statistic:
    """Statistic enum values."""

    SAMPLE_COUNT = "SAMPLE_COUNT"
    AVERAGE = "AVERAGE"
    SUM = "SUM"
    MINIMUM = "MINIMUM"
    MAXIMUM = "MAXIMUM"


class StepCancellationOption:
    """StepCancellationOption enum values."""

    SEND_INTERRUPT = "SEND_INTERRUPT"
    TERMINATE_PROCESS = "TERMINATE_PROCESS"


class StepExecutionState:
    """StepExecutionState enum values."""

    PENDING = "PENDING"
    RUNNING = "RUNNING"
    CONTINUE = "CONTINUE"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    INTERRUPTED = "INTERRUPTED"


class StepState:
    """StepState enum values."""

    PENDING = "PENDING"
    CANCEL_PENDING = "CANCEL_PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    INTERRUPTED = "INTERRUPTED"


class StepStateChangeReasonCode:
    """StepStateChangeReasonCode enum values."""

    NONE = "NONE"


class Unit:
    """Unit enum values."""

    NONE = "NONE"
    SECONDS = "SECONDS"
    MICRO_SECONDS = "MICRO_SECONDS"
    MILLI_SECONDS = "MILLI_SECONDS"
    BYTES = "BYTES"
    KILO_BYTES = "KILO_BYTES"
    MEGA_BYTES = "MEGA_BYTES"
    GIGA_BYTES = "GIGA_BYTES"
    TERA_BYTES = "TERA_BYTES"
    BITS = "BITS"
    KILO_BITS = "KILO_BITS"
    MEGA_BITS = "MEGA_BITS"
    GIGA_BITS = "GIGA_BITS"
    TERA_BITS = "TERA_BITS"
    PERCENT = "PERCENT"
    COUNT = "COUNT"
    BYTES_PER_SECOND = "BYTES_PER_SECOND"
    KILO_BYTES_PER_SECOND = "KILO_BYTES_PER_SECOND"
    MEGA_BYTES_PER_SECOND = "MEGA_BYTES_PER_SECOND"
    GIGA_BYTES_PER_SECOND = "GIGA_BYTES_PER_SECOND"
    TERA_BYTES_PER_SECOND = "TERA_BYTES_PER_SECOND"
    BITS_PER_SECOND = "BITS_PER_SECOND"
    KILO_BITS_PER_SECOND = "KILO_BITS_PER_SECOND"
    MEGA_BITS_PER_SECOND = "MEGA_BITS_PER_SECOND"
    GIGA_BITS_PER_SECOND = "GIGA_BITS_PER_SECOND"
    TERA_BITS_PER_SECOND = "TERA_BITS_PER_SECOND"
    COUNT_PER_SECOND = "COUNT_PER_SECOND"


@dataclass
class HadoopJarStepConfig(PropertyType):
    ARGS = "Args"
    MAIN_CLASS = "MainClass"
    STEP_PROPERTIES = "StepProperties"
    JAR = "Jar"

    _property_mappings: ClassVar[dict[str, str]] = {
        "args": "Args",
        "main_class": "MainClass",
        "step_properties": "StepProperties",
        "jar": "Jar",
    }

    args: Optional[Union[list[str], Ref]] = None
    main_class: Optional[Union[str, Ref, GetAtt, Sub]] = None
    step_properties: Optional[list[KeyValue]] = None
    jar: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KeyValue(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

