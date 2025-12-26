"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class ECRURL:
    """URL of the ECR Repository."""

    resource: Parameter
    type = STRING
    description = 'URL of the ECR Repository.'
    default = '123456789012.dkr.ecr.us-east-2.amazonaws.com/cfntest:apache'


@cloudformation_dataclass
class TCPPORT:
    """Port on which the container is listening."""

    resource: Parameter
    type = NUMBER
    description = 'Port on which the container is listening.'
    default = 80
