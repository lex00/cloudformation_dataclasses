"""PropertyTypes for AWS::WorkSpaces::Workspace."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class WorkspaceProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "compute_type_name": "ComputeTypeName",
        "root_volume_size_gib": "RootVolumeSizeGib",
        "running_mode": "RunningMode",
        "running_mode_auto_stop_timeout_in_minutes": "RunningModeAutoStopTimeoutInMinutes",
        "user_volume_size_gib": "UserVolumeSizeGib",
    }

    compute_type_name: Optional[Union[str, Compute, Ref, GetAtt, Sub]] = None
    root_volume_size_gib: Optional[Union[int, Ref, GetAtt, Sub]] = None
    running_mode: Optional[Union[str, RunningMode, Ref, GetAtt, Sub]] = None
    running_mode_auto_stop_timeout_in_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    user_volume_size_gib: Optional[Union[int, Ref, GetAtt, Sub]] = None

