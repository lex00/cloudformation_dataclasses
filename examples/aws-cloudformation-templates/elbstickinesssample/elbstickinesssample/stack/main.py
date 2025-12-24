"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceSecurityGroupEgress:
    resource: ec2.security_group.Egress
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = ref(SSHLocation)


@cloudformation_dataclass
class InstanceSecurityGroupEgress1:
    resource: ec2.security_group.Egress
    ip_protocol = 'tcp'
    from_port = '80'
    to_port = '80'
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable SSH access and HTTP access on the inbound port'
    security_group_ingress = [InstanceSecurityGroupEgress, InstanceSecurityGroupEgress1]


@cloudformation_dataclass
class EC2Instance1:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    subnet_id = ref(SubnetId)
    security_group_ids = [get_att(InstanceSecurityGroup, "GroupId")]
    key_name = ref(KeyName)
    instance_type = ref(InstanceType)
    image_id = ref(LatestAmiId)
    user_data = Base64(Sub("""#!/bin/bash -xe          
yum update -y aws-cfn-bootstrap 
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} \
         --resource EC2Instance1 \
         --region ${AWS::Region}

/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} \
         --resource EC2Instance1 \
         --region ${AWS::Region} 
"""))


@cloudformation_dataclass
class EC2Instance2:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    subnet_id = ref(SubnetId)
    security_group_ids = [get_att(InstanceSecurityGroup, "GroupId")]
    key_name = ref(KeyName)
    instance_type = ref(InstanceType)
    image_id = ref(LatestAmiId)
    user_data = Base64(Sub("""#!/bin/bash -xe          
yum update -y aws-cfn-bootstrap 
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} \
         --resource EC2Instance1 \
         --region ${AWS::Region}

/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} \
         --resource EC2Instance2 \
         --region ${AWS::Region} 
"""))


@cloudformation_dataclass
class ElasticLoadBalancerLBCookieStickinessPolicy:
    resource: elasticloadbalancing.load_balancer.LBCookieStickinessPolicy
    policy_name = 'myLBPolicy'
    cookie_expiration_period = '180'


@cloudformation_dataclass
class ElasticLoadBalancerListeners:
    resource: elasticloadbalancing.load_balancer.Listeners
    load_balancer_port = '80'
    instance_port = '80'
    protocol = 'HTTP'
    policy_names = ['myLBPolicy']


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
    instances = [ref(EC2Instance1), ref(EC2Instance2)]
    lb_cookie_stickiness_policy = [ElasticLoadBalancerLBCookieStickinessPolicy]
    listeners = [ElasticLoadBalancerListeners]
    health_check = ElasticLoadBalancerHealthCheck
