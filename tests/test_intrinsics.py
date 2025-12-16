"""
Tests for CloudFormation intrinsic functions.

Tests all intrinsic function classes to ensure they serialize correctly
to CloudFormation JSON format.
"""

import pytest

from cloudformation_dataclasses.intrinsics.functions import (
    And,
    Base64,
    Cidr,
    Equals,
    FindInMap,
    GetAtt,
    GetAZs,
    If,
    ImportValue,
    Join,
    Not,
    Or,
    Ref,
    Select,
    Split,
    Sub,
)


class TestRef:
    """Tests for Ref intrinsic function."""

    def test_ref_basic(self):
        """Test basic Ref serialization."""
        ref = Ref(logical_id="MyVPC")
        assert ref.to_dict() == {"Ref": "MyVPC"}

    def test_ref_with_parameter(self):
        """Test Ref to a parameter."""
        ref = Ref(logical_id="InstanceType")
        assert ref.to_dict() == {"Ref": "InstanceType"}


class TestGetAtt:
    """Tests for GetAtt intrinsic function."""

    def test_get_att_basic(self):
        """Test basic GetAtt serialization."""
        get_att = GetAtt(logical_id="MyInstance", attribute_name="PublicIp")
        assert get_att.to_dict() == {"Fn::GetAtt": ["MyInstance", "PublicIp"]}

    def test_get_att_bucket_arn(self):
        """Test GetAtt for S3 bucket ARN."""
        get_att = GetAtt(logical_id="MyBucket", attribute_name="Arn")
        assert get_att.to_dict() == {"Fn::GetAtt": ["MyBucket", "Arn"]}


class TestSub:
    """Tests for Sub intrinsic function."""

    def test_sub_simple(self):
        """Test Sub with simple template string."""
        sub = Sub(template_string="arn:aws:s3:::${BucketName}")
        assert sub.to_dict() == {"Fn::Sub": "arn:aws:s3:::${BucketName}"}

    def test_sub_with_variables(self):
        """Test Sub with explicit variables."""
        sub = Sub(
            template_string="My ${Key1} is ${Key2}",
            variables={"Key1": "value1", "Key2": "value2"}
        )
        assert sub.to_dict() == {
            "Fn::Sub": [
                "My ${Key1} is ${Key2}",
                {"Key1": "value1", "Key2": "value2"}
            ]
        }

    def test_sub_with_ref_variable(self):
        """Test Sub with Ref in variables."""
        sub = Sub(
            template_string="Instance type is ${InstanceType}",
            variables={"InstanceType": Ref("InstanceTypeParameter")}
        )
        result = sub.to_dict()
        assert result == {
            "Fn::Sub": [
                "Instance type is ${InstanceType}",
                {"InstanceType": {"Ref": "InstanceTypeParameter"}}
            ]
        }

    def test_sub_complex_arn(self):
        """Test Sub for complex ARN construction."""
        sub = Sub(
            template_string="arn:aws:s3:::${Bucket}/*",
            variables={"Bucket": Ref("MyBucket")}
        )
        result = sub.to_dict()
        assert result["Fn::Sub"][0] == "arn:aws:s3:::${Bucket}/*"
        assert result["Fn::Sub"][1]["Bucket"] == {"Ref": "MyBucket"}


class TestJoin:
    """Tests for Join intrinsic function."""

    def test_join_simple(self):
        """Test Join with simple strings."""
        join = Join(delimiter="-", values=["a", "b", "c"])
        assert join.to_dict() == {"Fn::Join": ["-", ["a", "b", "c"]]}

    def test_join_empty_delimiter(self):
        """Test Join with empty delimiter."""
        join = Join(delimiter="", values=["hello", "world"])
        assert join.to_dict() == {"Fn::Join": ["", ["hello", "world"]]}

    def test_join_with_ref(self):
        """Test Join with Ref values."""
        join = Join(delimiter=":", values=["arn", "aws", "s3", "", "", Ref("BucketName")])
        result = join.to_dict()
        assert result["Fn::Join"][0] == ":"
        assert result["Fn::Join"][1] == ["arn", "aws", "s3", "", "", {"Ref": "BucketName"}]

    def test_join_mixed_values(self):
        """Test Join with mixed string and intrinsic values."""
        join = Join(
            delimiter="-",
            values=["prefix", Ref("Environment"), "suffix"]
        )
        result = join.to_dict()
        assert result["Fn::Join"][1] == ["prefix", {"Ref": "Environment"}, "suffix"]


class TestSelect:
    """Tests for Select intrinsic function."""

    def test_select_basic(self):
        """Test Select with simple list."""
        select = Select(index=2, objects=["a", "b", "c", "d"])
        assert select.to_dict() == {"Fn::Select": [2, ["a", "b", "c", "d"]]}

    def test_select_first_element(self):
        """Test Select getting first element."""
        select = Select(index=0, objects=["first", "second", "third"])
        assert select.to_dict() == {"Fn::Select": [0, ["first", "second", "third"]]}

    def test_select_with_intrinsic(self):
        """Test Select with intrinsic function in list."""
        select = Select(index=1, objects=["a", Ref("MyParam"), "c"])
        result = select.to_dict()
        assert result["Fn::Select"][0] == 1
        assert result["Fn::Select"][1] == ["a", {"Ref": "MyParam"}, "c"]


class TestSplit:
    """Tests for Split intrinsic function."""

    def test_split_basic(self):
        """Test Split with simple string."""
        split = Split(delimiter=",", source="a,b,c")
        assert split.to_dict() == {"Fn::Split": [",", "a,b,c"]}

    def test_split_with_ref(self):
        """Test Split with Ref source."""
        split = Split(delimiter="|", source=Ref("MyParameter"))
        result = split.to_dict()
        assert result["Fn::Split"][0] == "|"
        assert result["Fn::Split"][1] == {"Ref": "MyParameter"}

    def test_split_hyphen_delimiter(self):
        """Test Split with hyphen delimiter."""
        split = Split(delimiter="-", source="one-two-three")
        assert split.to_dict() == {"Fn::Split": ["-", "one-two-three"]}


class TestIf:
    """Tests for If intrinsic function."""

    def test_if_basic(self):
        """Test If with simple values."""
        if_func = If(
            condition_name="IsProduction",
            value_if_true="m5.large",
            value_if_false="t3.micro"
        )
        assert if_func.to_dict() == {
            "Fn::If": ["IsProduction", "m5.large", "t3.micro"]
        }

    def test_if_with_intrinsics(self):
        """Test If with intrinsic function values."""
        if_func = If(
            condition_name="UseCustomVPC",
            value_if_true=Ref("CustomVPCId"),
            value_if_false=Ref("DefaultVPCId")
        )
        result = if_func.to_dict()
        assert result["Fn::If"][0] == "UseCustomVPC"
        assert result["Fn::If"][1] == {"Ref": "CustomVPCId"}
        assert result["Fn::If"][2] == {"Ref": "DefaultVPCId"}

    def test_if_nested(self):
        """Test If with nested If."""
        inner_if = If(
            condition_name="IsStaging",
            value_if_true="staging-value",
            value_if_false="dev-value"
        )
        outer_if = If(
            condition_name="IsProduction",
            value_if_true="prod-value",
            value_if_false=inner_if
        )
        result = outer_if.to_dict()
        assert result["Fn::If"][0] == "IsProduction"
        assert result["Fn::If"][1] == "prod-value"
        assert result["Fn::If"][2] == {
            "Fn::If": ["IsStaging", "staging-value", "dev-value"]
        }


class TestEquals:
    """Tests for Equals intrinsic function."""

    def test_equals_basic(self):
        """Test Equals with simple values."""
        equals = Equals(value1="production", value2="production")
        assert equals.to_dict() == {"Fn::Equals": ["production", "production"]}

    def test_equals_with_ref(self):
        """Test Equals with Ref."""
        equals = Equals(value1=Ref("Environment"), value2="production")
        result = equals.to_dict()
        assert result["Fn::Equals"][0] == {"Ref": "Environment"}
        assert result["Fn::Equals"][1] == "production"

    def test_equals_both_refs(self):
        """Test Equals with two Refs."""
        equals = Equals(value1=Ref("Param1"), value2=Ref("Param2"))
        result = equals.to_dict()
        assert result["Fn::Equals"][0] == {"Ref": "Param1"}
        assert result["Fn::Equals"][1] == {"Ref": "Param2"}


class TestAnd:
    """Tests for And intrinsic function."""

    def test_and_basic(self):
        """Test And with multiple conditions."""
        and_func = And(conditions=[
            Equals(Ref("Env"), "prod"),
            Equals(Ref("Region"), "us-east-1")
        ])
        result = and_func.to_dict()
        assert len(result["Fn::And"]) == 2
        assert result["Fn::And"][0] == {
            "Fn::Equals": [{"Ref": "Env"}, "prod"]
        }
        assert result["Fn::And"][1] == {
            "Fn::Equals": [{"Ref": "Region"}, "us-east-1"]
        }

    def test_and_three_conditions(self):
        """Test And with three conditions."""
        and_func = And(conditions=[
            Equals("a", "a"),
            Equals("b", "b"),
            Equals("c", "c")
        ])
        result = and_func.to_dict()
        assert len(result["Fn::And"]) == 3


class TestOr:
    """Tests for Or intrinsic function."""

    def test_or_basic(self):
        """Test Or with multiple conditions."""
        or_func = Or(conditions=[
            Equals(Ref("Env"), "dev"),
            Equals(Ref("Env"), "test")
        ])
        result = or_func.to_dict()
        assert len(result["Fn::Or"]) == 2
        assert result["Fn::Or"][0] == {
            "Fn::Equals": [{"Ref": "Env"}, "dev"]
        }

    def test_or_three_conditions(self):
        """Test Or with three conditions."""
        or_func = Or(conditions=[
            Equals("a", "x"),
            Equals("b", "y"),
            Equals("c", "z")
        ])
        result = or_func.to_dict()
        assert len(result["Fn::Or"]) == 3


class TestNot:
    """Tests for Not intrinsic function."""

    def test_not_basic(self):
        """Test Not with simple condition."""
        not_func = Not(condition=Equals(Ref("Env"), "production"))
        result = not_func.to_dict()
        assert result == {
            "Fn::Not": [{
                "Fn::Equals": [{"Ref": "Env"}, "production"]
            }]
        }

    def test_not_with_and(self):
        """Test Not with And condition."""
        not_func = Not(condition=And(conditions=[
            Equals("a", "a"),
            Equals("b", "b")
        ]))
        result = not_func.to_dict()
        assert "Fn::Not" in result
        assert "Fn::And" in result["Fn::Not"][0]


class TestBase64:
    """Tests for Base64 intrinsic function."""

    def test_base64_string(self):
        """Test Base64 with string value."""
        b64 = Base64(value_to_encode="Hello World")
        assert b64.to_dict() == {"Fn::Base64": "Hello World"}

    def test_base64_with_ref(self):
        """Test Base64 with Ref."""
        b64 = Base64(value_to_encode=Ref("UserData"))
        result = b64.to_dict()
        assert result == {"Fn::Base64": {"Ref": "UserData"}}

    def test_base64_with_join(self):
        """Test Base64 with Join."""
        b64 = Base64(value_to_encode=Join(delimiter="\n", values=["#!/bin/bash", "echo hello"]))
        result = b64.to_dict()
        assert "Fn::Base64" in result
        assert "Fn::Join" in result["Fn::Base64"]


class TestGetAZs:
    """Tests for GetAZs intrinsic function."""

    def test_get_azs_current_region(self):
        """Test GetAZs for current region."""
        azs = GetAZs()
        assert azs.to_dict() == {"Fn::GetAZs": ""}

    def test_get_azs_specific_region(self):
        """Test GetAZs for specific region."""
        azs = GetAZs(region="us-east-1")
        assert azs.to_dict() == {"Fn::GetAZs": "us-east-1"}

    def test_get_azs_other_region(self):
        """Test GetAZs for different region."""
        azs = GetAZs(region="eu-west-1")
        assert azs.to_dict() == {"Fn::GetAZs": "eu-west-1"}


class TestImportValue:
    """Tests for ImportValue intrinsic function."""

    def test_import_value_string(self):
        """Test ImportValue with string."""
        import_val = ImportValue(shared_value_to_import="NetworkStackVPCId")
        assert import_val.to_dict() == {"Fn::ImportValue": "NetworkStackVPCId"}

    def test_import_value_with_sub(self):
        """Test ImportValue with Sub."""
        import_val = ImportValue(
            shared_value_to_import=Sub(
                template_string="${StackName}-VPCId",
                variables={"StackName": Ref("NetworkStack")}
            )
        )
        result = import_val.to_dict()
        assert "Fn::ImportValue" in result
        assert "Fn::Sub" in result["Fn::ImportValue"]


class TestFindInMap:
    """Tests for FindInMap intrinsic function."""

    def test_find_in_map_basic(self):
        """Test FindInMap with simple keys."""
        find = FindInMap(
            map_name="RegionMap",
            top_level_key="us-east-1",
            second_level_key="AMI"
        )
        assert find.to_dict() == {
            "Fn::FindInMap": ["RegionMap", "us-east-1", "AMI"]
        }

    def test_find_in_map_with_ref(self):
        """Test FindInMap with Ref key."""
        find = FindInMap(
            map_name="RegionMap",
            top_level_key=Ref("AWS::Region"),
            second_level_key="AMI"
        )
        result = find.to_dict()
        assert result["Fn::FindInMap"][0] == "RegionMap"
        assert result["Fn::FindInMap"][1] == {"Ref": "AWS::Region"}
        assert result["Fn::FindInMap"][2] == "AMI"

    def test_find_in_map_both_refs(self):
        """Test FindInMap with both keys as Refs."""
        find = FindInMap(
            map_name="EnvironmentMap",
            top_level_key=Ref("Environment"),
            second_level_key=Ref("InstanceSize")
        )
        result = find.to_dict()
        assert result["Fn::FindInMap"][1] == {"Ref": "Environment"}
        assert result["Fn::FindInMap"][2] == {"Ref": "InstanceSize"}


class TestCidr:
    """Tests for Cidr intrinsic function."""

    def test_cidr_basic(self):
        """Test Cidr with simple values."""
        cidr = Cidr(ip_block="10.0.0.0/16", count=6, cidr_bits=8)
        assert cidr.to_dict() == {"Fn::Cidr": ["10.0.0.0/16", 6, 8]}

    def test_cidr_with_ref(self):
        """Test Cidr with Ref for IP block."""
        cidr = Cidr(ip_block=Ref("VPCCidr"), count=3, cidr_bits=4)
        result = cidr.to_dict()
        assert result["Fn::Cidr"][0] == {"Ref": "VPCCidr"}
        assert result["Fn::Cidr"][1] == 3
        assert result["Fn::Cidr"][2] == 4

    def test_cidr_large_subnet_count(self):
        """Test Cidr with larger subnet count."""
        cidr = Cidr(ip_block="192.168.0.0/16", count=256, cidr_bits=8)
        result = cidr.to_dict()
        assert result["Fn::Cidr"][1] == 256


class TestComplexIntrinsicCombinations:
    """Tests for complex combinations of intrinsic functions."""

    def test_join_with_multiple_intrinsics(self):
        """Test Join containing multiple intrinsic functions."""
        join = Join(
            delimiter="",
            values=[
                "arn:aws:s3:::",
                Ref("BucketName"),
                "/",
                GetAtt("MyObject", "Key")
            ]
        )
        result = join.to_dict()
        assert len(result["Fn::Join"][1]) == 4
        assert result["Fn::Join"][1][1] == {"Ref": "BucketName"}
        assert result["Fn::Join"][1][3] == {"Fn::GetAtt": ["MyObject", "Key"]}

    def test_sub_with_nested_intrinsics(self):
        """Test Sub with complex nested intrinsics in variables."""
        sub = Sub(
            template_string="Instance ${ID} in ${AZ}",
            variables={
                "ID": GetAtt("MyInstance", "InstanceId"),
                "AZ": Select(index=0, objects=["us-east-1a", "us-east-1b", "us-east-1c"])
            }
        )
        result = sub.to_dict()
        assert "Fn::Sub" in result
        variables = result["Fn::Sub"][1]
        assert "Fn::GetAtt" in variables["ID"]
        assert "Fn::Select" in variables["AZ"]

    def test_if_with_equals_condition(self):
        """Test combining If with Equals for conditional logic."""
        # This pattern is commonly used in templates
        condition = Equals(Ref("Environment"), "production")
        if_result = If(
            condition_name="IsProduction",
            value_if_true=Sub("prod-${AWS::StackName}"),
            value_if_false=Sub("dev-${AWS::StackName}")
        )

        # Verify the condition serializes correctly
        assert condition.to_dict() == {
            "Fn::Equals": [{"Ref": "Environment"}, "production"]
        }

        # Verify the If serializes correctly
        result = if_result.to_dict()
        assert "Fn::If" in result
        assert "Fn::Sub" in result["Fn::If"][1]
        assert "Fn::Sub" in result["Fn::If"][2]

    def test_deeply_nested_intrinsics(self):
        """Test deeply nested intrinsic functions."""
        # Sub containing Join containing Refs and GetAtts
        nested = Sub(
            template_string="URL: ${URL}",
            variables={
                "URL": Join(
                    delimiter="",
                    values=[
                        "https://",
                        GetAtt("LoadBalancer", "DNSName"),
                        "/api/",
                        Ref("APIVersion")
                    ]
                )
            }
        )
        result = nested.to_dict()
        assert "Fn::Sub" in result
        url_var = result["Fn::Sub"][1]["URL"]
        assert "Fn::Join" in url_var
        join_values = url_var["Fn::Join"][1]
        assert join_values[1] == {"Fn::GetAtt": ["LoadBalancer", "DNSName"]}
        assert join_values[3] == {"Ref": "APIVersion"}
