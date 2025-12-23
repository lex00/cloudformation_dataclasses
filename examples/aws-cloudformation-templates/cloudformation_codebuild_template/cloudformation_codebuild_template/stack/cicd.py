"""Cicd resources: CodeCommitRepo, AppBuild, AppDeploy."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CodeCommitRepo:
    """AWS::CodeCommit::Repository resource."""

    resource: codecommit.Repository
    repository_name = Sub('${AWS::StackName}-repo')
    repository_description = Sub('This is a repository for the ${AWS::StackName} project.')


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
