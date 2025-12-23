"""PropertyTypes for AWS::EKS::Cluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AccessConfig(PropertyType):
    AUTHENTICATION_MODE = "AuthenticationMode"
    BOOTSTRAP_CLUSTER_CREATOR_ADMIN_PERMISSIONS = "BootstrapClusterCreatorAdminPermissions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "authentication_mode": "AuthenticationMode",
        "bootstrap_cluster_creator_admin_permissions": "BootstrapClusterCreatorAdminPermissions",
    }

    authentication_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bootstrap_cluster_creator_admin_permissions: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class BlockStorage(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ClusterLogging(PropertyType):
    ENABLED_TYPES = "EnabledTypes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled_types": "EnabledTypes",
    }

    enabled_types: Optional[list[LoggingTypeConfig]] = None


@dataclass
class ComputeConfig(PropertyType):
    NODE_POOLS = "NodePools"
    NODE_ROLE_ARN = "NodeRoleArn"
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "node_pools": "NodePools",
        "node_role_arn": "NodeRoleArn",
        "enabled": "Enabled",
    }

    node_pools: Optional[Union[list[str], Ref]] = None
    node_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ControlPlanePlacement(PropertyType):
    GROUP_NAME = "GroupName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "group_name": "GroupName",
    }

    group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ControlPlaneScalingConfig(PropertyType):
    TIER = "Tier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "tier": "Tier",
    }

    tier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ElasticLoadBalancing(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionConfig(PropertyType):
    RESOURCES = "Resources"
    PROVIDER = "Provider"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resources": "Resources",
        "provider": "Provider",
    }

    resources: Optional[Union[list[str], Ref]] = None
    provider: Optional[Provider] = None


@dataclass
class KubernetesNetworkConfig(PropertyType):
    SERVICE_IPV4_CIDR = "ServiceIpv4Cidr"
    SERVICE_IPV6_CIDR = "ServiceIpv6Cidr"
    IP_FAMILY = "IpFamily"
    ELASTIC_LOAD_BALANCING = "ElasticLoadBalancing"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service_ipv4_cidr": "ServiceIpv4Cidr",
        "service_ipv6_cidr": "ServiceIpv6Cidr",
        "ip_family": "IpFamily",
        "elastic_load_balancing": "ElasticLoadBalancing",
    }

    service_ipv4_cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None
    service_ipv6_cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ip_family: Optional[Union[str, Ref, GetAtt, Sub]] = None
    elastic_load_balancing: Optional[ElasticLoadBalancing] = None


@dataclass
class Logging(PropertyType):
    CLUSTER_LOGGING = "ClusterLogging"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_logging": "ClusterLogging",
    }

    cluster_logging: Optional[ClusterLogging] = None


@dataclass
class LoggingTypeConfig(PropertyType):
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OutpostConfig(PropertyType):
    OUTPOST_ARNS = "OutpostArns"
    CONTROL_PLANE_PLACEMENT = "ControlPlanePlacement"
    CONTROL_PLANE_INSTANCE_TYPE = "ControlPlaneInstanceType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "outpost_arns": "OutpostArns",
        "control_plane_placement": "ControlPlanePlacement",
        "control_plane_instance_type": "ControlPlaneInstanceType",
    }

    outpost_arns: Optional[Union[list[str], Ref]] = None
    control_plane_placement: Optional[ControlPlanePlacement] = None
    control_plane_instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Provider(PropertyType):
    KEY_ARN = "KeyArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "key_arn": "KeyArn",
    }

    key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RemoteNetworkConfig(PropertyType):
    REMOTE_NODE_NETWORKS = "RemoteNodeNetworks"
    REMOTE_POD_NETWORKS = "RemotePodNetworks"

    _property_mappings: ClassVar[dict[str, str]] = {
        "remote_node_networks": "RemoteNodeNetworks",
        "remote_pod_networks": "RemotePodNetworks",
    }

    remote_node_networks: Optional[list[RemoteNodeNetwork]] = None
    remote_pod_networks: Optional[list[RemotePodNetwork]] = None


@dataclass
class RemoteNodeNetwork(PropertyType):
    CIDRS = "Cidrs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cidrs": "Cidrs",
    }

    cidrs: Optional[Union[list[str], Ref]] = None


@dataclass
class RemotePodNetwork(PropertyType):
    CIDRS = "Cidrs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cidrs": "Cidrs",
    }

    cidrs: Optional[Union[list[str], Ref]] = None


@dataclass
class ResourcesVpcConfig(PropertyType):
    ENDPOINT_PUBLIC_ACCESS = "EndpointPublicAccess"
    PUBLIC_ACCESS_CIDRS = "PublicAccessCidrs"
    ENDPOINT_PRIVATE_ACCESS = "EndpointPrivateAccess"
    SECURITY_GROUP_IDS = "SecurityGroupIds"
    SUBNET_IDS = "SubnetIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "endpoint_public_access": "EndpointPublicAccess",
        "public_access_cidrs": "PublicAccessCidrs",
        "endpoint_private_access": "EndpointPrivateAccess",
        "security_group_ids": "SecurityGroupIds",
        "subnet_ids": "SubnetIds",
    }

    endpoint_public_access: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    public_access_cidrs: Optional[Union[list[str], Ref]] = None
    endpoint_private_access: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class StorageConfig(PropertyType):
    BLOCK_STORAGE = "BlockStorage"

    _property_mappings: ClassVar[dict[str, str]] = {
        "block_storage": "BlockStorage",
    }

    block_storage: Optional[BlockStorage] = None


@dataclass
class UpgradePolicy(PropertyType):
    SUPPORT_TYPE = "SupportType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "support_type": "SupportType",
    }

    support_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ZonalShiftConfig(PropertyType):
    ENABLED = "Enabled"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
    }

    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None

