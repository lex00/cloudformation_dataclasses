"""PropertyTypes for AWS::MSK::Cluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BrokerLogs(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_group": "LogGroup",
        "enabled": "Enabled",
    }

    log_group: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ConfigurationInfo(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "revision": "Revision",
        "arn": "Arn",
    }

    revision: Optional[Union[int, Ref, GetAtt, Sub]] = None
    arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectivityInfo(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "provisioned_throughput": "ProvisionedThroughput",
        "volume_size": "VolumeSize",
    }

    provisioned_throughput: Optional[ProvisionedThroughput] = None
    volume_size: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionAtRest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_volume_kms_key_id": "DataVolumeKMSKeyId",
    }

    data_volume_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionInTransit(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "client_broker": "ClientBroker",
        "in_cluster": "InCluster",
    }

    client_broker: Optional[Union[str, ClientBroker, Ref, GetAtt, Sub]] = None
    in_cluster: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionInfo(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_at_rest": "EncryptionAtRest",
        "encryption_in_transit": "EncryptionInTransit",
    }

    encryption_at_rest: Optional[EncryptionAtRest] = None
    encryption_in_transit: Optional[EncryptionInTransit] = None


@dataclass
class Firehose(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "delivery_stream": "DeliveryStream",
        "enabled": "Enabled",
    }

    delivery_stream: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Iam(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class JmxExporter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled_in_broker": "EnabledInBroker",
    }

    enabled_in_broker: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class LoggingInfo(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "broker_logs": "BrokerLogs",
    }

    broker_logs: Optional[BrokerLogs] = None


@dataclass
class NodeExporter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled_in_broker": "EnabledInBroker",
    }

    enabled_in_broker: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class OpenMonitoring(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "prometheus": "Prometheus",
    }

    prometheus: Optional[Prometheus] = None


@dataclass
class Prometheus(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "jmx_exporter": "JmxExporter",
        "node_exporter": "NodeExporter",
    }

    jmx_exporter: Optional[JmxExporter] = None
    node_exporter: Optional[NodeExporter] = None


@dataclass
class ProvisionedThroughput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "volume_throughput": "VolumeThroughput",
        "enabled": "Enabled",
    }

    volume_throughput: Optional[Union[int, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class PublicAccess(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Rebalancing(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
    }

    status: Optional[Union[str, RebalancingStatus, Ref, GetAtt, Sub]] = None


@dataclass
class S3(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "iam": "Iam",
        "scram": "Scram",
    }

    iam: Optional[Iam] = None
    scram: Optional[Scram] = None


@dataclass
class Scram(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class StorageInfo(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs_storage_info": "EBSStorageInfo",
    }

    ebs_storage_info: Optional[EBSStorageInfo] = None


@dataclass
class Tls(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "certificate_authority_arn_list": "CertificateAuthorityArnList",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    certificate_authority_arn_list: Optional[Union[list[str], Ref]] = None


@dataclass
class Unauthenticated(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConnectivity(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "client_authentication": "ClientAuthentication",
    }

    client_authentication: Optional[VpcConnectivityClientAuthentication] = None


@dataclass
class VpcConnectivityClientAuthentication(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sasl": "Sasl",
        "tls": "Tls",
    }

    sasl: Optional[VpcConnectivitySasl] = None
    tls: Optional[VpcConnectivityTls] = None


@dataclass
class VpcConnectivityIam(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConnectivitySasl(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iam": "Iam",
        "scram": "Scram",
    }

    iam: Optional[VpcConnectivityIam] = None
    scram: Optional[VpcConnectivityScram] = None


@dataclass
class VpcConnectivityScram(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class VpcConnectivityTls(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

