"""PropertyTypes for AWS::IoTFleetWise::Campaign."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CollectionScheme(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "time_based_collection_scheme": "TimeBasedCollectionScheme",
        "condition_based_collection_scheme": "ConditionBasedCollectionScheme",
    }

    time_based_collection_scheme: Optional[TimeBasedCollectionScheme] = None
    condition_based_collection_scheme: Optional[ConditionBasedCollectionScheme] = None


@dataclass
class ConditionBasedCollectionScheme(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "minimum_trigger_interval_ms": "MinimumTriggerIntervalMs",
        "expression": "Expression",
        "trigger_mode": "TriggerMode",
        "condition_language_version": "ConditionLanguageVersion",
    }

    minimum_trigger_interval_ms: Optional[Union[float, Ref, GetAtt, Sub]] = None
    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trigger_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    condition_language_version: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ConditionBasedSignalFetchConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "condition_expression": "ConditionExpression",
        "trigger_mode": "TriggerMode",
    }

    condition_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    trigger_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataDestinationConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_config": "S3Config",
        "mqtt_topic_config": "MqttTopicConfig",
        "timestream_config": "TimestreamConfig",
    }

    s3_config: Optional[S3Config] = None
    mqtt_topic_config: Optional[MqttTopicConfig] = None
    timestream_config: Optional[TimestreamConfig] = None


@dataclass
class DataPartition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "upload_options": "UploadOptions",
        "storage_options": "StorageOptions",
        "id": "Id",
    }

    upload_options: Optional[DataPartitionUploadOptions] = None
    storage_options: Optional[DataPartitionStorageOptions] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataPartitionStorageOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "maximum_size": "MaximumSize",
        "storage_location": "StorageLocation",
        "minimum_time_to_live": "MinimumTimeToLive",
    }

    maximum_size: Optional[StorageMaximumSize] = None
    storage_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    minimum_time_to_live: Optional[StorageMinimumTimeToLive] = None


@dataclass
class DataPartitionUploadOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "expression": "Expression",
        "condition_language_version": "ConditionLanguageVersion",
    }

    expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    condition_language_version: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class MqttTopicConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "execution_role_arn": "ExecutionRoleArn",
        "mqtt_topic_arn": "MqttTopicArn",
    }

    execution_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mqtt_topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3Config(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketArn",
        "data_format": "DataFormat",
        "storage_compression_format": "StorageCompressionFormat",
        "prefix": "Prefix",
    }

    bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    storage_compression_format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SignalFetchConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "condition_based": "ConditionBased",
        "time_based": "TimeBased",
    }

    condition_based: Optional[ConditionBasedSignalFetchConfig] = None
    time_based: Optional[TimeBasedSignalFetchConfig] = None


@dataclass
class SignalFetchInformation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "actions": "Actions",
        "fully_qualified_name": "FullyQualifiedName",
        "signal_fetch_config": "SignalFetchConfig",
        "condition_language_version": "ConditionLanguageVersion",
    }

    actions: Optional[Union[list[str], Ref]] = None
    fully_qualified_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    signal_fetch_config: Optional[SignalFetchConfig] = None
    condition_language_version: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class SignalInformation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_sample_count": "MaxSampleCount",
        "data_partition_id": "DataPartitionId",
        "minimum_sampling_interval_ms": "MinimumSamplingIntervalMs",
        "name": "Name",
    }

    max_sample_count: Optional[Union[float, Ref, GetAtt, Sub]] = None
    data_partition_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    minimum_sampling_interval_ms: Optional[Union[float, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StorageMaximumSize(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StorageMinimumTimeToLive(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[int, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TimeBasedCollectionScheme(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "period_ms": "PeriodMs",
    }

    period_ms: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class TimeBasedSignalFetchConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "execution_frequency_ms": "ExecutionFrequencyMs",
    }

    execution_frequency_ms: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class TimestreamConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "execution_role_arn": "ExecutionRoleArn",
        "timestream_table_arn": "TimestreamTableArn",
    }

    execution_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    timestream_table_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

