"""PropertyTypes for AWS::ControlTower::EnabledControl."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class BaselineOperationStatus:
    """BaselineOperationStatus enum values."""

    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"


class BaselineOperationType:
    """BaselineOperationType enum values."""

    ENABLE_BASELINE = "ENABLE_BASELINE"
    DISABLE_BASELINE = "DISABLE_BASELINE"
    UPDATE_ENABLED_BASELINE = "UPDATE_ENABLED_BASELINE"
    RESET_ENABLED_BASELINE = "RESET_ENABLED_BASELINE"


class ControlOperationStatus:
    """ControlOperationStatus enum values."""

    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"


class ControlOperationType:
    """ControlOperationType enum values."""

    ENABLE_CONTROL = "ENABLE_CONTROL"
    DISABLE_CONTROL = "DISABLE_CONTROL"
    UPDATE_ENABLED_CONTROL = "UPDATE_ENABLED_CONTROL"
    RESET_ENABLED_CONTROL = "RESET_ENABLED_CONTROL"


class DriftStatus:
    """DriftStatus enum values."""

    DRIFTED = "DRIFTED"
    IN_SYNC = "IN_SYNC"
    NOT_CHECKING = "NOT_CHECKING"
    UNKNOWN = "UNKNOWN"


class EnabledBaselineDriftStatus:
    """EnabledBaselineDriftStatus enum values."""

    IN_SYNC = "IN_SYNC"
    DRIFTED = "DRIFTED"


class EnablementStatus:
    """EnablementStatus enum values."""

    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    UNDER_CHANGE = "UNDER_CHANGE"


class LandingZoneDriftStatus:
    """LandingZoneDriftStatus enum values."""

    DRIFTED = "DRIFTED"
    IN_SYNC = "IN_SYNC"


class LandingZoneOperationStatus:
    """LandingZoneOperationStatus enum values."""

    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"


class LandingZoneOperationType:
    """LandingZoneOperationType enum values."""

    DELETE = "DELETE"
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    RESET = "RESET"


class LandingZoneStatus:
    """LandingZoneStatus enum values."""

    ACTIVE = "ACTIVE"
    PROCESSING = "PROCESSING"
    FAILED = "FAILED"


class RemediationType:
    """RemediationType enum values."""

    INHERITANCE_DRIFT = "INHERITANCE_DRIFT"


@dataclass
class EnabledControlParameter(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None

