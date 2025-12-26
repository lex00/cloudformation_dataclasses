"""Security resources: CodeBuildRole."""

from . import *  # noqa: F403


@cloudformation_dataclass
class CodeBuildRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 'codebuild.amazonaws.com',
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class CodeBuildRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [CodeBuildRoleAllowStatement0]


@cloudformation_dataclass
class CodeBuildRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'logs:CreateLogStream',
        'logs:CreateLogGroup',
        'logs:PutLogEvents',
    ]
    resource_arn = [Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/codebuild/${AWS::StackName}*:log-stream:*')]


@cloudformation_dataclass
class CodeBuildRoleAllowStatement1:
    resource: PolicyStatement
    action = [
        's3:GetObject',
        's3:PutObject',
    ]
    resource_arn = [
        get_att(PipelineS3Bucket, "Arn"),
        Sub('${PipelineS3Bucket.Arn}/*'),
    ]


@cloudformation_dataclass
class CodeBuildRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [CodeBuildRoleAllowStatement0_1, CodeBuildRoleAllowStatement1]


@cloudformation_dataclass
class CodeBuildRolePolicy:
    resource: iam.user.Policy
    policy_name = 'CanLog'
    policy_document = CodeBuildRolePolicies0PolicyDocument


@cloudformation_dataclass
class CodeBuildRoleAllowStatement0_2:
    resource: PolicyStatement
    action = ['s3:GetObject']
    resource_arn = [get_att(PipelineS3Bucket, "Arn")]


@cloudformation_dataclass
class CodeBuildRolePolicies1PolicyDocument:
    resource: PolicyDocument
    statement = [CodeBuildRoleAllowStatement0_2]


@cloudformation_dataclass
class CodeBuildRolePolicy1:
    resource: iam.user.Policy
    policy_name = 'CanAccessS3'
    policy_document = CodeBuildRolePolicies1PolicyDocument


@cloudformation_dataclass
class CodeBuildRoleAllowStatement0_3:
    resource: PolicyStatement
    action = ['codebuild:*']
    resource_arn = [Sub('arn:${AWS::Partition}:codebuild:${AWS::Region}:${AWS::AccountId}:report-group/${AWS::StackName}*')]


@cloudformation_dataclass
class CodeBuildRolePolicies2PolicyDocument:
    resource: PolicyDocument
    statement = [CodeBuildRoleAllowStatement0_3]


@cloudformation_dataclass
class CodeBuildRolePolicy2:
    resource: iam.user.Policy
    policy_name = 'CanCreateReports'
    policy_document = CodeBuildRolePolicies2PolicyDocument


@cloudformation_dataclass
class CodeBuildRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = CodeBuildRoleAssumeRolePolicyDocument
    policies = [CodeBuildRolePolicy, CodeBuildRolePolicy1, CodeBuildRolePolicy2]
