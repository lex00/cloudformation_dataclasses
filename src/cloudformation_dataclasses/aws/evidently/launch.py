"""PropertyTypes for AWS::Evidently::Launch."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ExecutionStatusObject(PropertyType):
    STATUS = "Status"
    DESIRED_STATE = "DesiredState"
    REASON = "Reason"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "desired_state": "DesiredState",
        "reason": "Reason",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    desired_state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    reason: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class GroupToWeight(PropertyType):
    GROUP_NAME = "GroupName"
    SPLIT_WEIGHT = "SplitWeight"

    _property_mappings: ClassVar[dict[str, str]] = {
        "group_name": "GroupName",
        "split_weight": "SplitWeight",
    }

    group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    split_weight: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class LaunchGroupObject(PropertyType):
    GROUP_NAME = "GroupName"
    DESCRIPTION = "Description"
    VARIATION = "Variation"
    FEATURE = "Feature"

    _property_mappings: ClassVar[dict[str, str]] = {
        "group_name": "GroupName",
        "description": "Description",
        "variation": "Variation",
        "feature": "Feature",
    }

    group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    variation: Optional[Union[str, Ref, GetAtt, Sub]] = None
    feature: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetricDefinitionObject(PropertyType):
    ENTITY_ID_KEY = "EntityIdKey"
    METRIC_NAME = "MetricName"
    EVENT_PATTERN = "EventPattern"
    VALUE_KEY = "ValueKey"
    UNIT_LABEL = "UnitLabel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entity_id_key": "EntityIdKey",
        "metric_name": "MetricName",
        "event_pattern": "EventPattern",
        "value_key": "ValueKey",
        "unit_label": "UnitLabel",
    }

    entity_id_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    event_pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unit_label: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SegmentOverride(PropertyType):
    WEIGHTS = "Weights"
    EVALUATION_ORDER = "EvaluationOrder"
    SEGMENT = "Segment"

    _property_mappings: ClassVar[dict[str, str]] = {
        "weights": "Weights",
        "evaluation_order": "EvaluationOrder",
        "segment": "Segment",
    }

    weights: Optional[list[GroupToWeight]] = None
    evaluation_order: Optional[Union[int, Ref, GetAtt, Sub]] = None
    segment: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StepConfig(PropertyType):
    GROUP_WEIGHTS = "GroupWeights"
    SEGMENT_OVERRIDES = "SegmentOverrides"
    START_TIME = "StartTime"

    _property_mappings: ClassVar[dict[str, str]] = {
        "group_weights": "GroupWeights",
        "segment_overrides": "SegmentOverrides",
        "start_time": "StartTime",
    }

    group_weights: Optional[list[GroupToWeight]] = None
    segment_overrides: Optional[list[SegmentOverride]] = None
    start_time: Optional[Union[str, Ref, GetAtt, Sub]] = None

