"""PropertyTypes for AWS::S3::StorageLens."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccountLevel(PropertyType):
    ADVANCED_DATA_PROTECTION_METRICS = "AdvancedDataProtectionMetrics"
    STORAGE_LENS_GROUP_LEVEL = "StorageLensGroupLevel"
    ACTIVITY_METRICS = "ActivityMetrics"
    ADVANCED_PERFORMANCE_METRICS = "AdvancedPerformanceMetrics"
    BUCKET_LEVEL = "BucketLevel"
    ADVANCED_COST_OPTIMIZATION_METRICS = "AdvancedCostOptimizationMetrics"
    DETAILED_STATUS_CODES_METRICS = "DetailedStatusCodesMetrics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "advanced_data_protection_metrics": "AdvancedDataProtectionMetrics",
        "storage_lens_group_level": "StorageLensGroupLevel",
        "activity_metrics": "ActivityMetrics",
        "advanced_performance_metrics": "AdvancedPerformanceMetrics",
        "bucket_level": "BucketLevel",
        "advanced_cost_optimization_metrics": "AdvancedCostOptimizationMetrics",
        "detailed_status_codes_metrics": "DetailedStatusCodesMetrics",
    }

    advanced_data_protection_metrics: Optional[AdvancedDataProtectionMetrics] = None
    storage_lens_group_level: Optional[StorageLensGroupLevel] = None
    activity_metrics: Optional[ActivityMetrics] = None
    advanced_performance_metrics: Optional[AdvancedPerformanceMetrics] = None
    bucket_level: Optional[BucketLevel] = None
    advanced_cost_optimization_metrics: Optional[AdvancedCostOptimizationMetrics] = None
    detailed_status_codes_metrics: Optional[DetailedStatusCodesMetrics] = None


@dataclass
class ActivityMetrics(PropertyType):
    IS_ENABLED = "IsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_enabled": "IsEnabled",
    }

    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class AdvancedCostOptimizationMetrics(PropertyType):
    IS_ENABLED = "IsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_enabled": "IsEnabled",
    }

    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class AdvancedDataProtectionMetrics(PropertyType):
    IS_ENABLED = "IsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_enabled": "IsEnabled",
    }

    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class AdvancedPerformanceMetrics(PropertyType):
    IS_ENABLED = "IsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_enabled": "IsEnabled",
    }

    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class AwsOrg(PropertyType):
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "Arn",
    }

    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BucketLevel(PropertyType):
    ADVANCED_DATA_PROTECTION_METRICS = "AdvancedDataProtectionMetrics"
    PREFIX_LEVEL = "PrefixLevel"
    ACTIVITY_METRICS = "ActivityMetrics"
    ADVANCED_PERFORMANCE_METRICS = "AdvancedPerformanceMetrics"
    ADVANCED_COST_OPTIMIZATION_METRICS = "AdvancedCostOptimizationMetrics"
    DETAILED_STATUS_CODES_METRICS = "DetailedStatusCodesMetrics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "advanced_data_protection_metrics": "AdvancedDataProtectionMetrics",
        "prefix_level": "PrefixLevel",
        "activity_metrics": "ActivityMetrics",
        "advanced_performance_metrics": "AdvancedPerformanceMetrics",
        "advanced_cost_optimization_metrics": "AdvancedCostOptimizationMetrics",
        "detailed_status_codes_metrics": "DetailedStatusCodesMetrics",
    }

    advanced_data_protection_metrics: Optional[AdvancedDataProtectionMetrics] = None
    prefix_level: Optional[PrefixLevel] = None
    activity_metrics: Optional[ActivityMetrics] = None
    advanced_performance_metrics: Optional[AdvancedPerformanceMetrics] = None
    advanced_cost_optimization_metrics: Optional[AdvancedCostOptimizationMetrics] = None
    detailed_status_codes_metrics: Optional[DetailedStatusCodesMetrics] = None


@dataclass
class BucketsAndRegions(PropertyType):
    REGIONS = "Regions"
    BUCKETS = "Buckets"

    _property_mappings: ClassVar[dict[str, str]] = {
        "regions": "Regions",
        "buckets": "Buckets",
    }

    regions: Optional[Union[list[str], Ref]] = None
    buckets: Optional[Union[list[str], Ref]] = None


@dataclass
class CloudWatchMetrics(PropertyType):
    IS_ENABLED = "IsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_enabled": "IsEnabled",
    }

    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DataExport(PropertyType):
    STORAGE_LENS_TABLE_DESTINATION = "StorageLensTableDestination"
    S3_BUCKET_DESTINATION = "S3BucketDestination"
    CLOUD_WATCH_METRICS = "CloudWatchMetrics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_lens_table_destination": "StorageLensTableDestination",
        "s3_bucket_destination": "S3BucketDestination",
        "cloud_watch_metrics": "CloudWatchMetrics",
    }

    storage_lens_table_destination: Optional[StorageLensTableDestination] = None
    s3_bucket_destination: Optional[S3BucketDestination] = None
    cloud_watch_metrics: Optional[CloudWatchMetrics] = None


@dataclass
class DetailedStatusCodesMetrics(PropertyType):
    IS_ENABLED = "IsEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_enabled": "IsEnabled",
    }

    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Encryption(PropertyType):
    SSEKMS = "SSEKMS"
    SSES3 = "SSES3"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ssekms": "SSEKMS",
        "sses3": "SSES3",
    }

    ssekms: Optional[SSEKMS] = None
    sses3: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class PrefixLevel(PropertyType):
    STORAGE_METRICS = "StorageMetrics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_metrics": "StorageMetrics",
    }

    storage_metrics: Optional[PrefixLevelStorageMetrics] = None


@dataclass
class PrefixLevelStorageMetrics(PropertyType):
    IS_ENABLED = "IsEnabled"
    SELECTION_CRITERIA = "SelectionCriteria"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_enabled": "IsEnabled",
        "selection_criteria": "SelectionCriteria",
    }

    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    selection_criteria: Optional[SelectionCriteria] = None


@dataclass
class S3BucketDestination(PropertyType):
    OUTPUT_SCHEMA_VERSION = "OutputSchemaVersion"
    FORMAT = "Format"
    ACCOUNT_ID = "AccountId"
    PREFIX = "Prefix"
    ENCRYPTION = "Encryption"
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "output_schema_version": "OutputSchemaVersion",
        "format": "Format",
        "account_id": "AccountId",
        "prefix": "Prefix",
        "encryption": "Encryption",
        "arn": "Arn",
    }

    output_schema_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption: Optional[Encryption] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SSEKMS(PropertyType):
    KEY_ID = "KeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "key_id": "KeyId",
    }

    key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SelectionCriteria(PropertyType):
    DELIMITER = "Delimiter"
    MAX_DEPTH = "MaxDepth"
    MIN_STORAGE_BYTES_PERCENTAGE = "MinStorageBytesPercentage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delimiter": "Delimiter",
        "max_depth": "MaxDepth",
        "min_storage_bytes_percentage": "MinStorageBytesPercentage",
    }

    delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_depth: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_storage_bytes_percentage: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class StorageLensConfiguration(PropertyType):
    ACCOUNT_LEVEL = "AccountLevel"
    EXCLUDE = "Exclude"
    IS_ENABLED = "IsEnabled"
    INCLUDE = "Include"
    PREFIX_DELIMITER = "PrefixDelimiter"
    AWS_ORG = "AwsOrg"
    ID = "Id"
    STORAGE_LENS_ARN = "StorageLensArn"
    DATA_EXPORT = "DataExport"
    EXPANDED_PREFIXES_DATA_EXPORT = "ExpandedPrefixesDataExport"

    _property_mappings: ClassVar[dict[str, str]] = {
        "account_level": "AccountLevel",
        "exclude": "Exclude",
        "is_enabled": "IsEnabled",
        "include": "Include",
        "prefix_delimiter": "PrefixDelimiter",
        "aws_org": "AwsOrg",
        "id": "Id",
        "storage_lens_arn": "StorageLensArn",
        "data_export": "DataExport",
        "expanded_prefixes_data_export": "ExpandedPrefixesDataExport",
    }

    account_level: Optional[AccountLevel] = None
    exclude: Optional[BucketsAndRegions] = None
    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    include: Optional[BucketsAndRegions] = None
    prefix_delimiter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aws_org: Optional[AwsOrg] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    storage_lens_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_export: Optional[DataExport] = None
    expanded_prefixes_data_export: Optional[StorageLensExpandedPrefixesDataExport] = None


@dataclass
class StorageLensExpandedPrefixesDataExport(PropertyType):
    STORAGE_LENS_TABLE_DESTINATION = "StorageLensTableDestination"
    S3_BUCKET_DESTINATION = "S3BucketDestination"

    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_lens_table_destination": "StorageLensTableDestination",
        "s3_bucket_destination": "S3BucketDestination",
    }

    storage_lens_table_destination: Optional[StorageLensTableDestination] = None
    s3_bucket_destination: Optional[S3BucketDestination] = None


@dataclass
class StorageLensGroupLevel(PropertyType):
    STORAGE_LENS_GROUP_SELECTION_CRITERIA = "StorageLensGroupSelectionCriteria"

    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_lens_group_selection_criteria": "StorageLensGroupSelectionCriteria",
    }

    storage_lens_group_selection_criteria: Optional[StorageLensGroupSelectionCriteria] = None


@dataclass
class StorageLensGroupSelectionCriteria(PropertyType):
    EXCLUDE = "Exclude"
    INCLUDE = "Include"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exclude": "Exclude",
        "include": "Include",
    }

    exclude: Optional[Union[list[str], Ref]] = None
    include: Optional[Union[list[str], Ref]] = None


@dataclass
class StorageLensTableDestination(PropertyType):
    IS_ENABLED = "IsEnabled"
    ENCRYPTION = "Encryption"

    _property_mappings: ClassVar[dict[str, str]] = {
        "is_enabled": "IsEnabled",
        "encryption": "Encryption",
    }

    is_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    encryption: Optional[Encryption] = None

