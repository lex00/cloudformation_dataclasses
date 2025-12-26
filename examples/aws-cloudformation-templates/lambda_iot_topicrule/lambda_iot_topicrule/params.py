"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class Name:
    resource: Parameter
    type = STRING


@cloudformation_dataclass
class DomainName:
    resource: Parameter
    type = STRING


@cloudformation_dataclass
class Port:
    resource: Parameter
    type = STRING
    default = 80
