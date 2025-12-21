from __future__ import annotations

"""ServiceCatalogPortfolioProductAssociation - AWS::ServiceCatalog::PortfolioProductAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceCatalogPortfolioProductAssociation:
    """AWS::ServiceCatalog::PortfolioProductAssociation resource."""

    resource: PortfolioProductAssociation
    portfolio_id = ImportValue({
    'Fn::Sub': '${ServiceCatalogPortfolioStackName}-ServiceCatalogPortfolio',
})
    product_id: Ref[ServiceCatalogCloudFormationProduct] = ref()
    depends_on = ["ServiceCatalogCloudFormationProduct"]
