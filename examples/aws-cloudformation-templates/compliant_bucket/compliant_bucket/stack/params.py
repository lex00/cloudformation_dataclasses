"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AppName:
    """This name be used as a prefix for resource names"""

    resource: Parameter
    type = STRING
    description = 'This name be used as a prefix for resource names'
