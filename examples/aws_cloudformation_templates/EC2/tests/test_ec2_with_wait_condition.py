"""Tests for ec2_with_wait_condition example."""

import json

from ..ec2_with_wait_condition import (
    build_template,
    WebInstance,
    InstanceWaitHandle,
    InstanceWaitCondition,
    InstanceSecurityGroup,
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
    assert "InstanceName" in params
    assert "InstanceTypeParam" in params
    assert "ImageId" in params
    assert "VpcId" in params
    assert "SubnetId" in params
    assert "SSHLocation" in params

    # Verify types
    assert params["KeyName"]["Type"] == "AWS::EC2::KeyPair::KeyName"
    assert params["ImageId"]["Type"] == "AWS::EC2::Image::Id"
    assert params["VpcId"]["Type"] == "String"
    assert params["SubnetId"]["Type"] == "String"


def test_template_resources():
    """Verify all resources are present."""
    template = build_template()
    result = template.to_dict()
    resources = result["Resources"]

    # All resources present
    assert "InstanceSecurityGroup" in resources
    assert "InstanceWaitHandle" in resources
    assert "InstanceWaitCondition" in resources
    assert "WebInstance" in resources

    # Verify types
    assert resources["InstanceSecurityGroup"]["Type"] == "AWS::EC2::SecurityGroup"
    assert resources["InstanceWaitHandle"]["Type"] == "AWS::CloudFormation::WaitConditionHandle"
    assert resources["InstanceWaitCondition"]["Type"] == "AWS::CloudFormation::WaitCondition"
    assert resources["WebInstance"]["Type"] == "AWS::EC2::Instance"


def test_wait_condition_handle():
    """Verify WaitConditionHandle resource exists."""
    template = build_template()
    result = template.to_dict()
    handle = result["Resources"]["InstanceWaitHandle"]

    # WaitConditionHandle has no properties
    assert handle["Type"] == "AWS::CloudFormation::WaitConditionHandle"


def test_wait_condition():
    """Verify WaitCondition references handle and has timeout."""
    template = build_template()
    result = template.to_dict()
    condition = result["Resources"]["InstanceWaitCondition"]["Properties"]

    # References the handle
    assert condition["Handle"] == {"Ref": "InstanceWaitHandle"}

    # Has timeout
    assert condition["Timeout"] == "300"


def test_security_group_ingress_rules():
    """Verify security group has all required ingress rules."""
    template = build_template()
    result = template.to_dict()
    sg = result["Resources"]["InstanceSecurityGroup"]["Properties"]

    assert "SecurityGroupIngress" in sg
    ingress_rules = sg["SecurityGroupIngress"]
    assert len(ingress_rules) == 4

    # Extract rules by port
    rules_by_port = {}
    for rule in ingress_rules:
        if rule["IpProtocol"] == "icmp":
            rules_by_port["icmp"] = rule
        else:
            rules_by_port[rule["FromPort"]] = rule

    # HTTP rule
    assert 80 in rules_by_port
    assert rules_by_port[80]["CidrIp"] == "0.0.0.0/0"

    # HTTPS rule
    assert 443 in rules_by_port
    assert rules_by_port[443]["CidrIp"] == "0.0.0.0/0"

    # SSH rule with parameter reference
    assert 22 in rules_by_port
    assert rules_by_port[22]["CidrIp"] == {"Ref": "SSHLocation"}

    # ICMP rule
    assert "icmp" in rules_by_port
    assert rules_by_port["icmp"]["FromPort"] == -1


def test_instance_user_data_signals():
    """Verify instance UserData signals via WaitConditionHandle."""
    template = build_template()
    result = template.to_dict()
    instance = result["Resources"]["WebInstance"]["Properties"]

    assert "UserData" in instance
    user_data = instance["UserData"]

    # UserData should be Base64 encoded
    assert "Fn::Base64" in user_data

    # Should contain Join
    base64_content = user_data["Fn::Base64"]
    assert "Fn::Join" in base64_content

    join_content = base64_content["Fn::Join"]
    join_values = join_content[1]

    # Should reference WaitHandle multiple times (for error_exit and success)
    wait_handle_refs = [v for v in join_values if v == {"Ref": "InstanceWaitHandle"}]
    assert len(wait_handle_refs) >= 2  # At least error and success signals

    # Should reference AWS::StackId and AWS::Region pseudo-parameters
    stack_id_refs = [v for v in join_values if v == {"Ref": "AWS::StackId"}]
    region_refs = [v for v in join_values if v == {"Ref": "AWS::Region"}]
    assert len(stack_id_refs) >= 1
    assert len(region_refs) >= 1


def test_instance_tags():
    """Verify instance has Name tag from parameter."""
    template = build_template()
    result = template.to_dict()
    instance = result["Resources"]["WebInstance"]["Properties"]

    assert "Tags" in instance
    tags = instance["Tags"]
    assert len(tags) >= 1

    # Find Name tag
    name_tag = next((t for t in tags if t["Key"] == "Name"), None)
    assert name_tag is not None
    assert name_tag["Value"] == {"Ref": "InstanceName"}


def test_template_outputs():
    """Verify outputs reference instance."""
    template = build_template()
    result = template.to_dict()
    outputs = result["Outputs"]

    # Both outputs present
    assert "WebsiteURLOutput" in outputs
    assert "InstanceIdOutput" in outputs

    # Website URL uses Join with GetAtt
    url_value = outputs["WebsiteURLOutput"]["Value"]
    assert "Fn::Join" in url_value

    # Instance ID is Ref
    assert outputs["InstanceIdOutput"]["Value"] == {"Ref": "WebInstance"}


def test_template_json_serialization():
    """Verify template can be serialized to JSON."""
    template = build_template()
    json_str = template.to_json()

    # Should be valid JSON
    parsed = json.loads(json_str)
    assert "Resources" in parsed
    assert "InstanceWaitHandle" in parsed["Resources"]
    assert "InstanceWaitCondition" in parsed["Resources"]


def test_template_validation():
    """Verify template passes basic validation."""
    template = build_template()
    errors = template.validate()
    assert errors == []
