"""ServiceCatalogPortfolioShare - AWS::ServiceCatalog::PortfolioShare resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceCatalogPortfolioShare:
    """AWS::ServiceCatalog::PortfolioShare resource."""

    resource: servicecatalog.PortfolioShare
    account_id = ref(AccountIdOfChildAWSAccount)
    portfolio_id = ref(ServiceCatalogPortfolio)
    condition = 'ConditionShareThisPortfolio'
