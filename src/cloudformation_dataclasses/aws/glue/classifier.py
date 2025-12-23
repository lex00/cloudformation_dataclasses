"""PropertyTypes for AWS::Glue::Classifier."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CsvClassifier(PropertyType):
    CONTAINS_CUSTOM_DATATYPE = "ContainsCustomDatatype"
    QUOTE_SYMBOL = "QuoteSymbol"
    CONTAINS_HEADER = "ContainsHeader"
    DELIMITER = "Delimiter"
    HEADER = "Header"
    ALLOW_SINGLE_COLUMN = "AllowSingleColumn"
    CUSTOM_DATATYPE_CONFIGURED = "CustomDatatypeConfigured"
    DISABLE_VALUE_TRIMMING = "DisableValueTrimming"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "contains_custom_datatype": "ContainsCustomDatatype",
        "quote_symbol": "QuoteSymbol",
        "contains_header": "ContainsHeader",
        "delimiter": "Delimiter",
        "header": "Header",
        "allow_single_column": "AllowSingleColumn",
        "custom_datatype_configured": "CustomDatatypeConfigured",
        "disable_value_trimming": "DisableValueTrimming",
        "name": "Name",
    }

    contains_custom_datatype: Optional[Union[list[str], Ref]] = None
    quote_symbol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    contains_header: Optional[Union[str, CsvHeaderOption, Ref, GetAtt, Sub]] = None
    delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    header: Optional[Union[list[str], Ref]] = None
    allow_single_column: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    custom_datatype_configured: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    disable_value_trimming: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GrokClassifier(PropertyType):
    CUSTOM_PATTERNS = "CustomPatterns"
    GROK_PATTERN = "GrokPattern"
    CLASSIFICATION = "Classification"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_patterns": "CustomPatterns",
        "grok_pattern": "GrokPattern",
        "classification": "Classification",
        "name": "Name",
    }

    custom_patterns: Optional[Union[str, Ref, GetAtt, Sub]] = None
    grok_pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None
    classification: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class JsonClassifier(PropertyType):
    JSON_PATH = "JsonPath"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "json_path": "JsonPath",
        "name": "Name",
    }

    json_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class XMLClassifier(PropertyType):
    ROW_TAG = "RowTag"
    CLASSIFICATION = "Classification"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "row_tag": "RowTag",
        "classification": "Classification",
        "name": "Name",
    }

    row_tag: Optional[Union[str, Ref, GetAtt, Sub]] = None
    classification: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

