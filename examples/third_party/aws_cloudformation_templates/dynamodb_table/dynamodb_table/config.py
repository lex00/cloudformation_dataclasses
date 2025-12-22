"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class HashKeyElementName:
    """HashType PrimaryKey Name"""

    resource: Parameter
    type = STRING
    description = 'HashType PrimaryKey Name'
    allowed_pattern = '[a-zA-Z0-9]*'
    min_length = 1
    max_length = 2048
    constraint_description = 'must contain only alphanumberic characters'


@cloudformation_dataclass
class HashKeyElementType:
    """HashType PrimaryKey Type"""

    resource: Parameter
    type = STRING
    description = 'HashType PrimaryKey Type'
    default = 'S'
    allowed_pattern = '[S|N]'
    min_length = 1
    max_length = 1
    constraint_description = 'must be either S or N'


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
