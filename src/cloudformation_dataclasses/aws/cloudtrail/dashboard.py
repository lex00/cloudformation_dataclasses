"""PropertyTypes for AWS::CloudTrail::Dashboard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Frequency(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RefreshSchedule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "time_of_day": "TimeOfDay",
        "frequency": "Frequency",
    }

    status: Optional[Union[str, RefreshScheduleStatus, Ref, GetAtt, Sub]] = None
    time_of_day: Optional[Union[str, Ref, GetAtt, Sub]] = None
    frequency: Optional[Frequency] = None


@dataclass
class Widget(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "query_statement": "QueryStatement",
        "query_parameters": "QueryParameters",
        "view_properties": "ViewProperties",
    }

    query_statement: Optional[Union[str, Ref, GetAtt, Sub]] = None
    query_parameters: Optional[Union[list[str], Ref]] = None
    view_properties: Optional[dict[str, str]] = None

