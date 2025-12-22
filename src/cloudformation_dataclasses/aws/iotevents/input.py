"""PropertyTypes for AWS::IoTEvents::Input."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AlarmModelVersionStatus:
    """AlarmModelVersionStatus enum values."""

    ACTIVE = "ACTIVE"
    ACTIVATING = "ACTIVATING"
    INACTIVE = "INACTIVE"
    FAILED = "FAILED"


class AnalysisResultLevel:
    """AnalysisResultLevel enum values."""

    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class AnalysisStatus:
    """AnalysisStatus enum values."""

    RUNNING = "RUNNING"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"


class ComparisonOperator:
    """ComparisonOperator enum values."""

    GREATER = "GREATER"
    GREATER_OR_EQUAL = "GREATER_OR_EQUAL"
    LESS = "LESS"
    LESS_OR_EQUAL = "LESS_OR_EQUAL"
    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"


class DetectorModelVersionStatus:
    """DetectorModelVersionStatus enum values."""

    ACTIVE = "ACTIVE"
    ACTIVATING = "ACTIVATING"
    INACTIVE = "INACTIVE"
    DEPRECATED = "DEPRECATED"
    DRAFT = "DRAFT"
    PAUSED = "PAUSED"
    FAILED = "FAILED"


class EvaluationMethod:
    """EvaluationMethod enum values."""

    BATCH = "BATCH"
    SERIAL = "SERIAL"


class InputStatus:
    """InputStatus enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


class LoggingLevel:
    """LoggingLevel enum values."""

    ERROR = "ERROR"
    INFO = "INFO"
    DEBUG = "DEBUG"


class PayloadType:
    """PayloadType enum values."""

    STRING = "STRING"
    JSON = "JSON"


@dataclass
class Attribute(PropertyType):
    JSON_PATH = "JsonPath"

    _property_mappings: ClassVar[dict[str, str]] = {
        "json_path": "JsonPath",
    }

    json_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputDefinition(PropertyType):
    ATTRIBUTES = "Attributes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attributes": "Attributes",
    }

    attributes: Optional[list[Attribute]] = None

