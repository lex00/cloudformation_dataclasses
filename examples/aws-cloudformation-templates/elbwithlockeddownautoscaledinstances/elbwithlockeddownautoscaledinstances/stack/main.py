"""Stack resources."""

from .. import *  # noqa: F403


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
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable SSH access and HTTP access on the inbound port'
    security_group_ingress = [{
        'IpProtocol': 'tcp',
        'FromPort': '80',
        'ToPort': '80',
        'SourceSecurityGroupOwnerId': get_att(ElasticLoadBalancer, "SourceSecurityGroup.OwnerAlias"),
        'SourceSecurityGroupName': get_att(ElasticLoadBalancer, "SourceSecurityGroup.GroupName"),
    }, {
        'IpProtocol': 'tcp',
        'FromPort': '22',
        'ToPort': '22',
        'CidrIp': ref(SSHLocation),
    }]


@cloudformation_dataclass
class LaunchConfig:
    """AWS::AutoScaling::LaunchConfiguration resource."""

    resource: autoscaling.LaunchConfiguration
    image_id = ref(LatestAmiId)
    security_groups = [ref(InstanceSecurityGroup)]
    instance_type = ref(InstanceType)
    key_name = ref(KeyName)
    user_data = Base64(Sub("""#!/bin/bash -xe          
yum update -y aws-cfn-bootstrap 
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} \
         --resource LaunchConfig \
         --region ${AWS::Region}

/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} \
         --resource WebServerGroup \
         --region ${AWS::Region} 
"""))


@cloudformation_dataclass
class WebServerGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: autoscaling.AutoScalingGroup
    availability_zones = GetAZs()
    launch_configuration_name = ref(LaunchConfig)
    min_size = '2'
    max_size = '2'
    load_balancer_names = [ref(ElasticLoadBalancer)]
