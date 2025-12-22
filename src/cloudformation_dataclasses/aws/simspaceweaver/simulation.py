"""PropertyTypes for AWS::SimSpaceWeaver::Simulation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ClockStatus:
    """ClockStatus enum values."""

    UNKNOWN = "UNKNOWN"
    STARTING = "STARTING"
    STARTED = "STARTED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class ClockTargetStatus:
    """ClockTargetStatus enum values."""

    UNKNOWN = "UNKNOWN"
    STARTED = "STARTED"
    STOPPED = "STOPPED"


class LifecycleManagementStrategy:
    """LifecycleManagementStrategy enum values."""

    UNKNOWN = "Unknown"
    PERWORKER = "PerWorker"
    BYSPATIALSUBDIVISION = "BySpatialSubdivision"
    BYREQUEST = "ByRequest"


class SimulationAppStatus:
    """SimulationAppStatus enum values."""

    STARTING = "STARTING"
    STARTED = "STARTED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    ERROR = "ERROR"
    UNKNOWN = "UNKNOWN"


class SimulationAppTargetStatus:
    """SimulationAppTargetStatus enum values."""

    UNKNOWN = "UNKNOWN"
    STARTED = "STARTED"
    STOPPED = "STOPPED"


class SimulationStatus:
    """SimulationStatus enum values."""

    UNKNOWN = "UNKNOWN"
    STARTING = "STARTING"
    STARTED = "STARTED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    FAILED = "FAILED"
    DELETING = "DELETING"
    DELETED = "DELETED"
    SNAPSHOT_IN_PROGRESS = "SNAPSHOT_IN_PROGRESS"


class SimulationTargetStatus:
    """SimulationTargetStatus enum values."""

    UNKNOWN = "UNKNOWN"
    STARTED = "STARTED"
    STOPPED = "STOPPED"
    DELETED = "DELETED"


@dataclass
class S3Location(PropertyType):
    BUCKET_NAME = "BucketName"
    OBJECT_KEY = "ObjectKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "object_key": "ObjectKey",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object_key: Optional[Union[str, Ref, GetAtt, Sub]] = None

