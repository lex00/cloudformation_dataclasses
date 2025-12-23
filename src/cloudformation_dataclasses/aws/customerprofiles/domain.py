"""PropertyTypes for AWS::CustomerProfiles::Domain."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AttributeTypesSelector(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "address": "Address",
        "attribute_matching_model": "AttributeMatchingModel",
        "phone_number": "PhoneNumber",
        "email_address": "EmailAddress",
    }

    address: Optional[Union[list[str], Ref]] = None
    attribute_matching_model: Optional[Union[str, Ref, GetAtt, Sub]] = None
    phone_number: Optional[Union[list[str], Ref]] = None
    email_address: Optional[Union[list[str], Ref]] = None


@dataclass
class AutoMerging(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "consolidation": "Consolidation",
        "enabled": "Enabled",
        "conflict_resolution": "ConflictResolution",
        "min_allowed_confidence_score_for_merging": "MinAllowedConfidenceScoreForMerging",
    }

    consolidation: Optional[Consolidation] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    conflict_resolution: Optional[ConflictResolution] = None
    min_allowed_confidence_score_for_merging: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ConflictResolution(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "conflict_resolving_model": "ConflictResolvingModel",
        "source_name": "SourceName",
    }

    conflict_resolving_model: Optional[Union[str, Ref, GetAtt, Sub]] = None
    source_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Consolidation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "matching_attributes_list": "MatchingAttributesList",
    }

    matching_attributes_list: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class DataStore(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "readiness": "Readiness",
        "enabled": "Enabled",
    }

    readiness: Optional[Readiness] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DomainStats(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "metering_profile_count": "MeteringProfileCount",
        "profile_count": "ProfileCount",
        "object_count": "ObjectCount",
        "total_size": "TotalSize",
    }

    metering_profile_count: Optional[Union[float, Ref, GetAtt, Sub]] = None
    profile_count: Optional[Union[float, Ref, GetAtt, Sub]] = None
    object_count: Optional[Union[float, Ref, GetAtt, Sub]] = None
    total_size: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class ExportingConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_exporting": "S3Exporting",
    }

    s3_exporting: Optional[S3ExportingConfig] = None


@dataclass
class JobSchedule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "day_of_the_week": "DayOfTheWeek",
        "time": "Time",
    }

    day_of_the_week: Optional[Union[str, Ref, GetAtt, Sub]] = None
    time: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Matching(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_merging": "AutoMerging",
        "job_schedule": "JobSchedule",
        "enabled": "Enabled",
        "exporting_config": "ExportingConfig",
    }

    auto_merging: Optional[AutoMerging] = None
    job_schedule: Optional[JobSchedule] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    exporting_config: Optional[ExportingConfig] = None


@dataclass
class MatchingRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rule": "Rule",
    }

    rule: Optional[Union[list[str], Ref]] = None


@dataclass
class Readiness(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "message": "Message",
        "progress_percentage": "ProgressPercentage",
    }

    message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    progress_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RuleBasedMatching(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "max_allowed_rule_level_for_merging": "MaxAllowedRuleLevelForMerging",
        "enabled": "Enabled",
        "matching_rules": "MatchingRules",
        "attribute_types_selector": "AttributeTypesSelector",
        "conflict_resolution": "ConflictResolution",
        "exporting_config": "ExportingConfig",
        "max_allowed_rule_level_for_matching": "MaxAllowedRuleLevelForMatching",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_allowed_rule_level_for_merging: Optional[Union[int, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    matching_rules: Optional[list[MatchingRule]] = None
    attribute_types_selector: Optional[AttributeTypesSelector] = None
    conflict_resolution: Optional[ConflictResolution] = None
    exporting_config: Optional[ExportingConfig] = None
    max_allowed_rule_level_for_matching: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class S3ExportingConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_bucket_name": "S3BucketName",
        "s3_key_name": "S3KeyName",
    }

    s3_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_key_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

