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
class ContainerInstancesIamInstanceProfile:
    resource: ec2.launch_template.IamInstanceProfile
    arn = get_att(EC2InstanceProfile, "Arn")


@cloudformation_dataclass
class ContainerInstancesLaunchTemplateData:
    resource: ec2.launch_template.LaunchTemplateData
    image_id = ref(ECSAMI)
    security_group_ids = [ref(EcsHostSecurityGroup)]
    instance_type = ref(InstanceType)
    iam_instance_profile = ContainerInstancesIamInstanceProfile
    user_data = Base64(Sub("""#!/bin/bash -xe
echo ECS_CLUSTER=${ECSCluster} >> /etc/ecs/ecs.config
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource ECSAutoScalingGroup --region ${AWS::Region}
"""))


@cloudformation_dataclass
class ContainerInstances:
    """AWS::EC2::LaunchTemplate resource."""

    resource: ec2.LaunchTemplate
    launch_template_data = ContainerInstancesLaunchTemplateData


@cloudformation_dataclass
class ECSAutoScalingGroupLaunchTemplateSpecification:
    resource: autoscaling.auto_scaling_group.LaunchTemplateSpecification
    launch_template_id = ref(ContainerInstances)
    version = get_att(ContainerInstances, "LatestVersionNumber")


@cloudformation_dataclass
class ECSAutoScalingGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: autoscaling.AutoScalingGroup
    vpc_zone_identifier = [ref(PrivateSubnetOne), ref(PrivateSubnetTwo)]
    launch_template = ECSAutoScalingGroupLaunchTemplateSpecification
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
