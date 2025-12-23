"""PropertyTypes for AWS::Backup::Framework."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ControlInputParameter(PropertyType):
    PARAMETER_VALUE = "ParameterValue"
    PARAMETER_NAME = "ParameterName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_value": "ParameterValue",
        "parameter_name": "ParameterName",
    }

    parameter_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ControlScope(PropertyType):
    COMPLIANCE_RESOURCE_TYPES = "ComplianceResourceTypes"
    TAGS = "Tags"
    COMPLIANCE_RESOURCE_IDS = "ComplianceResourceIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "compliance_resource_types": "ComplianceResourceTypes",
        "tags": "Tags",
        "compliance_resource_ids": "ComplianceResourceIds",
    }

    compliance_resource_types: Optional[Union[list[str], Ref]] = None
    tags: Optional[list[Tag]] = None
    compliance_resource_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class FrameworkControl(PropertyType):
    CONTROL_NAME = "ControlName"
    CONTROL_INPUT_PARAMETERS = "ControlInputParameters"
    CONTROL_SCOPE = "ControlScope"

    _property_mappings: ClassVar[dict[str, str]] = {
        "control_name": "ControlName",
        "control_input_parameters": "ControlInputParameters",
        "control_scope": "ControlScope",
    }

    control_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    control_input_parameters: Optional[list[ControlInputParameter]] = None
    control_scope: Optional[ControlScope] = None

