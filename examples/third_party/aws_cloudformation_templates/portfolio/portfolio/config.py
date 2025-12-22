"""Configuration - Parameters, Mappings, Conditions."""

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
class ProductEnv:
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
class ProductDept:
    """Please specify the Department. Used for tagging"""

    resource: Parameter
    type = STRING
    description = 'Please specify the Department. Used for tagging'
    default = '1234'


@cloudformation_dataclass
class ProductUser:
    """Please specify the User. Used for tagging"""

    resource: Parameter
    type = STRING
    description = 'Please specify the User. Used for tagging'
    default = 'User'


@cloudformation_dataclass
class ProductOwner:
    """Please specify the Owner. Used for tagging"""

    resource: Parameter
    type = STRING
    description = 'Please specify the Owner. Used for tagging'
    default = 'Owner'


@cloudformation_dataclass
class PortfolioProviderName:
    """Please specify the Portfolio Provider Name."""

    resource: Parameter
    type = STRING
    description = 'Please specify the Portfolio Provider Name.'
    default = 'IT Provider'


@cloudformation_dataclass
class PortfolioDescription:
    """Please specify the Portfolio Description."""

    resource: Parameter
    type = STRING
    description = 'Please specify the Portfolio Description.'
    default = 'Service Catalog Portfolio for Business Unit (BU)'


@cloudformation_dataclass
class PortfolioDisplayName:
    """Please specify the Portfolio Description. Must satisfy regular expression pattern, (^[a-zA-Z0-9_\-]*)"""

    resource: Parameter
    type = STRING
    description = 'Please specify the Portfolio Description. Must satisfy regular expression pattern, (^[a-zA-Z0-9_\\-]*)'
    default = 'Test_Portfolio'


@cloudformation_dataclass
class ActivateProductTagOptions:
    """Activate Custom Tag Options? Used for portfolio tagging"""

    resource: Parameter
    type = STRING
    description = 'Activate Custom Tag Options? Used for portfolio tagging'
    default = 'true'
    allowed_values = [
    'true',
    'false',
]


@cloudformation_dataclass
class ShareThisPortfolio:
    """Please specify if this Portfolio will be Shared with additonal accounts?"""

    resource: Parameter
    type = STRING
    description = 'Please specify if this Portfolio will be Shared with additonal accounts?'
    default = 'false'
    allowed_values = [
    'true',
    'false',
]


@cloudformation_dataclass
class AccountIdOfChildAWSAccount:
    """Please specify the Sub AWS Account ID."""

    resource: Parameter
    type = STRING
    description = 'Please specify the Sub AWS Account ID.'
    default = '1234567890'


@cloudformation_dataclass
class ConditionShareThisPortfolioCondition:
    resource: Condition
    expression = Equals(ref(ShareThisPortfolio), 'true')
