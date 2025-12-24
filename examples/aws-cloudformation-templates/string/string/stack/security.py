"""Security resources: TransformExecutionRole."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TransformExecutionRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class TransformExecutionRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [TransformExecutionRoleAllowStatement0]


@cloudformation_dataclass
class TransformExecutionRoleAllowStatement0_1:
    resource: PolicyStatement
    action = ['logs:*']
    resource_arn = 'arn:aws:logs:*:*:*'


@cloudformation_dataclass
class TransformExecutionRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [TransformExecutionRoleAllowStatement0_1]


@cloudformation_dataclass
class TransformExecutionRolePolicy:
    resource: iam.user.Policy
    policy_name = 'root'
    policy_document = TransformExecutionRolePolicies0PolicyDocument


@cloudformation_dataclass
class TransformExecutionRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = TransformExecutionRoleAssumeRolePolicyDocument
    path = '/'
    policies = [TransformExecutionRolePolicy]
