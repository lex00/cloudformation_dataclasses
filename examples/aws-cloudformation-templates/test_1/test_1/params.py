"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class TestCount:
    resource: Parameter
    type = NUMBER
    default = 3


@cloudformation_dataclass
class TestList:
    resource: Parameter
    type = ParameterType.COMMA_DELIMITED_LIST
    default = 'foo,bar'
