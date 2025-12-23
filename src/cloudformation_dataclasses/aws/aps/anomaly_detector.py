"""PropertyTypes for AWS::APS::AnomalyDetector."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AnomalyDetectorConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "random_cut_forest": "RandomCutForest",
    }

    random_cut_forest: Optional[RandomCutForestConfiguration] = None


@dataclass
class IgnoreNearExpected(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "amount": "Amount",
        "ratio": "Ratio",
    }

    amount: Optional[Union[float, Ref, GetAtt, Sub]] = None
    ratio: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class Label(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MissingDataAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mark_as_anomaly": "MarkAsAnomaly",
        "skip": "Skip",
    }

    mark_as_anomaly: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    skip: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class RandomCutForestConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sample_size": "SampleSize",
        "query": "Query",
        "shingle_size": "ShingleSize",
        "ignore_near_expected_from_below": "IgnoreNearExpectedFromBelow",
        "ignore_near_expected_from_above": "IgnoreNearExpectedFromAbove",
    }

    sample_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    query: Optional[Union[str, Ref, GetAtt, Sub]] = None
    shingle_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    ignore_near_expected_from_below: Optional[IgnoreNearExpected] = None
    ignore_near_expected_from_above: Optional[IgnoreNearExpected] = None

