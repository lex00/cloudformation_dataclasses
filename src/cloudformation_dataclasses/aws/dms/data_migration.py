"""PropertyTypes for AWS::DMS::DataMigration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DataMigrationSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "selection_rules": "SelectionRules",
        "cloudwatch_logs_enabled": "CloudwatchLogsEnabled",
        "number_of_jobs": "NumberOfJobs",
    }

    selection_rules: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cloudwatch_logs_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    number_of_jobs: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SourceDataSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cdc_start_time": "CDCStartTime",
        "cdc_stop_time": "CDCStopTime",
        "slot_name": "SlotName",
        "cdc_start_position": "CDCStartPosition",
    }

    cdc_start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cdc_stop_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    slot_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cdc_start_position: Optional[Union[str, Ref, GetAtt, Sub]] = None

