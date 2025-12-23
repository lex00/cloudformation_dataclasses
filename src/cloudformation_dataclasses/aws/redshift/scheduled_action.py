"""PropertyTypes for AWS::Redshift::ScheduledAction."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class PauseClusterMessage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_identifier": "ClusterIdentifier",
    }

    cluster_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResizeClusterMessage(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_identifier": "ClusterIdentifier",
    }

    cluster_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScheduledActionType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "pause_cluster": "PauseCluster",
        "resume_cluster": "ResumeCluster",
        "resize_cluster": "ResizeCluster",
    }

    pause_cluster: Optional[PauseClusterMessage] = None
    resume_cluster: Optional[ResumeClusterMessage] = None
    resize_cluster: Optional[ResizeClusterMessage] = None

