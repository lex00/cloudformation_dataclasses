"""Deployment context for production environment."""

from . import *  # noqa: F403


@cloudformation_dataclass
class ProdDeploymentContext:
    """
    Deployment context for production environment.

    Provides environment defaults, naming conventions, and shared tags.

    Resource naming pattern: {component}-{resource_name}-{stage}-{deployment_name}-{deployment_group}-{region}
    - resource_name comes directly from class name (e.g., MyData)
    - deployment_group is used for blue/green deployments
    - Example: DataPlatform-MyData-prod-001-blue-us-east-1
    """

    context: DeploymentContext
    component: str = "DataPlatform"
    stage: str = "prod"
    deployment_name: str = "001"
    deployment_group: str = "blue"  # For blue/green deployments
    region: str = "us-east-1"
    account_id: str = "123456789012"
    project_name: str = "analytics"
    # Tags will be automatically applied to all resources using this context
    tags = [
        {"Key": "Environment", "Value": "Production"},
        {"Key": "Project", "Value": "MyApplication"},
        {"Key": "ManagedBy", "Value": "cloudformation-dataclasses"},
    ]


# Instantiate context once - reused across all production resources
ctx = ProdDeploymentContext()
