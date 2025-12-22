"""PropertyTypes for AWS::AutoScaling::LaunchConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AcceleratorManufacturer:
    """AcceleratorManufacturer enum values."""

    NVIDIA = "nvidia"
    AMD = "amd"
    AMAZON_WEB_SERVICES = "amazon-web-services"
    XILINX = "xilinx"


class AcceleratorName:
    """AcceleratorName enum values."""

    A100 = "a100"
    V100 = "v100"
    K80 = "k80"
    T4 = "t4"
    M60 = "m60"
    RADEON_PRO_V520 = "radeon-pro-v520"
    VU9P = "vu9p"


class AcceleratorType:
    """AcceleratorType enum values."""

    GPU = "gpu"
    FPGA = "fpga"
    INFERENCE = "inference"


class BareMetal:
    """BareMetal enum values."""

    INCLUDED = "included"
    EXCLUDED = "excluded"
    REQUIRED = "required"


class BurstablePerformance:
    """BurstablePerformance enum values."""

    INCLUDED = "included"
    EXCLUDED = "excluded"
    REQUIRED = "required"


class CapacityDistributionStrategy:
    """CapacityDistributionStrategy enum values."""

    BALANCED_ONLY = "balanced-only"
    BALANCED_BEST_EFFORT = "balanced-best-effort"


class CapacityReservationPreference:
    """CapacityReservationPreference enum values."""

    CAPACITY_RESERVATIONS_ONLY = "capacity-reservations-only"
    CAPACITY_RESERVATIONS_FIRST = "capacity-reservations-first"
    NONE = "none"
    DEFAULT = "default"


class CpuManufacturer:
    """CpuManufacturer enum values."""

    INTEL = "intel"
    AMD = "amd"
    AMAZON_WEB_SERVICES = "amazon-web-services"
    APPLE = "apple"


class ImpairedZoneHealthCheckBehavior:
    """ImpairedZoneHealthCheckBehavior enum values."""

    REPLACEUNHEALTHY = "ReplaceUnhealthy"
    IGNOREUNHEALTHY = "IgnoreUnhealthy"


class InstanceGeneration:
    """InstanceGeneration enum values."""

    CURRENT = "current"
    PREVIOUS = "previous"


class InstanceMetadataEndpointState:
    """InstanceMetadataEndpointState enum values."""

    DISABLED = "disabled"
    ENABLED = "enabled"


class InstanceMetadataHttpTokensState:
    """InstanceMetadataHttpTokensState enum values."""

    OPTIONAL = "optional"
    REQUIRED = "required"


class InstanceRefreshStatus:
    """InstanceRefreshStatus enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    SUCCESSFUL = "Successful"
    FAILED = "Failed"
    CANCELLING = "Cancelling"
    CANCELLED = "Cancelled"
    ROLLBACKINPROGRESS = "RollbackInProgress"
    ROLLBACKFAILED = "RollbackFailed"
    ROLLBACKSUCCESSFUL = "RollbackSuccessful"
    BAKING = "Baking"


class LifecycleState:
    """LifecycleState enum values."""

    PENDING = "Pending"
    PENDING_WAIT = "Pending:Wait"
    PENDING_PROCEED = "Pending:Proceed"
    QUARANTINED = "Quarantined"
    INSERVICE = "InService"
    TERMINATING = "Terminating"
    TERMINATING_WAIT = "Terminating:Wait"
    TERMINATING_PROCEED = "Terminating:Proceed"
    TERMINATED = "Terminated"
    DETACHING = "Detaching"
    DETACHED = "Detached"
    ENTERINGSTANDBY = "EnteringStandby"
    STANDBY = "Standby"
    WARMED_PENDING = "Warmed:Pending"
    WARMED_PENDING_WAIT = "Warmed:Pending:Wait"
    WARMED_PENDING_PROCEED = "Warmed:Pending:Proceed"
    WARMED_TERMINATING = "Warmed:Terminating"
    WARMED_TERMINATING_WAIT = "Warmed:Terminating:Wait"
    WARMED_TERMINATING_PROCEED = "Warmed:Terminating:Proceed"
    WARMED_TERMINATED = "Warmed:Terminated"
    WARMED_STOPPED = "Warmed:Stopped"
    WARMED_RUNNING = "Warmed:Running"
    WARMED_HIBERNATED = "Warmed:Hibernated"


class LocalStorage:
    """LocalStorage enum values."""

    INCLUDED = "included"
    EXCLUDED = "excluded"
    REQUIRED = "required"


class LocalStorageType:
    """LocalStorageType enum values."""

    HDD = "hdd"
    SSD = "ssd"


class MetricStatistic:
    """MetricStatistic enum values."""

    AVERAGE = "Average"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"
    SAMPLECOUNT = "SampleCount"
    SUM = "Sum"


class MetricType:
    """MetricType enum values."""

    ASGAVERAGECPUUTILIZATION = "ASGAverageCPUUtilization"
    ASGAVERAGENETWORKIN = "ASGAverageNetworkIn"
    ASGAVERAGENETWORKOUT = "ASGAverageNetworkOut"
    ALBREQUESTCOUNTPERTARGET = "ALBRequestCountPerTarget"


class PredefinedLoadMetricType:
    """PredefinedLoadMetricType enum values."""

    ASGTOTALCPUUTILIZATION = "ASGTotalCPUUtilization"
    ASGTOTALNETWORKIN = "ASGTotalNetworkIn"
    ASGTOTALNETWORKOUT = "ASGTotalNetworkOut"
    ALBTARGETGROUPREQUESTCOUNT = "ALBTargetGroupRequestCount"


class PredefinedMetricPairType:
    """PredefinedMetricPairType enum values."""

    ASGCPUUTILIZATION = "ASGCPUUtilization"
    ASGNETWORKIN = "ASGNetworkIn"
    ASGNETWORKOUT = "ASGNetworkOut"
    ALBREQUESTCOUNT = "ALBRequestCount"


class PredefinedScalingMetricType:
    """PredefinedScalingMetricType enum values."""

    ASGAVERAGECPUUTILIZATION = "ASGAverageCPUUtilization"
    ASGAVERAGENETWORKIN = "ASGAverageNetworkIn"
    ASGAVERAGENETWORKOUT = "ASGAverageNetworkOut"
    ALBREQUESTCOUNTPERTARGET = "ALBRequestCountPerTarget"


class PredictiveScalingMaxCapacityBreachBehavior:
    """PredictiveScalingMaxCapacityBreachBehavior enum values."""

    HONORMAXCAPACITY = "HonorMaxCapacity"
    INCREASEMAXCAPACITY = "IncreaseMaxCapacity"


class PredictiveScalingMode:
    """PredictiveScalingMode enum values."""

    FORECASTANDSCALE = "ForecastAndScale"
    FORECASTONLY = "ForecastOnly"


class RefreshStrategy:
    """RefreshStrategy enum values."""

    ROLLING = "Rolling"
    REPLACEROOTVOLUME = "ReplaceRootVolume"


class RetentionAction:
    """RetentionAction enum values."""

    RETAIN = "retain"
    TERMINATE = "terminate"


class RetryStrategy:
    """RetryStrategy enum values."""

    RETRY_WITH_GROUP_CONFIGURATION = "retry-with-group-configuration"
    NONE = "none"


class ScaleInProtectedInstances:
    """ScaleInProtectedInstances enum values."""

    REFRESH = "Refresh"
    IGNORE = "Ignore"
    WAIT = "Wait"


class ScalingActivityStatusCode:
    """ScalingActivityStatusCode enum values."""

    PENDINGSPOTBIDPLACEMENT = "PendingSpotBidPlacement"
    WAITINGFORSPOTINSTANCEREQUESTID = "WaitingForSpotInstanceRequestId"
    WAITINGFORSPOTINSTANCEID = "WaitingForSpotInstanceId"
    WAITINGFORINSTANCEID = "WaitingForInstanceId"
    PREINSERVICE = "PreInService"
    INPROGRESS = "InProgress"
    WAITINGFORELBCONNECTIONDRAINING = "WaitingForELBConnectionDraining"
    MIDLIFECYCLEACTION = "MidLifecycleAction"
    WAITINGFORINSTANCEWARMUP = "WaitingForInstanceWarmup"
    SUCCESSFUL = "Successful"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    WAITINGFORCONNECTIONDRAINING = "WaitingForConnectionDraining"
    WAITINGFORINPLACEUPDATETOSTART = "WaitingForInPlaceUpdateToStart"
    WAITINGFORINPLACEUPDATETOFINALIZE = "WaitingForInPlaceUpdateToFinalize"
    INPLACEUPDATEINPROGRESS = "InPlaceUpdateInProgress"


class StandbyInstances:
    """StandbyInstances enum values."""

    TERMINATE = "Terminate"
    IGNORE = "Ignore"
    WAIT = "Wait"


class WarmPoolState:
    """WarmPoolState enum values."""

    STOPPED = "Stopped"
    RUNNING = "Running"
    HIBERNATED = "Hibernated"


class WarmPoolStatus:
    """WarmPoolStatus enum values."""

    PENDINGDELETE = "PendingDelete"


@dataclass
class BlockDevice(PropertyType):
    SNAPSHOT_ID = "SnapshotId"
    VOLUME_TYPE = "VolumeType"
    ENCRYPTED = "Encrypted"
    THROUGHPUT = "Throughput"
    IOPS = "Iops"
    VOLUME_SIZE = "VolumeSize"
    DELETE_ON_TERMINATION = "DeleteOnTermination"

    _property_mappings: ClassVar[dict[str, str]] = {
        "snapshot_id": "SnapshotId",
        "volume_type": "VolumeType",
        "encrypted": "Encrypted",
        "throughput": "Throughput",
        "iops": "Iops",
        "volume_size": "VolumeSize",
        "delete_on_termination": "DeleteOnTermination",
    }

    snapshot_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    volume_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encrypted: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    throughput: Optional[Union[int, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    delete_on_termination: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class BlockDeviceMapping(PropertyType):
    EBS = "Ebs"
    NO_DEVICE = "NoDevice"
    VIRTUAL_NAME = "VirtualName"
    DEVICE_NAME = "DeviceName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs": "Ebs",
        "no_device": "NoDevice",
        "virtual_name": "VirtualName",
        "device_name": "DeviceName",
    }

    ebs: Optional[BlockDevice] = None
    no_device: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    virtual_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    device_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetadataOptions(PropertyType):
    HTTP_PUT_RESPONSE_HOP_LIMIT = "HttpPutResponseHopLimit"
    HTTP_TOKENS = "HttpTokens"
    HTTP_ENDPOINT = "HttpEndpoint"

    _property_mappings: ClassVar[dict[str, str]] = {
        "http_put_response_hop_limit": "HttpPutResponseHopLimit",
        "http_tokens": "HttpTokens",
        "http_endpoint": "HttpEndpoint",
    }

    http_put_response_hop_limit: Optional[Union[int, Ref, GetAtt, Sub]] = None
    http_tokens: Optional[Union[str, Ref, GetAtt, Sub]] = None
    http_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None

