"""DescribeHealthRole - AWS::IAM::Role resource."""

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

    resource: Role
    assume_role_policy_document = DescribeHealthRoleAssumeRolePolicyDocument
    path = '/'
    policies = [DescribeHealthRolePolicy]
