"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class AccountIdSource:
    """Account Id of the source AWS Account for replication (ie: 123456789012)."""

    resource: Parameter
    type = STRING
    description = 'Account Id of the source AWS Account for replication (ie: 123456789012).'
