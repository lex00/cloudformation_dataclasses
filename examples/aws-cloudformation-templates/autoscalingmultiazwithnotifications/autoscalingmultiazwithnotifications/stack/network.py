"""Network resources: TargetGroup, LoadBalancerSecurityGroup, ElasticLoadBalancer, LoadBalancerListener, InstanceSecurityGroup."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TargetGroup:
    """AWS::ElasticLoadBalancingV2::TargetGroup resource."""

    # Unknown resource type: AWS::ElasticLoadBalancingV2::TargetGroup
    resource: CloudFormationResource
    health_check_path = '/'
    name = 'MyTargetGroup'
    port = 80
    protocol = 'HTTP'
    target_type = 'instance'
    vpc_id = ref(VPC)


@cloudformation_dataclass
class LoadBalancerSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    # Unknown resource type: AWS::EC2::SecurityGroup
    resource: CloudFormationResource
    group_description = 'Allows inbound traffic on port 443'
    security_group_ingress = [{
        'IpProtocol': 'tcp',
        'FromPort': 443,
        'ToPort': 443,
        'CidrIp': '0.0.0.0/0',
    }]
    vpc_id = ref(VPC)


@cloudformation_dataclass
class ElasticLoadBalancer:
    """AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

    # Unknown resource type: AWS::ElasticLoadBalancingV2::LoadBalancer
    resource: CloudFormationResource
    scheme = 'internet-facing'
    security_groups = [ref(LoadBalancerSecurityGroup)]
    subnets = ref(Subnets)
    type_ = 'application'


@cloudformation_dataclass
class LoadBalancerListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    # Unknown resource type: AWS::ElasticLoadBalancingV2::Listener
    resource: CloudFormationResource
    default_actions = [{
        'Type': 'forward',
        'TargetGroupArn': ref(TargetGroup),
    }]
    load_balancer_arn = ref(ElasticLoadBalancer)
    port = 443
    protocol = 'HTTPS'
    ssl_policy = 'ELBSecurityPolicy-2016-08'
    certificates = [{
        'CertificateArn': ref(CertificateArn),
    }]


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    # Unknown resource type: AWS::EC2::SecurityGroup
    resource: CloudFormationResource
    group_description = 'Enable SSH access and HTTP from the load balancer only'
    security_group_ingress = [{
        'IpProtocol': 'tcp',
        'FromPort': 22,
        'ToPort': 22,
        'CidrIp': ref(SSHLocation),
    }, {
        'IpProtocol': 'tcp',
        'FromPort': 80,
        'ToPort': 80,
        'SourceSecurityGroupId': ref(LoadBalancerSecurityGroup),
    }]
