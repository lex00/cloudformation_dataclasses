"""Tests for eip_with_association example."""

import json

from ..eip_with_association import (
    build_template,
    EC2Instance,
    IPAddress,
    IPAssoc,
)


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

    # All parameters present
    assert "KeyName" in params
    assert "InstanceTypeParam" in params
    assert "SSHLocation" in params
    assert "LatestAmiId" in params
    assert "Subnets" in params


def test_template_resources():
    """Verify all resources are present."""
    template = build_template()
    result = template.to_dict()
    resources = result["Resources"]

    # All resources present
    assert "InstanceSecurityGroup" in resources
    assert "IPAddress" in resources
    assert "EC2Instance" in resources
    assert "IPAssoc" in resources

    # Verify types
    assert resources["InstanceSecurityGroup"]["Type"] == "AWS::EC2::SecurityGroup"
    assert resources["IPAddress"]["Type"] == "AWS::EC2::EIP"
    assert resources["EC2Instance"]["Type"] == "AWS::EC2::Instance"
    assert resources["IPAssoc"]["Type"] == "AWS::EC2::EIPAssociation"


def test_eip_association():
    """Verify EIP association links instance and EIP."""
    template = build_template()
    result = template.to_dict()
    assoc = result["Resources"]["IPAssoc"]["Properties"]

    # References the instance
    assert assoc["InstanceId"] == {"Ref": "EC2Instance"}

    # Uses GetAtt for AllocationId
    assert assoc["AllocationId"] == {"Fn::GetAtt": ["IPAddress", "AllocationId"]}


def test_instance_user_data():
    """Verify instance has UserData with EIP reference."""
    template = build_template()
    result = template.to_dict()
    instance = result["Resources"]["EC2Instance"]["Properties"]

    assert "UserData" in instance
    user_data = instance["UserData"]

    # UserData should be Base64 encoded
    assert "Fn::Base64" in user_data

    # Should contain Join with IPAddress reference
    base64_content = user_data["Fn::Base64"]
    assert "Fn::Join" in base64_content

    join_content = base64_content["Fn::Join"]
    assert join_content[0] == ""  # Empty delimiter
    assert {"Ref": "IPAddress"} in join_content[1]


def test_template_outputs():
    """Verify outputs reference instance and IP."""
    template = build_template()
    result = template.to_dict()
    outputs = result["Outputs"]

    # Both outputs present
    assert "InstanceIdOutput" in outputs
    assert "InstanceIPAddressOutput" in outputs

    # Verify values
    assert outputs["InstanceIdOutput"]["Value"] == {"Ref": "EC2Instance"}
    assert outputs["InstanceIPAddressOutput"]["Value"] == {"Ref": "IPAddress"}


def test_template_json_serialization():
    """Verify template can be serialized to JSON."""
    template = build_template()
    json_str = template.to_json()

    # Should be valid JSON
    parsed = json.loads(json_str)
    assert "Resources" in parsed
    assert "IPAddress" in parsed["Resources"]
    assert "IPAssoc" in parsed["Resources"]


def test_template_validation():
    """Verify template passes basic validation."""
    template = build_template()
    errors = template.validate()
    assert errors == []
