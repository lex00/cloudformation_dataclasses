"""PropertyTypes for AWS::MediaStore::Container."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CorsRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allowed_methods": "AllowedMethods",
        "allowed_origins": "AllowedOrigins",
        "expose_headers": "ExposeHeaders",
        "max_age_seconds": "MaxAgeSeconds",
        "allowed_headers": "AllowedHeaders",
    }

    allowed_methods: Optional[Union[list[str], Ref]] = None
    allowed_origins: Optional[Union[list[str], Ref]] = None
    expose_headers: Optional[Union[list[str], Ref]] = None
    max_age_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    allowed_headers: Optional[Union[list[str], Ref]] = None


@dataclass
class MetricPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "container_level_metrics": "ContainerLevelMetrics",
        "metric_policy_rules": "MetricPolicyRules",
    }

    container_level_metrics: Optional[Union[str, ContainerLevelMetrics, Ref, GetAtt, Sub]] = None
    metric_policy_rules: Optional[list[MetricPolicyRule]] = None


@dataclass
class MetricPolicyRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "object_group": "ObjectGroup",
        "object_group_name": "ObjectGroupName",
    }

    object_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

