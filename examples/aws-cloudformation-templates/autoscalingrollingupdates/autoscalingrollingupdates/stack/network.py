"""Network resources: InstanceSecurityGroup, ElasticLoadBalancer."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    # Unknown resource type: AWS::EC2::SecurityGroup
    resource: CloudFormationResource
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
class ElasticLoadBalancer:
    """AWS::ElasticLoadBalancing::LoadBalancer resource."""

    # Unknown resource type: AWS::ElasticLoadBalancing::LoadBalancer
    resource: CloudFormationResource
    availability_zones = GetAZs()
    cross_zone = 'true'
    listeners = [{
        'LoadBalancerPort': '80',
        'InstancePort': '80',
        'Protocol': 'HTTP',
    }]
    health_check = {
        'Target': 'HTTP:80/',
        'HealthyThreshold': '3',
        'UnhealthyThreshold': '5',
        'Interval': '30',
        'Timeout': '5',
    }
