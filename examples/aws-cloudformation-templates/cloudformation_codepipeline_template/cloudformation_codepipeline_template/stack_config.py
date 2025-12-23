"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class CodeBuildStack:
    """Name of the code build stack which should have been deployed before this stack"""

    resource: Parameter
    type = STRING
    description = 'Name of the code build stack which should have been deployed before this stack'
