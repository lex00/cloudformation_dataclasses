"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CodeCommitRepo:
    """AWS::CodeCommit::Repository resource."""

    resource: codecommit.Repository
    repository_name = Sub('${AWS::StackName}-repo')
    repository_description = Sub('This is a repository for the ${AWS::StackName} project.')


@cloudformation_dataclass
class PipelineS3BucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class PipelineS3BucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = PipelineS3BucketServerSideEncryptionByDefault


@cloudformation_dataclass
class PipelineS3BucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [PipelineS3BucketServerSideEncryptionRule]


@cloudformation_dataclass
class PipelineS3BucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class PipelineS3Bucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_name = Sub('${AWS::StackName}-bucket')
    bucket_encryption = PipelineS3BucketBucketEncryption
    public_access_block_configuration = PipelineS3BucketPublicAccessBlockConfiguration


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


@cloudformation_dataclass
class AppBuildArtifacts:
    resource: codebuild.project.Artifacts
    type_ = 'CODEPIPELINE'
    encryption_disabled = True


@cloudformation_dataclass
class AppBuildEnvironmentVariable:
    resource: codebuild.project.EnvironmentVariable
    name = 'SAMPLEENVVAR'
    type_ = 'PLAINTEXT'
    value = 'test'


@cloudformation_dataclass
class AppBuildEnvironment:
    resource: codebuild.project.Environment
    compute_type = 'BUILD_GENERAL1_SMALL'
    environment_variables = [AppBuildEnvironmentVariable]
    image = ref(DockerImage)
    type_ = 'LINUX_CONTAINER'


@cloudformation_dataclass
class AppBuildSource:
    resource: codebuild.project.Source
    type_ = 'CODEPIPELINE'
    build_spec = 'codebuild-app-build.yml'


@cloudformation_dataclass
class AppBuild:
    """AWS::CodeBuild::Project resource."""

    resource: codebuild.Project
    name = Sub('${AWS::StackName}-app-build')
    artifacts = AppBuildArtifacts
    environment = AppBuildEnvironment
    service_role = ref(CodeBuildRole)
    source = AppBuildSource


@cloudformation_dataclass
class AppDeployArtifacts:
    resource: codebuild.project.Artifacts
    type_ = 'CODEPIPELINE'
    encryption_disabled = True


@cloudformation_dataclass
class AppDeployEnvironmentVariable:
    resource: codebuild.project.EnvironmentVariable
    name = 'SAMPLEENVVAR'
    type_ = 'PLAINTEXT'
    value = 'test'


@cloudformation_dataclass
class AppDeployEnvironment:
    resource: codebuild.project.Environment
    compute_type = 'BUILD_GENERAL1_SMALL'
    environment_variables = [AppDeployEnvironmentVariable]
    image = ref(DockerImage)
    type_ = 'LINUX_CONTAINER'


@cloudformation_dataclass
class AppDeploySource:
    resource: codebuild.project.Source
    type_ = 'CODEPIPELINE'
    build_spec = 'codebuild-app-deploy.yml'


@cloudformation_dataclass
class AppDeploy:
    """AWS::CodeBuild::Project resource."""

    resource: codebuild.Project
    name = Sub('${AWS::StackName}-app-deploy')
    artifacts = AppDeployArtifacts
    environment = AppDeployEnvironment
    service_role = ref(CodeBuildRole)
    source = AppDeploySource
