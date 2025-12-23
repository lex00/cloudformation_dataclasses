"""PropertyTypes for AWS::Lightsail::Distribution."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CacheBehavior(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "behavior": "Behavior",
    }

    behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CacheBehaviorPerPath(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "path": "Path",
        "behavior": "Behavior",
    }

    path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    behavior: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CacheSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "forwarded_cookies": "ForwardedCookies",
        "minimum_ttl": "MinimumTTL",
        "cached_http_methods": "CachedHTTPMethods",
        "allowed_http_methods": "AllowedHTTPMethods",
        "maximum_ttl": "MaximumTTL",
        "forwarded_headers": "ForwardedHeaders",
        "default_ttl": "DefaultTTL",
        "forwarded_query_strings": "ForwardedQueryStrings",
    }

    forwarded_cookies: Optional[CookieObject] = None
    minimum_ttl: Optional[Union[int, Ref, GetAtt, Sub]] = None
    cached_http_methods: Optional[Union[str, Ref, GetAtt, Sub]] = None
    allowed_http_methods: Optional[Union[str, Ref, GetAtt, Sub]] = None
    maximum_ttl: Optional[Union[int, Ref, GetAtt, Sub]] = None
    forwarded_headers: Optional[HeaderObject] = None
    default_ttl: Optional[Union[int, Ref, GetAtt, Sub]] = None
    forwarded_query_strings: Optional[QueryStringObject] = None


@dataclass
class CookieObject(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cookies_allow_list": "CookiesAllowList",
        "option": "Option",
    }

    cookies_allow_list: Optional[Union[list[str], Ref]] = None
    option: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HeaderObject(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "headers_allow_list": "HeadersAllowList",
        "option": "Option",
    }

    headers_allow_list: Optional[Union[list[str], Ref]] = None
    option: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InputOrigin(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "region_name": "RegionName",
        "protocol_policy": "ProtocolPolicy",
        "name": "Name",
    }

    region_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class QueryStringObject(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "option": "Option",
        "query_strings_allow_list": "QueryStringsAllowList",
    }

    option: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    query_strings_allow_list: Optional[Union[list[str], Ref]] = None

