"""GreengrassResourceRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class GreengrassResourceRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 'greengrass.amazonaws.com',
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class GreengrassResourceRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [GreengrassResourceRoleAllowStatement0]


@cloudformation_dataclass
class GreengrassResourceRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'logs:CreateLogGroup',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:*:*:*')


@cloudformation_dataclass
class GreengrassResourceRoleAllowStatement1:
    resource: PolicyStatement
    action = ['iot:*']
    resource_arn = '*'


@cloudformation_dataclass
class GreengrassResourceRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [GreengrassResourceRoleAllowStatement0_1, GreengrassResourceRoleAllowStatement1]


@cloudformation_dataclass
class GreengrassResourceRolePolicy:
    resource: iam.user.Policy
    policy_document = GreengrassResourceRolePolicies0PolicyDocument
    policy_name = 'root'


@cloudformation_dataclass
class GreengrassResourceRole:
    """AWS::IAM::Role resource."""

    resource: Role
    assume_role_policy_document = GreengrassResourceRoleAssumeRolePolicyDocument
    policies = [GreengrassResourceRolePolicy]
