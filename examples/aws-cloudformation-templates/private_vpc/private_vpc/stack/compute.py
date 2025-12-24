"""Compute resources: ECSCluster, EcsSecurityGroupIngressFromPublicALB, EcsSecurityGroupIngressFromPrivateALB, EcsSecurityGroupIngressFromSelf, PrivateLoadBalancerIngressFromECS."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ECSCluster:
    """AWS::ECS::Cluster resource."""

    resource: ecs.Cluster


@cloudformation_dataclass
class EcsSecurityGroupIngressFromPublicALB:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    description = 'Ingress from the public ALB'
    group_id = ref(FargateContainerSecurityGroup)
    ip_protocol = '-1'
    source_security_group_id = ref(PublicLoadBalancerSG)


@cloudformation_dataclass
class EcsSecurityGroupIngressFromPrivateALB:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    description = 'Ingress from the private ALB'
    group_id = ref(FargateContainerSecurityGroup)
    ip_protocol = '-1'
    source_security_group_id = ref(PrivateLoadBalancerSG)


@cloudformation_dataclass
class EcsSecurityGroupIngressFromSelf:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    description = 'Ingress from other containers in the same security group'
    group_id = ref(FargateContainerSecurityGroup)
    ip_protocol = '-1'
    source_security_group_id = ref(FargateContainerSecurityGroup)


@cloudformation_dataclass
class PrivateLoadBalancerIngressFromECS:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    description = 'Only accept traffic from a container in the fargate container security group'
    group_id = ref(PrivateLoadBalancerSG)
    ip_protocol = '-1'
    source_security_group_id = ref(FargateContainerSecurityGroup)
