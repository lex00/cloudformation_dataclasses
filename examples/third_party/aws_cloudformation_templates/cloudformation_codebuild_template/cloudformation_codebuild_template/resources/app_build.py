"""AppBuild - AWS::CodeBuild::Project resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AppBuildArtifacts:
    resource: Artifacts
    type_ = 'CODEPIPELINE'
    encryption_disabled = True


@cloudformation_dataclass
class AppBuildEnvironmentVariable:
    resource: codebuild.EnvironmentVariable
    name = 'SAMPLEENVVAR'
    type_ = 'PLAINTEXT'
    value = 'test'


@cloudformation_dataclass
class AppBuildEnvironment:
    resource: codebuild.Environment
    compute_type = 'BUILD_GENERAL1_SMALL'
    environment_variables = [AppBuildEnvironmentVariable]
    image = ref(DockerImage)
    type_ = 'LINUX_CONTAINER'


@cloudformation_dataclass
class AppBuildSource:
    resource: codebuild.Source
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
