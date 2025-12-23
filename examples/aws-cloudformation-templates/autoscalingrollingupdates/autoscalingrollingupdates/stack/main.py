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
class DescribeHealthRole:
    """AWS::IAM::Role resource."""

    # Unknown resource type: AWS::IAM::Role
    resource: CloudFormationResource
    assume_role_policy_document = DescribeHealthRoleAssumeRolePolicyDocument
    path = '/'
    policies = [{
        'PolicyName': 'describe-instance-health-policy',
        'PolicyDocument': {
            'Statement': [{
                'Effect': 'Allow',
                'Action': ['elasticloadbalancing:DescribeInstanceHealth'],
                'Resource': '*',
            }],
        },
    }]


@cloudformation_dataclass
class WebServerInstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    # Unknown resource type: AWS::IAM::InstanceProfile
    resource: CloudFormationResource
    path = '/'
    roles = [ref(DescribeHealthRole)]


@cloudformation_dataclass
class LaunchTemplate:
    """AWS::EC2::LaunchTemplate resource."""

    # Unknown resource type: AWS::EC2::LaunchTemplate
    resource: CloudFormationResource
    launch_template_data = {
        'KeyName': ref(KeyName),
        'ImageId': FindInMap("AWSRegionArch2AMI", AWS_REGION, FindInMap("AWSInstanceType2Arch", ref(InstanceType), 'Arch')),
        'InstanceType': ref(InstanceType),
        'SecurityGroups': [ref(InstanceSecurityGroup)],
        'IamInstanceProfile': {
            'Name': ref(WebServerInstanceProfile),
        },
        'UserData': Base64(Sub("""#!/bin/bash -xe
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-init -v --stack ${AWS::StackId} --resource LaunchTemplate --configsets full_install --region ${AWS::Region}
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackId} --resource WebServerGroup --region ${AWS::Region}
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
    max_size = 4
    load_balancer_names = [ref(ElasticLoadBalancer)]
