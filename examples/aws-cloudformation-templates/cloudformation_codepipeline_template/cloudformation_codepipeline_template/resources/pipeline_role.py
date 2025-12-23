"""PipelineRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PipelineRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['codepipeline.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class PipelineRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [PipelineRoleAllowStatement0]


@cloudformation_dataclass
class PipelineRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'codecommit:GetBranch',
        'codecommit:GetCommit',
        'codecommit:UploadArchive',
        'codecommit:GetUploadArchiveStatus',
    ]
    resource_arn = [ImportValue(Sub('${CodeBuildStack}-CodeCommitArn'))]


@cloudformation_dataclass
class PipelineRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [PipelineRoleAllowStatement0_1]


@cloudformation_dataclass
class PipelineRolePolicy:
    resource: iam.user.Policy
    policy_name = 'CanAccessCodeCommit'
    policy_document = PipelineRolePolicies0PolicyDocument


@cloudformation_dataclass
class PipelineRoleAllowStatement0_2:
    resource: PolicyStatement
    action = 's3:ListBucket'
    resource_arn = '*'


@cloudformation_dataclass
class PipelineRoleAllowStatement1:
    resource: PolicyStatement
    action = [
        's3:GetObject',
        's3:GetObjectVersion',
        's3:GetBucketVersioning',
        's3:PutObject',
        's3:GetBucketPolicy',
        's3:GetObjectAcl',
        's3:PutObjectAcl',
        's3:DeleteObject',
    ]
    resource_arn = [
        ImportValue(Sub('${CodeBuildStack}-PipelineS3BucketArn')),
        Sub('${filename}/*', {
    'filename': ImportValue(Sub('${CodeBuildStack}-PipelineS3BucketArn')),
}),
    ]


@cloudformation_dataclass
class PipelineRolePolicies1PolicyDocument:
    resource: PolicyDocument
    statement = [PipelineRoleAllowStatement0_2, PipelineRoleAllowStatement1]


@cloudformation_dataclass
class PipelineRolePolicy1:
    resource: iam.user.Policy
    policy_name = 'CanAccessS3'
    policy_document = PipelineRolePolicies1PolicyDocument


@cloudformation_dataclass
class PipelineRoleAllowStatement0_3:
    resource: PolicyStatement
    action = [
        'codebuild:BatchGetBuilds',
        'codebuild:StartBuild',
    ]
    resource_arn = [
        ImportValue(Sub('${CodeBuildStack}-AppBuildArn')),
        ImportValue(Sub('${CodeBuildStack}-AppDeployArn')),
    ]


@cloudformation_dataclass
class PipelineRolePolicies2PolicyDocument:
    resource: PolicyDocument
    statement = [PipelineRoleAllowStatement0_3]


@cloudformation_dataclass
class PipelineRolePolicy2:
    resource: iam.user.Policy
    policy_name = 'CanStartCodeBuild'
    policy_document = PipelineRolePolicies2PolicyDocument


@cloudformation_dataclass
class PipelineRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = PipelineRoleAssumeRolePolicyDocument
    policies = [PipelineRolePolicy, PipelineRolePolicy1, PipelineRolePolicy2]
