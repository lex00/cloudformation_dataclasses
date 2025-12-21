"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class PolicyBucketName:
    resource: Parameter
    type = STRING
