"""ServiceCatalogCustomTagOptionsAssociation - AWS::ServiceCatalog::TagOptionAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceCatalogCustomTagOptionsAssociation:
    """AWS::ServiceCatalog::TagOptionAssociation resource."""

    resource: servicecatalog.TagOptionAssociation
    tag_option_id = ImportValue(Sub('${ServiceCatalogPortfolioStackName}-ServiceCatalogProductTagOptionsDept'))
    resource_id = ref(ServiceCatalogCloudFormationProduct)
