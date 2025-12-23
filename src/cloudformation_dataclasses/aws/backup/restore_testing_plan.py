"""PropertyTypes for AWS::Backup::RestoreTestingPlan."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class RestoreTestingRecoveryPointSelection(PropertyType):
    SELECTION_WINDOW_DAYS = "SelectionWindowDays"
    RECOVERY_POINT_TYPES = "RecoveryPointTypes"
    INCLUDE_VAULTS = "IncludeVaults"
    EXCLUDE_VAULTS = "ExcludeVaults"
    ALGORITHM = "Algorithm"

    _property_mappings: ClassVar[dict[str, str]] = {
        "selection_window_days": "SelectionWindowDays",
        "recovery_point_types": "RecoveryPointTypes",
        "include_vaults": "IncludeVaults",
        "exclude_vaults": "ExcludeVaults",
        "algorithm": "Algorithm",
    }

    selection_window_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    recovery_point_types: Optional[Union[list[str], Ref]] = None
    include_vaults: Optional[Union[list[str], Ref]] = None
    exclude_vaults: Optional[Union[list[str], Ref]] = None
    algorithm: Optional[Union[str, RestoreTestingRecoveryPointSelectionAlgorithm, Ref, GetAtt, Sub]] = None

