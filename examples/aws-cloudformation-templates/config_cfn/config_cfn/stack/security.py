"""Security resources: ConfigRole, LambdaExecutionRole."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ConfigRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['config.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class ConfigRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ConfigRoleAllowStatement0]


@cloudformation_dataclass
class ConfigRoleAllowStatement0_1:
    resource: PolicyStatement
    action = 's3:GetBucketAcl'
    resource_arn = Join('', [
    'arn:aws:s3:::',
    ref(ConfigBucket),
])


@cloudformation_dataclass
class ConfigRoleAllowStatement1:
    resource: PolicyStatement
    action = 's3:PutObject'
    resource_arn = Join('', [
    'arn:aws:s3:::',
    ref(ConfigBucket),
    '/AWSLogs/',
    AWS_ACCOUNT_ID,
    '/*',
])
    condition = {
        STRING_EQUALS: {
            's3:x-amz-acl': 'bucket-owner-full-control',
        },
    }


@cloudformation_dataclass
class ConfigRoleAllowStatement2:
    resource: PolicyStatement
    action = 'config:Put*'
    resource_arn = '*'


@cloudformation_dataclass
class ConfigRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ConfigRoleAllowStatement0_1, ConfigRoleAllowStatement1, ConfigRoleAllowStatement2]


@cloudformation_dataclass
class ConfigRolePolicy:
    resource: iam.user.Policy
    policy_name = 'root'
    policy_document = ConfigRolePolicies0PolicyDocument


@cloudformation_dataclass
class ConfigRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = ConfigRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AWS_ConfigRole']
    policies = [ConfigRolePolicy]


@cloudformation_dataclass
class LambdaExecutionRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class LambdaExecutionRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [LambdaExecutionRoleAllowStatement0]


@cloudformation_dataclass
class LambdaExecutionRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'logs:*',
        'config:PutEvaluations',
        'ec2:DescribeVolumeAttribute',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class LambdaExecutionRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [LambdaExecutionRoleAllowStatement0_1]


@cloudformation_dataclass
class LambdaExecutionRolePolicy:
    resource: iam.user.Policy
    policy_name = 'root'
    policy_document = LambdaExecutionRolePolicies0PolicyDocument


@cloudformation_dataclass
class LambdaExecutionRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = LambdaExecutionRoleAssumeRolePolicyDocument
    policies = [LambdaExecutionRolePolicy]
