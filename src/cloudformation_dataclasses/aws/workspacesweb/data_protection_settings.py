"""PropertyTypes for AWS::WorkSpacesWeb::DataProtectionSettings."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CustomPattern(PropertyType):
    KEYWORD_REGEX = "KeywordRegex"
    PATTERN_DESCRIPTION = "PatternDescription"
    PATTERN_NAME = "PatternName"
    PATTERN_REGEX = "PatternRegex"

    _property_mappings: ClassVar[dict[str, str]] = {
        "keyword_regex": "KeywordRegex",
        "pattern_description": "PatternDescription",
        "pattern_name": "PatternName",
        "pattern_regex": "PatternRegex",
    }

    keyword_regex: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pattern_description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pattern_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    pattern_regex: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InlineRedactionConfiguration(PropertyType):
    INLINE_REDACTION_PATTERNS = "InlineRedactionPatterns"
    GLOBAL_CONFIDENCE_LEVEL = "GlobalConfidenceLevel"
    GLOBAL_EXEMPT_URLS = "GlobalExemptUrls"
    GLOBAL_ENFORCED_URLS = "GlobalEnforcedUrls"

    _property_mappings: ClassVar[dict[str, str]] = {
        "inline_redaction_patterns": "InlineRedactionPatterns",
        "global_confidence_level": "GlobalConfidenceLevel",
        "global_exempt_urls": "GlobalExemptUrls",
        "global_enforced_urls": "GlobalEnforcedUrls",
    }

    inline_redaction_patterns: Optional[list[InlineRedactionPattern]] = None
    global_confidence_level: Optional[Union[float, Ref, GetAtt, Sub]] = None
    global_exempt_urls: Optional[Union[list[str], Ref]] = None
    global_enforced_urls: Optional[Union[list[str], Ref]] = None


@dataclass
class InlineRedactionPattern(PropertyType):
    ENFORCED_URLS = "EnforcedUrls"
    CONFIDENCE_LEVEL = "ConfidenceLevel"
    CUSTOM_PATTERN = "CustomPattern"
    EXEMPT_URLS = "ExemptUrls"
    BUILT_IN_PATTERN_ID = "BuiltInPatternId"
    REDACTION_PLACE_HOLDER = "RedactionPlaceHolder"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enforced_urls": "EnforcedUrls",
        "confidence_level": "ConfidenceLevel",
        "custom_pattern": "CustomPattern",
        "exempt_urls": "ExemptUrls",
        "built_in_pattern_id": "BuiltInPatternId",
        "redaction_place_holder": "RedactionPlaceHolder",
    }

    enforced_urls: Optional[Union[list[str], Ref]] = None
    confidence_level: Optional[Union[float, Ref, GetAtt, Sub]] = None
    custom_pattern: Optional[CustomPattern] = None
    exempt_urls: Optional[Union[list[str], Ref]] = None
    built_in_pattern_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    redaction_place_holder: Optional[RedactionPlaceHolder] = None


@dataclass
class RedactionPlaceHolder(PropertyType):
    REDACTION_PLACE_HOLDER_TYPE = "RedactionPlaceHolderType"
    REDACTION_PLACE_HOLDER_TEXT = "RedactionPlaceHolderText"

    _property_mappings: ClassVar[dict[str, str]] = {
        "redaction_place_holder_type": "RedactionPlaceHolderType",
        "redaction_place_holder_text": "RedactionPlaceHolderText",
    }

    redaction_place_holder_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    redaction_place_holder_text: Optional[Union[str, Ref, GetAtt, Sub]] = None

