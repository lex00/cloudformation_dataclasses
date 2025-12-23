"""PropertyTypes for AWS::EC2::VerifiedAccessEndpoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CidrOptions(PropertyType):
    CIDR = "Cidr"
    PORT_RANGES = "PortRanges"
    PROTOCOL = "Protocol"
    SUBNET_IDS = "SubnetIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cidr": "Cidr",
        "port_ranges": "PortRanges",
        "protocol": "Protocol",
        "subnet_ids": "SubnetIds",
    }

    cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port_ranges: Optional[list[PortRange]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class LoadBalancerOptions(PropertyType):
    LOAD_BALANCER_ARN = "LoadBalancerArn"
    PORT = "Port"
    PORT_RANGES = "PortRanges"
    PROTOCOL = "Protocol"
    SUBNET_IDS = "SubnetIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "load_balancer_arn": "LoadBalancerArn",
        "port": "Port",
        "port_ranges": "PortRanges",
        "protocol": "Protocol",
        "subnet_ids": "SubnetIds",
    }

    load_balancer_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    port_ranges: Optional[list[PortRange]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class NetworkInterfaceOptions(PropertyType):
    PORT = "Port"
    PORT_RANGES = "PortRanges"
    NETWORK_INTERFACE_ID = "NetworkInterfaceId"
    PROTOCOL = "Protocol"

    _property_mappings: ClassVar[dict[str, str]] = {
        "port": "Port",
        "port_ranges": "PortRanges",
        "network_interface_id": "NetworkInterfaceId",
        "protocol": "Protocol",
    }

    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    port_ranges: Optional[list[PortRange]] = None
    network_interface_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PortRange(PropertyType):
    FROM_PORT = "FromPort"
    TO_PORT = "ToPort"

    _property_mappings: ClassVar[dict[str, str]] = {
        "from_port": "FromPort",
        "to_port": "ToPort",
    }

    from_port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    to_port: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RdsOptions(PropertyType):
    RDS_DB_PROXY_ARN = "RdsDbProxyArn"
    RDS_DB_CLUSTER_ARN = "RdsDbClusterArn"
    RDS_ENDPOINT = "RdsEndpoint"
    PORT = "Port"
    RDS_DB_INSTANCE_ARN = "RdsDbInstanceArn"
    PROTOCOL = "Protocol"
    SUBNET_IDS = "SubnetIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rds_db_proxy_arn": "RdsDbProxyArn",
        "rds_db_cluster_arn": "RdsDbClusterArn",
        "rds_endpoint": "RdsEndpoint",
        "port": "Port",
        "rds_db_instance_arn": "RdsDbInstanceArn",
        "protocol": "Protocol",
        "subnet_ids": "SubnetIds",
    }

    rds_db_proxy_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rds_db_cluster_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rds_endpoint: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rds_db_instance_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class SseSpecification(PropertyType):
    CUSTOMER_MANAGED_KEY_ENABLED = "CustomerManagedKeyEnabled"
    KMS_KEY_ARN = "KmsKeyArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "customer_managed_key_enabled": "CustomerManagedKeyEnabled",
        "kms_key_arn": "KmsKeyArn",
    }

    customer_managed_key_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None

