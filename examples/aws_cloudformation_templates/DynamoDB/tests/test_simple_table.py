"""Tests for simple_table DynamoDB example."""

import json

from ..simple_table import build_template


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

    # All 4 parameters present
    assert "HashKeyName" in params
    assert "HashKeyType" in params
    assert "ReadCapacity" in params
    assert "WriteCapacity" in params

    # Verify types
    assert params["HashKeyName"]["Type"] == "String"
    assert params["HashKeyType"]["Type"] == "String"
    assert params["ReadCapacity"]["Type"] == "Number"
    assert params["WriteCapacity"]["Type"] == "Number"

    # Verify defaults
    assert params["HashKeyName"]["Default"] == "id"
    assert params["HashKeyType"]["Default"] == "S"
    assert params["ReadCapacity"]["Default"] == 5
    assert params["WriteCapacity"]["Default"] == 10

    # Verify constraints
    assert params["HashKeyName"]["AllowedPattern"] == "[a-zA-Z0-9]*"
    assert params["HashKeyType"]["AllowedPattern"] == "[S|N]"
    assert params["ReadCapacity"]["MinValue"] == 5
    assert params["ReadCapacity"]["MaxValue"] == 10000


def test_template_resources():
    """Verify DynamoDB table resource configuration."""
    template = build_template()
    result = template.to_dict()
    resources = result["Resources"]

    # Logical ID matches class name
    assert "MyTable" in resources
    table = resources["MyTable"]

    # Correct type
    assert table["Type"] == "AWS::DynamoDB::Table"

    # Has all required properties
    props = table["Properties"]
    assert "AttributeDefinitions" in props
    assert "KeySchema" in props
    assert "ProvisionedThroughput" in props
    assert "PointInTimeRecoverySpecification" in props

    # Verify attribute definitions use Ref
    attr_def = props["AttributeDefinitions"][0]
    assert attr_def["AttributeName"] == {"Ref": "HashKeyName"}
    assert attr_def["AttributeType"] == {"Ref": "HashKeyType"}

    # Verify key schema
    key_schema = props["KeySchema"][0]
    assert key_schema["AttributeName"] == {"Ref": "HashKeyName"}
    assert key_schema["KeyType"] == "HASH"

    # Verify provisioned throughput uses Ref
    throughput = props["ProvisionedThroughput"]
    assert throughput["ReadCapacityUnits"] == {"Ref": "ReadCapacity"}
    assert throughput["WriteCapacityUnits"] == {"Ref": "WriteCapacity"}

    # Point-in-time recovery is enabled
    assert props["PointInTimeRecoverySpecification"]["PointInTimeRecoveryEnabled"] is True


def test_template_outputs():
    """Verify output references the table."""
    template = build_template()
    result = template.to_dict()
    outputs = result["Outputs"]

    assert "TableName" in outputs
    assert outputs["TableName"]["Value"] == {"Ref": "MyTable"}
    assert "Description" in outputs["TableName"]


def test_template_json_serialization():
    """Verify template can be serialized to JSON."""
    template = build_template()
    json_str = template.to_json()

    # Should be valid JSON
    parsed = json.loads(json_str)
    assert "Resources" in parsed
    assert "MyTable" in parsed["Resources"]


def test_template_validation():
    """Verify template passes basic validation."""
    template = build_template()
    errors = template.validate()
    assert errors == []
