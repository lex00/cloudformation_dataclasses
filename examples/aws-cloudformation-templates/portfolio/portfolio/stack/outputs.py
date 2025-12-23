"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceCatalogPortfolioOutput:
    resource: Output
    value = ref(ServiceCatalogPortfolio)
    export_name = Sub('${AWS::StackName}-ServiceCatalogPortfolio')


@cloudformation_dataclass
class ServiceCatalogPortfolioNameOutput:
    resource: Output
    value = get_att(ServiceCatalogPortfolio, "PortfolioName")
    export_name = Sub('${AWS::StackName}-ServiceCatalogPortfolioName')


@cloudformation_dataclass
class ServiceCatalogProductTagOptionsDeptOutput:
    resource: Output
    value = ref(ServiceCatalogProductTagOptionsDept)
    export_name = Sub('${AWS::StackName}-ServiceCatalogProductTagOptionsDept')
