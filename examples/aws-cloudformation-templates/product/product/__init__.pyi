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
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import servicecatalog
from cloudformation_dataclasses.intrinsics import ImportValue, Sub
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .infra import ServiceCatalogCloudFormationProduct as ServiceCatalogCloudFormationProduct
from .infra import ServiceCatalogCloudFormationProductProvisioningArtifactProperties as ServiceCatalogCloudFormationProductProvisioningArtifactProperties
from .infra import ServiceCatalogCloudFormationProductProvisioningParameter as ServiceCatalogCloudFormationProductProvisioningParameter
from .infra import ServiceCatalogCloudFormationProductProvisioningParameter1 as ServiceCatalogCloudFormationProductProvisioningParameter1
from .infra import ServiceCatalogCloudFormationProductProvisioningParameter2 as ServiceCatalogCloudFormationProductProvisioningParameter2
from .infra import ServiceCatalogCloudFormationProductProvisioningParameter3 as ServiceCatalogCloudFormationProductProvisioningParameter3
from .infra import ServiceCatalogCloudFormationProductProvisioningParameter4 as ServiceCatalogCloudFormationProductProvisioningParameter4
from .infra import ServiceCatalogCloudFormationProductProvisioningParameter5 as ServiceCatalogCloudFormationProductProvisioningParameter5
from .infra import ServiceCatalogCustomTagOptionsAssociation as ServiceCatalogCustomTagOptionsAssociation
from .infra import ServiceCatalogPortfolioProductAssociation as ServiceCatalogPortfolioProductAssociation
from .outputs import ServiceCatalogCloudFormationProductNameOutput as ServiceCatalogCloudFormationProductNameOutput
from .outputs import ServiceCatalogProvisioningArtifactIdsOutput as ServiceCatalogProvisioningArtifactIdsOutput
from .outputs import ServiceCatalogProvisioningArtifactNamesOutput as ServiceCatalogProvisioningArtifactNamesOutput
from .params import AppName as AppName
from .params import Dept as Dept
from .params import Env as Env
from .params import Owner as Owner
from .params import ProvisioningArtifactDescriptionParameter as ProvisioningArtifactDescriptionParameter
from .params import ProvisioningArtifactNameParameter as ProvisioningArtifactNameParameter
from .params import ProvisioningArtifactTemplateUrl as ProvisioningArtifactTemplateUrl
from .params import SCProductDescription as SCProductDescription
from .params import SCProductDistributor as SCProductDistributor
from .params import SCProductName as SCProductName
from .params import SCProductOwner as SCProductOwner
from .params import SCProductSupport as SCProductSupport
from .params import SCSupportEmail as SCSupportEmail
from .params import SCSupportUrl as SCSupportUrl
from .params import ServiceCatalogPortfolioStackName as ServiceCatalogPortfolioStackName
from .params import User as User

__all__: list[str] = ['AppName', 'Dept', 'Env', 'ImportValue', 'Output', 'Owner', 'Parameter', 'ProvisioningArtifactDescriptionParameter', 'ProvisioningArtifactNameParameter', 'ProvisioningArtifactTemplateUrl', 'SCProductDescription', 'SCProductDistributor', 'SCProductName', 'SCProductOwner', 'SCProductSupport', 'SCSupportEmail', 'SCSupportUrl', 'STRING', 'ServiceCatalogCloudFormationProduct', 'ServiceCatalogCloudFormationProductNameOutput', 'ServiceCatalogCloudFormationProductProvisioningArtifactProperties', 'ServiceCatalogCloudFormationProductProvisioningParameter', 'ServiceCatalogCloudFormationProductProvisioningParameter1', 'ServiceCatalogCloudFormationProductProvisioningParameter2', 'ServiceCatalogCloudFormationProductProvisioningParameter3', 'ServiceCatalogCloudFormationProductProvisioningParameter4', 'ServiceCatalogCloudFormationProductProvisioningParameter5', 'ServiceCatalogCustomTagOptionsAssociation', 'ServiceCatalogPortfolioProductAssociation', 'ServiceCatalogPortfolioStackName', 'ServiceCatalogProvisioningArtifactIdsOutput', 'ServiceCatalogProvisioningArtifactNamesOutput', 'Sub', 'Template', 'User', 'cloudformation_dataclass', 'get_att', 'ref', 'servicecatalog', 'setup_resources']
