"""PropertyTypes for AWS::CloudFront::ResponseHeadersPolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccessControlAllowHeaders(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "items": "Items",
    }

    items: Optional[Union[list[str], Ref]] = None


@dataclass
class AccessControlAllowMethods(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "items": "Items",
    }

    items: Optional[Union[list[str], Ref]] = None


@dataclass
class AccessControlAllowOrigins(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "items": "Items",
    }

    items: Optional[Union[list[str], Ref]] = None


@dataclass
class AccessControlExposeHeaders(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "items": "Items",
    }

    items: Optional[Union[list[str], Ref]] = None


@dataclass
class ContentSecurityPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "content_security_policy": "ContentSecurityPolicy",
        "override": "Override",
    }

    content_security_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    override: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ContentTypeOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "override": "Override",
    }

    override: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CorsConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "access_control_allow_credentials": "AccessControlAllowCredentials",
        "access_control_allow_headers": "AccessControlAllowHeaders",
        "origin_override": "OriginOverride",
        "access_control_allow_methods": "AccessControlAllowMethods",
        "access_control_expose_headers": "AccessControlExposeHeaders",
        "access_control_allow_origins": "AccessControlAllowOrigins",
        "access_control_max_age_sec": "AccessControlMaxAgeSec",
    }

    access_control_allow_credentials: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    access_control_allow_headers: Optional[AccessControlAllowHeaders] = None
    origin_override: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    access_control_allow_methods: Optional[AccessControlAllowMethods] = None
    access_control_expose_headers: Optional[AccessControlExposeHeaders] = None
    access_control_allow_origins: Optional[AccessControlAllowOrigins] = None
    access_control_max_age_sec: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CustomHeader(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "header": "Header",
        "value": "Value",
        "override": "Override",
    }

    header: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    override: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CustomHeadersConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "items": "Items",
    }

    items: Optional[list[CustomHeader]] = None


@dataclass
class FrameOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "frame_option": "FrameOption",
        "override": "Override",
    }

    frame_option: Optional[Union[str, Ref, GetAtt, Sub]] = None
    override: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ReferrerPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "override": "Override",
        "referrer_policy": "ReferrerPolicy",
    }

    override: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    referrer_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RemoveHeader(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "header": "Header",
    }

    header: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RemoveHeadersConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "items": "Items",
    }

    items: Optional[list[RemoveHeader]] = None


@dataclass
class ResponseHeadersPolicyConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "comment": "Comment",
        "security_headers_config": "SecurityHeadersConfig",
        "remove_headers_config": "RemoveHeadersConfig",
        "cors_config": "CorsConfig",
        "server_timing_headers_config": "ServerTimingHeadersConfig",
        "custom_headers_config": "CustomHeadersConfig",
        "name": "Name",
    }

    comment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    security_headers_config: Optional[SecurityHeadersConfig] = None
    remove_headers_config: Optional[RemoveHeadersConfig] = None
    cors_config: Optional[CorsConfig] = None
    server_timing_headers_config: Optional[ServerTimingHeadersConfig] = None
    custom_headers_config: Optional[CustomHeadersConfig] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SecurityHeadersConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "content_security_policy": "ContentSecurityPolicy",
        "frame_options": "FrameOptions",
        "content_type_options": "ContentTypeOptions",
        "strict_transport_security": "StrictTransportSecurity",
        "xss_protection": "XSSProtection",
        "referrer_policy": "ReferrerPolicy",
    }

    content_security_policy: Optional[ContentSecurityPolicy] = None
    frame_options: Optional[FrameOptions] = None
    content_type_options: Optional[ContentTypeOptions] = None
    strict_transport_security: Optional[StrictTransportSecurity] = None
    xss_protection: Optional[XSSProtection] = None
    referrer_policy: Optional[ReferrerPolicy] = None


@dataclass
class ServerTimingHeadersConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "sampling_rate": "SamplingRate",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    sampling_rate: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class StrictTransportSecurity(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "preload": "Preload",
        "access_control_max_age_sec": "AccessControlMaxAgeSec",
        "include_subdomains": "IncludeSubdomains",
        "override": "Override",
    }

    preload: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    access_control_max_age_sec: Optional[Union[int, Ref, GetAtt, Sub]] = None
    include_subdomains: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    override: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class XSSProtection(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "report_uri": "ReportUri",
        "override": "Override",
        "protection": "Protection",
        "mode_block": "ModeBlock",
    }

    report_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    override: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    protection: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    mode_block: Optional[Union[bool, Ref, GetAtt, Sub]] = None

