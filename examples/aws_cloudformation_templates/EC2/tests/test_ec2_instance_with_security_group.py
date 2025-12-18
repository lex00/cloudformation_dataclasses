"""Tests for ec2_instance_with_security_group example."""

import json

from ..ec2_instance_with_security_group import (
    build_template,
    EC2Instance,
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
    assert "InstanceTypeParam" in params
    assert "SSHLocation" in params
    assert "LatestAmiId" in params
    assert "Subnets" in params

    # Verify types
    assert params["KeyName"]["Type"] == "AWS::EC2::KeyPair::KeyName"
    assert params["InstanceTypeParam"]["Type"] == "String"
    assert params["SSHLocation"]["Type"] == "String"
    assert params["LatestAmiId"]["Type"] == "AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>"
    assert params["Subnets"]["Type"] == "List<AWS::EC2::Subnet::Id>"

    # Verify instance type allowed values
    assert "t3.small" in params["InstanceTypeParam"]["AllowedValues"]
    assert params["InstanceTypeParam"]["Default"] == "t3.small"


def test_template_resources():
    """Verify security group and instance resources."""
    template = build_template()
    result = template.to_dict()
    resources = result["Resources"]

    # Both resources present
    assert "InstanceSecurityGroup" in resources
    assert "EC2Instance" in resources

    # Verify types
    assert resources["InstanceSecurityGroup"]["Type"] == "AWS::EC2::SecurityGroup"
    assert resources["EC2Instance"]["Type"] == "AWS::EC2::Instance"


def test_security_group_ingress():
    """Verify security group has SSH ingress rule."""
    template = build_template()
    result = template.to_dict()
    sg = result["Resources"]["InstanceSecurityGroup"]["Properties"]

    assert "SecurityGroupIngress" in sg
    ingress_rules = sg["SecurityGroupIngress"]
    assert len(ingress_rules) == 1

    ssh_rule = ingress_rules[0]
    assert ssh_rule["IpProtocol"] == "tcp"
    assert ssh_rule["FromPort"] == 22
    assert ssh_rule["ToPort"] == 22
    assert ssh_rule["CidrIp"] == {"Ref": "SSHLocation"}


def test_instance_references_security_group():
    """Verify instance references security group via GetAtt."""
    template = build_template()
    result = template.to_dict()
    instance = result["Resources"]["EC2Instance"]["Properties"]

    assert "SecurityGroupIds" in instance
    sg_ids = instance["SecurityGroupIds"]
    assert len(sg_ids) == 1
    assert sg_ids[0] == {"Fn::GetAtt": ["InstanceSecurityGroup", "GroupId"]}


def test_instance_uses_select_for_subnet():
    """Verify instance uses Select to pick first subnet."""
    template = build_template()
    result = template.to_dict()
    instance = result["Resources"]["EC2Instance"]["Properties"]

    assert "SubnetId" in instance
    subnet_id = instance["SubnetId"]
    assert subnet_id == {"Fn::Select": [0, {"Ref": "Subnets"}]}


def test_instance_references_parameters():
    """Verify instance references parameter values."""
    template = build_template()
    result = template.to_dict()
    instance = result["Resources"]["EC2Instance"]["Properties"]

    assert instance["InstanceType"] == {"Ref": "InstanceTypeParam"}
    assert instance["KeyName"] == {"Ref": "KeyName"}
    assert instance["ImageId"] == {"Ref": "LatestAmiId"}


def test_template_outputs():
    """Verify outputs reference the instance."""
    template = build_template()
    result = template.to_dict()
    outputs = result["Outputs"]

    # All outputs present
    assert "InstanceIdOutput" in outputs
    assert "AZOutput" in outputs
    assert "PublicDNSOutput" in outputs
    assert "PublicIPOutput" in outputs

    # Verify values
    assert outputs["InstanceIdOutput"]["Value"] == {"Ref": "EC2Instance"}
    assert outputs["AZOutput"]["Value"] == {"Fn::GetAtt": ["EC2Instance", "AvailabilityZone"]}
    assert outputs["PublicDNSOutput"]["Value"] == {"Fn::GetAtt": ["EC2Instance", "PublicDnsName"]}
    assert outputs["PublicIPOutput"]["Value"] == {"Fn::GetAtt": ["EC2Instance", "PublicIp"]}


def test_template_json_serialization():
    """Verify template can be serialized to JSON."""
    template = build_template()
    json_str = template.to_json()

    # Should be valid JSON
    parsed = json.loads(json_str)
    assert "Resources" in parsed
    assert "EC2Instance" in parsed["Resources"]


def test_template_validation():
    """Verify template passes basic validation."""
    template = build_template()
    errors = template.validate()
    assert errors == []
