"""PropertyTypes for AWS::APS::Workspace."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CloudWatchLogDestination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group_arn": "LogGroupArn",
    }

    log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Label(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LimitsPerLabelSet(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "limits": "Limits",
        "label_set": "LabelSet",
    }

    limits: Optional[LimitsPerLabelSetEntry] = None
    label_set: Optional[list[Label]] = None


@dataclass
class LimitsPerLabelSetEntry(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_series": "MaxSeries",
    }

    max_series: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class LoggingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group_arn": "LogGroupArn",
    }

    log_group_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LoggingDestination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filters": "Filters",
        "cloud_watch_logs": "CloudWatchLogs",
    }

    filters: Optional[LoggingFilter] = None
    cloud_watch_logs: Optional[CloudWatchLogDestination] = None


@dataclass
class LoggingFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "qsp_threshold": "QspThreshold",
    }

    qsp_threshold: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class QueryLoggingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destinations": "Destinations",
    }

    destinations: Optional[list[LoggingDestination]] = None


@dataclass
class WorkspaceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "retention_period_in_days": "RetentionPeriodInDays",
        "limits_per_label_sets": "LimitsPerLabelSets",
    }

    retention_period_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    limits_per_label_sets: Optional[list[LimitsPerLabelSet]] = None

