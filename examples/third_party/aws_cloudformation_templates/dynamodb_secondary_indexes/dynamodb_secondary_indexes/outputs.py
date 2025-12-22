"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class TableNameOutput:
    """Name of the newly created DynamoDB table"""

    resource: Output
    value = ref("TableOfBooks")
    description = 'Name of the newly created DynamoDB table'
