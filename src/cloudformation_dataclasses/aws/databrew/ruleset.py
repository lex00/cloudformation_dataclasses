"""PropertyTypes for AWS::DataBrew::Ruleset."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ColumnSelector(PropertyType):
    REGEX = "Regex"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "regex": "Regex",
        "name": "Name",
    }

    regex: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Rule(PropertyType):
    COLUMN_SELECTORS = "ColumnSelectors"
    DISABLED = "Disabled"
    SUBSTITUTION_MAP = "SubstitutionMap"
    NAME = "Name"
    CHECK_EXPRESSION = "CheckExpression"
    THRESHOLD = "Threshold"

    _property_mappings: ClassVar[dict[str, str]] = {
        "column_selectors": "ColumnSelectors",
        "disabled": "Disabled",
        "substitution_map": "SubstitutionMap",
        "name": "Name",
        "check_expression": "CheckExpression",
        "threshold": "Threshold",
    }

    column_selectors: Optional[list[ColumnSelector]] = None
    disabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    substitution_map: Optional[list[SubstitutionValue]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    check_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    threshold: Optional[Threshold] = None


@dataclass
class SubstitutionValue(PropertyType):
    VALUE = "Value"
    VALUE_REFERENCE = "ValueReference"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "value_reference": "ValueReference",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value_reference: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Threshold(PropertyType):
    TYPE = "Type"
    VALUE = "Value"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
        "unit": "Unit",
    }

    type_: Optional[Union[str, ThresholdType, Ref, GetAtt, Sub]] = None
    value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, ThresholdUnit, Ref, GetAtt, Sub]] = None

