"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Output,
    Parameter,
    PolicyDocument,
    PolicyStatement,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import (
    codebuild,
    codecommit,
    iam,
    s3,
)
from cloudformation_dataclasses.aws.s3 import ServerSideEncryption
from cloudformation_dataclasses.intrinsics import Sub

from .cicd import AppBuild as AppBuild
from .cicd import AppBuildArtifacts as AppBuildArtifacts
from .cicd import AppBuildEnvironment as AppBuildEnvironment
from .cicd import AppBuildEnvironmentVariable as AppBuildEnvironmentVariable
from .cicd import AppBuildSource as AppBuildSource
from .cicd import AppDeploy as AppDeploy
from .cicd import AppDeployArtifacts as AppDeployArtifacts
from .cicd import AppDeployEnvironment as AppDeployEnvironment
from .cicd import AppDeployEnvironmentVariable as AppDeployEnvironmentVariable
from .cicd import AppDeploySource as AppDeploySource
from .cicd import CodeCommitRepo as CodeCommitRepo
from .outputs import AppBuildArnOutput as AppBuildArnOutput
from .outputs import AppBuildOutput as AppBuildOutput
from .outputs import AppDeployOutput as AppDeployOutput
from .outputs import AppDeploydArnOutput as AppDeploydArnOutput
from .outputs import CodeBuildRoleArnOutput as CodeBuildRoleArnOutput
from .outputs import CodeBuildRoleOutput as CodeBuildRoleOutput
from .outputs import CodeCommitArnOutput as CodeCommitArnOutput
from .outputs import CodeCommitNameOutput as CodeCommitNameOutput
from .outputs import PipelineS3BucketArnOutput as PipelineS3BucketArnOutput
from .outputs import PipelineS3BucketOutput as PipelineS3BucketOutput
from .params import DockerImage as DockerImage
from .security import CodeBuildRole as CodeBuildRole
from .security import CodeBuildRoleAllowStatement0 as CodeBuildRoleAllowStatement0
from .security import CodeBuildRoleAllowStatement0_1 as CodeBuildRoleAllowStatement0_1
from .security import CodeBuildRoleAllowStatement0_2 as CodeBuildRoleAllowStatement0_2
from .security import CodeBuildRoleAllowStatement0_3 as CodeBuildRoleAllowStatement0_3
from .security import CodeBuildRoleAllowStatement1 as CodeBuildRoleAllowStatement1
from .security import CodeBuildRoleAssumeRolePolicyDocument as CodeBuildRoleAssumeRolePolicyDocument
from .security import CodeBuildRolePolicies0PolicyDocument as CodeBuildRolePolicies0PolicyDocument
from .security import CodeBuildRolePolicies1PolicyDocument as CodeBuildRolePolicies1PolicyDocument
from .security import CodeBuildRolePolicies2PolicyDocument as CodeBuildRolePolicies2PolicyDocument
from .security import CodeBuildRolePolicy as CodeBuildRolePolicy
from .security import CodeBuildRolePolicy1 as CodeBuildRolePolicy1
from .security import CodeBuildRolePolicy2 as CodeBuildRolePolicy2
from .storage import PipelineS3Bucket as PipelineS3Bucket
from .storage import PipelineS3BucketBucketEncryption as PipelineS3BucketBucketEncryption
from .storage import PipelineS3BucketPublicAccessBlockConfiguration as PipelineS3BucketPublicAccessBlockConfiguration
from .storage import PipelineS3BucketServerSideEncryptionByDefault as PipelineS3BucketServerSideEncryptionByDefault
from .storage import PipelineS3BucketServerSideEncryptionRule as PipelineS3BucketServerSideEncryptionRule

__all__: list[str] = ['AppBuild', 'AppBuildArnOutput', 'AppBuildArtifacts', 'AppBuildEnvironment', 'AppBuildEnvironmentVariable', 'AppBuildOutput', 'AppBuildSource', 'AppDeploy', 'AppDeployArtifacts', 'AppDeployEnvironment', 'AppDeployEnvironmentVariable', 'AppDeployOutput', 'AppDeploySource', 'AppDeploydArnOutput', 'CodeBuildRole', 'CodeBuildRoleAllowStatement0', 'CodeBuildRoleAllowStatement0_1', 'CodeBuildRoleAllowStatement0_2', 'CodeBuildRoleAllowStatement0_3', 'CodeBuildRoleAllowStatement1', 'CodeBuildRoleArnOutput', 'CodeBuildRoleAssumeRolePolicyDocument', 'CodeBuildRoleOutput', 'CodeBuildRolePolicies0PolicyDocument', 'CodeBuildRolePolicies1PolicyDocument', 'CodeBuildRolePolicies2PolicyDocument', 'CodeBuildRolePolicy', 'CodeBuildRolePolicy1', 'CodeBuildRolePolicy2', 'CodeCommitArnOutput', 'CodeCommitNameOutput', 'CodeCommitRepo', 'DockerImage', 'Output', 'Parameter', 'PipelineS3Bucket', 'PipelineS3BucketArnOutput', 'PipelineS3BucketBucketEncryption', 'PipelineS3BucketOutput', 'PipelineS3BucketPublicAccessBlockConfiguration', 'PipelineS3BucketServerSideEncryptionByDefault', 'PipelineS3BucketServerSideEncryptionRule', 'PolicyDocument', 'PolicyStatement', 'STRING', 'ServerSideEncryption', 'Sub', 'Template', 'cloudformation_dataclass', 'codebuild', 'codecommit', 'get_att', 'iam', 'ref', 's3', 'setup_resources']
