"""PropertyTypes for AWS::CloudFront::OriginRequestPolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CookiesConfig(PropertyType):
    COOKIES = "Cookies"
    COOKIE_BEHAVIOR = "CookieBehavior"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cookies": "Cookies",
        "cookie_behavior": "CookieBehavior",
    }

    cookies: Optional[Union[list[str], Ref]] = None
    cookie_behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HeadersConfig(PropertyType):
    HEADERS = "Headers"
    HEADER_BEHAVIOR = "HeaderBehavior"

    _property_mappings: ClassVar[dict[str, str]] = {
        "headers": "Headers",
        "header_behavior": "HeaderBehavior",
    }

    headers: Optional[Union[list[str], Ref]] = None
    header_behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OriginRequestPolicyConfig(PropertyType):
    COMMENT = "Comment"
    HEADERS_CONFIG = "HeadersConfig"
    COOKIES_CONFIG = "CookiesConfig"
    QUERY_STRINGS_CONFIG = "QueryStringsConfig"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comment": "Comment",
        "headers_config": "HeadersConfig",
        "cookies_config": "CookiesConfig",
        "query_strings_config": "QueryStringsConfig",
        "name": "Name",
    }

    comment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    headers_config: Optional[HeadersConfig] = None
    cookies_config: Optional[CookiesConfig] = None
    query_strings_config: Optional[QueryStringsConfig] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QueryStringsConfig(PropertyType):
    QUERY_STRINGS = "QueryStrings"
    QUERY_STRING_BEHAVIOR = "QueryStringBehavior"

    _property_mappings: ClassVar[dict[str, str]] = {
        "query_strings": "QueryStrings",
        "query_string_behavior": "QueryStringBehavior",
    }

    query_strings: Optional[Union[list[str], Ref]] = None
    query_string_behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None

