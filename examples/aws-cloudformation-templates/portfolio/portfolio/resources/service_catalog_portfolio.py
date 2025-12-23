"""ServiceCatalogPortfolio - AWS::ServiceCatalog::Portfolio resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceCatalogPortfolioProvisioningParameter:
    resource: servicecatalog.cloud_formation_provisioned_product.ProvisioningParameter
    key = 'Name'
    value = Sub('${PortfolioDisplayName}')


@cloudformation_dataclass
class ServiceCatalogPortfolioProvisioningParameter1:
    resource: servicecatalog.cloud_formation_provisioned_product.ProvisioningParameter
    key = 'Dept'
    value = Sub('${Dept}')


@cloudformation_dataclass
class ServiceCatalogPortfolioProvisioningParameter2:
    resource: servicecatalog.cloud_formation_provisioned_product.ProvisioningParameter
    key = 'Env'
    value = Sub('${Env}')


@cloudformation_dataclass
class ServiceCatalogPortfolioProvisioningParameter3:
    resource: servicecatalog.cloud_formation_provisioned_product.ProvisioningParameter
    key = 'User'
    value = Sub('${User}')


@cloudformation_dataclass
class ServiceCatalogPortfolioProvisioningParameter4:
    resource: servicecatalog.cloud_formation_provisioned_product.ProvisioningParameter
    key = 'Owner'
    value = Sub('${Owner}')


@cloudformation_dataclass
class ServiceCatalogPortfolio:
    """AWS::ServiceCatalog::Portfolio resource."""

    resource: Portfolio
    provider_name = ref(PortfolioProviderName)
    description = ref(PortfolioDescription)
    display_name = ref(PortfolioDisplayName)
    tags = [ServiceCatalogPortfolioProvisioningParameter, ServiceCatalogPortfolioProvisioningParameter1, ServiceCatalogPortfolioProvisioningParameter2, ServiceCatalogPortfolioProvisioningParameter3, ServiceCatalogPortfolioProvisioningParameter4]
