"""Security resources: DescribeHealthRole, WebServerInstanceProfile."""

from .. import *  # noqa: F403


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
