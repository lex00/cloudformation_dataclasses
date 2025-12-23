"""PropertyTypes for AWS::Oam::Link."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

