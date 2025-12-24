"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AccountIdDestination:
    """Account Id of the destination AWS Account for replication (ie: 123456789012)."""

    resource: Parameter
    type = STRING
    description = 'Account Id of the destination AWS Account for replication (ie: 123456789012).'
