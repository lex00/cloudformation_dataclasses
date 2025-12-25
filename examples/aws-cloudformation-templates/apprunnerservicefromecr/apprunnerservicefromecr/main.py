"""Stack resources."""

from . import *  # noqa: F403


@cloudformation_dataclass
class AppRunnerAuthenticationConfiguration:
    resource: apprunner.service.AuthenticationConfiguration
    access_role_arn = get_att(AppRunnerRole, "Arn")


@cloudformation_dataclass
class AppRunnerImageConfiguration:
    resource: apprunner.service.ImageConfiguration
    port = ref(TCPPORT)


@cloudformation_dataclass
class AppRunnerImageRepository:
    resource: apprunner.service.ImageRepository
    image_repository_type = 'ECR'
    image_identifier = ref(ECRURL)
    image_configuration = AppRunnerImageConfiguration


@cloudformation_dataclass
class AppRunnerSourceConfiguration:
    resource: apprunner.service.SourceConfiguration
    authentication_configuration = AppRunnerAuthenticationConfiguration
    auto_deployments_enabled = True
    image_repository = AppRunnerImageRepository


@cloudformation_dataclass
class AppRunner:
    """AWS::AppRunner::Service resource."""

    resource: apprunner.Service
    service_name = Join('', [
    AWS_STACK_NAME,
    '-service',
])
    source_configuration = AppRunnerSourceConfiguration
