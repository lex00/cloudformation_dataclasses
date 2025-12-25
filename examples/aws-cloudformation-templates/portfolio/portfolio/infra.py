"""Infra resources: ServiceCatalogPortfolio, ServiceCatalogProductTagOptionsDept, ServiceCatalogProductTagOptionsEnv, ServiceCatalogProductTagOptionsUser, ServiceCatalogProductTagOptionsOwner, ServiceCatalogPortfolioShare."""

from . import *  # noqa: F403


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

    resource: servicecatalog.Portfolio
    provider_name = ref(PortfolioProviderName)
    description = ref(PortfolioDescription)
    display_name = ref(PortfolioDisplayName)
    tags = [ServiceCatalogPortfolioProvisioningParameter, ServiceCatalogPortfolioProvisioningParameter1, ServiceCatalogPortfolioProvisioningParameter2, ServiceCatalogPortfolioProvisioningParameter3, ServiceCatalogPortfolioProvisioningParameter4]


@cloudformation_dataclass
class ServiceCatalogProductTagOptionsDept:
    """AWS::ServiceCatalog::TagOption resource."""

    resource: servicecatalog.TagOption
    active = ref(ActivateProductTagOptions)
    key = 'Dept'
    value = Sub('${ProductDept}')


@cloudformation_dataclass
class ServiceCatalogProductTagOptionsEnv:
    """AWS::ServiceCatalog::TagOption resource."""

    resource: servicecatalog.TagOption
    active = ref(ActivateProductTagOptions)
    key = 'Env'
    value = Sub('${ProductEnv}')


@cloudformation_dataclass
class ServiceCatalogProductTagOptionsUser:
    """AWS::ServiceCatalog::TagOption resource."""

    resource: servicecatalog.TagOption
    active = ref(ActivateProductTagOptions)
    key = 'User'
    value = Sub('${ProductUser}')


@cloudformation_dataclass
class ServiceCatalogProductTagOptionsOwner:
    """AWS::ServiceCatalog::TagOption resource."""

    resource: servicecatalog.TagOption
    active = ref(ActivateProductTagOptions)
    key = 'Owner'
    value = Sub('${ProductOwner}')


@cloudformation_dataclass
class ServiceCatalogPortfolioShare:
    """AWS::ServiceCatalog::PortfolioShare resource."""

    resource: servicecatalog.PortfolioShare
    account_id = ref(AccountIdOfChildAWSAccount)
    portfolio_id = ref(ServiceCatalogPortfolio)
    condition = 'ConditionShareThisPortfolio'
