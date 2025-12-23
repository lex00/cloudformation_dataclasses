"""PropertyTypes for AWS::EC2::FlowLog."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DestinationOptions(PropertyType):
    PER_HOUR_PARTITION = "PerHourPartition"
    HIVE_COMPATIBLE_PARTITIONS = "HiveCompatiblePartitions"
    FILE_FORMAT = "FileFormat"

    _property_mappings: ClassVar[dict[str, str]] = {
        "per_hour_partition": "PerHourPartition",
        "hive_compatible_partitions": "HiveCompatiblePartitions",
        "file_format": "FileFormat",
    }

    per_hour_partition: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    hive_compatible_partitions: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    file_format: Optional[Union[str, Ref, GetAtt, Sub]] = None

