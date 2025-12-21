from __future__ import annotations

"""ControlPlane - AWS::EKS::Cluster resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ControlPlaneResourcesVpcConfig:
    resource: ResourcesVpcConfig
    security_group_ids = [ref("ControlPlaneSecurityGroup")]
    subnet_ids = [ref("PublicSubnet1"), ref("PublicSubnet2"), ref("PublicSubnet3"), ref("PrivateSubnet1"), ref("PrivateSubnet2"), ref("PrivateSubnet3")]


@cloudformation_dataclass
class ControlPlane:
    """AWS::EKS::Cluster resource."""

    resource: Cluster
    name = Sub('${AWS::StackName}-cluster')
    resources_vpc_config = ControlPlaneResourcesVpcConfig
    role_arn: GetAtt[EKSClusterRole] = get_att("Arn")
    version = ref(EKSClusterVersion)
