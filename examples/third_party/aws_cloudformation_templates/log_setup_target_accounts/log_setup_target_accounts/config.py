"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class CentralEventBusArn:
    resource: Parameter
    type = STRING
