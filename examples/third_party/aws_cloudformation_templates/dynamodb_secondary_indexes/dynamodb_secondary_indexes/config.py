"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class ReadCapacityUnits:
    """Provisioned read throughput"""

    resource: Parameter
    type = NUMBER
    description = 'Provisioned read throughput'
    default = '5'
    min_value = 5
    max_value = 10000
    constraint_description = 'must be between 5 and 10000'


@cloudformation_dataclass
class WriteCapacityUnits:
    """Provisioned write throughput"""

    resource: Parameter
    type = NUMBER
    description = 'Provisioned write throughput'
    default = '10'
    min_value = 5
    max_value = 10000
    constraint_description = 'must be between 5 and 10000'
