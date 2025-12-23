"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class myDynamoDBTableAttributeDefinition:
    resource: dynamodb.global_table.AttributeDefinition
    attribute_name = ref(HashKeyElementName)
    attribute_type = ref(HashKeyElementType)


@cloudformation_dataclass
class myDynamoDBTableKeySchema:
    resource: dynamodb.global_table.KeySchema
    attribute_name = ref(HashKeyElementName)
    key_type = KeyType.HASH


@cloudformation_dataclass
class myDynamoDBTableProvisionedThroughput:
    resource: dynamodb.table.ProvisionedThroughput
    read_capacity_units = ref(ReadCapacityUnits)
    write_capacity_units = ref(WriteCapacityUnits)


@cloudformation_dataclass
class myDynamoDBTablePointInTimeRecoverySpecification:
    resource: dynamodb.global_table.PointInTimeRecoverySpecification
    point_in_time_recovery_enabled = True


@cloudformation_dataclass
class myDynamoDBTable:
    """AWS::DynamoDB::Table resource."""

    resource: dynamodb.Table
    attribute_definitions = [myDynamoDBTableAttributeDefinition]
    key_schema = [myDynamoDBTableKeySchema]
    provisioned_throughput = myDynamoDBTableProvisionedThroughput
    point_in_time_recovery_specification = myDynamoDBTablePointInTimeRecoverySpecification
