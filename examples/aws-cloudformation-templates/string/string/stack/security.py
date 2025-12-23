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
class TransformExecutionRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = TransformExecutionRoleAssumeRolePolicyDocument
    path = '/'
    policies = [{
        'PolicyName': 'root',
        'PolicyDocument': {
            'Version': '2012-10-17',
            'Statement': [{
                'Effect': 'Allow',
                'Action': ['logs:*'],
                'Resource': 'arn:aws:logs:*:*:*',
            }],
        },
    }]
