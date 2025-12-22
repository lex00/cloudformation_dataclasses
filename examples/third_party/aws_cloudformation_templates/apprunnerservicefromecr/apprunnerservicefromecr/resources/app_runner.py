from __future__ import annotations

"""AppRunner - AWS::AppRunner::Service resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AppRunnerAuthenticationConfiguration:
    resource: AuthenticationConfiguration
    access_role_arn = get_att(AppRunnerRole, "Arn")


@cloudformation_dataclass
class AppRunnerImageConfiguration:
    resource: ImageConfiguration
    port = ref(TCPPORT)


@cloudformation_dataclass
class AppRunnerImageRepository:
    resource: ImageRepository
    image_repository_type = 'ECR'
    image_identifier = ref(ECRURL)
    image_configuration = AppRunnerImageConfiguration


@cloudformation_dataclass
class AppRunnerSourceConfiguration:
    resource: SourceConfiguration
    authentication_configuration = AppRunnerAuthenticationConfiguration
    auto_deployments_enabled = True
    image_repository = AppRunnerImageRepository


@cloudformation_dataclass
class AppRunner:
    """AWS::AppRunner::Service resource."""

    resource: Service
    service_name = Join('', [
    AWS_STACK_NAME,
    '-service',
])
    source_configuration = AppRunnerSourceConfiguration
