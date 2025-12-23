"""Stack resources."""

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
class LaunchTemplate:
    """AWS::EC2::LaunchTemplate resource."""

    # Unknown resource type: AWS::EC2::LaunchTemplate
    resource: CloudFormationResource
    launch_template_data = {
        'KeyName': ref(KeyName),
        'ImageId': FindInMap("AWSRegionArch2AMI", AWS_REGION, FindInMap("AWSInstanceType2Arch", ref(InstanceType), 'Arch')),
        'SecurityGroups': [ref(InstanceSecurityGroup)],
        'InstanceType': ref(InstanceType),
        'UserData': Base64(Sub("""#!/bin/bash -xe
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource LaunchTemplate  --region ${AWS::Region}
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource WebServerGroup --region ${AWS::Region}
""")),
    }


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


@cloudformation_dataclass
class WebServerGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    # Unknown resource type: AWS::AutoScaling::AutoScalingGroup
    resource: CloudFormationResource
    availability_zones = GetAZs()
    launch_template = {
        'LaunchTemplateId': ref(LaunchTemplate),
        'Version': get_att(LaunchTemplate, "LatestVersionNumber"),
    }
    min_size = 2
    max_size = 5
    load_balancer_names = [ref(ElasticLoadBalancer)]


@cloudformation_dataclass
class ScheduledActionUp:
    """AWS::AutoScaling::ScheduledAction resource."""

    # Unknown resource type: AWS::AutoScaling::ScheduledAction
    resource: CloudFormationResource
    auto_scaling_group_name = ref(WebServerGroup)
    max_size = '10'
    min_size = '5'
    recurrence = '0 7 * * *'


@cloudformation_dataclass
class ScheduledActionDown:
    """AWS::AutoScaling::ScheduledAction resource."""

    # Unknown resource type: AWS::AutoScaling::ScheduledAction
    resource: CloudFormationResource
    auto_scaling_group_name = ref(WebServerGroup)
    max_size = '1'
    min_size = '1'
    recurrence = '0 19 * * *'
