"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    NUMBER,
    Output,
    Parameter,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import dynamodb
from cloudformation_dataclasses.aws.dynamodb import KeyType

from .database import myDynamoDBTable as myDynamoDBTable
from .database import myDynamoDBTableAttributeDefinition as myDynamoDBTableAttributeDefinition
from .database import myDynamoDBTableKeySchema as myDynamoDBTableKeySchema
from .database import myDynamoDBTablePointInTimeRecoverySpecification as myDynamoDBTablePointInTimeRecoverySpecification
from .database import myDynamoDBTableProvisionedThroughput as myDynamoDBTableProvisionedThroughput
from .outputs import TableNameOutput as TableNameOutput
from .params import HashKeyElementName as HashKeyElementName
from .params import HashKeyElementType as HashKeyElementType
from .params import ReadCapacityUnits as ReadCapacityUnits
from .params import WriteCapacityUnits as WriteCapacityUnits

__all__: list[str] = ['HashKeyElementName', 'HashKeyElementType', 'KeyType', 'NUMBER', 'Output', 'Parameter', 'ReadCapacityUnits', 'STRING', 'TableNameOutput', 'Template', 'WriteCapacityUnits', 'cloudformation_dataclass', 'dynamodb', 'get_att', 'myDynamoDBTable', 'myDynamoDBTableAttributeDefinition', 'myDynamoDBTableKeySchema', 'myDynamoDBTablePointInTimeRecoverySpecification', 'myDynamoDBTableProvisionedThroughput', 'ref', 'setup_resources']
