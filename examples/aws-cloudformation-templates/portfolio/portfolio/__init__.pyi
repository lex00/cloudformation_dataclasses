"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Output,
    Parameter,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.template import Condition as TemplateCondition
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import servicecatalog
from cloudformation_dataclasses.intrinsics import Equals, Sub
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .infra import ServiceCatalogPortfolio as ServiceCatalogPortfolio
from .infra import ServiceCatalogPortfolioProvisioningParameter as ServiceCatalogPortfolioProvisioningParameter
from .infra import ServiceCatalogPortfolioProvisioningParameter1 as ServiceCatalogPortfolioProvisioningParameter1
from .infra import ServiceCatalogPortfolioProvisioningParameter2 as ServiceCatalogPortfolioProvisioningParameter2
from .infra import ServiceCatalogPortfolioProvisioningParameter3 as ServiceCatalogPortfolioProvisioningParameter3
from .infra import ServiceCatalogPortfolioProvisioningParameter4 as ServiceCatalogPortfolioProvisioningParameter4
from .infra import ServiceCatalogPortfolioShare as ServiceCatalogPortfolioShare
from .infra import ServiceCatalogProductTagOptionsDept as ServiceCatalogProductTagOptionsDept
from .infra import ServiceCatalogProductTagOptionsEnv as ServiceCatalogProductTagOptionsEnv
from .infra import ServiceCatalogProductTagOptionsOwner as ServiceCatalogProductTagOptionsOwner
from .infra import ServiceCatalogProductTagOptionsUser as ServiceCatalogProductTagOptionsUser
from .outputs import ServiceCatalogPortfolioNameOutput as ServiceCatalogPortfolioNameOutput
from .outputs import ServiceCatalogPortfolioOutput as ServiceCatalogPortfolioOutput
from .outputs import ServiceCatalogProductTagOptionsDeptOutput as ServiceCatalogProductTagOptionsDeptOutput
from .params import AccountIdOfChildAWSAccount as AccountIdOfChildAWSAccount
from .params import ActivateProductTagOptions as ActivateProductTagOptions
from .params import ConditionShareThisPortfolioCondition as ConditionShareThisPortfolioCondition
from .params import Dept as Dept
from .params import Env as Env
from .params import Owner as Owner
from .params import PortfolioDescription as PortfolioDescription
from .params import PortfolioDisplayName as PortfolioDisplayName
from .params import PortfolioProviderName as PortfolioProviderName
from .params import ProductDept as ProductDept
from .params import ProductEnv as ProductEnv
from .params import ProductOwner as ProductOwner
from .params import ProductUser as ProductUser
from .params import ShareThisPortfolio as ShareThisPortfolio
from .params import User as User

__all__: list[str] = ['AccountIdOfChildAWSAccount', 'ActivateProductTagOptions', 'ConditionShareThisPortfolioCondition', 'Dept', 'Env', 'Equals', 'Output', 'Owner', 'Parameter', 'PortfolioDescription', 'PortfolioDisplayName', 'PortfolioProviderName', 'ProductDept', 'ProductEnv', 'ProductOwner', 'ProductUser', 'STRING', 'ServiceCatalogPortfolio', 'ServiceCatalogPortfolioNameOutput', 'ServiceCatalogPortfolioOutput', 'ServiceCatalogPortfolioProvisioningParameter', 'ServiceCatalogPortfolioProvisioningParameter1', 'ServiceCatalogPortfolioProvisioningParameter2', 'ServiceCatalogPortfolioProvisioningParameter3', 'ServiceCatalogPortfolioProvisioningParameter4', 'ServiceCatalogPortfolioShare', 'ServiceCatalogProductTagOptionsDept', 'ServiceCatalogProductTagOptionsDeptOutput', 'ServiceCatalogProductTagOptionsEnv', 'ServiceCatalogProductTagOptionsOwner', 'ServiceCatalogProductTagOptionsUser', 'ShareThisPortfolio', 'Sub', 'Template', 'TemplateCondition', 'User', 'cloudformation_dataclass', 'get_att', 'ref', 'servicecatalog', 'setup_resources']
