"""LambdaExecutionRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LambdaExecutionRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 'lambda.amazonaws.com',
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class LambdaExecutionRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [LambdaExecutionRoleAllowStatement0]


@cloudformation_dataclass
class LambdaExecutionRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'logs:CreateLogGroup',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:*:*:*')


@cloudformation_dataclass
class LambdaExecutionRoleAllowStatement1:
    resource: PolicyStatement
    action = ['iot:*']
    resource_arn = '*'


@cloudformation_dataclass
class LambdaExecutionRoleAllowStatement2:
    resource: PolicyStatement
    action = ['greengrass:*']
    resource_arn = '*'


@cloudformation_dataclass
class LambdaExecutionRoleAllowStatement3:
    resource: PolicyStatement
    action = ['ec2:DescribeReservedInstancesOfferings']
    resource_arn = '*'


@cloudformation_dataclass
class LambdaExecutionRoleAllowStatement4:
    resource: PolicyStatement
    action = [
        'iam:CreateRole',
        'iam:AttachRolePolicy',
        'iam:GetRole',
        'iam:DeleteRole',
        'iam:PassRole',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:iam::${AWS::AccountId}:role/greengrass_cfn_${AWS::StackName}_ServiceRole')


@cloudformation_dataclass
class LambdaExecutionRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [LambdaExecutionRoleAllowStatement0_1, LambdaExecutionRoleAllowStatement1, LambdaExecutionRoleAllowStatement2, LambdaExecutionRoleAllowStatement3, LambdaExecutionRoleAllowStatement4]


@cloudformation_dataclass
class LambdaExecutionRolePolicy:
    resource: iam.user.Policy
    policy_document = LambdaExecutionRolePolicies0PolicyDocument
    policy_name = 'root'


@cloudformation_dataclass
class LambdaExecutionRole:
    """AWS::IAM::Role resource."""

    resource: Role
    assume_role_policy_document = LambdaExecutionRoleAssumeRolePolicyDocument
    policies = [LambdaExecutionRolePolicy]
