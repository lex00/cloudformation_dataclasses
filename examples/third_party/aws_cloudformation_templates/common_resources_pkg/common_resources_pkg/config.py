"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class AppName:
    """This name will be used as part of resource names"""

    resource: Parameter
    type = STRING
    description = 'This name will be used as part of resource names'
    default = 'stacksets-sample'
