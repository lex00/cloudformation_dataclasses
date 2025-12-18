"""Deployment context for production environment."""

from . import *  # noqa: F403


# =============================================================================
# Tags
# =============================================================================


@cloudformation_dataclass
class EnvironmentTag:
    """Environment tag for production."""

    resource: Tag
    key = "Environment"
    value = "Production"


@cloudformation_dataclass
class ProjectTag:
    """Project tag."""

    resource: Tag
    key = "Project"
    value = "MyApplication"


@cloudformation_dataclass
class ManagedByTag:
    """ManagedBy tag."""

    resource: Tag
    key = "ManagedBy"
    value = "cloudformation-dataclasses"


# =============================================================================
# Deployment Context
# =============================================================================


@cloudformation_dataclass
class ProdDeploymentContext:
    """
    Deployment context for production environment.

    Provides environment defaults, naming conventions, and shared tags.

    Resource naming pattern: {project_name}-{component}-{resource_name}-{stage}-{deployment_name}-{deployment_group}-{region}
    - project_name is the top-level project/organization name
    - resource_name comes directly from class name (e.g., MyData)
    - deployment_group is used for blue/green deployments
    - Example: analytics-DataPlatform-MyData-prod-001-blue-us-east-1
    """

    context: DeploymentContext
    component = "DataPlatform"
    stage = "prod"
    deployment_name = "001"
    deployment_group = "blue"  # For blue/green deployments
    region = "us-east-1"
    account_id = "123456789012"
    project_name = "analytics"
    # Tags will be automatically applied to all resources using this context
    tags = [EnvironmentTag, ProjectTag, ManagedByTag]


# Instantiate context once - reused across all production resources
ctx = ProdDeploymentContext()
