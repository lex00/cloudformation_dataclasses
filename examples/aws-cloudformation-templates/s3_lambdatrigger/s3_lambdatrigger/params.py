"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class NotificationBucket:
    """S3 bucket name that is the trigger to lambda"""

    resource: Parameter
    type = STRING
    description = 'S3 bucket name that is the trigger to lambda'
