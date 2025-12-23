"""PropertyTypes for AWS::Athena::WorkGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AclConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_acl_option": "S3AclOption",
    }

    s3_acl_option: Optional[Union[str, S3AclOption, Ref, GetAtt, Sub]] = None


@dataclass
class Classification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "properties": "Properties",
        "name": "Name",
    }

    properties: Optional[dict[str, str]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CloudWatchLoggingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group": "LogGroup",
        "enabled": "Enabled",
        "log_stream_name_prefix": "LogStreamNamePrefix",
        "log_types": "LogTypes",
    }

    log_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    log_stream_name_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_types: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class CustomerContentEncryptionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key": "KmsKey",
    }

    kms_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_option": "EncryptionOption",
        "kms_key": "KmsKey",
    }

    encryption_option: Optional[Union[str, EncryptionOption, Ref, GetAtt, Sub]] = None
    kms_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EngineConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "spark_properties": "SparkProperties",
        "classifications": "Classifications",
        "max_concurrent_dpus": "MaxConcurrentDpus",
        "coordinator_dpu_size": "CoordinatorDpuSize",
        "default_executor_dpu_size": "DefaultExecutorDpuSize",
        "additional_configs": "AdditionalConfigs",
    }

    spark_properties: Optional[dict[str, str]] = None
    classifications: Optional[list[Classification]] = None
    max_concurrent_dpus: Optional[Union[int, Ref, GetAtt, Sub]] = None
    coordinator_dpu_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    default_executor_dpu_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    additional_configs: Optional[dict[str, str]] = None


@dataclass
class EngineVersion(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "selected_engine_version": "SelectedEngineVersion",
        "effective_engine_version": "EffectiveEngineVersion",
    }

    selected_engine_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    effective_engine_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ManagedLoggingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "kms_key": "KmsKey",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    kms_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ManagedQueryResultsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_configuration": "EncryptionConfiguration",
        "enabled": "Enabled",
    }

    encryption_configuration: Optional[ManagedStorageEncryptionConfiguration] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ManagedStorageEncryptionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key": "KmsKey",
    }

    kms_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MonitoringConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_logging_configuration": "S3LoggingConfiguration",
        "managed_logging_configuration": "ManagedLoggingConfiguration",
        "cloud_watch_logging_configuration": "CloudWatchLoggingConfiguration",
    }

    s3_logging_configuration: Optional[S3LoggingConfiguration] = None
    managed_logging_configuration: Optional[ManagedLoggingConfiguration] = None
    cloud_watch_logging_configuration: Optional[CloudWatchLoggingConfiguration] = None


@dataclass
class ResultConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_configuration": "EncryptionConfiguration",
        "output_location": "OutputLocation",
        "acl_configuration": "AclConfiguration",
        "expected_bucket_owner": "ExpectedBucketOwner",
    }

    encryption_configuration: Optional[EncryptionConfiguration] = None
    output_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    acl_configuration: Optional[AclConfiguration] = None
    expected_bucket_owner: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3LoggingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_location": "LogLocation",
        "enabled": "Enabled",
        "kms_key": "KmsKey",
    }

    log_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    kms_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WorkGroupConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enforce_work_group_configuration": "EnforceWorkGroupConfiguration",
        "engine_version": "EngineVersion",
        "publish_cloud_watch_metrics_enabled": "PublishCloudWatchMetricsEnabled",
        "result_configuration": "ResultConfiguration",
        "additional_configuration": "AdditionalConfiguration",
        "engine_configuration": "EngineConfiguration",
        "customer_content_encryption_configuration": "CustomerContentEncryptionConfiguration",
        "bytes_scanned_cutoff_per_query": "BytesScannedCutoffPerQuery",
        "monitoring_configuration": "MonitoringConfiguration",
        "requester_pays_enabled": "RequesterPaysEnabled",
        "managed_query_results_configuration": "ManagedQueryResultsConfiguration",
        "execution_role": "ExecutionRole",
    }

    enforce_work_group_configuration: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    engine_version: Optional[EngineVersion] = None
    publish_cloud_watch_metrics_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    result_configuration: Optional[ResultConfiguration] = None
    additional_configuration: Optional[Union[str, Ref, GetAtt, Sub]] = None
    engine_configuration: Optional[EngineConfiguration] = None
    customer_content_encryption_configuration: Optional[CustomerContentEncryptionConfiguration] = None
    bytes_scanned_cutoff_per_query: Optional[Union[int, Ref, GetAtt, Sub]] = None
    monitoring_configuration: Optional[MonitoringConfiguration] = None
    requester_pays_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    managed_query_results_configuration: Optional[ManagedQueryResultsConfiguration] = None
    execution_role: Optional[Union[str, Ref, GetAtt, Sub]] = None

