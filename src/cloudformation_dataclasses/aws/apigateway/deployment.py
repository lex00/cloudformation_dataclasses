"""PropertyTypes for AWS::ApiGateway::Deployment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccessLogSetting(PropertyType):
    FORMAT = "Format"
    DESTINATION_ARN = "DestinationArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "format": "Format",
        "destination_arn": "DestinationArn",
    }

    format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CanarySetting(PropertyType):
    STAGE_VARIABLE_OVERRIDES = "StageVariableOverrides"
    PERCENT_TRAFFIC = "PercentTraffic"
    USE_STAGE_CACHE = "UseStageCache"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stage_variable_overrides": "StageVariableOverrides",
        "percent_traffic": "PercentTraffic",
        "use_stage_cache": "UseStageCache",
    }

    stage_variable_overrides: Optional[dict[str, str]] = None
    percent_traffic: Optional[Union[float, Ref, GetAtt, Sub]] = None
    use_stage_cache: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentCanarySettings(PropertyType):
    STAGE_VARIABLE_OVERRIDES = "StageVariableOverrides"
    PERCENT_TRAFFIC = "PercentTraffic"
    USE_STAGE_CACHE = "UseStageCache"

    _property_mappings: ClassVar[dict[str, str]] = {
        "stage_variable_overrides": "StageVariableOverrides",
        "percent_traffic": "PercentTraffic",
        "use_stage_cache": "UseStageCache",
    }

    stage_variable_overrides: Optional[dict[str, str]] = None
    percent_traffic: Optional[Union[float, Ref, GetAtt, Sub]] = None
    use_stage_cache: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MethodSetting(PropertyType):
    CACHE_TTL_IN_SECONDS = "CacheTtlInSeconds"
    LOGGING_LEVEL = "LoggingLevel"
    RESOURCE_PATH = "ResourcePath"
    CACHE_DATA_ENCRYPTED = "CacheDataEncrypted"
    DATA_TRACE_ENABLED = "DataTraceEnabled"
    THROTTLING_BURST_LIMIT = "ThrottlingBurstLimit"
    CACHING_ENABLED = "CachingEnabled"
    METRICS_ENABLED = "MetricsEnabled"
    HTTP_METHOD = "HttpMethod"
    THROTTLING_RATE_LIMIT = "ThrottlingRateLimit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cache_ttl_in_seconds": "CacheTtlInSeconds",
        "logging_level": "LoggingLevel",
        "resource_path": "ResourcePath",
        "cache_data_encrypted": "CacheDataEncrypted",
        "data_trace_enabled": "DataTraceEnabled",
        "throttling_burst_limit": "ThrottlingBurstLimit",
        "caching_enabled": "CachingEnabled",
        "metrics_enabled": "MetricsEnabled",
        "http_method": "HttpMethod",
        "throttling_rate_limit": "ThrottlingRateLimit",
    }

    cache_ttl_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    logging_level: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cache_data_encrypted: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    data_trace_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    throttling_burst_limit: Optional[Union[int, Ref, GetAtt, Sub]] = None
    caching_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    metrics_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    http_method: Optional[Union[str, Ref, GetAtt, Sub]] = None
    throttling_rate_limit: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class StageDescription(PropertyType):
    CACHE_TTL_IN_SECONDS = "CacheTtlInSeconds"
    DESCRIPTION = "Description"
    LOGGING_LEVEL = "LoggingLevel"
    CANARY_SETTING = "CanarySetting"
    THROTTLING_RATE_LIMIT = "ThrottlingRateLimit"
    CLIENT_CERTIFICATE_ID = "ClientCertificateId"
    VARIABLES = "Variables"
    DOCUMENTATION_VERSION = "DocumentationVersion"
    CACHE_DATA_ENCRYPTED = "CacheDataEncrypted"
    DATA_TRACE_ENABLED = "DataTraceEnabled"
    THROTTLING_BURST_LIMIT = "ThrottlingBurstLimit"
    CACHING_ENABLED = "CachingEnabled"
    TRACING_ENABLED = "TracingEnabled"
    METHOD_SETTINGS = "MethodSettings"
    ACCESS_LOG_SETTING = "AccessLogSetting"
    CACHE_CLUSTER_SIZE = "CacheClusterSize"
    METRICS_ENABLED = "MetricsEnabled"
    TAGS = "Tags"
    CACHE_CLUSTER_ENABLED = "CacheClusterEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cache_ttl_in_seconds": "CacheTtlInSeconds",
        "description": "Description",
        "logging_level": "LoggingLevel",
        "canary_setting": "CanarySetting",
        "throttling_rate_limit": "ThrottlingRateLimit",
        "client_certificate_id": "ClientCertificateId",
        "variables": "Variables",
        "documentation_version": "DocumentationVersion",
        "cache_data_encrypted": "CacheDataEncrypted",
        "data_trace_enabled": "DataTraceEnabled",
        "throttling_burst_limit": "ThrottlingBurstLimit",
        "caching_enabled": "CachingEnabled",
        "tracing_enabled": "TracingEnabled",
        "method_settings": "MethodSettings",
        "access_log_setting": "AccessLogSetting",
        "cache_cluster_size": "CacheClusterSize",
        "metrics_enabled": "MetricsEnabled",
        "tags": "Tags",
        "cache_cluster_enabled": "CacheClusterEnabled",
    }

    cache_ttl_in_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    logging_level: Optional[Union[str, Ref, GetAtt, Sub]] = None
    canary_setting: Optional[CanarySetting] = None
    throttling_rate_limit: Optional[Union[float, Ref, GetAtt, Sub]] = None
    client_certificate_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    variables: Optional[dict[str, str]] = None
    documentation_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cache_data_encrypted: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    data_trace_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    throttling_burst_limit: Optional[Union[int, Ref, GetAtt, Sub]] = None
    caching_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    tracing_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    method_settings: Optional[list[MethodSetting]] = None
    access_log_setting: Optional[AccessLogSetting] = None
    cache_cluster_size: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metrics_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    tags: Optional[list[Tag]] = None
    cache_cluster_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

