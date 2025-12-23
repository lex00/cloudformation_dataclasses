"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable SSH access and HTTP access on the configured port'
    security_group_ingress = [{
        'IpProtocol': 'tcp',
        'FromPort': '22',
        'ToPort': '22',
        'CidrIp': ref(SSHLocation),
    }, {
        'IpProtocol': 'tcp',
        'FromPort': '80',
        'ToPort': '80',
        'CidrIp': '0.0.0.0/0',
    }]


@cloudformation_dataclass
class DescribeHealthRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class DescribeHealthRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [DescribeHealthRoleAllowStatement0]


@cloudformation_dataclass
class DescribeHealthRoleAllowStatement0_1:
    resource: PolicyStatement
    action = ['elasticloadbalancing:DescribeInstanceHealth']
    resource_arn = '*'


@cloudformation_dataclass
class DescribeHealthRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [DescribeHealthRoleAllowStatement0_1]


@cloudformation_dataclass
class DescribeHealthRolePolicy:
    resource: iam.user.Policy
    policy_name = 'describe-instance-health-policy'
    policy_document = DescribeHealthRolePolicies0PolicyDocument


@cloudformation_dataclass
class DescribeHealthRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = DescribeHealthRoleAssumeRolePolicyDocument
    path = '/'
    policies = [DescribeHealthRolePolicy]


@cloudformation_dataclass
class WebServerInstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: iam.InstanceProfile
    path = '/'
    roles = [ref(DescribeHealthRole)]


@cloudformation_dataclass
class LaunchConfig:
    """AWS::AutoScaling::LaunchConfiguration resource."""

    resource: autoscaling.LaunchConfiguration
    key_name = ref(KeyName)
    image_id = ref(LatestAmiId)
    instance_type = ref(InstanceType)
    security_groups = [ref(InstanceSecurityGroup)]
    iam_instance_profile = ref(WebServerInstanceProfile)
    user_data = Base64(Sub("""#!/bin/bash -xe          
yum update -y aws-cfn-bootstrap 
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} \
         --resource LaunchConfig \
         --configsets full_install \
         --region ${AWS::Region}

/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} \
         --resource WebServerGroup \
         --region ${AWS::Region} 
"""))


@cloudformation_dataclass
class ElasticLoadBalancerListeners:
    resource: elasticloadbalancing.load_balancer.Listeners
    load_balancer_port = '80'
    instance_port = '80'
    protocol = 'HTTP'


@cloudformation_dataclass
class ElasticLoadBalancerHealthCheck:
    resource: elasticloadbalancing.load_balancer.HealthCheck
    target = 'HTTP:80/'
    healthy_threshold = '3'
    unhealthy_threshold = '5'
    interval = '30'
    timeout = '5'


@cloudformation_dataclass
class ElasticLoadBalancer:
    """AWS::ElasticLoadBalancing::LoadBalancer resource."""

    resource: elasticloadbalancing.LoadBalancer
    availability_zones = GetAZs()
    cross_zone = 'true'
    listeners = [ElasticLoadBalancerListeners]
    health_check = ElasticLoadBalancerHealthCheck


@cloudformation_dataclass
class WebServerGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: autoscaling.AutoScalingGroup
    availability_zones = GetAZs()
    launch_configuration_name = ref(LaunchConfig)
    min_size = '2'
    max_size = '4'
    load_balancer_names = [ref(ElasticLoadBalancer)]
