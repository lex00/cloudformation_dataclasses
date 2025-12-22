"""PropertyTypes for AWS::Oam::Link."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ResourceType:
    """ResourceType enum values."""

    AWS_CLOUDWATCH_METRIC = "AWS::CloudWatch::Metric"
    AWS_LOGS_LOGGROUP = "AWS::Logs::LogGroup"
    AWS_XRAY_TRACE = "AWS::XRay::Trace"
    AWS_APPLICATIONINSIGHTS_APPLICATION = "AWS::ApplicationInsights::Application"
    AWS_INTERNETMONITOR_MONITOR = "AWS::InternetMonitor::Monitor"
    AWS_APPLICATIONSIGNALS_SERVICE = "AWS::ApplicationSignals::Service"
    AWS_APPLICATIONSIGNALS_SERVICELEVELOBJECTIVE = "AWS::ApplicationSignals::ServiceLevelObjective"


@dataclass
class LinkConfiguration(PropertyType):
    LOG_GROUP_CONFIGURATION = "LogGroupConfiguration"
    METRIC_CONFIGURATION = "MetricConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group_configuration": "LogGroupConfiguration",
        "metric_configuration": "MetricConfiguration",
    }

    log_group_configuration: Optional[LinkFilter] = None
    metric_configuration: Optional[LinkFilter] = None


@dataclass
class LinkFilter(PropertyType):
    FILTER = "Filter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
    }

    filter: Optional[Union[str, Ref, GetAtt, Sub]] = None

