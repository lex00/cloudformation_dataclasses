"""Database resources: TableOfBooks."""

from . import *  # noqa: F403


@cloudformation_dataclass
class TableOfBooksAttributeDefinition:
    resource: dynamodb.global_table.AttributeDefinition
    attribute_name = 'Title'
    attribute_type = AttributeType.S


@cloudformation_dataclass
class TableOfBooksAttributeDefinition1:
    resource: dynamodb.global_table.AttributeDefinition
    attribute_name = 'Category'
    attribute_type = AttributeType.S


@cloudformation_dataclass
class TableOfBooksAttributeDefinition2:
    resource: dynamodb.global_table.AttributeDefinition
    attribute_name = 'Language'
    attribute_type = AttributeType.S


@cloudformation_dataclass
class TableOfBooksKeySchema:
    resource: dynamodb.global_table.KeySchema
    attribute_name = 'Category'
    key_type = KeyType.HASH


@cloudformation_dataclass
class TableOfBooksKeySchema1:
    resource: dynamodb.global_table.KeySchema
    attribute_name = 'Title'
    key_type = KeyType.RANGE


@cloudformation_dataclass
class TableOfBooksProvisionedThroughput:
    resource: dynamodb.table.ProvisionedThroughput
    read_capacity_units = ref(ReadCapacityUnits)
    write_capacity_units = ref(WriteCapacityUnits)


@cloudformation_dataclass
class TableOfBooksKeySchema2:
    resource: dynamodb.global_table.KeySchema
    attribute_name = 'Category'
    key_type = KeyType.HASH


@cloudformation_dataclass
class TableOfBooksKeySchema3:
    resource: dynamodb.global_table.KeySchema
    attribute_name = 'Language'
    key_type = KeyType.RANGE


@cloudformation_dataclass
class TableOfBooksProjection:
    resource: dynamodb.global_table.Projection
    projection_type = ProjectionType.KEYS_ONLY


@cloudformation_dataclass
class TableOfBooksLocalSecondaryIndex:
    resource: dynamodb.global_table.LocalSecondaryIndex
    index_name = 'LanguageIndex'
    key_schema = [TableOfBooksKeySchema2, TableOfBooksKeySchema3]
    projection = TableOfBooksProjection


@cloudformation_dataclass
class TableOfBooksKeySchema4:
    resource: dynamodb.table.KeySchema
    attribute_name = 'Title'
    key_type = KeyType.HASH


@cloudformation_dataclass
class TableOfBooksProjection1:
    resource: dynamodb.table.Projection
    projection_type = ProjectionType.KEYS_ONLY


@cloudformation_dataclass
class TableOfBooksProvisionedThroughput1:
    resource: dynamodb.table.ProvisionedThroughput
    read_capacity_units = ref(ReadCapacityUnits)
    write_capacity_units = ref(WriteCapacityUnits)


@cloudformation_dataclass
class TableOfBooksGlobalSecondaryIndex:
    resource: dynamodb.table.GlobalSecondaryIndex
    index_name = 'TitleIndex'
    key_schema = [TableOfBooksKeySchema4]
    projection = TableOfBooksProjection1
    provisioned_throughput = TableOfBooksProvisionedThroughput1


@cloudformation_dataclass
class TableOfBooksPointInTimeRecoverySpecification:
    resource: dynamodb.global_table.PointInTimeRecoverySpecification
    point_in_time_recovery_enabled = True


@cloudformation_dataclass
class TableOfBooks:
    """AWS::DynamoDB::Table resource."""

    resource: dynamodb.Table
    attribute_definitions = [TableOfBooksAttributeDefinition, TableOfBooksAttributeDefinition1, TableOfBooksAttributeDefinition2]
    key_schema = [TableOfBooksKeySchema, TableOfBooksKeySchema1]
    provisioned_throughput = TableOfBooksProvisionedThroughput
    local_secondary_indexes = [TableOfBooksLocalSecondaryIndex]
    global_secondary_indexes = [TableOfBooksGlobalSecondaryIndex]
    point_in_time_recovery_specification = TableOfBooksPointInTimeRecoverySpecification
