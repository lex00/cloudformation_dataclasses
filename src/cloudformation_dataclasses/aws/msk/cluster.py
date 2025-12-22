"""PropertyTypes for AWS::MSK::Cluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class BrokerAZDistribution:
    """BrokerAZDistribution enum values."""

    DEFAULT = "DEFAULT"


class ClientBroker:
    """ClientBroker enum values."""

    TLS = "TLS"
    TLS_PLAINTEXT = "TLS_PLAINTEXT"
    PLAINTEXT = "PLAINTEXT"


class ClusterState:
    """ClusterState enum values."""

    ACTIVE = "ACTIVE"
    CREATING = "CREATING"
    DELETING = "DELETING"
    FAILED = "FAILED"
    HEALING = "HEALING"
    MAINTENANCE = "MAINTENANCE"
    REBOOTING_BROKER = "REBOOTING_BROKER"
    UPDATING = "UPDATING"


class ClusterType:
    """ClusterType enum values."""

    PROVISIONED = "PROVISIONED"
    SERVERLESS = "SERVERLESS"


class ConfigurationState:
    """ConfigurationState enum values."""

    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"


class CustomerActionStatus:
    """CustomerActionStatus enum values."""

    CRITICAL_ACTION_REQUIRED = "CRITICAL_ACTION_REQUIRED"
    ACTION_RECOMMENDED = "ACTION_RECOMMENDED"
    NONE = "NONE"


class EnhancedMonitoring:
    """EnhancedMonitoring enum values."""

    DEFAULT = "DEFAULT"
    PER_BROKER = "PER_BROKER"
    PER_TOPIC_PER_BROKER = "PER_TOPIC_PER_BROKER"
    PER_TOPIC_PER_PARTITION = "PER_TOPIC_PER_PARTITION"


class KafkaVersionStatus:
    """KafkaVersionStatus enum values."""

    ACTIVE = "ACTIVE"
    DEPRECATED = "DEPRECATED"


class NodeType:
    """NodeType enum values."""

    BROKER = "BROKER"


class RebalancingStatus:
    """RebalancingStatus enum values."""

    PAUSED = "PAUSED"
    ACTIVE = "ACTIVE"


class ReplicationStartingPositionType:
    """ReplicationStartingPositionType enum values."""

    LATEST = "LATEST"
    EARLIEST = "EARLIEST"


class ReplicationTopicNameConfigurationType:
    """ReplicationTopicNameConfigurationType enum values."""

    PREFIXED_WITH_SOURCE_CLUSTER_ALIAS = "PREFIXED_WITH_SOURCE_CLUSTER_ALIAS"
    IDENTICAL = "IDENTICAL"


class ReplicatorState:
    """ReplicatorState enum values."""

    RUNNING = "RUNNING"
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    FAILED = "FAILED"


class StorageMode:
    """StorageMode enum values."""

    LOCAL = "LOCAL"
    TIERED = "TIERED"


class TargetCompressionType:
    """TargetCompressionType enum values."""

    NONE = "NONE"
    GZIP = "GZIP"
    SNAPPY = "SNAPPY"
    LZ4 = "LZ4"
    ZSTD = "ZSTD"


class TopicState:
    """TopicState enum values."""

    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"


class UserIdentityType:
    """UserIdentityType enum values."""

    AWSACCOUNT = "AWSACCOUNT"
    AWSSERVICE = "AWSSERVICE"


class VpcConnectionState:
    """VpcConnectionState enum values."""

    CREATING = "CREATING"
    AVAILABLE = "AVAILABLE"
    INACTIVE = "INACTIVE"
    DEACTIVATING = "DEACTIVATING"
    DELETING = "DELETING"
    FAILED = "FAILED"
    REJECTED = "REJECTED"
    REJECTING = "REJECTING"


@dataclass
class BrokerLogs(PropertyType):
    S3 = "S3"
    FIREHOSE = "Firehose"
    CLOUD_WATCH_LOGS = "CloudWatchLogs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3": "S3",
        "firehose": "Firehose",
        "cloud_watch_logs": "CloudWatchLogs",
    }

    s3: Optional[S3] = None
    firehose: Optional[Firehose] = None
    cloud_watch_logs: Optional[CloudWatchLogs] = None


@dataclass
class BrokerNodeGroupInfo(PropertyType):
    SECURITY_GROUPS = "SecurityGroups"
    CLIENT_SUBNETS = "ClientSubnets"
    CONNECTIVITY_INFO = "ConnectivityInfo"
    STORAGE_INFO = "StorageInfo"
    BROKER_AZ_DISTRIBUTION = "BrokerAZDistribution"
    INSTANCE_TYPE = "InstanceType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "security_groups": "SecurityGroups",
        "client_subnets": "ClientSubnets",
        "connectivity_info": "ConnectivityInfo",
        "storage_info": "StorageInfo",
        "broker_az_distribution": "BrokerAZDistribution",
        "instance_type": "InstanceType",
    }

    security_groups: Optional[Union[list[str], Ref]] = None
    client_subnets: Optional[Union[list[str], Ref]] = None
    connectivity_info: Optional[ConnectivityInfo] = None
    storage_info: Optional[StorageInfo] = None
    broker_az_distribution: Optional[Union[str, BrokerAZDistribution, Ref, GetAtt, Sub]] = None
    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ClientAuthentication(PropertyType):
    SASL = "Sasl"
    UNAUTHENTICATED = "Unauthenticated"
    TLS = "Tls"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sasl": "Sasl",
        "unauthenticated": "Unauthenticated",
        "tls": "Tls",
    }

    sasl: Optional[Sasl] = None
    unauthenticated: Optional[Unauthenticated] = None
    tls: Optional[Tls] = None


@dataclass
class CloudWatchLogs(PropertyType):
    LOG_GROUP = "LogGroup"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group": "LogGroup",
        "enabled": "Enabled",
    }

    log_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ConfigurationInfo(PropertyType):
    REVISION = "Revision"
    ARN = "Arn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "revision": "Revision",
        "arn": "Arn",
    }

    revision: Optional[Union[int, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectivityInfo(PropertyType):
    NETWORK_TYPE = "NetworkType"
    VPC_CONNECTIVITY = "VpcConnectivity"
    PUBLIC_ACCESS = "PublicAccess"

    _property_mappings: ClassVar[dict[str, str]] = {
        "network_type": "NetworkType",
        "vpc_connectivity": "VpcConnectivity",
        "public_access": "PublicAccess",
    }

    network_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpc_connectivity: Optional[VpcConnectivity] = None
    public_access: Optional[PublicAccess] = None


@dataclass
class EBSStorageInfo(PropertyType):
    PROVISIONED_THROUGHPUT = "ProvisionedThroughput"
    VOLUME_SIZE = "VolumeSize"

    _property_mappings: ClassVar[dict[str, str]] = {
        "provisioned_throughput": "ProvisionedThroughput",
        "volume_size": "VolumeSize",
    }

    provisioned_throughput: Optional[ProvisionedThroughput] = None
    volume_size: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionAtRest(PropertyType):
    DATA_VOLUME_KMS_KEY_ID = "DataVolumeKMSKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "data_volume_kms_key_id": "DataVolumeKMSKeyId",
    }

    data_volume_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionInTransit(PropertyType):
    CLIENT_BROKER = "ClientBroker"
    IN_CLUSTER = "InCluster"

    _property_mappings: ClassVar[dict[str, str]] = {
        "client_broker": "ClientBroker",
        "in_cluster": "InCluster",
    }

    client_broker: Optional[Union[str, ClientBroker, Ref, GetAtt, Sub]] = None
    in_cluster: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionInfo(PropertyType):
    ENCRYPTION_AT_REST = "EncryptionAtRest"
    ENCRYPTION_IN_TRANSIT = "EncryptionInTransit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_at_rest": "EncryptionAtRest",
        "encryption_in_transit": "EncryptionInTransit",
    }

    encryption_at_rest: Optional[EncryptionAtRest] = None
    encryption_in_transit: Optional[EncryptionInTransit] = None


@dataclass
class Firehose(PropertyType):
    DELIVERY_STREAM = "DeliveryStream"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "delivery_stream": "DeliveryStream",
        "enabled": "Enabled",
    }

    delivery_stream: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Iam(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class JmxExporter(PropertyType):
    ENABLED_IN_BROKER = "EnabledInBroker"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled_in_broker": "EnabledInBroker",
    }

    enabled_in_broker: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class LoggingInfo(PropertyType):
    BROKER_LOGS = "BrokerLogs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "broker_logs": "BrokerLogs",
    }

    broker_logs: Optional[BrokerLogs] = None


@dataclass
class NodeExporter(PropertyType):
    ENABLED_IN_BROKER = "EnabledInBroker"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled_in_broker": "EnabledInBroker",
    }

    enabled_in_broker: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class OpenMonitoring(PropertyType):
    PROMETHEUS = "Prometheus"

    _property_mappings: ClassVar[dict[str, str]] = {
        "prometheus": "Prometheus",
    }

    prometheus: Optional[Prometheus] = None


@dataclass
class Prometheus(PropertyType):
    JMX_EXPORTER = "JmxExporter"
    NODE_EXPORTER = "NodeExporter"

    _property_mappings: ClassVar[dict[str, str]] = {
        "jmx_exporter": "JmxExporter",
        "node_exporter": "NodeExporter",
    }

    jmx_exporter: Optional[JmxExporter] = None
    node_exporter: Optional[NodeExporter] = None


@dataclass
class ProvisionedThroughput(PropertyType):
    VOLUME_THROUGHPUT = "VolumeThroughput"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "volume_throughput": "VolumeThroughput",
        "enabled": "Enabled",
    }

    volume_throughput: Optional[Union[int, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class PublicAccess(PropertyType):
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Rebalancing(PropertyType):
    STATUS = "Status"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
    }

    status: Optional[Union[str, RebalancingStatus, Ref, GetAtt, Sub]] = None


@dataclass
class S3(PropertyType):
    BUCKET = "Bucket"
    ENABLED = "Enabled"
    PREFIX = "Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket": "Bucket",
        "enabled": "Enabled",
        "prefix": "Prefix",
    }

    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Sasl(PropertyType):
    IAM = "Iam"
    SCRAM = "Scram"

    _property_mappings: ClassVar[dict[str, str]] = {
        "iam": "Iam",
        "scram": "Scram",
    }

    iam: Optional[Iam] = None
    scram: Optional[Scram] = None


@dataclass
class Scram(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class StorageInfo(PropertyType):
    EBS_STORAGE_INFO = "EBSStorageInfo"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs_storage_info": "EBSStorageInfo",
    }

    ebs_storage_info: Optional[EBSStorageInfo] = None


@dataclass
class Tls(PropertyType):
    ENABLED = "Enabled"
    CERTIFICATE_AUTHORITY_ARN_LIST = "CertificateAuthorityArnList"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "certificate_authority_arn_list": "CertificateAuthorityArnList",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    certificate_authority_arn_list: Optional[Union[list[str], Ref]] = None


@dataclass
class Unauthenticated(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConnectivity(PropertyType):
    CLIENT_AUTHENTICATION = "ClientAuthentication"

    _property_mappings: ClassVar[dict[str, str]] = {
        "client_authentication": "ClientAuthentication",
    }

    client_authentication: Optional[VpcConnectivityClientAuthentication] = None


@dataclass
class VpcConnectivityClientAuthentication(PropertyType):
    SASL = "Sasl"
    TLS = "Tls"

    _property_mappings: ClassVar[dict[str, str]] = {
        "sasl": "Sasl",
        "tls": "Tls",
    }

    sasl: Optional[VpcConnectivitySasl] = None
    tls: Optional[VpcConnectivityTls] = None


@dataclass
class VpcConnectivityIam(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConnectivitySasl(PropertyType):
    IAM = "Iam"
    SCRAM = "Scram"

    _property_mappings: ClassVar[dict[str, str]] = {
        "iam": "Iam",
        "scram": "Scram",
    }

    iam: Optional[VpcConnectivityIam] = None
    scram: Optional[VpcConnectivityScram] = None


@dataclass
class VpcConnectivityScram(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConnectivityTls(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

