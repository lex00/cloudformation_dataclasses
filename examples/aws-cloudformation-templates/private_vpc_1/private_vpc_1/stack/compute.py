"""Compute resources: ECSCluster, EcsSecurityGroupIngressFromPublicALB, EcsSecurityGroupIngressFromPrivateALB, EcsSecurityGroupIngressFromSelf, ContainerInstances, ECSAutoScalingGroup, PrivateLoadBalancerIngressFromECS."""

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
    group_id = ref(EcsHostSecurityGroup)
    ip_protocol = -1
    source_security_group_id = ref(PublicLoadBalancerSG)


@cloudformation_dataclass
class EcsSecurityGroupIngressFromPrivateALB:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    description = 'Ingress from the private ALB'
    group_id = ref(EcsHostSecurityGroup)
    ip_protocol = -1
    source_security_group_id = ref(PrivateLoadBalancerSG)


@cloudformation_dataclass
class EcsSecurityGroupIngressFromSelf:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    description = 'Ingress from other containers in the same security group'
    group_id = ref(EcsHostSecurityGroup)
    ip_protocol = -1
    source_security_group_id = ref(EcsHostSecurityGroup)


@cloudformation_dataclass
class ContainerInstances:
    """AWS::EC2::LaunchTemplate resource."""

    resource: ec2.LaunchTemplate
    launch_template_data = {
        'ImageId': ref(ECSAMI),
        'SecurityGroupIds': [ref(EcsHostSecurityGroup)],
        'InstanceType': ref(InstanceType),
        'IamInstanceProfile': {
            'Arn': get_att(EC2InstanceProfile, "Arn"),
        },
        'UserData': Base64(Sub("""#!/bin/bash -xe
echo ECS_CLUSTER=${ECSCluster} >> /etc/ecs/ecs.config
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource ECSAutoScalingGroup --region ${AWS::Region}
""")),
    }


@cloudformation_dataclass
class ECSAutoScalingGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: autoscaling.AutoScalingGroup
    vpc_zone_identifier = [ref(PrivateSubnetOne), ref(PrivateSubnetTwo)]
    launch_template = {
        'LaunchTemplateId': ref(ContainerInstances),
        'Version': get_att(ContainerInstances, "LatestVersionNumber"),
    }
    min_size = 1
    max_size = ref(MaxSize)
    desired_capacity = ref(DesiredCapacity)


@cloudformation_dataclass
class PrivateLoadBalancerIngressFromECS:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    description = 'Only accept traffic from a container in the container host security group'
    group_id = ref(PrivateLoadBalancerSG)
    ip_protocol = -1
    source_security_group_id = ref(EcsHostSecurityGroup)
