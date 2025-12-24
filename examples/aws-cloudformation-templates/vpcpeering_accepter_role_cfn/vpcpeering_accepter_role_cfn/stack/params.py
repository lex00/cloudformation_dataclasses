"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PeerOwnerIds:
    """AWS account IDs (comma-separated) of the owners of the requester VPCs. (i.e., 123456789012,4567890123)"""

    resource: Parameter
    type = STRING
    description = 'AWS account IDs (comma-separated) of the owners of the requester VPCs. (i.e., 123456789012,4567890123)'
    allowed_pattern = '^(\\d{12})$|^((\\d{12}(,|, ))*\\d{12})$'
    constraint_description = 'Must be 12 digits. Additional accounts can be provided, separated by a "comma"'
