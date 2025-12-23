"""PropertyTypes for AWS::InternetMonitor::Monitor."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class HealthEventsConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "availability_local_health_events_config": "AvailabilityLocalHealthEventsConfig",
        "performance_score_threshold": "PerformanceScoreThreshold",
        "performance_local_health_events_config": "PerformanceLocalHealthEventsConfig",
        "availability_score_threshold": "AvailabilityScoreThreshold",
    }

    availability_local_health_events_config: Optional[LocalHealthEventsConfig] = None
    performance_score_threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None
    performance_local_health_events_config: Optional[LocalHealthEventsConfig] = None
    availability_score_threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class InternetMeasurementsLogDelivery(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_config": "S3Config",
    }

    s3_config: Optional[S3Config] = None


@dataclass
class LocalHealthEventsConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "health_score_threshold": "HealthScoreThreshold",
        "min_traffic_impact": "MinTrafficImpact",
    }

    status: Optional[Union[str, LocalHealthEventsConfigStatus, Ref, GetAtt, Sub]] = None
    health_score_threshold: Optional[Union[float, Ref, GetAtt, Sub]] = None
    min_traffic_impact: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class S3Config(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_name": "BucketName",
        "log_delivery_status": "LogDeliveryStatus",
        "bucket_prefix": "BucketPrefix",
    }

    bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_delivery_status: Optional[Union[str, LogDeliveryStatus, Ref, GetAtt, Sub]] = None
    bucket_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None

