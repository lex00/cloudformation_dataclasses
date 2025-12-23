"""PropertyTypes for AWS::CloudFront::ContinuousDeploymentPolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ContinuousDeploymentPolicyConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "single_header_policy_config": "SingleHeaderPolicyConfig",
        "enabled": "Enabled",
        "staging_distribution_dns_names": "StagingDistributionDnsNames",
        "traffic_config": "TrafficConfig",
        "single_weight_policy_config": "SingleWeightPolicyConfig",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    single_header_policy_config: Optional[SingleHeaderPolicyConfig] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    staging_distribution_dns_names: Optional[Union[list[str], Ref]] = None
    traffic_config: Optional[TrafficConfig] = None
    single_weight_policy_config: Optional[SingleWeightPolicyConfig] = None


@dataclass
class SessionStickinessConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "idle_ttl": "IdleTTL",
        "maximum_ttl": "MaximumTTL",
    }

    idle_ttl: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_ttl: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SingleHeaderConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "header": "Header",
        "value": "Value",
    }

    header: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SingleHeaderPolicyConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "header": "Header",
        "value": "Value",
    }

    header: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SingleWeightConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "session_stickiness_config": "SessionStickinessConfig",
        "weight": "Weight",
    }

    session_stickiness_config: Optional[SessionStickinessConfig] = None
    weight: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class SingleWeightPolicyConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "session_stickiness_config": "SessionStickinessConfig",
        "weight": "Weight",
    }

    session_stickiness_config: Optional[SessionStickinessConfig] = None
    weight: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class TrafficConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "single_weight_config": "SingleWeightConfig",
        "type_": "Type",
        "single_header_config": "SingleHeaderConfig",
    }

    single_weight_config: Optional[SingleWeightConfig] = None
    type_: Optional[Union[str, ContinuousDeploymentPolicyType, Ref, GetAtt, Sub]] = None
    single_header_config: Optional[SingleHeaderConfig] = None

