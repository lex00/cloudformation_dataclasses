"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import AppName, Dept, Env, Owner, ProvisioningArtifactDescriptionParameter, ProvisioningArtifactNameParameter, ProvisioningArtifactTemplateUrl, SCProductDescription, SCProductDistributor, SCProductName, SCProductOwner, SCProductSupport, SCSupportEmail, SCSupportUrl, ServiceCatalogPortfolioStackName, User
from .outputs import ServiceCatalogCloudFormationProductNameOutput, ServiceCatalogProvisioningArtifactIdsOutput, ServiceCatalogProvisioningArtifactNamesOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='CI/CD optimized AWS CloudFormation Sample Template for AWS Service Catalog Product creation. ### Before deployment please make sure that all parameters are reviewed and updated according the specific use case. ### **WARNING** This template creates AWS Service Catalog Product, please make sure you review billing costs for AWS Service Catalog.',
        parameters=[Env, AppName, Dept, User, Owner, ServiceCatalogPortfolioStackName, SCProductName, SCProductDescription, SCProductOwner, SCProductSupport, SCProductDistributor, SCSupportEmail, SCSupportUrl, ProvisioningArtifactTemplateUrl, ProvisioningArtifactNameParameter, ProvisioningArtifactDescriptionParameter],
        outputs=[ServiceCatalogCloudFormationProductNameOutput, ServiceCatalogProvisioningArtifactIdsOutput, ServiceCatalogProvisioningArtifactNamesOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
