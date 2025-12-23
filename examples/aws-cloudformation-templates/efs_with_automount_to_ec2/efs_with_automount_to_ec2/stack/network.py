"""Network resources: ELBSecurityGroup, InstanceSecurityGroup, EFSSecurityGroup, ElasticLoadBalancer."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ELBSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable public access HTTP and HTTPS'
    security_group_ingress = [{
        'CidrIp': '0.0.0.0/0',
        'FromPort': '80',
        'IpProtocol': 'tcp',
        'ToPort': '80',
    }, {
        'CidrIp': '0.0.0.0/0',
        'FromPort': '443',
        'IpProtocol': 'tcp',
        'ToPort': '443',
    }]
    vpc_id = ref(VPC)


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable SSH public access and HTTP from the load balancer only'
    security_group_ingress = [{
        'CidrIp': '0.0.0.0/0',
        'FromPort': '22',
        'IpProtocol': 'tcp',
        'ToPort': '22',
    }, {
        'FromPort': '80',
        'IpProtocol': 'tcp',
        'SourceSecurityGroupId': get_att(ELBSecurityGroup, "GroupId"),
        'ToPort': '80',
    }]
    vpc_id = ref(VPC)


@cloudformation_dataclass
class EFSSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable NFS access from EC2'
    security_group_ingress = [{
        'FromPort': '2049',
        'IpProtocol': 'tcp',
        'ToPort': '2049',
        'SourceSecurityGroupId': get_att(InstanceSecurityGroup, "GroupId"),
    }]
    vpc_id = ref(VPC)


@cloudformation_dataclass
class ElasticLoadBalancerHealthCheck:
    resource: elasticloadbalancing.load_balancer.HealthCheck
    healthy_threshold = '3'
    interval = '30'
    target = Join('', [
    'HTTP:',
    '80',
    '/',
])
    timeout = '5'
    unhealthy_threshold = '5'


@cloudformation_dataclass
class ElasticLoadBalancerListeners:
    resource: elasticloadbalancing.load_balancer.Listeners
    instance_port = '80'
    load_balancer_port = '80'
    protocol = 'HTTP'


@cloudformation_dataclass
class ElasticLoadBalancer:
    """AWS::ElasticLoadBalancing::LoadBalancer resource."""

    resource: elasticloadbalancing.LoadBalancer
    security_groups = [ref(ELBSecurityGroup)]
    subnets = ref(Subnets)
    cross_zone = 'true'
    health_check = ElasticLoadBalancerHealthCheck
    listeners = [ElasticLoadBalancerListeners]
