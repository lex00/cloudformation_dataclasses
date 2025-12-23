"""PropertyTypes for AWS::ElasticBeanstalk::Application."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ApplicationResourceLifecycleConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "service_role": "ServiceRole",
        "version_lifecycle_config": "VersionLifecycleConfig",
    }

    service_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version_lifecycle_config: Optional[ApplicationVersionLifecycleConfig] = None


@dataclass
class ApplicationVersionLifecycleConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_count_rule": "MaxCountRule",
        "max_age_rule": "MaxAgeRule",
    }

    max_count_rule: Optional[MaxCountRule] = None
    max_age_rule: Optional[MaxAgeRule] = None


@dataclass
class MaxAgeRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "delete_source_from_s3": "DeleteSourceFromS3",
        "max_age_in_days": "MaxAgeInDays",
        "enabled": "Enabled",
    }

    delete_source_from_s3: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    max_age_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MaxCountRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "delete_source_from_s3": "DeleteSourceFromS3",
        "enabled": "Enabled",
        "max_count": "MaxCount",
    }

    delete_source_from_s3: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    max_count: Optional[Union[int, Ref, GetAtt, Sub]] = None

