"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class AppName:
    """This name be used as a prefix for resource names"""

    resource: Parameter
    type = STRING
    description = 'This name be used as a prefix for resource names'


@cloudformation_dataclass
class WebACL:
    """The web acl id of a CLOUDFRONT scoped web acl in us-east-1"""

    resource: Parameter
    type = STRING
    description = 'The web acl id of a CLOUDFRONT scoped web acl in us-east-1'
