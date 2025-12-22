"""TestTable - AWS::DynamoDB::Table resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TestTableAttributeDefinition:
    resource: dynamodb.global_table.AttributeDefinition
    attribute_name = 'id'
    attribute_type = AttributeType.S


@cloudformation_dataclass
class TestTableKeySchema:
    resource: dynamodb.global_table.KeySchema
    attribute_name = 'id'
    key_type = KeyType.HASH


@cloudformation_dataclass
class TestTable:
    """AWS::DynamoDB::Table resource."""

    resource: dynamodb.Table
    billing_mode = 'PAY_PER_REQUEST'
    table_name = Sub('${AppName}-test')
    attribute_definitions = [TestTableAttributeDefinition]
    key_schema = [TestTableKeySchema]
