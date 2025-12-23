"""PropertyTypes for AWS::CloudFront::CachePolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CachePolicyConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "comment": "Comment",
        "min_ttl": "MinTTL",
        "max_ttl": "MaxTTL",
        "parameters_in_cache_key_and_forwarded_to_origin": "ParametersInCacheKeyAndForwardedToOrigin",
        "default_ttl": "DefaultTTL",
        "name": "Name",
    }

    comment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    min_ttl: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max_ttl: Optional[Union[float, Ref, GetAtt, Sub]] = None
    parameters_in_cache_key_and_forwarded_to_origin: Optional[ParametersInCacheKeyAndForwardedToOrigin] = None
    default_ttl: Optional[Union[float, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CookiesConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cookies": "Cookies",
        "cookie_behavior": "CookieBehavior",
    }

    cookies: Optional[Union[list[str], Ref]] = None
    cookie_behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HeadersConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "headers": "Headers",
        "header_behavior": "HeaderBehavior",
    }

    headers: Optional[Union[list[str], Ref]] = None
    header_behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ParametersInCacheKeyAndForwardedToOrigin(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_accept_encoding_brotli": "EnableAcceptEncodingBrotli",
        "headers_config": "HeadersConfig",
        "cookies_config": "CookiesConfig",
        "enable_accept_encoding_gzip": "EnableAcceptEncodingGzip",
        "query_strings_config": "QueryStringsConfig",
    }

    enable_accept_encoding_brotli: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    headers_config: Optional[HeadersConfig] = None
    cookies_config: Optional[CookiesConfig] = None
    enable_accept_encoding_gzip: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    query_strings_config: Optional[QueryStringsConfig] = None


@dataclass
class QueryStringsConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "query_strings": "QueryStrings",
        "query_string_behavior": "QueryStringBehavior",
    }

    query_strings: Optional[Union[list[str], Ref]] = None
    query_string_behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None

