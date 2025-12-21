from __future__ import annotations

"""TableOfBooks - AWS::DynamoDB::Table resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TableOfBooksAttributeDefinition:
    resource: AttributeDefinition
    attribute_name = 'Title'
    attribute_type = AttributeType.S


@cloudformation_dataclass
class TableOfBooksAttributeDefinition1:
    resource: AttributeDefinition
    attribute_name = 'Category'
    attribute_type = AttributeType.S


@cloudformation_dataclass
class TableOfBooksAttributeDefinition2:
    resource: AttributeDefinition
    attribute_name = 'Language'
    attribute_type = AttributeType.S


@cloudformation_dataclass
class TableOfBooksKeySchema:
    resource: KeySchema
    attribute_name = 'Category'
    key_type = KeyType.HASH


@cloudformation_dataclass
class TableOfBooksKeySchema1:
    resource: KeySchema
    attribute_name = 'Title'
    key_type = KeyType.RANGE


@cloudformation_dataclass
class TableOfBooksProvisionedThroughput:
    resource: ProvisionedThroughput
    read_capacity_units = ref(ReadCapacityUnits)
    write_capacity_units = ref(WriteCapacityUnits)


@cloudformation_dataclass
class TableOfBooksKeySchema2:
    resource: KeySchema
    attribute_name = 'Category'
    key_type = KeyType.HASH


@cloudformation_dataclass
class TableOfBooksKeySchema3:
    resource: KeySchema
    attribute_name = 'Language'
    key_type = KeyType.RANGE


@cloudformation_dataclass
class TableOfBooksProjection:
    resource: Projection
    projection_type = ProjectionType.KEYS_ONLY


@cloudformation_dataclass
class TableOfBooksLocalSecondaryIndex:
    resource: LocalSecondaryIndex
    index_name = 'LanguageIndex'
    key_schema = [TableOfBooksKeySchema2, TableOfBooksKeySchema3]
    projection = TableOfBooksProjection


@cloudformation_dataclass
class TableOfBooksKeySchema4:
    resource: KeySchema
    attribute_name = 'Title'
    key_type = KeyType.HASH


@cloudformation_dataclass
class TableOfBooksProjection1:
    resource: Projection
    projection_type = ProjectionType.KEYS_ONLY


@cloudformation_dataclass
class TableOfBooksProvisionedThroughput1:
    resource: ProvisionedThroughput
    read_capacity_units = ref(ReadCapacityUnits)
    write_capacity_units = ref(WriteCapacityUnits)


@cloudformation_dataclass
class TableOfBooksGlobalSecondaryIndex:
    resource: GlobalSecondaryIndex
    index_name = 'TitleIndex'
    key_schema = [TableOfBooksKeySchema4]
    projection = TableOfBooksProjection1
    provisioned_throughput = TableOfBooksProvisionedThroughput1


@cloudformation_dataclass
class TableOfBooksPointInTimeRecoverySpecification:
    resource: PointInTimeRecoverySpecification
    point_in_time_recovery_enabled = True


@cloudformation_dataclass
class TableOfBooks:
    """AWS::DynamoDB::Table resource."""

    resource: Table
    attribute_definitions = [TableOfBooksAttributeDefinition, TableOfBooksAttributeDefinition1, TableOfBooksAttributeDefinition2]
    key_schema = [TableOfBooksKeySchema, TableOfBooksKeySchema1]
    provisioned_throughput = TableOfBooksProvisionedThroughput
    local_secondary_indexes = [TableOfBooksLocalSecondaryIndex]
    global_secondary_indexes = [TableOfBooksGlobalSecondaryIndex]
    point_in_time_recovery_specification = TableOfBooksPointInTimeRecoverySpecification
