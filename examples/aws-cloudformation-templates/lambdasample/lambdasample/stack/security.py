"""Security resources: LambdaRole."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LambdaRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class LambdaRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [LambdaRoleAllowStatement0]


@cloudformation_dataclass
class LambdaRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = 'lambda-role'
    assume_role_policy_document = LambdaRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/AWSLambdaExecute', 'arn:aws:iam::aws:policy/AmazonS3FullAccess', 'arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess', 'arn:aws:iam::aws:policy/AmazonKinesisFullAccess']
    path = '/'
