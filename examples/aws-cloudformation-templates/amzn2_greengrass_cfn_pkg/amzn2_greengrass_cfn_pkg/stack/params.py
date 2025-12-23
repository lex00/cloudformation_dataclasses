"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DBName:
    """The database name"""

    resource: Parameter
    type = STRING
    description = 'The database name'
    default = 'MyDatabase'
    allowed_pattern = '[a-zA-Z][a-zA-Z0-9]*'
    min_length = 1
    max_length = 64
    constraint_description = 'must begin with a letter and contain only alphanumeric characters.'


@cloudformation_dataclass
class DBUser:
    """The database admin account username"""

    resource: Parameter
    type = STRING
    description = 'The database admin account username'
    allowed_pattern = '[a-zA-Z][a-zA-Z0-9]*'
    min_length = 1
    max_length = 16
    constraint_description = 'must begin with a letter and contain only alphanumeric characters.'
    no_echo = True
