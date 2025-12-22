"""PropertyTypes for AWS::EMR::InstanceFleetConfig."""

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
class Configuration(PropertyType):
    CLASSIFICATION = "Classification"
    CONFIGURATION_PROPERTIES = "ConfigurationProperties"
    CONFIGURATIONS = "Configurations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "classification": "Classification",
        "configuration_properties": "ConfigurationProperties",
        "configurations": "Configurations",
    }

    classification: Optional[Union[str, Ref, GetAtt, Sub]] = None
    configuration_properties: Optional[dict[str, str]] = None
    configurations: Optional[list[Configuration]] = None


@dataclass
class EbsBlockDeviceConfig(PropertyType):
    VOLUME_SPECIFICATION = "VolumeSpecification"
    VOLUMES_PER_INSTANCE = "VolumesPerInstance"

    _property_mappings: ClassVar[dict[str, str]] = {
        "volume_specification": "VolumeSpecification",
        "volumes_per_instance": "VolumesPerInstance",
    }

    volume_specification: Optional[VolumeSpecification] = None
    volumes_per_instance: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EbsConfiguration(PropertyType):
    EBS_BLOCK_DEVICE_CONFIGS = "EbsBlockDeviceConfigs"
    EBS_OPTIMIZED = "EbsOptimized"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs_block_device_configs": "EbsBlockDeviceConfigs",
        "ebs_optimized": "EbsOptimized",
    }

    ebs_block_device_configs: Optional[list[EbsBlockDeviceConfig]] = None
    ebs_optimized: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceFleetProvisioningSpecifications(PropertyType):
    ON_DEMAND_SPECIFICATION = "OnDemandSpecification"
    SPOT_SPECIFICATION = "SpotSpecification"

    _property_mappings: ClassVar[dict[str, str]] = {
        "on_demand_specification": "OnDemandSpecification",
        "spot_specification": "SpotSpecification",
    }

    on_demand_specification: Optional[OnDemandProvisioningSpecification] = None
    spot_specification: Optional[SpotProvisioningSpecification] = None


@dataclass
class InstanceFleetResizingSpecifications(PropertyType):
    ON_DEMAND_RESIZE_SPECIFICATION = "OnDemandResizeSpecification"
    SPOT_RESIZE_SPECIFICATION = "SpotResizeSpecification"

    _property_mappings: ClassVar[dict[str, str]] = {
        "on_demand_resize_specification": "OnDemandResizeSpecification",
        "spot_resize_specification": "SpotResizeSpecification",
    }

    on_demand_resize_specification: Optional[OnDemandResizingSpecification] = None
    spot_resize_specification: Optional[SpotResizingSpecification] = None


@dataclass
class InstanceTypeConfig(PropertyType):
    BID_PRICE = "BidPrice"
    BID_PRICE_AS_PERCENTAGE_OF_ON_DEMAND_PRICE = "BidPriceAsPercentageOfOnDemandPrice"
    CONFIGURATIONS = "Configurations"
    CUSTOM_AMI_ID = "CustomAmiId"
    EBS_CONFIGURATION = "EbsConfiguration"
    INSTANCE_TYPE = "InstanceType"
    PRIORITY = "Priority"
    WEIGHTED_CAPACITY = "WeightedCapacity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bid_price": "BidPrice",
        "bid_price_as_percentage_of_on_demand_price": "BidPriceAsPercentageOfOnDemandPrice",
        "configurations": "Configurations",
        "custom_ami_id": "CustomAmiId",
        "ebs_configuration": "EbsConfiguration",
        "instance_type": "InstanceType",
        "priority": "Priority",
        "weighted_capacity": "WeightedCapacity",
    }

    bid_price: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bid_price_as_percentage_of_on_demand_price: Optional[Union[float, Ref, GetAtt, Sub]] = None
    configurations: Optional[list[Configuration]] = None
    custom_ami_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ebs_configuration: Optional[EbsConfiguration] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    priority: Optional[Union[float, Ref, GetAtt, Sub]] = None
    weighted_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class OnDemandCapacityReservationOptions(PropertyType):
    CAPACITY_RESERVATION_PREFERENCE = "CapacityReservationPreference"
    CAPACITY_RESERVATION_RESOURCE_GROUP_ARN = "CapacityReservationResourceGroupArn"
    USAGE_STRATEGY = "UsageStrategy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "capacity_reservation_preference": "CapacityReservationPreference",
        "capacity_reservation_resource_group_arn": "CapacityReservationResourceGroupArn",
        "usage_strategy": "UsageStrategy",
    }

    capacity_reservation_preference: Optional[Union[str, OnDemandCapacityReservationPreference, Ref, GetAtt, Sub]] = None
    capacity_reservation_resource_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    usage_strategy: Optional[Union[str, OnDemandCapacityReservationUsageStrategy, Ref, GetAtt, Sub]] = None


@dataclass
class OnDemandProvisioningSpecification(PropertyType):
    ALLOCATION_STRATEGY = "AllocationStrategy"
    CAPACITY_RESERVATION_OPTIONS = "CapacityReservationOptions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allocation_strategy": "AllocationStrategy",
        "capacity_reservation_options": "CapacityReservationOptions",
    }

    allocation_strategy: Optional[Union[str, OnDemandProvisioningAllocationStrategy, Ref, GetAtt, Sub]] = None
    capacity_reservation_options: Optional[OnDemandCapacityReservationOptions] = None


@dataclass
class OnDemandResizingSpecification(PropertyType):
    ALLOCATION_STRATEGY = "AllocationStrategy"
    CAPACITY_RESERVATION_OPTIONS = "CapacityReservationOptions"
    TIMEOUT_DURATION_MINUTES = "TimeoutDurationMinutes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allocation_strategy": "AllocationStrategy",
        "capacity_reservation_options": "CapacityReservationOptions",
        "timeout_duration_minutes": "TimeoutDurationMinutes",
    }

    allocation_strategy: Optional[Union[str, OnDemandProvisioningAllocationStrategy, Ref, GetAtt, Sub]] = None
    capacity_reservation_options: Optional[OnDemandCapacityReservationOptions] = None
    timeout_duration_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SpotProvisioningSpecification(PropertyType):
    ALLOCATION_STRATEGY = "AllocationStrategy"
    BLOCK_DURATION_MINUTES = "BlockDurationMinutes"
    TIMEOUT_ACTION = "TimeoutAction"
    TIMEOUT_DURATION_MINUTES = "TimeoutDurationMinutes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allocation_strategy": "AllocationStrategy",
        "block_duration_minutes": "BlockDurationMinutes",
        "timeout_action": "TimeoutAction",
        "timeout_duration_minutes": "TimeoutDurationMinutes",
    }

    allocation_strategy: Optional[Union[str, SpotProvisioningAllocationStrategy, Ref, GetAtt, Sub]] = None
    block_duration_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    timeout_action: Optional[Union[str, SpotProvisioningTimeoutAction, Ref, GetAtt, Sub]] = None
    timeout_duration_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SpotResizingSpecification(PropertyType):
    ALLOCATION_STRATEGY = "AllocationStrategy"
    TIMEOUT_DURATION_MINUTES = "TimeoutDurationMinutes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allocation_strategy": "AllocationStrategy",
        "timeout_duration_minutes": "TimeoutDurationMinutes",
    }

    allocation_strategy: Optional[Union[str, SpotProvisioningAllocationStrategy, Ref, GetAtt, Sub]] = None
    timeout_duration_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VolumeSpecification(PropertyType):
    IOPS = "Iops"
    SIZE_IN_GB = "SizeInGB"
    THROUGHPUT = "Throughput"
    VOLUME_TYPE = "VolumeType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "iops": "Iops",
        "size_in_gb": "SizeInGB",
        "throughput": "Throughput",
        "volume_type": "VolumeType",
    }

    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None
    size_in_gb: Optional[Union[int, Ref, GetAtt, Sub]] = None
    throughput: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

