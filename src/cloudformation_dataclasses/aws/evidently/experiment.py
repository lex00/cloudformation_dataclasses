"""PropertyTypes for AWS::Evidently::Experiment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class MetricGoalObject(PropertyType):
    ENTITY_ID_KEY = "EntityIdKey"
    DESIRED_CHANGE = "DesiredChange"
    METRIC_NAME = "MetricName"
    EVENT_PATTERN = "EventPattern"
    VALUE_KEY = "ValueKey"
    UNIT_LABEL = "UnitLabel"

    _property_mappings: ClassVar[dict[str, str]] = {
        "entity_id_key": "EntityIdKey",
        "desired_change": "DesiredChange",
        "metric_name": "MetricName",
        "event_pattern": "EventPattern",
        "value_key": "ValueKey",
        "unit_label": "UnitLabel",
    }

    entity_id_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    desired_change: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metric_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    event_pattern: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    unit_label: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OnlineAbConfigObject(PropertyType):
    TREATMENT_WEIGHTS = "TreatmentWeights"
    CONTROL_TREATMENT_NAME = "ControlTreatmentName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "treatment_weights": "TreatmentWeights",
        "control_treatment_name": "ControlTreatmentName",
    }

    treatment_weights: Optional[list[TreatmentToWeight]] = None
    control_treatment_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RunningStatusObject(PropertyType):
    STATUS = "Status"
    DESIRED_STATE = "DesiredState"
    ANALYSIS_COMPLETE_TIME = "AnalysisCompleteTime"
    REASON = "Reason"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "desired_state": "DesiredState",
        "analysis_complete_time": "AnalysisCompleteTime",
        "reason": "Reason",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    desired_state: Optional[Union[str, Ref, GetAtt, Sub]] = None
    analysis_complete_time: Optional[Union[str, Ref, GetAtt, Sub]] = None
    reason: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TreatmentObject(PropertyType):
    DESCRIPTION = "Description"
    VARIATION = "Variation"
    FEATURE = "Feature"
    TREATMENT_NAME = "TreatmentName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "variation": "Variation",
        "feature": "Feature",
        "treatment_name": "TreatmentName",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    variation: Optional[Union[str, Ref, GetAtt, Sub]] = None
    feature: Optional[Union[str, Ref, GetAtt, Sub]] = None
    treatment_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TreatmentToWeight(PropertyType):
    TREATMENT = "Treatment"
    SPLIT_WEIGHT = "SplitWeight"

    _property_mappings: ClassVar[dict[str, str]] = {
        "treatment": "Treatment",
        "split_weight": "SplitWeight",
    }

    treatment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    split_weight: Optional[Union[int, Ref, GetAtt, Sub]] = None

