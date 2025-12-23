"""PropertyTypes for AWS::RTBFabric::ResponderGateway."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AutoScalingGroupsConfiguration(PropertyType):
    AUTO_SCALING_GROUP_NAME_LIST = "AutoScalingGroupNameList"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_scaling_group_name_list": "AutoScalingGroupNameList",
        "role_arn": "RoleArn",
    }

    auto_scaling_group_name_list: Optional[Union[list[str], Ref]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EksEndpointsConfiguration(PropertyType):
    CLUSTER_API_SERVER_CA_CERTIFICATE_CHAIN = "ClusterApiServerCaCertificateChain"
    ENDPOINTS_RESOURCE_NAME = "EndpointsResourceName"
    CLUSTER_API_SERVER_ENDPOINT_URI = "ClusterApiServerEndpointUri"
    CLUSTER_NAME = "ClusterName"
    ENDPOINTS_RESOURCE_NAMESPACE = "EndpointsResourceNamespace"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_api_server_ca_certificate_chain": "ClusterApiServerCaCertificateChain",
        "endpoints_resource_name": "EndpointsResourceName",
        "cluster_api_server_endpoint_uri": "ClusterApiServerEndpointUri",
        "cluster_name": "ClusterName",
        "endpoints_resource_namespace": "EndpointsResourceNamespace",
        "role_arn": "RoleArn",
    }

    cluster_api_server_ca_certificate_chain: Optional[Union[str, Ref, GetAtt, Sub]] = None
    endpoints_resource_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cluster_api_server_endpoint_uri: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cluster_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    endpoints_resource_namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ManagedEndpointConfiguration(PropertyType):
    EKS_ENDPOINTS_CONFIGURATION = "EksEndpointsConfiguration"
    AUTO_SCALING_GROUPS_CONFIGURATION = "AutoScalingGroupsConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "eks_endpoints_configuration": "EksEndpointsConfiguration",
        "auto_scaling_groups_configuration": "AutoScalingGroupsConfiguration",
    }

    eks_endpoints_configuration: Optional[EksEndpointsConfiguration] = None
    auto_scaling_groups_configuration: Optional[AutoScalingGroupsConfiguration] = None


@dataclass
class TrustStoreConfiguration(PropertyType):
    CERTIFICATE_AUTHORITY_CERTIFICATES = "CertificateAuthorityCertificates"

    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_authority_certificates": "CertificateAuthorityCertificates",
    }

    certificate_authority_certificates: Optional[Union[list[str], Ref]] = None

