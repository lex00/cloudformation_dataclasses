"""PropertyTypes for AWS::Logs::MetricFilter."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Dimension(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetricTransformation(PropertyType):
    DEFAULT_VALUE = "DefaultValue"
    METRIC_NAME = "MetricName"
    METRIC_VALUE = "MetricValue"
    METRIC_NAMESPACE = "MetricNamespace"
    DIMENSIONS = "Dimensions"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "metric_name": "MetricName",
        "metric_value": "MetricValue",
        "metric_namespace": "MetricNamespace",
        "dimensions": "Dimensions",
        "unit": "Unit",
    }

    default_value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    metric_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric_namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None
    dimensions: Optional[list[Dimension]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None

