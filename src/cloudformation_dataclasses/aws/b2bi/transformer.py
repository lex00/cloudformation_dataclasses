"""PropertyTypes for AWS::B2BI::Transformer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AdvancedOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "x12": "X12",
    }

    x12: Optional[X12AdvancedOptions] = None


@dataclass
class FormatOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "x12": "X12",
    }

    x12: Optional[X12Details] = None


@dataclass
class InputConversion(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "advanced_options": "AdvancedOptions",
        "format_options": "FormatOptions",
        "from_format": "FromFormat",
    }

    advanced_options: Optional[AdvancedOptions] = None
    format_options: Optional[FormatOptions] = None
    from_format: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Mapping(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "template_language": "TemplateLanguage",
        "template": "Template",
    }

    template_language: Optional[Union[str, Ref, GetAtt, Sub]] = None
    template: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OutputConversion(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "advanced_options": "AdvancedOptions",
        "to_format": "ToFormat",
        "format_options": "FormatOptions",
    }

    advanced_options: Optional[AdvancedOptions] = None
    to_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    format_options: Optional[FormatOptions] = None


@dataclass
class SampleDocumentKeys(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "input": "Input",
        "output": "Output",
    }

    input: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SampleDocuments(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "keys": "Keys",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    keys: Optional[list[SampleDocumentKeys]] = None


@dataclass
class X12AdvancedOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "validation_options": "ValidationOptions",
        "split_options": "SplitOptions",
    }

    validation_options: Optional[X12ValidationOptions] = None
    split_options: Optional[X12SplitOptions] = None


@dataclass
class X12CodeListValidationRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "codes_to_add": "CodesToAdd",
        "codes_to_remove": "CodesToRemove",
        "element_id": "ElementId",
    }

    codes_to_add: Optional[Union[list[str], Ref]] = None
    codes_to_remove: Optional[Union[list[str], Ref]] = None
    element_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class X12Details(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "version": "Version",
        "transaction_set": "TransactionSet",
    }

    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    transaction_set: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class X12ElementLengthValidationRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "min_length": "MinLength",
        "max_length": "MaxLength",
        "element_id": "ElementId",
    }

    min_length: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max_length: Optional[Union[float, Ref, GetAtt, Sub]] = None
    element_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class X12ElementRequirementValidationRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "requirement": "Requirement",
        "element_position": "ElementPosition",
    }

    requirement: Optional[Union[str, Ref, GetAtt, Sub]] = None
    element_position: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class X12SplitOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "split_by": "SplitBy",
    }

    split_by: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class X12ValidationOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "validation_rules": "ValidationRules",
    }

    validation_rules: Optional[list[X12ValidationRule]] = None


@dataclass
class X12ValidationRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "element_requirement_validation_rule": "ElementRequirementValidationRule",
        "code_list_validation_rule": "CodeListValidationRule",
        "element_length_validation_rule": "ElementLengthValidationRule",
    }

    element_requirement_validation_rule: Optional[X12ElementRequirementValidationRule] = None
    code_list_validation_rule: Optional[X12CodeListValidationRule] = None
    element_length_validation_rule: Optional[X12ElementLengthValidationRule] = None

