"""PropertyTypes for AWS::EKS::Nodegroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class LaunchTemplateSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "version": "Version",
        "id": "Id",
        "name": "Name",
    }

    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NodeRepairConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "node_repair_config_overrides": "NodeRepairConfigOverrides",
        "max_parallel_nodes_repaired_count": "MaxParallelNodesRepairedCount",
        "enabled": "Enabled",
        "max_unhealthy_node_threshold_percentage": "MaxUnhealthyNodeThresholdPercentage",
        "max_parallel_nodes_repaired_percentage": "MaxParallelNodesRepairedPercentage",
        "max_unhealthy_node_threshold_count": "MaxUnhealthyNodeThresholdCount",
    }

    node_repair_config_overrides: Optional[list[NodeRepairConfigOverrides]] = None
    max_parallel_nodes_repaired_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    max_unhealthy_node_threshold_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_parallel_nodes_repaired_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_unhealthy_node_threshold_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NodeRepairConfigOverrides(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "node_unhealthy_reason": "NodeUnhealthyReason",
        "repair_action": "RepairAction",
        "min_repair_wait_time_mins": "MinRepairWaitTimeMins",
        "node_monitoring_condition": "NodeMonitoringCondition",
    }

    node_unhealthy_reason: Optional[Union[str, Ref, GetAtt, Sub]] = None
    repair_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    min_repair_wait_time_mins: Optional[Union[int, Ref, GetAtt, Sub]] = None
    node_monitoring_condition: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RemoteAccess(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_security_groups": "SourceSecurityGroups",
        "ec2_ssh_key": "Ec2SshKey",
    }

    source_security_groups: Optional[Union[list[str], Ref]] = None
    ec2_ssh_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScalingConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min_size": "MinSize",
        "desired_size": "DesiredSize",
        "max_size": "MaxSize",
    }

    min_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    desired_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_size: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Taint(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "effect": "Effect",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    effect: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UpdateConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_unavailable_percentage": "MaxUnavailablePercentage",
        "update_strategy": "UpdateStrategy",
        "max_unavailable": "MaxUnavailable",
    }

    max_unavailable_percentage: Optional[Union[float, Ref, GetAtt, Sub]] = None
    update_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_unavailable: Optional[Union[float, Ref, GetAtt, Sub]] = None

