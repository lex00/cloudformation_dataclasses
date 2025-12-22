"""LambdaEdgeIAMRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LambdaEdgeIAMRoleAllowStatement0:
    resource: PolicyStatement
    sid = 'AllowLambdaServiceToAssumeRole'
    principal = {
        'Service': [
            'edgelambda.amazonaws.com',
            'lambda.amazonaws.com',
        ],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class LambdaEdgeIAMRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [LambdaEdgeIAMRoleAllowStatement0]


@cloudformation_dataclass
class LambdaEdgeIAMRoleAllowStatement0_1:
    resource: PolicyStatement
    action = ['lambda:PublishVersion']
    resource_arn = '*'


@cloudformation_dataclass
class LambdaEdgeIAMRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [LambdaEdgeIAMRoleAllowStatement0_1]


@cloudformation_dataclass
class LambdaEdgeIAMRolePolicy:
    resource: iam.user.Policy
    policy_name = 'PublishNewLambdaEdgeVersion'
    policy_document = LambdaEdgeIAMRolePolicies0PolicyDocument


@cloudformation_dataclass
class LambdaEdgeIAMRole:
    """AWS::IAM::Role resource."""

    resource: Role
    role_name = Sub('${AppName}-iam-lambda-edge-role-${Environment}')
    assume_role_policy_document = LambdaEdgeIAMRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole', 'arn:aws:iam::aws:policy/AWSXrayWriteOnlyAccess']
    path = '/'
    policies = [LambdaEdgeIAMRolePolicy]
