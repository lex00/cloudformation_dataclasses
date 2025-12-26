"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class TableNameOutput:
    """Table name of the newly created DynamoDB table"""

    resource: Output
    value = ref(myDynamoDBTable)
    description = 'Table name of the newly created DynamoDB table'
