"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class DockerImage:
    """Docker image to use for the build phase"""

    resource: Parameter
    type = STRING
    description = 'Docker image to use for the build phase'
    default = 'aws/codebuild/standard:7.0'
