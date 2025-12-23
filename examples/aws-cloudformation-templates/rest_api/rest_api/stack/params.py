"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AppName:
    resource: Parameter
    type = STRING


@cloudformation_dataclass
class UserPoolArn:
    resource: Parameter
    type = STRING
