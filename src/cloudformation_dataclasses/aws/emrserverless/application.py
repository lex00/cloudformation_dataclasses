"""PropertyTypes for AWS::EMRServerless::Application."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AutoStartConfiguration(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class AutoStopConfiguration(PropertyType):
    ENABLED = "Enabled"
    IDLE_TIMEOUT_MINUTES = "IdleTimeoutMinutes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "idle_timeout_minutes": "IdleTimeoutMinutes",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    idle_timeout_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CloudWatchLoggingConfiguration(PropertyType):
    ENCRYPTION_KEY_ARN = "EncryptionKeyArn"
    ENABLED = "Enabled"
    LOG_STREAM_NAME_PREFIX = "LogStreamNamePrefix"
    LOG_GROUP_NAME = "LogGroupName"
    LOG_TYPE_MAP = "LogTypeMap"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_key_arn": "EncryptionKeyArn",
        "enabled": "Enabled",
        "log_stream_name_prefix": "LogStreamNamePrefix",
        "log_group_name": "LogGroupName",
        "log_type_map": "LogTypeMap",
    }

    encryption_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    log_stream_name_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    log_type_map: Optional[list[LogTypeMapKeyValuePair]] = None


@dataclass
class ConfigurationObject(PropertyType):
    CLASSIFICATION = "Classification"
    PROPERTIES = "Properties"
    CONFIGURATIONS = "Configurations"

    _property_mappings: ClassVar[dict[str, str]] = {
        "classification": "Classification",
        "properties": "Properties",
        "configurations": "Configurations",
    }

    classification: Optional[Union[str, Ref, GetAtt, Sub]] = None
    properties: Optional[dict[str, str]] = None
    configurations: Optional[list[ConfigurationObject]] = None


@dataclass
class IdentityCenterConfiguration(PropertyType):
    IDENTITY_CENTER_INSTANCE_ARN = "IdentityCenterInstanceArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "identity_center_instance_arn": "IdentityCenterInstanceArn",
    }

    identity_center_instance_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ImageConfigurationInput(PropertyType):
    IMAGE_URI = "ImageUri"

    _property_mappings: ClassVar[dict[str, str]] = {
        "image_uri": "ImageUri",
    }

    image_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InitialCapacityConfig(PropertyType):
    WORKER_CONFIGURATION = "WorkerConfiguration"
    WORKER_COUNT = "WorkerCount"

    _property_mappings: ClassVar[dict[str, str]] = {
        "worker_configuration": "WorkerConfiguration",
        "worker_count": "WorkerCount",
    }

    worker_configuration: Optional[WorkerConfiguration] = None
    worker_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class InitialCapacityConfigKeyValuePair(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[InitialCapacityConfig] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InteractiveConfiguration(PropertyType):
    STUDIO_ENABLED = "StudioEnabled"
    LIVY_ENDPOINT_ENABLED = "LivyEndpointEnabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "studio_enabled": "StudioEnabled",
        "livy_endpoint_enabled": "LivyEndpointEnabled",
    }

    studio_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    livy_endpoint_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class LogTypeMapKeyValuePair(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[list[str], Ref]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ManagedPersistenceMonitoringConfiguration(PropertyType):
    ENCRYPTION_KEY_ARN = "EncryptionKeyArn"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_key_arn": "EncryptionKeyArn",
        "enabled": "Enabled",
    }

    encryption_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class MaximumAllowedResources(PropertyType):
    MEMORY = "Memory"
    CPU = "Cpu"
    DISK = "Disk"

    _property_mappings: ClassVar[dict[str, str]] = {
        "memory": "Memory",
        "cpu": "Cpu",
        "disk": "Disk",
    }

    memory: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cpu: Optional[Union[str, Ref, GetAtt, Sub]] = None
    disk: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MonitoringConfiguration(PropertyType):
    S3_MONITORING_CONFIGURATION = "S3MonitoringConfiguration"
    PROMETHEUS_MONITORING_CONFIGURATION = "PrometheusMonitoringConfiguration"
    MANAGED_PERSISTENCE_MONITORING_CONFIGURATION = "ManagedPersistenceMonitoringConfiguration"
    CLOUD_WATCH_LOGGING_CONFIGURATION = "CloudWatchLoggingConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_monitoring_configuration": "S3MonitoringConfiguration",
        "prometheus_monitoring_configuration": "PrometheusMonitoringConfiguration",
        "managed_persistence_monitoring_configuration": "ManagedPersistenceMonitoringConfiguration",
        "cloud_watch_logging_configuration": "CloudWatchLoggingConfiguration",
    }

    s3_monitoring_configuration: Optional[S3MonitoringConfiguration] = None
    prometheus_monitoring_configuration: Optional[PrometheusMonitoringConfiguration] = None
    managed_persistence_monitoring_configuration: Optional[ManagedPersistenceMonitoringConfiguration] = None
    cloud_watch_logging_configuration: Optional[CloudWatchLoggingConfiguration] = None


@dataclass
class NetworkConfiguration(PropertyType):
    SUBNET_IDS = "SubnetIds"
    SECURITY_GROUP_IDS = "SecurityGroupIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "subnet_ids": "SubnetIds",
        "security_group_ids": "SecurityGroupIds",
    }

    subnet_ids: Optional[Union[list[str], Ref]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class PrometheusMonitoringConfiguration(PropertyType):
    REMOTE_WRITE_URL = "RemoteWriteUrl"

    _property_mappings: ClassVar[dict[str, str]] = {
        "remote_write_url": "RemoteWriteUrl",
    }

    remote_write_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class S3MonitoringConfiguration(PropertyType):
    LOG_URI = "LogUri"
    ENCRYPTION_KEY_ARN = "EncryptionKeyArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_uri": "LogUri",
        "encryption_key_arn": "EncryptionKeyArn",
    }

    log_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SchedulerConfiguration(PropertyType):
    QUEUE_TIMEOUT_MINUTES = "QueueTimeoutMinutes"
    MAX_CONCURRENT_RUNS = "MaxConcurrentRuns"

    _property_mappings: ClassVar[dict[str, str]] = {
        "queue_timeout_minutes": "QueueTimeoutMinutes",
        "max_concurrent_runs": "MaxConcurrentRuns",
    }

    queue_timeout_minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_concurrent_runs: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class WorkerConfiguration(PropertyType):
    DISK_TYPE = "DiskType"
    MEMORY = "Memory"
    CPU = "Cpu"
    DISK = "Disk"

    _property_mappings: ClassVar[dict[str, str]] = {
        "disk_type": "DiskType",
        "memory": "Memory",
        "cpu": "Cpu",
        "disk": "Disk",
    }

    disk_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    memory: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cpu: Optional[Union[str, Ref, GetAtt, Sub]] = None
    disk: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WorkerTypeSpecificationInput(PropertyType):
    IMAGE_CONFIGURATION = "ImageConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "image_configuration": "ImageConfiguration",
    }

    image_configuration: Optional[ImageConfigurationInput] = None

