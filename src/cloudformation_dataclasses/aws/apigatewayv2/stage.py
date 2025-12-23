"""PropertyTypes for AWS::ApiGatewayV2::Stage."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccessLogSettings(PropertyType):
    FORMAT = "Format"
    DESTINATION_ARN = "DestinationArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "format": "Format",
        "destination_arn": "DestinationArn",
    }

    format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RouteSettings(PropertyType):
    LOGGING_LEVEL = "LoggingLevel"
    DATA_TRACE_ENABLED = "DataTraceEnabled"
    THROTTLING_BURST_LIMIT = "ThrottlingBurstLimit"
    DETAILED_METRICS_ENABLED = "DetailedMetricsEnabled"
    THROTTLING_RATE_LIMIT = "ThrottlingRateLimit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "logging_level": "LoggingLevel",
        "data_trace_enabled": "DataTraceEnabled",
        "throttling_burst_limit": "ThrottlingBurstLimit",
        "detailed_metrics_enabled": "DetailedMetricsEnabled",
        "throttling_rate_limit": "ThrottlingRateLimit",
    }

    logging_level: Optional[Union[str, LoggingLevel, Ref, GetAtt, Sub]] = None
    data_trace_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    throttling_burst_limit: Optional[Union[int, Ref, GetAtt, Sub]] = None
    detailed_metrics_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    throttling_rate_limit: Optional[Union[float, Ref, GetAtt, Sub]] = None

