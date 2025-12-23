"""PropertyTypes for AWS::SecurityHub::ConfigurationPolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ParameterConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value_type": "ValueType",
        "value": "Value",
    }

    value_type: Optional[Union[str, ParameterValueType, Ref, GetAtt, Sub]] = None
    value: Optional[ParameterValue] = None


@dataclass
class ParameterValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enum": "Enum",
        "integer": "Integer",
        "string_list": "StringList",
        "enum_list": "EnumList",
        "integer_list": "IntegerList",
        "string": "String",
        "boolean": "Boolean",
        "double": "Double",
    }

    enum: Optional[Union[str, Ref, GetAtt, Sub]] = None
    integer: Optional[Union[int, Ref, GetAtt, Sub]] = None
    string_list: Optional[Union[list[str], Ref]] = None
    enum_list: Optional[Union[list[str], Ref]] = None
    integer_list: Optional[Union[list[int], Ref]] = None
    string: Optional[Union[str, Ref, GetAtt, Sub]] = None
    boolean: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    double: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class Policy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "security_hub": "SecurityHub",
    }

    security_hub: Optional[SecurityHubPolicy] = None


@dataclass
class SecurityControlCustomParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "security_control_id": "SecurityControlId",
        "parameters": "Parameters",
    }

    security_control_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameters: Optional[dict[str, Any]] = None


@dataclass
class SecurityControlsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "disabled_security_control_identifiers": "DisabledSecurityControlIdentifiers",
        "enabled_security_control_identifiers": "EnabledSecurityControlIdentifiers",
        "security_control_custom_parameters": "SecurityControlCustomParameters",
    }

    disabled_security_control_identifiers: Optional[Union[list[str], Ref]] = None
    enabled_security_control_identifiers: Optional[Union[list[str], Ref]] = None
    security_control_custom_parameters: Optional[list[SecurityControlCustomParameter]] = None


@dataclass
class SecurityHubPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled_standard_identifiers": "EnabledStandardIdentifiers",
        "service_enabled": "ServiceEnabled",
        "security_controls_configuration": "SecurityControlsConfiguration",
    }

    enabled_standard_identifiers: Optional[Union[list[str], Ref]] = None
    service_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    security_controls_configuration: Optional[SecurityControlsConfiguration] = None

