"""PropertyTypes for AWS::DMS::ReplicationConfig."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ComputeConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dns_name_servers": "DnsNameServers",
        "kms_key_id": "KmsKeyId",
        "vpc_security_group_ids": "VpcSecurityGroupIds",
        "max_capacity_units": "MaxCapacityUnits",
        "replication_subnet_group_id": "ReplicationSubnetGroupId",
        "availability_zone": "AvailabilityZone",
        "preferred_maintenance_window": "PreferredMaintenanceWindow",
        "min_capacity_units": "MinCapacityUnits",
        "multi_az": "MultiAZ",
    }

    dns_name_servers: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpc_security_group_ids: Optional[Union[list[str], Ref]] = None
    max_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None
    replication_subnet_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    availability_zone: Optional[Union[str, Ref, GetAtt, Sub]] = None
    preferred_maintenance_window: Optional[Union[str, Ref, GetAtt, Sub]] = None
    min_capacity_units: Optional[Union[int, Ref, GetAtt, Sub]] = None
    multi_az: Optional[Union[bool, Ref, GetAtt, Sub]] = None

