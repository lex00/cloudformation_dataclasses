"""
Simple DynamoDB Table example.

Inspired by AWS's DynamoDB/DynamoDB_Table.yaml template.
Demonstrates:
- DynamoDB Table with hash key
- Provisioned throughput configuration
- Point-in-time recovery
- Template parameters for flexibility
- Block-style @cloudformation_dataclass syntax
- DeploymentContext for resource naming and tagging
"""

from . import *  # noqa: F403


# =============================================================================
# Tags
# =============================================================================


@cloudformation_dataclass
class EnvironmentTag:
    """Environment tag for production."""

    resource: Tag
    key = "Environment"
    value = "Production"


@cloudformation_dataclass
class ManagedByTag:
    """ManagedBy tag."""

    resource: Tag
    key = "ManagedBy"
    value = "cloudformation-dataclasses"


# =============================================================================
# Deployment Context
# =============================================================================


@cloudformation_dataclass
class DynamoDBContext:
    """
    Deployment context for DynamoDB examples.

    Resource naming pattern: {project_name}-{component}-{resource_name}-{stage}
    Example: myapp-database-MyTable-prod
    """

    context: DeploymentContext
    project_name = "myapp"
    component = "database"
    stage = "prod"
    region = "us-east-1"
    tags = [EnvironmentTag, ManagedByTag]
    naming_pattern = "{project_name}-{component}-{resource_name}-{stage}"


ctx = DynamoDBContext()


# =============================================================================
# Parameters
# =============================================================================


@cloudformation_dataclass
class HashKeyName:
    """Name of the hash key attribute."""

    resource: Parameter
    type = STRING
    default = "id"
    allowed_pattern = "[a-zA-Z0-9]*"
    min_length = 1
    max_length = 2048
    constraint_description = "must contain only alphanumeric characters"


@cloudformation_dataclass
class HashKeyType:
    """Type of the hash key (S=String, N=Number)."""

    resource: Parameter
    type = STRING
    default = S
    allowed_pattern = "[S|N]"
    min_length = 1
    max_length = 1
    constraint_description = "must be either S or N"


@cloudformation_dataclass
class ReadCapacity:
    """Provisioned read throughput."""

    resource: Parameter
    type = NUMBER
    default = 5
    min_value = 5
    max_value = 10000
    constraint_description = "must be between 5 and 10000"


@cloudformation_dataclass
class WriteCapacity:
    """Provisioned write throughput."""

    resource: Parameter
    type = NUMBER
    default = 10
    min_value = 5
    max_value = 10000
    constraint_description = "must be between 5 and 10000"


# =============================================================================
# Resources
# =============================================================================


@cloudformation_dataclass
class MyAttributeDefinition:
    """Attribute definition using parameter references."""

    resource: AttributeDefinition
    attribute_name = ref(HashKeyName)
    attribute_type = ref(HashKeyType)


@cloudformation_dataclass
class MyKeySchema:
    """Key schema for hash key."""

    resource: KeySchema
    attribute_name = ref(HashKeyName)
    key_type = HASH


@cloudformation_dataclass
class MyProvisionedThroughput:
    """Provisioned throughput using parameter references."""

    resource: ProvisionedThroughput
    read_capacity_units = ref(ReadCapacity)
    write_capacity_units = ref(WriteCapacity)


@cloudformation_dataclass
class MyPointInTimeRecovery:
    """Point-in-time recovery configuration."""

    resource: PointInTimeRecoverySpecification
    point_in_time_recovery_enabled = True


@cloudformation_dataclass
class MyTable:
    """
    Simple DynamoDB table with hash key and point-in-time recovery.

    Resource naming uses the deployment context pattern:
    - Logical ID: MyTable (class name)
    - Physical name: myapp-database-MyTable-prod
    """

    resource: Table
    context = ctx
    attribute_definitions = [MyAttributeDefinition]
    key_schema = [MyKeySchema]
    provisioned_throughput = MyProvisionedThroughput
    point_in_time_recovery_specification = MyPointInTimeRecovery


# =============================================================================
# Outputs
# =============================================================================


@cloudformation_dataclass
class TableName:
    """Table name of the newly created DynamoDB table."""

    resource: Output
    value = ref(MyTable)
    description = "Table name of the newly created DynamoDB table"


# =============================================================================
# Template
# =============================================================================


@cloudformation_dataclass
class SimpleDynamoDBTemplate:
    """
    Simple DynamoDB table template.

    Demonstrates fully declarative template definition with:
    - Parameters as class references
    - Resources as class references
    - Outputs as class references
    """

    resource: Template
    description = (
        "AWS CloudFormation Sample Template DynamoDB_Table: "
        "This template demonstrates the creation of a DynamoDB table."
    )
    parameters = [HashKeyName, HashKeyType, ReadCapacity, WriteCapacity]
    resources = [MyTable]
    outputs = [TableName]


def build_template() -> Template:
    """Build the simple DynamoDB table template."""
    return SimpleDynamoDBTemplate().resource


if __name__ == "__main__":
    import json

    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))
