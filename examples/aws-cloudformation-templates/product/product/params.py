"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class Env:
    """Please specify the target Environment. Used for tagging and resource names. Mandatory LOWER CASE."""

    resource: Parameter
    type = STRING
    description = 'Please specify the target Environment. Used for tagging and resource names. Mandatory LOWER CASE.'
    default = 'dev'
    allowed_values = [
    'test',
    'dev',
    'prod',
]


@cloudformation_dataclass
class AppName:
    """Please specify the Application Name. Used for tagging and resource names. Mandatory LOWER CASE."""

    resource: Parameter
    type = STRING
    description = 'Please specify the Application Name. Used for tagging and resource names. Mandatory LOWER CASE.'
    default = 'app'


@cloudformation_dataclass
class Dept:
    """Please specify the Department. Used for tagging"""

    resource: Parameter
    type = STRING
    description = 'Please specify the Department. Used for tagging'
    default = '1234'


@cloudformation_dataclass
class User:
    """Please specify the User. Used for tagging"""

    resource: Parameter
    type = STRING
    description = 'Please specify the User. Used for tagging'
    default = 'User'


@cloudformation_dataclass
class Owner:
    """Please specify the Owner. Used for tagging"""

    resource: Parameter
    type = STRING
    description = 'Please specify the Owner. Used for tagging'
    default = 'Owner'


@cloudformation_dataclass
class ServiceCatalogPortfolioStackName:
    """Please specify the Service Catalog Portfolio Stack Name."""

    resource: Parameter
    type = STRING
    description = 'Please specify the Service Catalog Portfolio Stack Name.'
    default = ''


@cloudformation_dataclass
class SCProductName:
    """Please specify ServiceCatalog Product Name."""

    resource: Parameter
    type = STRING
    description = 'Please specify ServiceCatalog Product Name.'
    default = 'ProductName'


@cloudformation_dataclass
class SCProductDescription:
    """Please specify ServiceCatalog Product Name Description."""

    resource: Parameter
    type = STRING
    description = 'Please specify ServiceCatalog Product Name Description.'
    default = 'ProductDescription'


@cloudformation_dataclass
class SCProductOwner:
    """Please specify ServiceCatalog Product Owner."""

    resource: Parameter
    type = STRING
    description = 'Please specify ServiceCatalog Product Owner.'
    default = 'ProductOwner'


@cloudformation_dataclass
class SCProductSupport:
    """Please specify ServiceCatalog Product Support."""

    resource: Parameter
    type = STRING
    description = 'Please specify ServiceCatalog Product Support.'
    default = 'IT Support can be reached @support'


@cloudformation_dataclass
class SCProductDistributor:
    """Please specify ServiceCatalog Product Distributor."""

    resource: Parameter
    type = STRING
    description = 'Please specify ServiceCatalog Product Distributor.'
    default = 'App Vendor'


@cloudformation_dataclass
class SCSupportEmail:
    """Please specify ServiceCatalog Product Support Email."""

    resource: Parameter
    type = STRING
    description = 'Please specify ServiceCatalog Product Support Email.'
    default = 'support@example.com'


@cloudformation_dataclass
class SCSupportUrl:
    """Please specify ServiceCatalog Product Support URL."""

    resource: Parameter
    type = STRING
    description = 'Please specify ServiceCatalog Product Support URL.'
    default = 'https://www.support.example.com'


@cloudformation_dataclass
class ProvisioningArtifactTemplateUrl:
    """Please specify the S3 URL of the template"""

    resource: Parameter
    type = STRING
    description = 'Please specify the S3 URL of the template'
    default = 'https://awsdocs.s3.amazonaws.com/servicecatalog/development-environment.template'


@cloudformation_dataclass
class ProvisioningArtifactNameParameter:
    """Please specify ServiceCatalog Product Artifact Name."""

    resource: Parameter
    type = STRING
    description = 'Please specify ServiceCatalog Product Artifact Name.'
    default = 'ProductExample'


@cloudformation_dataclass
class ProvisioningArtifactDescriptionParameter:
    """Please specify ServiceCatalog Product Artifact Description."""

    resource: Parameter
    type = STRING
    description = 'Please specify ServiceCatalog Product Artifact Description.'
    default = 'ProductExample'
