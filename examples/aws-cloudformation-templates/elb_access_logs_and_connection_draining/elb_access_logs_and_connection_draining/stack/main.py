"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LogsBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    access_control = 'Private'
    deletion_policy = 'Retain'


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
class ElasticLoadBalancerConnectionDrainingPolicy:
    resource: elasticloadbalancing.load_balancer.ConnectionDrainingPolicy
    enabled = 'true'
    timeout = '300'


@cloudformation_dataclass
class ElasticLoadBalancerAccessLoggingPolicy:
    resource: elasticloadbalancing.load_balancer.AccessLoggingPolicy
    s3_bucket_name = ref(LogsBucket)
    s3_bucket_prefix = 'Logs'
    enabled = 'true'
    emit_interval = '60'


@cloudformation_dataclass
class ElasticLoadBalancer:
    """AWS::ElasticLoadBalancing::LoadBalancer resource."""

    resource: elasticloadbalancing.LoadBalancer
    availability_zones = GetAZs()
    cross_zone = 'true'
    listeners = [ElasticLoadBalancerListeners]
    health_check = ElasticLoadBalancerHealthCheck
    connection_draining_policy = ElasticLoadBalancerConnectionDrainingPolicy
    access_logging_policy = ElasticLoadBalancerAccessLoggingPolicy
    depends_on = ["LogsBucketPolicy"]


@cloudformation_dataclass
class LogsBucketPolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'ELBAccessLogs20130930'
    principal = {
        'AWS': FindInMap("Region2ELBAccountId", AWS_REGION, 'AccountId'),
    }
    action = ['s3:PutObject']
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${LogsBucket}/Logs/AWSLogs/${AWS::AccountId}/*')]


@cloudformation_dataclass
class LogsBucketPolicyDenyStatement1:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${LogsBucket}/Logs/AWSLogs/${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${LogsBucket}/Logs/AWSLogs/${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class LogsBucketPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [LogsBucketPolicyAllowStatement0, LogsBucketPolicyDenyStatement1]


@cloudformation_dataclass
class LogsBucketPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(LogsBucket)
    policy_document = LogsBucketPolicyPolicyDocument


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
class LaunchConfig:
    """AWS::AutoScaling::LaunchConfiguration resource."""

    resource: autoscaling.LaunchConfiguration
    key_name = ref(KeyName)
    image_id = ref(LatestAmiId)
    security_groups = [ref(InstanceSecurityGroup)]
    instance_type = ref(InstanceType)
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
    min_size = 2
    max_size = 2
    load_balancer_names = [ref(ElasticLoadBalancer)]
