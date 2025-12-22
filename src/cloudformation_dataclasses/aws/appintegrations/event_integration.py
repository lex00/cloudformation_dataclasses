"""PropertyTypes for AWS::AppIntegrations::EventIntegration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ApplicationType:
    """ApplicationType enum values."""

    STANDARD = "STANDARD"
    SERVICE = "SERVICE"
    MCP_SERVER = "MCP_SERVER"


class ContactHandlingScope:
    """ContactHandlingScope enum values."""

    CROSS_CONTACTS = "CROSS_CONTACTS"
    PER_CONTACT = "PER_CONTACT"


class ExecutionMode:
    """ExecutionMode enum values."""

    ON_DEMAND = "ON_DEMAND"
    SCHEDULED = "SCHEDULED"


class ExecutionStatus:
    """ExecutionStatus enum values."""

    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"


@dataclass
class EventFilter(PropertyType):
    SOURCE = "Source"

    _property_mappings: ClassVar[dict[str, str]] = {
        "source": "Source",
    }

    source: Optional[Union[str, Ref, GetAtt, Sub]] = None

