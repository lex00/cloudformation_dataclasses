"""Security resources: NeptuneCloudWatchPolicy, NeptuneS3Policy, NeptuneRole."""

from . import *  # noqa: F403


@cloudformation_dataclass
class NeptuneCloudWatchPolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'EnableLogGroups'
    action = [
        'logs:CreateLogGroup',
        'logs:PutRetentionPolicy',
    ]
    resource_arn = [Sub('arn:${AWS::Partition}:logs:*:*:log-group:/aws/neptune/*')]


@cloudformation_dataclass
class NeptuneCloudWatchPolicyAllowStatement1:
    resource: PolicyStatement
    sid = 'EnableLogStreams'
    action = [
        'logs:CreateLogStream',
        'logs:PutLogEvents',
        'logs:DescribeLogStreams',
        'logs:GetLogEvents',
    ]
    resource_arn = [Sub('arn:${AWS::Partition}:logs:*:*:log-group:/aws/neptune/*:log-stream:*')]


@cloudformation_dataclass
class NeptuneCloudWatchPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [NeptuneCloudWatchPolicyAllowStatement0, NeptuneCloudWatchPolicyAllowStatement1]


@cloudformation_dataclass
class NeptuneCloudWatchPolicy:
    """AWS::IAM::ManagedPolicy resource."""

    resource: iam.ManagedPolicy
    description = 'Default policy for CloudWatch logs'
    managed_policy_name = Sub('${Env}-${AppName}-neptune-cw-policy-${AWS::Region}')
    policy_document = NeptuneCloudWatchPolicyPolicyDocument


@cloudformation_dataclass
class NeptuneS3PolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'AllowNeptuneAccessToS3'
    action = [
        's3:Get*',
        's3:List*',
    ]
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::*')]


@cloudformation_dataclass
class NeptuneS3PolicyPolicyDocument:
    resource: PolicyDocument
    statement = [NeptuneS3PolicyAllowStatement0]


@cloudformation_dataclass
class NeptuneS3Policy:
    """AWS::IAM::ManagedPolicy resource."""

    resource: iam.ManagedPolicy
    description = 'Neptune default policy for S3 access for data load'
    managed_policy_name = Sub('${Env}-${AppName}-neptune-s3-policy-${AWS::Region}')
    policy_document = NeptuneS3PolicyPolicyDocument


@cloudformation_dataclass
class NeptuneRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': [
            'monitoring.rds.amazonaws.com',
            'rds.amazonaws.com',
        ],
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class NeptuneRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [NeptuneRoleAllowStatement0]


@cloudformation_dataclass
class NeptuneRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = Sub('${Env}-${AppName}-neptune-iam-role-${AWS::Region}')
    assume_role_policy_document = NeptuneRoleAssumeRolePolicyDocument
    managed_policy_arns = [ref(NeptuneCloudWatchPolicy), ref(NeptuneS3Policy)]
    condition = 'EnableAuditLogUpload'
