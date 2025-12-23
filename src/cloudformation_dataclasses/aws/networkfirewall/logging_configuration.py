"""PropertyTypes for AWS::NetworkFirewall::LoggingConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class LogDestinationConfig(PropertyType):
    LOG_TYPE = "LogType"
    LOG_DESTINATION = "LogDestination"
    LOG_DESTINATION_TYPE = "LogDestinationType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_type": "LogType",
        "log_destination": "LogDestination",
        "log_destination_type": "LogDestinationType",
    }

    log_type: Optional[Union[str, LogType, Ref, GetAtt, Sub]] = None
    log_destination: Optional[dict[str, str]] = None
    log_destination_type: Optional[Union[str, LogDestinationType, Ref, GetAtt, Sub]] = None


@dataclass
class LoggingConfiguration(PropertyType):
    LOG_DESTINATION_CONFIGS = "LogDestinationConfigs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_destination_configs": "LogDestinationConfigs",
    }

    log_destination_configs: Optional[list[LogDestinationConfig]] = None

