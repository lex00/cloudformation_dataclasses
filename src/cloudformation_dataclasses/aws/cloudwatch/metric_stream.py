"""PropertyTypes for AWS::CloudWatch::MetricStream."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MetricStreamFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_names": "MetricNames",
        "namespace": "Namespace",
    }

    metric_names: Optional[Union[list[str], Ref]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetricStreamStatisticsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "include_metrics": "IncludeMetrics",
        "additional_statistics": "AdditionalStatistics",
    }

    include_metrics: Optional[list[MetricStreamStatisticsMetric]] = None
    additional_statistics: Optional[Union[list[str], Ref]] = None


@dataclass
class MetricStreamStatisticsMetric(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "metric_name": "MetricName",
        "namespace": "Namespace",
    }

    metric_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None

