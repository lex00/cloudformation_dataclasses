"""PropertyTypes for AWS::Glue::Job."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConnectionsList(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "connections": "Connections",
    }

    connections: Optional[Union[list[str], Ref]] = None


@dataclass
class ExecutionProperty(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_concurrent_runs": "MaxConcurrentRuns",
    }

    max_concurrent_runs: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class JobCommand(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "runtime": "Runtime",
        "python_version": "PythonVersion",
        "script_location": "ScriptLocation",
        "name": "Name",
    }

    runtime: Optional[Union[str, Ref, GetAtt, Sub]] = None
    python_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    script_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NotificationProperty(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "notify_delay_after": "NotifyDelayAfter",
    }

    notify_delay_after: Optional[Union[int, Ref, GetAtt, Sub]] = None

