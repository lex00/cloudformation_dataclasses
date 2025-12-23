"""PropertyTypes for AWS::AppIntegrations::DataIntegration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class FileConfiguration(PropertyType):
    FILTERS = "Filters"
    FOLDERS = "Folders"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filters": "Filters",
        "folders": "Folders",
    }

    filters: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    folders: Optional[Union[list[str], Ref]] = None


@dataclass
class ScheduleConfig(PropertyType):
    FIRST_EXECUTION_FROM = "FirstExecutionFrom"
    SCHEDULE_EXPRESSION = "ScheduleExpression"
    OBJECT = "Object"

    _property_mappings: ClassVar[dict[str, str]] = {
        "first_execution_from": "FirstExecutionFrom",
        "schedule_expression": "ScheduleExpression",
        "object": "Object",
    }

    first_execution_from: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schedule_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object: Optional[Union[str, Ref, GetAtt, Sub]] = None

