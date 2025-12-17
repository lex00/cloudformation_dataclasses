"""Tests for secondary_indexes DynamoDB example."""

import json

from ..secondary_indexes import build_template


def test_template_structure():
    """Verify template has correct structure."""
    template = build_template()
    result = template.to_dict()

    assert result["AWSTemplateFormatVersion"] == "2010-09-09"
    assert "Description" in result
    assert "Parameters" in result
    assert "Resources" in result
    assert "Outputs" in result


def test_template_parameters():
    """Verify all parameters are present with correct types."""
    template = build_template()
    result = template.to_dict()
    params = result["Parameters"]

    # Both parameters present
    assert "ReadCapacityUnits" in params
    assert "WriteCapacityUnits" in params

    # Verify types
    assert params["ReadCapacityUnits"]["Type"] == "Number"
    assert params["WriteCapacityUnits"]["Type"] == "Number"

    # Verify defaults
    assert params["ReadCapacityUnits"]["Default"] == 5
    assert params["WriteCapacityUnits"]["Default"] == 10

    # Verify constraints
    assert params["ReadCapacityUnits"]["MinValue"] == 5
    assert params["ReadCapacityUnits"]["MaxValue"] == 10000
    assert params["WriteCapacityUnits"]["MinValue"] == 5
    assert params["WriteCapacityUnits"]["MaxValue"] == 10000


def test_template_resources():
    """Verify DynamoDB table resource configuration."""
    template = build_template()
    result = template.to_dict()
    resources = result["Resources"]

    # Logical ID matches class name
    assert "TableOfBooks" in resources
    table = resources["TableOfBooks"]

    # Correct type
    assert table["Type"] == "AWS::DynamoDB::Table"

    # Has all required properties
    props = table["Properties"]
    assert "AttributeDefinitions" in props
    assert "KeySchema" in props
    assert "ProvisionedThroughput" in props
    assert "LocalSecondaryIndexes" in props
    assert "GlobalSecondaryIndexes" in props
    assert "PointInTimeRecoverySpecification" in props


def test_attribute_definitions():
    """Verify all three attributes are defined."""
    template = build_template()
    result = template.to_dict()
    props = result["Resources"]["TableOfBooks"]["Properties"]
    attr_defs = props["AttributeDefinitions"]

    # Three attributes: Title, Category, Language
    assert len(attr_defs) == 3

    attr_names = {a["AttributeName"] for a in attr_defs}
    assert attr_names == {"Title", "Category", "Language"}

    # All are String type
    for attr in attr_defs:
        assert attr["AttributeType"] == "S"


def test_key_schema():
    """Verify composite key schema (Category HASH + Title RANGE)."""
    template = build_template()
    result = template.to_dict()
    props = result["Resources"]["TableOfBooks"]["Properties"]
    key_schema = props["KeySchema"]

    # Composite key with 2 elements
    assert len(key_schema) == 2

    # Find HASH and RANGE keys
    hash_key = next(k for k in key_schema if k["KeyType"] == "HASH")
    range_key = next(k for k in key_schema if k["KeyType"] == "RANGE")

    assert hash_key["AttributeName"] == "Category"
    assert range_key["AttributeName"] == "Title"


def test_local_secondary_index():
    """Verify Local Secondary Index configuration."""
    template = build_template()
    result = template.to_dict()
    props = result["Resources"]["TableOfBooks"]["Properties"]
    lsi_list = props["LocalSecondaryIndexes"]

    assert len(lsi_list) == 1
    lsi = lsi_list[0]

    # Index name
    assert lsi["IndexName"] == "LanguageIndex"

    # Key schema: Category (HASH) + Language (RANGE)
    key_schema = lsi["KeySchema"]
    assert len(key_schema) == 2

    hash_key = next(k for k in key_schema if k["KeyType"] == "HASH")
    range_key = next(k for k in key_schema if k["KeyType"] == "RANGE")

    assert hash_key["AttributeName"] == "Category"
    assert range_key["AttributeName"] == "Language"

    # Projection type
    assert lsi["Projection"]["ProjectionType"] == "KEYS_ONLY"


def test_global_secondary_index():
    """Verify Global Secondary Index configuration."""
    template = build_template()
    result = template.to_dict()
    props = result["Resources"]["TableOfBooks"]["Properties"]
    gsi_list = props["GlobalSecondaryIndexes"]

    assert len(gsi_list) == 1
    gsi = gsi_list[0]

    # Index name
    assert gsi["IndexName"] == "TitleIndex"

    # Key schema: Title (HASH) only
    key_schema = gsi["KeySchema"]
    assert len(key_schema) == 1
    assert key_schema[0]["AttributeName"] == "Title"
    assert key_schema[0]["KeyType"] == "HASH"

    # Projection type
    assert gsi["Projection"]["ProjectionType"] == "KEYS_ONLY"

    # GSI has its own provisioned throughput
    assert "ProvisionedThroughput" in gsi
    assert gsi["ProvisionedThroughput"]["ReadCapacityUnits"] == {"Ref": "ReadCapacityUnits"}
    assert gsi["ProvisionedThroughput"]["WriteCapacityUnits"] == {"Ref": "WriteCapacityUnits"}


def test_provisioned_throughput():
    """Verify provisioned throughput uses Ref."""
    template = build_template()
    result = template.to_dict()
    props = result["Resources"]["TableOfBooks"]["Properties"]
    throughput = props["ProvisionedThroughput"]

    assert throughput["ReadCapacityUnits"] == {"Ref": "ReadCapacityUnits"}
    assert throughput["WriteCapacityUnits"] == {"Ref": "WriteCapacityUnits"}


def test_point_in_time_recovery():
    """Verify point-in-time recovery is enabled."""
    template = build_template()
    result = template.to_dict()
    props = result["Resources"]["TableOfBooks"]["Properties"]

    assert props["PointInTimeRecoverySpecification"]["PointInTimeRecoveryEnabled"] is True


def test_template_outputs():
    """Verify output references the table."""
    template = build_template()
    result = template.to_dict()
    outputs = result["Outputs"]

    assert "TableName" in outputs
    assert outputs["TableName"]["Value"] == {"Ref": "TableOfBooks"}
    assert "Description" in outputs["TableName"]


def test_template_json_serialization():
    """Verify template can be serialized to JSON."""
    template = build_template()
    json_str = template.to_json()

    # Should be valid JSON
    parsed = json.loads(json_str)
    assert "Resources" in parsed
    assert "TableOfBooks" in parsed["Resources"]


def test_template_validation():
    """Verify template passes basic validation."""
    template = build_template()
    errors = template.validate()
    assert errors == []
