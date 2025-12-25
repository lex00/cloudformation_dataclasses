"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class AdministrationAccountId:
    """Account ID where the StackSet administration role exists"""

    resource: Parameter
    type = STRING
    description = 'Account ID where the StackSet administration role exists'
