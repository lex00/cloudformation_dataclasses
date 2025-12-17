"""
Simple DynamoDB Table example.

Inspired by AWS's DynamoDB/DynamoDB_Table.yaml template.
Demonstrates:
- DynamoDB Table with hash key
- Provisioned throughput configuration
- Point-in-time recovery
- Template parameters for flexibility
- Block-style @cloudformation_dataclass syntax
"""

from . import *  # noqa: F403


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
    """Simple DynamoDB table with hash key and point-in-time recovery."""

    resource: Table
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


def build_template() -> Template:
    """Build the simple DynamoDB table template."""
    template = Template(
        description=(
            "AWS CloudFormation Sample Template DynamoDB_Table: "
            "This template demonstrates the creation of a DynamoDB table."
        ),
    )

    # Add parameters
    template.add_parameter(HashKeyName())
    template.add_parameter(HashKeyType())
    template.add_parameter(ReadCapacity())
    template.add_parameter(WriteCapacity())

    # Add resources
    template.add_resource(MyTable())

    # Add outputs
    template.add_output(TableName())

    return template


if __name__ == "__main__":
    import json

    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))
