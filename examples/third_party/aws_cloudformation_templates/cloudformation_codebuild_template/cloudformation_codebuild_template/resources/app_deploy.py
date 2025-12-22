from __future__ import annotations

"""AppDeploy - AWS::CodeBuild::Project resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AppDeployArtifacts:
    resource: Artifacts
    type_ = 'CODEPIPELINE'
    encryption_disabled = True


@cloudformation_dataclass
class AppDeployEnvironmentVariable:
    resource: EnvironmentVariable
    name = 'SAMPLEENVVAR'
    type_ = 'PLAINTEXT'
    value = 'test'


@cloudformation_dataclass
class AppDeployEnvironment:
    resource: Environment
    compute_type = 'BUILD_GENERAL1_SMALL'
    environment_variables = [AppDeployEnvironmentVariable]
    image = ref(DockerImage)
    type_ = 'LINUX_CONTAINER'


@cloudformation_dataclass
class AppDeploySource:
    resource: Source
    type_ = 'CODEPIPELINE'
    build_spec = 'codebuild-app-deploy.yml'


@cloudformation_dataclass
class AppDeploy:
    """AWS::CodeBuild::Project resource."""

    resource: Project
    name = Sub('${AWS::StackName}-app-deploy')
    artifacts = AppDeployArtifacts
    environment = AppDeployEnvironment
    service_role = ref(CodeBuildRole)
    source = AppDeploySource
