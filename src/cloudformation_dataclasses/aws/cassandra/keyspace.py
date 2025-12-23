"""PropertyTypes for AWS::Cassandra::Keyspace."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ReplicationSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "replication_strategy": "ReplicationStrategy",
        "region_list": "RegionList",
    }

    replication_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region_list: Optional[Union[list[str], Ref]] = None

