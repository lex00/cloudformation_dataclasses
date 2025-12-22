"""PropertyTypes for AWS::CloudFront::ResponseHeadersPolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class CachePolicyCookieBehavior:
    """CachePolicyCookieBehavior enum values."""

    NONE = "none"
    WHITELIST = "whitelist"
    ALLEXCEPT = "allExcept"
    ALL = "all"


class CachePolicyHeaderBehavior:
    """CachePolicyHeaderBehavior enum values."""

    NONE = "none"
    WHITELIST = "whitelist"


class CachePolicyQueryStringBehavior:
    """CachePolicyQueryStringBehavior enum values."""

    NONE = "none"
    WHITELIST = "whitelist"
    ALLEXCEPT = "allExcept"
    ALL = "all"


class CachePolicyType:
    """CachePolicyType enum values."""

    MANAGED = "managed"
    CUSTOM = "custom"


class CertificateSource:
    """CertificateSource enum values."""

    CLOUDFRONT = "cloudfront"
    IAM = "iam"
    ACM = "acm"


class CertificateTransparencyLoggingPreference:
    """CertificateTransparencyLoggingPreference enum values."""

    ENABLED = "enabled"
    DISABLED = "disabled"


class ConnectionMode:
    """ConnectionMode enum values."""

    DIRECT = "direct"
    TENANT_ONLY = "tenant-only"


class ContinuousDeploymentPolicyType:
    """ContinuousDeploymentPolicyType enum values."""

    SINGLEWEIGHT = "SingleWeight"
    SINGLEHEADER = "SingleHeader"


class CustomizationActionType:
    """CustomizationActionType enum values."""

    OVERRIDE = "override"
    DISABLE = "disable"


class DistributionResourceType:
    """DistributionResourceType enum values."""

    DISTRIBUTION = "distribution"
    DISTRIBUTION_TENANT = "distribution-tenant"


class DnsConfigurationStatus:
    """DnsConfigurationStatus enum values."""

    VALID_CONFIGURATION = "valid-configuration"
    INVALID_CONFIGURATION = "invalid-configuration"
    UNKNOWN_CONFIGURATION = "unknown-configuration"


class DomainStatus:
    """DomainStatus enum values."""

    ACTIVE = "active"
    INACTIVE = "inactive"


class EventType:
    """EventType enum values."""

    VIEWER_REQUEST = "viewer-request"
    VIEWER_RESPONSE = "viewer-response"
    ORIGIN_REQUEST = "origin-request"
    ORIGIN_RESPONSE = "origin-response"


class Format:
    """Format enum values."""

    URLENCODED = "URLEncoded"


class FrameOptionsList:
    """FrameOptionsList enum values."""

    DENY = "DENY"
    SAMEORIGIN = "SAMEORIGIN"


class FunctionRuntime:
    """FunctionRuntime enum values."""

    CLOUDFRONT_JS_1_0 = "cloudfront-js-1.0"
    CLOUDFRONT_JS_2_0 = "cloudfront-js-2.0"


class FunctionStage:
    """FunctionStage enum values."""

    DEVELOPMENT = "DEVELOPMENT"
    LIVE = "LIVE"


class GeoRestrictionType:
    """GeoRestrictionType enum values."""

    BLACKLIST = "blacklist"
    WHITELIST = "whitelist"
    NONE = "none"


class HttpVersion:
    """HttpVersion enum values."""

    HTTP1_1 = "http1.1"
    HTTP2 = "http2"
    HTTP3 = "http3"
    HTTP2AND3 = "http2and3"


class ICPRecordalStatus:
    """ICPRecordalStatus enum values."""

    APPROVED = "APPROVED"
    SUSPENDED = "SUSPENDED"
    PENDING = "PENDING"


class ImportSourceType:
    """ImportSourceType enum values."""

    S3 = "S3"


class IpAddressType:
    """IpAddressType enum values."""

    IPV4 = "ipv4"
    IPV6 = "ipv6"
    DUALSTACK = "dualstack"


class IpamCidrStatus:
    """IpamCidrStatus enum values."""

    PROVISIONED = "provisioned"
    FAILED_PROVISION = "failed-provision"
    PROVISIONING = "provisioning"
    DEPROVISIONED = "deprovisioned"
    FAILED_DEPROVISION = "failed-deprovision"
    DEPROVISIONING = "deprovisioning"
    ADVERTISED = "advertised"
    FAILED_ADVERTISE = "failed-advertise"
    ADVERTISING = "advertising"
    WITHDRAWN = "withdrawn"
    FAILED_WITHDRAW = "failed-withdraw"
    WITHDRAWING = "withdrawing"


class ItemSelection:
    """ItemSelection enum values."""

    NONE = "none"
    WHITELIST = "whitelist"
    ALL = "all"


class ManagedCertificateStatus:
    """ManagedCertificateStatus enum values."""

    PENDING_VALIDATION = "pending-validation"
    ISSUED = "issued"
    INACTIVE = "inactive"
    EXPIRED = "expired"
    VALIDATION_TIMED_OUT = "validation-timed-out"
    REVOKED = "revoked"
    FAILED = "failed"


class Method:
    """Method enum values."""

    GET = "GET"
    HEAD = "HEAD"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    OPTIONS = "OPTIONS"
    DELETE = "DELETE"


class MinimumProtocolVersion:
    """MinimumProtocolVersion enum values."""

    SSLV3 = "SSLv3"
    TLSV1 = "TLSv1"
    TLSV1_2016 = "TLSv1_2016"
    TLSV1_1_2016 = "TLSv1.1_2016"
    TLSV1_2_2018 = "TLSv1.2_2018"
    TLSV1_2_2019 = "TLSv1.2_2019"
    TLSV1_2_2021 = "TLSv1.2_2021"
    TLSV1_3_2025 = "TLSv1.3_2025"
    TLSV1_2_2025 = "TLSv1.2_2025"


class OriginAccessControlOriginTypes:
    """OriginAccessControlOriginTypes enum values."""

    S3 = "s3"
    MEDIASTORE = "mediastore"
    MEDIAPACKAGEV2 = "mediapackagev2"
    LAMBDA = "lambda"


class OriginAccessControlSigningBehaviors:
    """OriginAccessControlSigningBehaviors enum values."""

    NEVER = "never"
    ALWAYS = "always"
    NO_OVERRIDE = "no-override"


class OriginAccessControlSigningProtocols:
    """OriginAccessControlSigningProtocols enum values."""

    SIGV4 = "sigv4"


class OriginGroupSelectionCriteria:
    """OriginGroupSelectionCriteria enum values."""

    DEFAULT = "default"
    MEDIA_QUALITY_BASED = "media-quality-based"


class OriginProtocolPolicy:
    """OriginProtocolPolicy enum values."""

    HTTP_ONLY = "http-only"
    MATCH_VIEWER = "match-viewer"
    HTTPS_ONLY = "https-only"


class OriginRequestPolicyCookieBehavior:
    """OriginRequestPolicyCookieBehavior enum values."""

    NONE = "none"
    WHITELIST = "whitelist"
    ALL = "all"
    ALLEXCEPT = "allExcept"


class OriginRequestPolicyHeaderBehavior:
    """OriginRequestPolicyHeaderBehavior enum values."""

    NONE = "none"
    WHITELIST = "whitelist"
    ALLVIEWER = "allViewer"
    ALLVIEWERANDWHITELISTCLOUDFRONT = "allViewerAndWhitelistCloudFront"
    ALLEXCEPT = "allExcept"


class OriginRequestPolicyQueryStringBehavior:
    """OriginRequestPolicyQueryStringBehavior enum values."""

    NONE = "none"
    WHITELIST = "whitelist"
    ALL = "all"
    ALLEXCEPT = "allExcept"


class OriginRequestPolicyType:
    """OriginRequestPolicyType enum values."""

    MANAGED = "managed"
    CUSTOM = "custom"


class PriceClass:
    """PriceClass enum values."""

    PRICECLASS_100 = "PriceClass_100"
    PRICECLASS_200 = "PriceClass_200"
    PRICECLASS_ALL = "PriceClass_All"
    NONE = "None"


class RealtimeMetricsSubscriptionStatus:
    """RealtimeMetricsSubscriptionStatus enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ReferrerPolicyList:
    """ReferrerPolicyList enum values."""

    NO_REFERRER = "no-referrer"
    NO_REFERRER_WHEN_DOWNGRADE = "no-referrer-when-downgrade"
    ORIGIN = "origin"
    ORIGIN_WHEN_CROSS_ORIGIN = "origin-when-cross-origin"
    SAME_ORIGIN = "same-origin"
    STRICT_ORIGIN = "strict-origin"
    STRICT_ORIGIN_WHEN_CROSS_ORIGIN = "strict-origin-when-cross-origin"
    UNSAFE_URL = "unsafe-url"


class ResponseHeadersPolicyAccessControlAllowMethodsValues:
    """ResponseHeadersPolicyAccessControlAllowMethodsValues enum values."""

    GET = "GET"
    POST = "POST"
    OPTIONS = "OPTIONS"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    HEAD = "HEAD"
    ALL = "ALL"


class ResponseHeadersPolicyType:
    """ResponseHeadersPolicyType enum values."""

    MANAGED = "managed"
    CUSTOM = "custom"


class SSLSupportMethod:
    """SSLSupportMethod enum values."""

    SNI_ONLY = "sni-only"
    VIP = "vip"
    STATIC_IP = "static-ip"


class SslProtocol:
    """SslProtocol enum values."""

    SSLV3 = "SSLv3"
    TLSV1 = "TLSv1"
    TLSV1_1 = "TLSv1.1"
    TLSV1_2 = "TLSv1.2"


class TrustStoreStatus:
    """TrustStoreStatus enum values."""

    PENDING = "pending"
    ACTIVE = "active"
    FAILED = "failed"


class ValidationTokenHost:
    """ValidationTokenHost enum values."""

    CLOUDFRONT = "cloudfront"
    SELF_HOSTED = "self-hosted"


class ViewerMtlsMode:
    """ViewerMtlsMode enum values."""

    REQUIRED = "required"
    OPTIONAL = "optional"


class ViewerProtocolPolicy:
    """ViewerProtocolPolicy enum values."""

    ALLOW_ALL = "allow-all"
    HTTPS_ONLY = "https-only"
    REDIRECT_TO_HTTPS = "redirect-to-https"


@dataclass
class AccessControlAllowHeaders(PropertyType):
    ITEMS = "Items"

    _property_mappings: ClassVar[dict[str, str]] = {
        "items": "Items",
    }

    items: Optional[Union[list[str], Ref]] = None


@dataclass
class AccessControlAllowMethods(PropertyType):
    ITEMS = "Items"

    _property_mappings: ClassVar[dict[str, str]] = {
        "items": "Items",
    }

    items: Optional[Union[list[str], Ref]] = None


@dataclass
class AccessControlAllowOrigins(PropertyType):
    ITEMS = "Items"

    _property_mappings: ClassVar[dict[str, str]] = {
        "items": "Items",
    }

    items: Optional[Union[list[str], Ref]] = None


@dataclass
class AccessControlExposeHeaders(PropertyType):
    ITEMS = "Items"

    _property_mappings: ClassVar[dict[str, str]] = {
        "items": "Items",
    }

    items: Optional[Union[list[str], Ref]] = None


@dataclass
class ContentSecurityPolicy(PropertyType):
    CONTENT_SECURITY_POLICY = "ContentSecurityPolicy"
    OVERRIDE = "Override"

    _property_mappings: ClassVar[dict[str, str]] = {
        "content_security_policy": "ContentSecurityPolicy",
        "override": "Override",
    }

    content_security_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None
    override: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ContentTypeOptions(PropertyType):
    OVERRIDE = "Override"

    _property_mappings: ClassVar[dict[str, str]] = {
        "override": "Override",
    }

    override: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CorsConfig(PropertyType):
    ACCESS_CONTROL_ALLOW_CREDENTIALS = "AccessControlAllowCredentials"
    ACCESS_CONTROL_ALLOW_HEADERS = "AccessControlAllowHeaders"
    ORIGIN_OVERRIDE = "OriginOverride"
    ACCESS_CONTROL_ALLOW_METHODS = "AccessControlAllowMethods"
    ACCESS_CONTROL_EXPOSE_HEADERS = "AccessControlExposeHeaders"
    ACCESS_CONTROL_ALLOW_ORIGINS = "AccessControlAllowOrigins"
    ACCESS_CONTROL_MAX_AGE_SEC = "AccessControlMaxAgeSec"

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
    HEADER = "Header"
    VALUE = "Value"
    OVERRIDE = "Override"

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
    ITEMS = "Items"

    _property_mappings: ClassVar[dict[str, str]] = {
        "items": "Items",
    }

    items: Optional[list[CustomHeader]] = None


@dataclass
class FrameOptions(PropertyType):
    FRAME_OPTION = "FrameOption"
    OVERRIDE = "Override"

    _property_mappings: ClassVar[dict[str, str]] = {
        "frame_option": "FrameOption",
        "override": "Override",
    }

    frame_option: Optional[Union[str, Ref, GetAtt, Sub]] = None
    override: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ReferrerPolicy(PropertyType):
    OVERRIDE = "Override"
    REFERRER_POLICY = "ReferrerPolicy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "override": "Override",
        "referrer_policy": "ReferrerPolicy",
    }

    override: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    referrer_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RemoveHeader(PropertyType):
    HEADER = "Header"

    _property_mappings: ClassVar[dict[str, str]] = {
        "header": "Header",
    }

    header: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RemoveHeadersConfig(PropertyType):
    ITEMS = "Items"

    _property_mappings: ClassVar[dict[str, str]] = {
        "items": "Items",
    }

    items: Optional[list[RemoveHeader]] = None


@dataclass
class ResponseHeadersPolicyConfig(PropertyType):
    COMMENT = "Comment"
    SECURITY_HEADERS_CONFIG = "SecurityHeadersConfig"
    REMOVE_HEADERS_CONFIG = "RemoveHeadersConfig"
    CORS_CONFIG = "CorsConfig"
    SERVER_TIMING_HEADERS_CONFIG = "ServerTimingHeadersConfig"
    CUSTOM_HEADERS_CONFIG = "CustomHeadersConfig"
    NAME = "Name"

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
    CONTENT_SECURITY_POLICY = "ContentSecurityPolicy"
    FRAME_OPTIONS = "FrameOptions"
    CONTENT_TYPE_OPTIONS = "ContentTypeOptions"
    STRICT_TRANSPORT_SECURITY = "StrictTransportSecurity"
    XSS_PROTECTION = "XSSProtection"
    REFERRER_POLICY = "ReferrerPolicy"

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
    ENABLED = "Enabled"
    SAMPLING_RATE = "SamplingRate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "sampling_rate": "SamplingRate",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    sampling_rate: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class StrictTransportSecurity(PropertyType):
    PRELOAD = "Preload"
    ACCESS_CONTROL_MAX_AGE_SEC = "AccessControlMaxAgeSec"
    INCLUDE_SUBDOMAINS = "IncludeSubdomains"
    OVERRIDE = "Override"

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
    REPORT_URI = "ReportUri"
    OVERRIDE = "Override"
    PROTECTION = "Protection"
    MODE_BLOCK = "ModeBlock"

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

