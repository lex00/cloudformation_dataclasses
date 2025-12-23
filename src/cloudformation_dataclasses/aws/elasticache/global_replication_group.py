"""PropertyTypes for AWS::ElastiCache::GlobalReplicationGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class GlobalReplicationGroupMember(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role": "Role",
        "replication_group_region": "ReplicationGroupRegion",
        "replication_group_id": "ReplicationGroupId",
    }

    role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    replication_group_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    replication_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RegionalConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "replication_group_region": "ReplicationGroupRegion",
        "replication_group_id": "ReplicationGroupId",
        "resharding_configurations": "ReshardingConfigurations",
    }

    replication_group_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    replication_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resharding_configurations: Optional[list[ReshardingConfiguration]] = None


@dataclass
class ReshardingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "node_group_id": "NodeGroupId",
        "preferred_availability_zones": "PreferredAvailabilityZones",
    }

    node_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    preferred_availability_zones: Optional[Union[list[str], Ref]] = None

