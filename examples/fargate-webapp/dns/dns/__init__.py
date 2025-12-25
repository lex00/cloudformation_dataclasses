"""DNS stack - Route53 hosted zone and ACM certificate."""

from cloudformation_dataclasses.core import *  # noqa: F403, F401
from cloudformation_dataclasses.aws import certificatemanager, route53
from cloudformation_dataclasses.aws.certificatemanager import certificate

from .stack import *  # noqa: F403, F401

# __all__ is intentionally not defined here so that `from .stack import *`
# re-exports all stack classes for child modules that use `from .. import *`
