from __future__ import annotations

"""ServiceCatalogPortfolioProductAssociation - AWS::ServiceCatalog::PortfolioProductAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceCatalogPortfolioProductAssociation:
    """AWS::ServiceCatalog::PortfolioProductAssociation resource."""

    resource: PortfolioProductAssociation
    portfolio_id = ImportValue(Sub('${ServiceCatalogPortfolioStackName}-ServiceCatalogPortfolio'))
    product_id = ref(ServiceCatalogCloudFormationProduct)
    depends_on = ["ServiceCatalogCloudFormationProduct"]
