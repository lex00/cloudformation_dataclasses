"""PropertyTypes for AWS::ElasticBeanstalk::Application."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ApplicationResourceLifecycleConfig(PropertyType):
    SERVICE_ROLE = "ServiceRole"
    VERSION_LIFECYCLE_CONFIG = "VersionLifecycleConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service_role": "ServiceRole",
        "version_lifecycle_config": "VersionLifecycleConfig",
    }

    service_role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version_lifecycle_config: Optional[ApplicationVersionLifecycleConfig] = None


@dataclass
class ApplicationVersionLifecycleConfig(PropertyType):
    MAX_COUNT_RULE = "MaxCountRule"
    MAX_AGE_RULE = "MaxAgeRule"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_count_rule": "MaxCountRule",
        "max_age_rule": "MaxAgeRule",
    }

    max_count_rule: Optional[MaxCountRule] = None
    max_age_rule: Optional[MaxAgeRule] = None


@dataclass
class MaxAgeRule(PropertyType):
    DELETE_SOURCE_FROM_S3 = "DeleteSourceFromS3"
    MAX_AGE_IN_DAYS = "MaxAgeInDays"
    ENABLED = "Enabled"

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
    DELETE_SOURCE_FROM_S3 = "DeleteSourceFromS3"
    ENABLED = "Enabled"
    MAX_COUNT = "MaxCount"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delete_source_from_s3": "DeleteSourceFromS3",
        "enabled": "Enabled",
        "max_count": "MaxCount",
    }

    delete_source_from_s3: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    max_count: Optional[Union[int, Ref, GetAtt, Sub]] = None

