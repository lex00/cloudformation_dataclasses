"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class GetFromListJsonData:
    """Example JSON data representing a list of values."""

    resource: Parameter
    type = STRING
    description = 'Example JSON data representing a list of values.'
    default = '["test0", "test1", "test2"]'


@cloudformation_dataclass
class GetFromListJsonDataQuery:
    """Example query for JSON data representing a list of values."""

    resource: Parameter
    type = STRING
    description = 'Example query for JSON data representing a list of values.'
    default = '[2]'


@cloudformation_dataclass
class GetFromMapJsonData:
    """Example JSON data representing a map data structure."""

    resource: Parameter
    type = STRING
    description = 'Example JSON data representing a map data structure.'
    default = '{"test": {"test1": ["x", "y"]}}'


@cloudformation_dataclass
class GetFromMapJsonDataQuery:
    """Example query for JSON data representing a map data structure."""

    resource: Parameter
    type = STRING
    description = 'Example query for JSON data representing a map data structure.'
    default = '["test"]["test1"][1]'
