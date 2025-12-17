"""
DynamoDB Table with Secondary Indexes example.

Inspired by AWS's DynamoDB/DynamoDB_Secondary_Indexes.yaml template.
Demonstrates:
- DynamoDB Table with composite key (hash + range)
- Local Secondary Index (LSI)
- Global Secondary Index (GSI)
- KEYS_ONLY projection type
- Block-style @cloudformation_dataclass syntax
- DeploymentContext for resource naming and tagging
"""

from . import *  # noqa: F403


# =============================================================================
# Deployment Context
# =============================================================================


@cloudformation_dataclass
class DynamoDBContext:
    """
    Deployment context for DynamoDB examples.

    Resource naming pattern: {project_name}-{component}-{resource_name}-{stage}
    Example: bookstore-catalog-TableOfBooks-prod
    """

    context: DeploymentContext
    project_name = "bookstore"
    component = "catalog"
    stage = "prod"
    region = "us-east-1"
    tags = [
        {"Key": "Environment", "Value": "Production"},
        {"Key": "ManagedBy", "Value": "cloudformation-dataclasses"},
    ]
    naming_pattern = "{project_name}-{component}-{resource_name}-{stage}"


ctx = DynamoDBContext()


# =============================================================================
# Parameters
# =============================================================================


@cloudformation_dataclass
class ReadCapacityUnits:
    """Provisioned read throughput."""

    resource: Parameter
    type = NUMBER
    default = 5
    min_value = 5
    max_value = 10000
    constraint_description = "must be between 5 and 10000"


@cloudformation_dataclass
class WriteCapacityUnits:
    """Provisioned write throughput."""

    resource: Parameter
    type = NUMBER
    default = 10
    min_value = 5
    max_value = 10000
    constraint_description = "must be between 5 and 10000"


# =============================================================================
# Attribute Definitions
# =============================================================================


@cloudformation_dataclass
class TitleAttribute:
    """Title attribute (String)."""

    resource: AttributeDefinition
    attribute_name = "Title"
    attribute_type = S


@cloudformation_dataclass
class CategoryAttribute:
    """Category attribute (String)."""

    resource: AttributeDefinition
    attribute_name = "Category"
    attribute_type = S


@cloudformation_dataclass
class LanguageAttribute:
    """Language attribute (String)."""

    resource: AttributeDefinition
    attribute_name = "Language"
    attribute_type = S


# =============================================================================
# Key Schemas
# =============================================================================


@cloudformation_dataclass
class CategoryKeySchema:
    """Category as hash key."""

    resource: KeySchema
    attribute_name = "Category"
    key_type = HASH


@cloudformation_dataclass
class TitleKeySchema:
    """Title as range key for main table."""

    resource: KeySchema
    attribute_name = "Title"
    key_type = RANGE


@cloudformation_dataclass
class LanguageKeySchema:
    """Language as range key for LSI."""

    resource: KeySchema
    attribute_name = "Language"
    key_type = RANGE


@cloudformation_dataclass
class TitleHashKeySchema:
    """Title as hash key for GSI."""

    resource: KeySchema
    attribute_name = "Title"
    key_type = HASH


# =============================================================================
# Projections
# =============================================================================


@cloudformation_dataclass
class KeysOnlyProjection:
    """KEYS_ONLY projection for indexes."""

    resource: Projection
    projection_type = KEYS_ONLY


# =============================================================================
# Provisioned Throughput
# =============================================================================


@cloudformation_dataclass
class TableProvisionedThroughput:
    """Provisioned throughput using parameter references."""

    resource: ProvisionedThroughput
    read_capacity_units = ref(ReadCapacityUnits)
    write_capacity_units = ref(WriteCapacityUnits)


# =============================================================================
# Secondary Indexes
# =============================================================================


@cloudformation_dataclass
class LanguageIndex:
    """Local Secondary Index for querying by language within a category."""

    resource: LocalSecondaryIndex
    index_name = "LanguageIndex"
    key_schema = [CategoryKeySchema, LanguageKeySchema]
    projection = KeysOnlyProjection


@cloudformation_dataclass
class TitleIndex:
    """Global Secondary Index for querying by title."""

    resource: GlobalSecondaryIndex
    index_name = "TitleIndex"
    key_schema = [TitleHashKeySchema]
    projection = KeysOnlyProjection
    provisioned_throughput = TableProvisionedThroughput


# =============================================================================
# Point-in-Time Recovery
# =============================================================================


@cloudformation_dataclass
class PointInTimeRecovery:
    """Point-in-time recovery configuration."""

    resource: PointInTimeRecoverySpecification
    point_in_time_recovery_enabled = True


# =============================================================================
# Resources
# =============================================================================


@cloudformation_dataclass
class TableOfBooks:
    """
    DynamoDB table storing books with composite key (Category + Title).

    - Primary Key: Category (HASH) + Title (RANGE)
    - LSI: LanguageIndex - Query books by language within a category
    - GSI: TitleIndex - Query books by title across all categories

    Resource naming uses the deployment context pattern:
    - Logical ID: TableOfBooks (class name)
    - Physical name: bookstore-catalog-TableOfBooks-prod
    """

    resource: Table
    context = ctx
    attribute_definitions = [TitleAttribute, CategoryAttribute, LanguageAttribute]
    key_schema = [CategoryKeySchema, TitleKeySchema]
    provisioned_throughput = TableProvisionedThroughput
    local_secondary_indexes = [LanguageIndex]
    global_secondary_indexes = [TitleIndex]
    point_in_time_recovery_specification = PointInTimeRecovery


# =============================================================================
# Outputs
# =============================================================================


@cloudformation_dataclass
class TableName:
    """Name of the newly created DynamoDB table."""

    resource: Output
    value = ref(TableOfBooks)
    description = "Name of the newly created DynamoDB table"


# =============================================================================
# Template
# =============================================================================


def build_template() -> Template:
    """Build the DynamoDB table with secondary indexes template."""
    template = Template(
        description=(
            "AWS CloudFormation Sample Template DynamoDB_Secondary_Indexes: "
            "Create a DynamoDB table with local and global secondary indexes. "
            "**WARNING** This template creates an Amazon DynamoDB table. "
            "You will be billed for the AWS resources used if you create a "
            "stack from this template."
        ),
    )

    # Add parameters
    template.add_parameter(ReadCapacityUnits())
    template.add_parameter(WriteCapacityUnits())

    # Add resources
    template.add_resource(TableOfBooks())

    # Add outputs
    template.add_output(TableName())

    return template


if __name__ == "__main__":
    import json

    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))
