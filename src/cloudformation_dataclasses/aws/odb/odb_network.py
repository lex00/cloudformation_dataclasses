"""PropertyTypes for AWS::ODB::OdbNetwork."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ManagedS3BackupAccess(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "ipv4_addresses": "Ipv4Addresses",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ipv4_addresses: Optional[Union[list[str], Ref]] = None


@dataclass
class ManagedServices(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "managed_services_ipv4_cidrs": "ManagedServicesIpv4Cidrs",
        "resource_gateway_arn": "ResourceGatewayArn",
        "managed_s3_backup_access": "ManagedS3BackupAccess",
        "service_network_endpoint": "ServiceNetworkEndpoint",
        "zero_etl_access": "ZeroEtlAccess",
        "service_network_arn": "ServiceNetworkArn",
        "s3_access": "S3Access",
    }

    managed_services_ipv4_cidrs: Optional[Union[list[str], Ref]] = None
    resource_gateway_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    managed_s3_backup_access: Optional[ManagedS3BackupAccess] = None
    service_network_endpoint: Optional[ServiceNetworkEndpoint] = None
    zero_etl_access: Optional[ZeroEtlAccess] = None
    service_network_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_access: Optional[S3Access] = None


@dataclass
class S3Access(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "ipv4_addresses": "Ipv4Addresses",
        "domain_name": "DomainName",
        "s3_policy_document": "S3PolicyDocument",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ipv4_addresses: Optional[Union[list[str], Ref]] = None
    domain_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_policy_document: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceNetworkEndpoint(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_endpoint_type": "VpcEndpointType",
        "vpc_endpoint_id": "VpcEndpointId",
    }

    vpc_endpoint_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpc_endpoint_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ZeroEtlAccess(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "cidr": "Cidr",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None

