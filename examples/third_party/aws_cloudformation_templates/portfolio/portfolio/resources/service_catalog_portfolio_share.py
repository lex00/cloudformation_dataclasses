from __future__ import annotations

"""ServiceCatalogPortfolioShare - AWS::ServiceCatalog::PortfolioShare resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceCatalogPortfolioShare:
    """AWS::ServiceCatalog::PortfolioShare resource."""

    resource: PortfolioShare
    account_id = ref(AccountIdOfChildAWSAccount)
    portfolio_id: Ref[ServiceCatalogPortfolio] = ref()
    condition = 'ConditionShareThisPortfolio'
