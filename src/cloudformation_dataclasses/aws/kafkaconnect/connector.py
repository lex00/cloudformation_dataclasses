"""PropertyTypes for AWS::KafkaConnect::Connector."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ApacheKafkaCluster(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc": "Vpc",
        "bootstrap_servers": "BootstrapServers",
    }

    vpc: Optional[Vpc] = None
    bootstrap_servers: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AutoScaling(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "scale_out_policy": "ScaleOutPolicy",
        "scale_in_policy": "ScaleInPolicy",
        "max_worker_count": "MaxWorkerCount",
        "min_worker_count": "MinWorkerCount",
        "mcu_count": "McuCount",
    }

    scale_out_policy: Optional[ScaleOutPolicy] = None
    scale_in_policy: Optional[ScaleInPolicy] = None
    max_worker_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_worker_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    mcu_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Capacity(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "provisioned_capacity": "ProvisionedCapacity",
        "auto_scaling": "AutoScaling",
    }

    provisioned_capacity: Optional[ProvisionedCapacity] = None
    auto_scaling: Optional[AutoScaling] = None


@dataclass
class CloudWatchLogsLogDelivery(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group": "LogGroup",
        "enabled": "Enabled",
    }

    log_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CustomPlugin(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_plugin_arn": "CustomPluginArn",
        "revision": "Revision",
    }

    custom_plugin_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    revision: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class FirehoseLogDelivery(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "delivery_stream": "DeliveryStream",
        "enabled": "Enabled",
    }

    delivery_stream: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class KafkaCluster(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "apache_kafka_cluster": "ApacheKafkaCluster",
    }

    apache_kafka_cluster: Optional[ApacheKafkaCluster] = None


@dataclass
class KafkaClusterClientAuthentication(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "authentication_type": "AuthenticationType",
    }

    authentication_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class KafkaClusterEncryptionInTransit(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_type": "EncryptionType",
    }

    encryption_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LogDelivery(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "worker_log_delivery": "WorkerLogDelivery",
    }

    worker_log_delivery: Optional[WorkerLogDelivery] = None


@dataclass
class Plugin(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_plugin": "CustomPlugin",
    }

    custom_plugin: Optional[CustomPlugin] = None


@dataclass
class ProvisionedCapacity(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "worker_count": "WorkerCount",
        "mcu_count": "McuCount",
    }

    worker_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    mcu_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class S3LogDelivery(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "enabled": "Enabled",
        "prefix": "Prefix",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScaleInPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cpu_utilization_percentage": "CpuUtilizationPercentage",
    }

    cpu_utilization_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ScaleOutPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cpu_utilization_percentage": "CpuUtilizationPercentage",
    }

    cpu_utilization_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Vpc(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "security_groups": "SecurityGroups",
        "subnets": "Subnets",
    }

    security_groups: Optional[Union[list[str], Ref]] = None
    subnets: Optional[Union[list[str], Ref]] = None


@dataclass
class WorkerConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "revision": "Revision",
        "worker_configuration_arn": "WorkerConfigurationArn",
    }

    revision: Optional[Union[int, Ref, GetAtt, Sub]] = None
    worker_configuration_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WorkerLogDelivery(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "firehose": "Firehose",
        "cloud_watch_logs": "CloudWatchLogs",
    }

    s3: Optional[S3LogDelivery] = None
    firehose: Optional[FirehoseLogDelivery] = None
    cloud_watch_logs: Optional[CloudWatchLogsLogDelivery] = None

