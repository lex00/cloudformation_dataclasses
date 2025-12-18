"""Tests for VPC with NAT example."""

import json

from ..vpc_with_nat import (
    build_template,
    MainVPC,
    PublicSubnet0,
    PrivateSubnet0,
    IGW,
    NATGateway0,
    PublicRouteTable,
    PrivateRouteTable0,
    PublicNetworkAcl,
)


def test_template_structure():
    """Verify template has correct structure."""
    template = build_template()
    result = template.to_dict()

    assert result["AWSTemplateFormatVersion"] == "2010-09-09"
    assert "Description" in result
    assert "Parameters" in result
    assert "Mappings" in result
    assert "Resources" in result
    assert "Outputs" in result


def test_template_parameters():
    """Verify VPCName parameter exists with default."""
    template = build_template()
    result = template.to_dict()
    params = result["Parameters"]

    assert "VPCName" in params
    assert params["VPCName"]["Type"] == "String"
    assert params["VPCName"]["Default"] == "VPC Public and Private with NAT"


def test_subnet_config_mapping():
    """Verify SubnetConfig mapping has all CIDR blocks."""
    template = build_template()
    result = template.to_dict()
    mappings = result["Mappings"]

    assert "SubnetConfig" in mappings
    subnet_config = mappings["SubnetConfig"]

    assert subnet_config["VPC"]["CIDR"] == "10.0.0.0/16"
    assert subnet_config["Public0"]["CIDR"] == "10.0.0.0/24"
    assert subnet_config["Public1"]["CIDR"] == "10.0.1.0/24"
    assert subnet_config["Private0"]["CIDR"] == "10.0.2.0/24"
    assert subnet_config["Private1"]["CIDR"] == "10.0.3.0/24"


def test_vpc_resource():
    """Verify VPC has correct configuration."""
    template = build_template()
    result = template.to_dict()
    vpc = result["Resources"]["MainVPC"]["Properties"]

    assert vpc["EnableDnsSupport"] is True
    assert vpc["EnableDnsHostnames"] is True
    assert vpc["CidrBlock"] == {"Fn::FindInMap": ["SubnetConfig", "VPC", "CIDR"]}


def test_resource_count():
    """Verify correct number of resources."""
    template = build_template()
    result = template.to_dict()
    resources = result["Resources"]

    # 1 VPC + 1 IGW + 1 Attachment + 4 Subnets + 3 Route Tables + 3 Routes
    # + 4 Route Table Associations + 1 NACL + 2 NACL Entries + 2 NACL Associations
    # + 2 EIPs + 2 NAT Gateways = 26
    assert len(resources) == 26


def test_public_subnets():
    """Verify public subnets configuration."""
    template = build_template()
    result = template.to_dict()

    public0 = result["Resources"]["PublicSubnet0"]["Properties"]
    public1 = result["Resources"]["PublicSubnet1"]["Properties"]

    # Both reference VPC
    assert public0["VpcId"] == {"Ref": "MainVPC"}
    assert public1["VpcId"] == {"Ref": "MainVPC"}

    # Both have public IPs on launch
    assert public0["MapPublicIpOnLaunch"] is True
    assert public1["MapPublicIpOnLaunch"] is True

    # Different AZs
    assert public0["AvailabilityZone"] == {"Fn::Select": [0, {"Fn::GetAZs": ""}]}
    assert public1["AvailabilityZone"] == {"Fn::Select": [1, {"Fn::GetAZs": ""}]}

    # Different CIDRs
    assert public0["CidrBlock"] == {"Fn::FindInMap": ["SubnetConfig", "Public0", "CIDR"]}
    assert public1["CidrBlock"] == {"Fn::FindInMap": ["SubnetConfig", "Public1", "CIDR"]}


def test_private_subnets():
    """Verify private subnets configuration."""
    template = build_template()
    result = template.to_dict()

    private0 = result["Resources"]["PrivateSubnet0"]["Properties"]
    private1 = result["Resources"]["PrivateSubnet1"]["Properties"]

    # Both reference VPC
    assert private0["VpcId"] == {"Ref": "MainVPC"}
    assert private1["VpcId"] == {"Ref": "MainVPC"}

    # No MapPublicIpOnLaunch (private)
    assert "MapPublicIpOnLaunch" not in private0
    assert "MapPublicIpOnLaunch" not in private1

    # Different AZs
    assert private0["AvailabilityZone"] == {"Fn::Select": [0, {"Fn::GetAZs": ""}]}
    assert private1["AvailabilityZone"] == {"Fn::Select": [1, {"Fn::GetAZs": ""}]}


def test_internet_gateway():
    """Verify Internet Gateway and attachment."""
    template = build_template()
    result = template.to_dict()

    assert "IGW" in result["Resources"]
    assert result["Resources"]["IGW"]["Type"] == "AWS::EC2::InternetGateway"

    attachment = result["Resources"]["GatewayToInternet"]["Properties"]
    assert attachment["VpcId"] == {"Ref": "MainVPC"}
    assert attachment["InternetGatewayId"] == {"Ref": "IGW"}


def test_nat_gateways():
    """Verify NAT Gateways configuration."""
    template = build_template()
    result = template.to_dict()

    nat0 = result["Resources"]["NATGateway0"]["Properties"]
    nat1 = result["Resources"]["NATGateway1"]["Properties"]

    # Allocation IDs from EIPs
    assert nat0["AllocationId"] == {"Fn::GetAtt": ["ElasticIP0", "AllocationId"]}
    assert nat1["AllocationId"] == {"Fn::GetAtt": ["ElasticIP1", "AllocationId"]}

    # In public subnets
    assert nat0["SubnetId"] == {"Ref": "PublicSubnet0"}
    assert nat1["SubnetId"] == {"Ref": "PublicSubnet1"}


def test_public_route():
    """Verify public route to Internet Gateway."""
    template = build_template()
    result = template.to_dict()

    route = result["Resources"]["PublicRoute"]["Properties"]
    assert route["RouteTableId"] == {"Ref": "PublicRouteTable"}
    assert route["DestinationCidrBlock"] == "0.0.0.0/0"
    assert route["GatewayId"] == {"Ref": "IGW"}


def test_private_routes():
    """Verify private routes to NAT Gateways."""
    template = build_template()
    result = template.to_dict()

    route0 = result["Resources"]["PrivateRouteToInternet0"]["Properties"]
    route1 = result["Resources"]["PrivateRouteToInternet1"]["Properties"]

    assert route0["NatGatewayId"] == {"Ref": "NATGateway0"}
    assert route1["NatGatewayId"] == {"Ref": "NATGateway1"}
    assert route0["DestinationCidrBlock"] == "0.0.0.0/0"
    assert route1["DestinationCidrBlock"] == "0.0.0.0/0"


def test_network_acl():
    """Verify Network ACL allows all traffic."""
    template = build_template()
    result = template.to_dict()

    nacl = result["Resources"]["PublicNetworkAcl"]["Properties"]
    assert nacl["VpcId"] == {"Ref": "MainVPC"}

    # Inbound rule
    inbound = result["Resources"]["InboundPublicNetworkAclEntry"]["Properties"]
    assert inbound["RuleNumber"] == 100
    assert inbound["Protocol"] == -1
    assert inbound["RuleAction"] == "allow"
    assert inbound["Egress"] is False
    assert inbound["CidrBlock"] == "0.0.0.0/0"

    # Outbound rule
    outbound = result["Resources"]["OutboundPublicNetworkAclEntry"]["Properties"]
    assert outbound["Egress"] is True


def test_outputs():
    """Verify outputs with exports."""
    template = build_template()
    result = template.to_dict()
    outputs = result["Outputs"]

    expected_outputs = [
        "VPCIdOutput",
        "PublicSubnet0Output",
        "PublicSubnet1Output",
        "PrivateSubnet0Output",
        "PrivateSubnet1Output",
        "DefaultSecurityGroupOutput",
    ]

    for output_name in expected_outputs:
        assert output_name in outputs
        assert "Export" in outputs[output_name]


def test_vpc_output_export():
    """Verify VPC output export name format."""
    template = build_template()
    result = template.to_dict()

    vpc_output = result["Outputs"]["VPCIdOutput"]
    assert vpc_output["Value"] == {"Ref": "MainVPC"}
    assert vpc_output["Export"]["Name"] == {"Fn::Sub": "${AWS::Region}-${AWS::StackName}-VPC"}


def test_default_security_group_output():
    """Verify DefaultSecurityGroup output uses GetAtt."""
    template = build_template()
    result = template.to_dict()

    sg_output = result["Outputs"]["DefaultSecurityGroupOutput"]
    assert sg_output["Value"] == {"Fn::GetAtt": ["MainVPC", "DefaultSecurityGroup"]}


def test_template_json_serialization():
    """Verify template can be serialized to JSON."""
    template = build_template()
    json_str = template.to_json()

    parsed = json.loads(json_str)
    assert "Resources" in parsed
    assert "MainVPC" in parsed["Resources"]


def test_template_validation():
    """Verify template passes basic validation."""
    template = build_template()
    errors = template.validate()
    assert errors == []
