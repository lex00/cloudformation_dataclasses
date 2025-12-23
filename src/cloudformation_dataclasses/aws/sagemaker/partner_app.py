"""PropertyTypes for AWS::SageMaker::PartnerApp."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class PartnerAppConfig(PropertyType):
    ADMIN_USERS = "AdminUsers"
    ARGUMENTS = "Arguments"

    _property_mappings: ClassVar[dict[str, str]] = {
        "admin_users": "AdminUsers",
        "arguments": "Arguments",
    }

    admin_users: Optional[Union[list[str], Ref]] = None
    arguments: Optional[dict[str, str]] = None


@dataclass
class PartnerAppMaintenanceConfig(PropertyType):
    MAINTENANCE_WINDOW_START = "MaintenanceWindowStart"

    _property_mappings: ClassVar[dict[str, str]] = {
        "maintenance_window_start": "MaintenanceWindowStart",
    }

    maintenance_window_start: Optional[Union[str, Ref, GetAtt, Sub]] = None

