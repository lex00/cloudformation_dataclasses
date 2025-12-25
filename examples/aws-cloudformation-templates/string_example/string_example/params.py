"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class InputString:
    resource: Parameter
    type = STRING
    default = 'This is a test input string'
