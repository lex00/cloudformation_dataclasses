"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    NUMBER,
    Output,
    Parameter,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import dynamodb
from cloudformation_dataclasses.aws.dynamodb import AttributeType, KeyType, ProjectionType
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .database import TableOfBooks as TableOfBooks
from .database import TableOfBooksAttributeDefinition as TableOfBooksAttributeDefinition
from .database import TableOfBooksAttributeDefinition1 as TableOfBooksAttributeDefinition1
from .database import TableOfBooksAttributeDefinition2 as TableOfBooksAttributeDefinition2
from .database import TableOfBooksGlobalSecondaryIndex as TableOfBooksGlobalSecondaryIndex
from .database import TableOfBooksKeySchema as TableOfBooksKeySchema
from .database import TableOfBooksKeySchema1 as TableOfBooksKeySchema1
from .database import TableOfBooksKeySchema2 as TableOfBooksKeySchema2
from .database import TableOfBooksKeySchema3 as TableOfBooksKeySchema3
from .database import TableOfBooksKeySchema4 as TableOfBooksKeySchema4
from .database import TableOfBooksLocalSecondaryIndex as TableOfBooksLocalSecondaryIndex
from .database import TableOfBooksPointInTimeRecoverySpecification as TableOfBooksPointInTimeRecoverySpecification
from .database import TableOfBooksProjection as TableOfBooksProjection
from .database import TableOfBooksProjection1 as TableOfBooksProjection1
from .database import TableOfBooksProvisionedThroughput as TableOfBooksProvisionedThroughput
from .database import TableOfBooksProvisionedThroughput1 as TableOfBooksProvisionedThroughput1
from .outputs import TableNameOutput as TableNameOutput
from .params import ReadCapacityUnits as ReadCapacityUnits
from .params import WriteCapacityUnits as WriteCapacityUnits

__all__: list[str] = ['AttributeType', 'KeyType', 'NUMBER', 'Output', 'Parameter', 'ProjectionType', 'ReadCapacityUnits', 'TableNameOutput', 'TableOfBooks', 'TableOfBooksAttributeDefinition', 'TableOfBooksAttributeDefinition1', 'TableOfBooksAttributeDefinition2', 'TableOfBooksGlobalSecondaryIndex', 'TableOfBooksKeySchema', 'TableOfBooksKeySchema1', 'TableOfBooksKeySchema2', 'TableOfBooksKeySchema3', 'TableOfBooksKeySchema4', 'TableOfBooksLocalSecondaryIndex', 'TableOfBooksPointInTimeRecoverySpecification', 'TableOfBooksProjection', 'TableOfBooksProjection1', 'TableOfBooksProvisionedThroughput', 'TableOfBooksProvisionedThroughput1', 'Template', 'WriteCapacityUnits', 'cloudformation_dataclass', 'dynamodb', 'get_att', 'ref', 'setup_resources']
