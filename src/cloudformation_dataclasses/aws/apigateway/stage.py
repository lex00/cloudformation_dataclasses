"""PropertyTypes for AWS::ApiGateway::Stage."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccessLogSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "format": "Format",
        "destination_arn": "DestinationArn",
    }

    format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CanarySetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "deployment_id": "DeploymentId",
        "stage_variable_overrides": "StageVariableOverrides",
        "percent_traffic": "PercentTraffic",
        "use_stage_cache": "UseStageCache",
    }

    deployment_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    stage_variable_overrides: Optional[dict[str, str]] = None
    percent_traffic: Optional[Union[float, Ref, GetAtt, Sub]] = None
    use_stage_cache: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MethodSetting(PropertyType):
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

