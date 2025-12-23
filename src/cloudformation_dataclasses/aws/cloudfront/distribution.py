"""PropertyTypes for AWS::CloudFront::Distribution."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CacheBehavior(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "compress": "Compress",
        "function_associations": "FunctionAssociations",
        "lambda_function_associations": "LambdaFunctionAssociations",
        "target_origin_id": "TargetOriginId",
        "viewer_protocol_policy": "ViewerProtocolPolicy",
        "response_headers_policy_id": "ResponseHeadersPolicyId",
        "grpc_config": "GrpcConfig",
        "realtime_log_config_arn": "RealtimeLogConfigArn",
        "trusted_signers": "TrustedSigners",
        "default_ttl": "DefaultTTL",
        "field_level_encryption_id": "FieldLevelEncryptionId",
        "trusted_key_groups": "TrustedKeyGroups",
        "allowed_methods": "AllowedMethods",
        "path_pattern": "PathPattern",
        "cached_methods": "CachedMethods",
        "smooth_streaming": "SmoothStreaming",
        "forwarded_values": "ForwardedValues",
        "origin_request_policy_id": "OriginRequestPolicyId",
        "min_ttl": "MinTTL",
        "cache_policy_id": "CachePolicyId",
        "max_ttl": "MaxTTL",
    }

    compress: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    function_associations: Optional[list[FunctionAssociation]] = None
    lambda_function_associations: Optional[list[LambdaFunctionAssociation]] = None
    target_origin_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    viewer_protocol_policy: Optional[Union[str, ViewerProtocolPolicy, Ref, GetAtt, Sub]] = None
    response_headers_policy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    grpc_config: Optional[GrpcConfig] = None
    realtime_log_config_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trusted_signers: Optional[Union[list[str], Ref]] = None
    default_ttl: Optional[Union[float, Ref, GetAtt, Sub]] = None
    field_level_encryption_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trusted_key_groups: Optional[Union[list[str], Ref]] = None
    allowed_methods: Optional[Union[list[str], Ref]] = None
    path_pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cached_methods: Optional[Union[list[str], Ref]] = None
    smooth_streaming: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    forwarded_values: Optional[ForwardedValues] = None
    origin_request_policy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    min_ttl: Optional[Union[float, Ref, GetAtt, Sub]] = None
    cache_policy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_ttl: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectionFunctionAssociation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "Id",
    }

    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Cookies(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "whitelisted_names": "WhitelistedNames",
        "forward": "Forward",
    }

    whitelisted_names: Optional[Union[list[str], Ref]] = None
    forward: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomErrorResponse(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "response_code": "ResponseCode",
        "error_caching_min_ttl": "ErrorCachingMinTTL",
        "error_code": "ErrorCode",
        "response_page_path": "ResponsePagePath",
    }

    response_code: Optional[Union[int, Ref, GetAtt, Sub]] = None
    error_caching_min_ttl: Optional[Union[float, Ref, GetAtt, Sub]] = None
    error_code: Optional[Union[int, Ref, GetAtt, Sub]] = None
    response_page_path: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CustomOriginConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_address_type": "IpAddressType",
        "origin_read_timeout": "OriginReadTimeout",
        "https_port": "HTTPSPort",
        "origin_keepalive_timeout": "OriginKeepaliveTimeout",
        "origin_ssl_protocols": "OriginSSLProtocols",
        "http_port": "HTTPPort",
        "origin_protocol_policy": "OriginProtocolPolicy",
    }

    ip_address_type: Optional[Union[str, IpAddressType, Ref, GetAtt, Sub]] = None
    origin_read_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    https_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    origin_keepalive_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    origin_ssl_protocols: Optional[Union[list[str], Ref]] = None
    http_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    origin_protocol_policy: Optional[Union[str, OriginProtocolPolicy, Ref, GetAtt, Sub]] = None


@dataclass
class DefaultCacheBehavior(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "compress": "Compress",
        "function_associations": "FunctionAssociations",
        "lambda_function_associations": "LambdaFunctionAssociations",
        "target_origin_id": "TargetOriginId",
        "viewer_protocol_policy": "ViewerProtocolPolicy",
        "response_headers_policy_id": "ResponseHeadersPolicyId",
        "grpc_config": "GrpcConfig",
        "realtime_log_config_arn": "RealtimeLogConfigArn",
        "trusted_signers": "TrustedSigners",
        "default_ttl": "DefaultTTL",
        "field_level_encryption_id": "FieldLevelEncryptionId",
        "trusted_key_groups": "TrustedKeyGroups",
        "allowed_methods": "AllowedMethods",
        "cached_methods": "CachedMethods",
        "smooth_streaming": "SmoothStreaming",
        "forwarded_values": "ForwardedValues",
        "origin_request_policy_id": "OriginRequestPolicyId",
        "min_ttl": "MinTTL",
        "cache_policy_id": "CachePolicyId",
        "max_ttl": "MaxTTL",
    }

    compress: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    function_associations: Optional[list[FunctionAssociation]] = None
    lambda_function_associations: Optional[list[LambdaFunctionAssociation]] = None
    target_origin_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    viewer_protocol_policy: Optional[Union[str, ViewerProtocolPolicy, Ref, GetAtt, Sub]] = None
    response_headers_policy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    grpc_config: Optional[GrpcConfig] = None
    realtime_log_config_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trusted_signers: Optional[Union[list[str], Ref]] = None
    default_ttl: Optional[Union[float, Ref, GetAtt, Sub]] = None
    field_level_encryption_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trusted_key_groups: Optional[Union[list[str], Ref]] = None
    allowed_methods: Optional[Union[list[str], Ref]] = None
    cached_methods: Optional[Union[list[str], Ref]] = None
    smooth_streaming: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    forwarded_values: Optional[ForwardedValues] = None
    origin_request_policy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    min_ttl: Optional[Union[float, Ref, GetAtt, Sub]] = None
    cache_policy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_ttl: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class Definition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "string_schema": "StringSchema",
    }

    string_schema: Optional[StringSchema] = None


@dataclass
class DistributionConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "price_class": "PriceClass",
        "staging": "Staging",
        "custom_error_responses": "CustomErrorResponses",
        "continuous_deployment_policy_id": "ContinuousDeploymentPolicyId",
        "origin_groups": "OriginGroups",
        "connection_function_association": "ConnectionFunctionAssociation",
        "ipv6_enabled": "IPV6Enabled",
        "tenant_config": "TenantConfig",
        "cnam_es": "CNAMEs",
        "viewer_mtls_config": "ViewerMtlsConfig",
        "http_version": "HttpVersion",
        "restrictions": "Restrictions",
        "cache_behaviors": "CacheBehaviors",
        "logging": "Logging",
        "comment": "Comment",
        "default_root_object": "DefaultRootObject",
        "origins": "Origins",
        "viewer_certificate": "ViewerCertificate",
        "anycast_ip_list_id": "AnycastIpListId",
        "custom_origin": "CustomOrigin",
        "s3_origin": "S3Origin",
        "default_cache_behavior": "DefaultCacheBehavior",
        "enabled": "Enabled",
        "aliases": "Aliases",
        "connection_mode": "ConnectionMode",
        "web_acl_id": "WebACLId",
    }

    price_class: Optional[Union[str, PriceClass, Ref, GetAtt, Sub]] = None
    staging: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    custom_error_responses: Optional[list[CustomErrorResponse]] = None
    continuous_deployment_policy_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    origin_groups: Optional[OriginGroups] = None
    connection_function_association: Optional[ConnectionFunctionAssociation] = None
    ipv6_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    tenant_config: Optional[TenantConfig] = None
    cnam_es: Optional[Union[list[str], Ref]] = None
    viewer_mtls_config: Optional[ViewerMtlsConfig] = None
    http_version: Optional[Union[str, HttpVersion, Ref, GetAtt, Sub]] = None
    restrictions: Optional[Restrictions] = None
    cache_behaviors: Optional[list[CacheBehavior]] = None
    logging: Optional[Logging] = None
    comment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default_root_object: Optional[Union[str, Ref, GetAtt, Sub]] = None
    origins: Optional[list[Origin]] = None
    viewer_certificate: Optional[ViewerCertificate] = None
    anycast_ip_list_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_origin: Optional[LegacyCustomOrigin] = None
    s3_origin: Optional[LegacyS3Origin] = None
    default_cache_behavior: Optional[DefaultCacheBehavior] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    aliases: Optional[Union[list[str], Ref]] = None
    connection_mode: Optional[Union[str, ConnectionMode, Ref, GetAtt, Sub]] = None
    web_acl_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ForwardedValues(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cookies": "Cookies",
        "headers": "Headers",
        "query_string": "QueryString",
        "query_string_cache_keys": "QueryStringCacheKeys",
    }

    cookies: Optional[Cookies] = None
    headers: Optional[Union[list[str], Ref]] = None
    query_string: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    query_string_cache_keys: Optional[Union[list[str], Ref]] = None


@dataclass
class FunctionAssociation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "function_arn": "FunctionARN",
        "event_type": "EventType",
    }

    function_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    event_type: Optional[Union[str, EventType, Ref, GetAtt, Sub]] = None


@dataclass
class GeoRestriction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "locations": "Locations",
        "restriction_type": "RestrictionType",
    }

    locations: Optional[Union[list[str], Ref]] = None
    restriction_type: Optional[Union[str, GeoRestrictionType, Ref, GetAtt, Sub]] = None


@dataclass
class GrpcConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class LambdaFunctionAssociation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "include_body": "IncludeBody",
        "event_type": "EventType",
        "lambda_function_arn": "LambdaFunctionARN",
    }

    include_body: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    event_type: Optional[Union[str, EventType, Ref, GetAtt, Sub]] = None
    lambda_function_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LegacyCustomOrigin(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "https_port": "HTTPSPort",
        "origin_ssl_protocols": "OriginSSLProtocols",
        "dns_name": "DNSName",
        "http_port": "HTTPPort",
        "origin_protocol_policy": "OriginProtocolPolicy",
    }

    https_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    origin_ssl_protocols: Optional[Union[list[str], Ref]] = None
    dns_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    http_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    origin_protocol_policy: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LegacyS3Origin(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "origin_access_identity": "OriginAccessIdentity",
        "dns_name": "DNSName",
    }

    origin_access_identity: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dns_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Logging(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "include_cookies": "IncludeCookies",
        "bucket": "Bucket",
        "prefix": "Prefix",
    }

    include_cookies: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Origin(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "connection_timeout": "ConnectionTimeout",
        "origin_access_control_id": "OriginAccessControlId",
        "connection_attempts": "ConnectionAttempts",
        "origin_custom_headers": "OriginCustomHeaders",
        "domain_name": "DomainName",
        "origin_shield": "OriginShield",
        "s3_origin_config": "S3OriginConfig",
        "vpc_origin_config": "VpcOriginConfig",
        "origin_path": "OriginPath",
        "response_completion_timeout": "ResponseCompletionTimeout",
        "id": "Id",
        "custom_origin_config": "CustomOriginConfig",
    }

    connection_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    origin_access_control_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connection_attempts: Optional[Union[int, Ref, GetAtt, Sub]] = None
    origin_custom_headers: Optional[list[OriginCustomHeader]] = None
    domain_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    origin_shield: Optional[OriginShield] = None
    s3_origin_config: Optional[S3OriginConfig] = None
    vpc_origin_config: Optional[VpcOriginConfig] = None
    origin_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    response_completion_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    custom_origin_config: Optional[CustomOriginConfig] = None


@dataclass
class OriginCustomHeader(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "header_value": "HeaderValue",
        "header_name": "HeaderName",
    }

    header_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    header_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OriginGroup(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "selection_criteria": "SelectionCriteria",
        "id": "Id",
        "failover_criteria": "FailoverCriteria",
        "members": "Members",
    }

    selection_criteria: Optional[Union[str, OriginGroupSelectionCriteria, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    failover_criteria: Optional[OriginGroupFailoverCriteria] = None
    members: Optional[OriginGroupMembers] = None


@dataclass
class OriginGroupFailoverCriteria(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status_codes": "StatusCodes",
    }

    status_codes: Optional[StatusCodes] = None


@dataclass
class OriginGroupMember(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "origin_id": "OriginId",
    }

    origin_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OriginGroupMembers(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "quantity": "Quantity",
        "items": "Items",
    }

    quantity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    items: Optional[list[OriginGroupMember]] = None


@dataclass
class OriginGroups(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "quantity": "Quantity",
        "items": "Items",
    }

    quantity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    items: Optional[list[OriginGroup]] = None


@dataclass
class OriginShield(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "origin_shield_region": "OriginShieldRegion",
        "enabled": "Enabled",
    }

    origin_shield_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ParameterDefinition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "definition": "Definition",
        "name": "Name",
    }

    definition: Optional[Definition] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Restrictions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "geo_restriction": "GeoRestriction",
    }

    geo_restriction: Optional[GeoRestriction] = None


@dataclass
class S3OriginConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "origin_read_timeout": "OriginReadTimeout",
        "origin_access_identity": "OriginAccessIdentity",
    }

    origin_read_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    origin_access_identity: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StatusCodes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "quantity": "Quantity",
        "items": "Items",
    }

    quantity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    items: Optional[Union[list[int], Ref]] = None


@dataclass
class StringSchema(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "comment": "Comment",
        "default_value": "DefaultValue",
        "required": "Required",
    }

    comment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    required: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class TenantConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_definitions": "ParameterDefinitions",
    }

    parameter_definitions: Optional[list[ParameterDefinition]] = None


@dataclass
class TrustStoreConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "trust_store_id": "TrustStoreId",
        "ignore_certificate_expiry": "IgnoreCertificateExpiry",
        "advertise_trust_store_ca_names": "AdvertiseTrustStoreCaNames",
    }

    trust_store_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ignore_certificate_expiry: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    advertise_trust_store_ca_names: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ViewerCertificate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iam_certificate_id": "IamCertificateId",
        "ssl_support_method": "SslSupportMethod",
        "minimum_protocol_version": "MinimumProtocolVersion",
        "cloud_front_default_certificate": "CloudFrontDefaultCertificate",
        "acm_certificate_arn": "AcmCertificateArn",
    }

    iam_certificate_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ssl_support_method: Optional[Union[str, Ref, GetAtt, Sub]] = None
    minimum_protocol_version: Optional[Union[str, MinimumProtocolVersion, Ref, GetAtt, Sub]] = None
    cloud_front_default_certificate: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    acm_certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ViewerMtlsConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mode": "Mode",
        "trust_store_config": "TrustStoreConfig",
    }

    mode: Optional[Union[str, ViewerMtlsMode, Ref, GetAtt, Sub]] = None
    trust_store_config: Optional[TrustStoreConfig] = None


@dataclass
class VpcOriginConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "origin_read_timeout": "OriginReadTimeout",
        "vpc_origin_id": "VpcOriginId",
        "origin_keepalive_timeout": "OriginKeepaliveTimeout",
        "owner_account_id": "OwnerAccountId",
    }

    origin_read_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    vpc_origin_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    origin_keepalive_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    owner_account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

