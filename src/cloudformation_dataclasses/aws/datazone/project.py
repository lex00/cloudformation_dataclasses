"""PropertyTypes for AWS::DataZone::Project."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EnvironmentConfigurationUserParameter(PropertyType):
    ENVIRONMENT_ID = "EnvironmentId"
    ENVIRONMENT_PARAMETERS = "EnvironmentParameters"
    ENVIRONMENT_CONFIGURATION_NAME = "EnvironmentConfigurationName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "environment_id": "EnvironmentId",
        "environment_parameters": "EnvironmentParameters",
        "environment_configuration_name": "EnvironmentConfigurationName",
    }

    environment_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    environment_parameters: Optional[list[EnvironmentParameter]] = None
    environment_configuration_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EnvironmentParameter(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

