"""PropertyTypes for AWS::OpsWorks::Layer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AutoScalingThresholds(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cpu_threshold": "CpuThreshold",
        "ignore_metrics_time": "IgnoreMetricsTime",
        "instance_count": "InstanceCount",
        "load_threshold": "LoadThreshold",
        "memory_threshold": "MemoryThreshold",
        "thresholds_wait_time": "ThresholdsWaitTime",
    }

    cpu_threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None
    ignore_metrics_time: Optional[Union[int, Ref, GetAtt, Sub]] = None
    instance_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    load_threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None
    memory_threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None
    thresholds_wait_time: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class LifecycleEventConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "shutdown_event_configuration": "ShutdownEventConfiguration",
    }

    shutdown_event_configuration: Optional[ShutdownEventConfiguration] = None


@dataclass
class LoadBasedAutoScaling(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "down_scaling": "DownScaling",
        "enable": "Enable",
        "up_scaling": "UpScaling",
    }

    down_scaling: Optional[AutoScalingThresholds] = None
    enable: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    up_scaling: Optional[AutoScalingThresholds] = None


@dataclass
class Recipes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "configure": "Configure",
        "deploy": "Deploy",
        "setup": "Setup",
        "shutdown": "Shutdown",
        "undeploy": "Undeploy",
    }

    configure: Optional[Union[list[str], Ref]] = None
    deploy: Optional[Union[list[str], Ref]] = None
    setup: Optional[Union[list[str], Ref]] = None
    shutdown: Optional[Union[list[str], Ref]] = None
    undeploy: Optional[Union[list[str], Ref]] = None


@dataclass
class ShutdownEventConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "delay_until_elb_connections_drained": "DelayUntilElbConnectionsDrained",
        "execution_timeout": "ExecutionTimeout",
    }

    delay_until_elb_connections_drained: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    execution_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VolumeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "encrypted": "Encrypted",
        "iops": "Iops",
        "mount_point": "MountPoint",
        "number_of_disks": "NumberOfDisks",
        "raid_level": "RaidLevel",
        "size": "Size",
        "volume_type": "VolumeType",
    }

    encrypted: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    iops: Optional[Union[int, Ref, GetAtt, Sub]] = None
    mount_point: Optional[Union[str, Ref, GetAtt, Sub]] = None
    number_of_disks: Optional[Union[int, Ref, GetAtt, Sub]] = None
    raid_level: Optional[Union[int, Ref, GetAtt, Sub]] = None
    size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    volume_type: Optional[Union[str, Ref, GetAtt, Sub]] = None

