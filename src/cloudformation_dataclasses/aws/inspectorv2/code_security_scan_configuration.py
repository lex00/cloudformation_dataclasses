"""PropertyTypes for AWS::InspectorV2::CodeSecurityScanConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CodeSecurityScanConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "continuous_integration_scan_configuration": "continuousIntegrationScanConfiguration",
        "periodic_scan_configuration": "periodicScanConfiguration",
        "rule_set_categories": "ruleSetCategories",
    }

    continuous_integration_scan_configuration: Optional[ContinuousIntegrationScanConfiguration] = None
    periodic_scan_configuration: Optional[PeriodicScanConfiguration] = None
    rule_set_categories: Optional[Union[list[str], Ref]] = None


@dataclass
class ContinuousIntegrationScanConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "supported_events": "supportedEvents",
    }

    supported_events: Optional[Union[list[str], Ref]] = None


@dataclass
class PeriodicScanConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "frequency_expression": "frequencyExpression",
        "frequency": "frequency",
    }

    frequency_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    frequency: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScopeSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "project_selection_scope": "projectSelectionScope",
    }

    project_selection_scope: Optional[Union[str, Ref, GetAtt, Sub]] = None

