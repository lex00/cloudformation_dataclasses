"""Tests for instance_with_cfn_init example."""

import json

from ..instance_with_cfn_init import build_template


def test_template_structure():
    """Verify template has correct structure."""
    template = build_template()
    result = template.to_dict()

    assert result["AWSTemplateFormatVersion"] == "2010-09-09"
    assert "Description" in result
    assert "Resources" in result


def test_template_resources():
    """Verify instance resource is present."""
    template = build_template()
    result = template.to_dict()
    resources = result["Resources"]

    assert "WebInstance" in resources
    assert resources["WebInstance"]["Type"] == "AWS::EC2::Instance"


def test_instance_metadata():
    """Verify instance has AWS::CloudFormation::Init metadata."""
    template = build_template()
    result = template.to_dict()
    instance = result["Resources"]["WebInstance"]

    assert "Metadata" in instance
    metadata = instance["Metadata"]

    assert "AWS::CloudFormation::Init" in metadata
    cfn_init = metadata["AWS::CloudFormation::Init"]

    # Verify config section exists
    assert "config" in cfn_init
    config = cfn_init["config"]

    # Verify packages
    assert "packages" in config
    assert "yum" in config["packages"]
    assert "httpd" in config["packages"]["yum"]

    # Verify files
    assert "files" in config
    assert "/var/www/html/index.html" in config["files"]
    assert "/etc/cfn/cfn-hup.conf" in config["files"]
    assert "/etc/cfn/hooks.d/cfn-auto-reloader.conf" in config["files"]

    # Verify services
    assert "services" in config
    assert "sysvinit" in config["services"]
    assert "httpd" in config["services"]["sysvinit"]
    assert "cfn-hup" in config["services"]["sysvinit"]


def test_instance_user_data():
    """Verify instance has UserData with cfn-init and cfn-signal."""
    template = build_template()
    result = template.to_dict()
    instance = result["Resources"]["WebInstance"]["Properties"]

    assert "UserData" in instance
    user_data = instance["UserData"]

    # UserData should be Base64 encoded
    assert "Fn::Base64" in user_data

    # Should contain Sub with cfn-init commands
    base64_content = user_data["Fn::Base64"]
    assert "Fn::Sub" in base64_content

    sub_content = base64_content["Fn::Sub"]
    assert "cfn-init" in sub_content
    assert "cfn-signal" in sub_content
    assert "${AWS::StackName}" in sub_content
    assert "${AWS::Region}" in sub_content


def test_instance_properties():
    """Verify instance has correct properties."""
    template = build_template()
    result = template.to_dict()
    instance = result["Resources"]["WebInstance"]["Properties"]

    assert instance["InstanceType"] == "t4g.nano"
    assert instance["KeyName"] == "sample"
    # AMI uses SSM dynamic reference
    assert "resolve:ssm" in instance["ImageId"]


def test_cfn_hup_conf_uses_sub():
    """Verify cfn-hup.conf uses Sub for stack/region."""
    template = build_template()
    result = template.to_dict()
    metadata = result["Resources"]["WebInstance"]["Metadata"]
    cfn_hup_conf = metadata["AWS::CloudFormation::Init"]["config"]["files"]["/etc/cfn/cfn-hup.conf"]

    assert "content" in cfn_hup_conf
    content = cfn_hup_conf["content"]
    assert "Fn::Sub" in content
    assert "${AWS::StackId}" in content["Fn::Sub"]
    assert "${AWS::Region}" in content["Fn::Sub"]


def test_template_json_serialization():
    """Verify template can be serialized to JSON."""
    template = build_template()
    json_str = template.to_json()

    # Should be valid JSON
    parsed = json.loads(json_str)
    assert "Resources" in parsed
    assert "WebInstance" in parsed["Resources"]


def test_template_validation():
    """Verify template passes basic validation."""
    template = build_template()
    errors = template.validate()
    assert errors == []
