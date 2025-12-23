"""PropertyTypes for AWS::Glue::UsageProfile."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ConfigurationObject(PropertyType):
    DEFAULT_VALUE = "DefaultValue"
    ALLOWED_VALUES = "AllowedValues"
    MIN_VALUE = "MinValue"
    MAX_VALUE = "MaxValue"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "allowed_values": "AllowedValues",
        "min_value": "MinValue",
        "max_value": "MaxValue",
    }

    default_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    allowed_values: Optional[Union[list[str], Ref]] = None
    min_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProfileConfiguration(PropertyType):
    JOB_CONFIGURATION = "JobConfiguration"
    SESSION_CONFIGURATION = "SessionConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "job_configuration": "JobConfiguration",
        "session_configuration": "SessionConfiguration",
    }

    job_configuration: Optional[dict[str, Any]] = None
    session_configuration: Optional[dict[str, Any]] = None

