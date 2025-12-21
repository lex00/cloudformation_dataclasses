"""Tests for individual lint rules."""

import pytest

from cloudformation_dataclasses.linter import (
    lint_code,
    fix_code,
    LintIssue,
    StringShouldBeConditionOperator,
    StringShouldBeParameterType,
    RefShouldBePseudoParameter,
    StringShouldBeEnum,
    DictShouldBePropertyType,
)


class TestStringShouldBeConditionOperator:
    """Tests for CFD001: condition operator string literals."""

    def test_detects_bool_in_dict(self):
        """Should detect 'Bool' as a dict key."""
        code = '''
condition = {"Bool": {"aws:SecureTransport": "false"}}
'''
        issues = lint_code(code, rules=[StringShouldBeConditionOperator()])
        assert len(issues) == 1
        assert issues[0].rule_id == "CFD001"
        assert "BOOL" in issues[0].suggestion
        assert '"Bool"' in issues[0].original

    def test_detects_string_equals(self):
        """Should detect 'StringEquals' as a dict key."""
        code = '''
condition = {"StringEquals": {"s3:x-amz-acl": "bucket-owner-full-control"}}
'''
        issues = lint_code(code, rules=[StringShouldBeConditionOperator()])
        assert len(issues) == 1
        assert "STRING_EQUALS" in issues[0].suggestion

    def test_detects_arn_like(self):
        """Should detect 'ArnLike' as a dict key."""
        code = '''
condition = {"ArnLike": {"aws:SourceArn": "arn:aws:s3:::my-bucket"}}
'''
        issues = lint_code(code, rules=[StringShouldBeConditionOperator()])
        assert len(issues) == 1
        assert "ARN_LIKE" in issues[0].suggestion

    def test_detects_multiple_operators(self):
        """Should detect multiple condition operators."""
        code = '''
condition = {
    "Bool": {"aws:SecureTransport": "false"},
    "StringEquals": {"s3:x-amz-acl": "bucket-owner-full-control"},
}
'''
        issues = lint_code(code, rules=[StringShouldBeConditionOperator()])
        assert len(issues) == 2

    def test_ignores_non_operator_strings(self):
        """Should not flag strings that aren't condition operators."""
        code = '''
data = {"Name": "value", "Description": "test"}
'''
        issues = lint_code(code, rules=[StringShouldBeConditionOperator()])
        assert len(issues) == 0

    def test_fix_replaces_bool(self):
        """Should replace 'Bool' with BOOL."""
        code = '''condition = {"Bool": {"aws:SecureTransport": "false"}}'''
        fixed = fix_code(code, rules=[StringShouldBeConditionOperator()], add_imports=False)
        assert "BOOL" in fixed
        assert '"Bool"' not in fixed


class TestStringShouldBeParameterType:
    """Tests for CFD002: parameter type string literals."""

    def test_detects_type_string(self):
        """Should detect type = 'String'."""
        code = '''
type = "String"
'''
        issues = lint_code(code, rules=[StringShouldBeParameterType()])
        assert len(issues) == 1
        assert issues[0].rule_id == "CFD002"
        assert "STRING" in issues[0].suggestion

    def test_detects_type_number(self):
        """Should detect type = 'Number'."""
        code = '''
type = "Number"
'''
        issues = lint_code(code, rules=[StringShouldBeParameterType()])
        assert len(issues) == 1
        assert "NUMBER" in issues[0].suggestion

    def test_detects_aws_ec2_types(self):
        """Should detect AWS EC2 parameter types."""
        code = '''
type = "AWS::EC2::VPC::Id"
'''
        issues = lint_code(code, rules=[StringShouldBeParameterType()])
        assert len(issues) == 1
        assert "ParameterType.AWS_EC2_VPC_ID" in issues[0].suggestion

    def test_detects_type_in_kwargs(self):
        """Should detect type in keyword arguments."""
        code = '''
param = Parameter(type="String", description="Test")
'''
        issues = lint_code(code, rules=[StringShouldBeParameterType()])
        assert len(issues) == 1
        assert "STRING" in issues[0].suggestion

    def test_ignores_non_parameter_types(self):
        """Should not flag arbitrary string assignments to type."""
        code = '''
type = "CustomType"
'''
        issues = lint_code(code, rules=[StringShouldBeParameterType()])
        assert len(issues) == 0

    def test_fix_replaces_string(self):
        """Should replace 'String' with STRING."""
        code = '''type = "String"'''
        fixed = fix_code(code, rules=[StringShouldBeParameterType()], add_imports=False)
        assert "STRING" in fixed
        assert '"String"' not in fixed


class TestRefShouldBePseudoParameter:
    """Tests for CFD003: Ref() with pseudo-parameters."""

    def test_detects_aws_region(self):
        """Should detect Ref('AWS::Region')."""
        code = '''
region = Ref("AWS::Region")
'''
        issues = lint_code(code, rules=[RefShouldBePseudoParameter()])
        assert len(issues) == 1
        assert issues[0].rule_id == "CFD003"
        assert "AWS_REGION" in issues[0].suggestion

    def test_detects_aws_stack_name(self):
        """Should detect Ref('AWS::StackName')."""
        code = '''
stack_name = Ref("AWS::StackName")
'''
        issues = lint_code(code, rules=[RefShouldBePseudoParameter()])
        assert len(issues) == 1
        assert "AWS_STACK_NAME" in issues[0].suggestion

    def test_detects_aws_account_id(self):
        """Should detect Ref('AWS::AccountId')."""
        code = '''
account_id = Ref("AWS::AccountId")
'''
        issues = lint_code(code, rules=[RefShouldBePseudoParameter()])
        assert len(issues) == 1
        assert "AWS_ACCOUNT_ID" in issues[0].suggestion

    def test_detects_all_pseudo_parameters(self):
        """Should detect all AWS pseudo-parameters."""
        code = '''
region = Ref("AWS::Region")
stack = Ref("AWS::StackName")
account = Ref("AWS::AccountId")
partition = Ref("AWS::Partition")
'''
        issues = lint_code(code, rules=[RefShouldBePseudoParameter()])
        assert len(issues) == 4

    def test_ignores_regular_refs(self):
        """Should not flag Ref() with regular resource/parameter references."""
        code = '''
bucket_ref = Ref("MyBucket")
param_ref = Ref("Environment")
'''
        issues = lint_code(code, rules=[RefShouldBePseudoParameter()])
        assert len(issues) == 0

    def test_fix_replaces_ref(self):
        """Should replace Ref('AWS::Region') with AWS_REGION."""
        code = '''region = Ref("AWS::Region")'''
        fixed = fix_code(code, rules=[RefShouldBePseudoParameter()], add_imports=False)
        assert "AWS_REGION" in fixed
        assert 'Ref("AWS::Region")' not in fixed


class TestStringShouldBeEnum:
    """Tests for CFD004: string literals that should be enums."""

    def test_detects_sse_algorithm_aes256(self):
        """Should detect sse_algorithm = 'AES256'."""
        code = '''
sse_algorithm = "AES256"
'''
        issues = lint_code(code, rules=[StringShouldBeEnum()])
        assert len(issues) == 1
        assert issues[0].rule_id == "CFD004"
        assert "ServerSideEncryption.AES256" in issues[0].suggestion

    def test_detects_sse_algorithm_aws_kms(self):
        """Should detect sse_algorithm = 'aws:kms'."""
        code = '''
sse_algorithm = "aws:kms"
'''
        issues = lint_code(code, rules=[StringShouldBeEnum()])
        assert len(issues) == 1
        assert "ServerSideEncryption.AWS_KMS" in issues[0].suggestion

    def test_detects_dynamodb_key_type(self):
        """Should detect DynamoDB key_type = 'HASH'."""
        code = '''
key_type = "HASH"
'''
        issues = lint_code(code, rules=[StringShouldBeEnum()])
        assert len(issues) == 1
        assert "KeyType.HASH" in issues[0].suggestion

    def test_detects_dynamodb_attribute_type(self):
        """Should detect DynamoDB attribute_type = 'S'."""
        code = '''
attribute_type = "S"
'''
        issues = lint_code(code, rules=[StringShouldBeEnum()])
        assert len(issues) == 1
        assert "AttributeType.S" in issues[0].suggestion

    def test_detects_enum_in_kwargs(self):
        """Should detect enum values in keyword arguments."""
        code = '''
encryption = ServerSideEncryptionByDefault(sse_algorithm="AES256")
'''
        issues = lint_code(code, rules=[StringShouldBeEnum()])
        assert len(issues) == 1
        assert "ServerSideEncryption.AES256" in issues[0].suggestion

    def test_ignores_unknown_field_names(self):
        """Should not flag unknown field names."""
        code = '''
unknown_field = "AES256"
'''
        issues = lint_code(code, rules=[StringShouldBeEnum()])
        assert len(issues) == 0

    def test_ignores_unknown_values(self):
        """Should not flag unknown values for known fields."""
        code = '''
sse_algorithm = "UNKNOWN_VALUE"
'''
        issues = lint_code(code, rules=[StringShouldBeEnum()])
        assert len(issues) == 0

    def test_fix_replaces_enum_value(self):
        """Should replace string with enum constant."""
        code = '''sse_algorithm = "AES256"'''
        fixed = fix_code(code, rules=[StringShouldBeEnum()], add_imports=False)
        assert "ServerSideEncryption.AES256" in fixed
        assert '"AES256"' not in fixed


class TestDictShouldBePropertyType:
    """Tests for CFD005: dict literals that should be PropertyType."""

    def test_detects_server_side_encryption_config(self):
        """Should detect ServerSideEncryptionConfiguration dict key."""
        code = '''
config = {"ServerSideEncryptionConfiguration": []}
'''
        issues = lint_code(code, rules=[DictShouldBePropertyType()])
        assert len(issues) == 1
        assert issues[0].rule_id == "CFD005"
        assert "BucketEncryption" in issues[0].suggestion

    def test_detects_versioning_configuration(self):
        """Should detect VersioningConfiguration dict key."""
        code = '''
versioning = {"VersioningConfiguration": {"Status": "Enabled"}}
'''
        issues = lint_code(code, rules=[DictShouldBePropertyType()])
        assert len(issues) == 1
        assert "VersioningConfiguration" in issues[0].suggestion

    def test_detects_dynamodb_key_schema(self):
        """Should detect KeySchema dict key."""
        code = '''
schema = {"KeySchema": [{"AttributeName": "id", "KeyType": "HASH"}]}
'''
        issues = lint_code(code, rules=[DictShouldBePropertyType()])
        assert len(issues) == 1
        assert "KeySchema" in issues[0].suggestion

    def test_ignores_unknown_dict_keys(self):
        """Should not flag dicts with unknown keys."""
        code = '''
data = {"Name": "value", "Value": 123}
'''
        issues = lint_code(code, rules=[DictShouldBePropertyType()])
        assert len(issues) == 0


class TestLintCodeIntegration:
    """Integration tests for lint_code with multiple rules."""

    def test_detects_multiple_issue_types(self):
        """Should detect issues from multiple rules."""
        code = '''
from cloudformation_dataclasses.intrinsics import Ref

type = "String"
region = Ref("AWS::Region")
sse_algorithm = "AES256"
condition = {"Bool": {"key": "value"}}
'''
        issues = lint_code(code)
        # Should find: STRING, AWS_REGION, ServerSideEncryption.AES256, BOOL
        assert len(issues) >= 4

        rule_ids = {issue.rule_id for issue in issues}
        assert "CFD001" in rule_ids  # Condition operator
        assert "CFD002" in rule_ids  # Parameter type
        assert "CFD003" in rule_ids  # Pseudo parameter
        assert "CFD004" in rule_ids  # Enum

    def test_fix_code_fixes_all_issues(self):
        """Should fix all detected issues."""
        code = '''type = "String"
sse_algorithm = "AES256"
condition = {"Bool": {"key": "value"}}
'''
        fixed = fix_code(code, add_imports=False)
        assert "STRING" in fixed
        assert "ServerSideEncryption.AES256" in fixed
        assert "BOOL" in fixed
        assert '"String"' not in fixed
        assert '"AES256"' not in fixed
        assert '"Bool"' not in fixed

    def test_fix_code_adds_imports(self):
        """Should add required imports."""
        code = '''sse_algorithm = "AES256"'''
        fixed = fix_code(code, add_imports=True)
        assert "from cloudformation_dataclasses.aws.s3 import ServerSideEncryption" in fixed
        assert "ServerSideEncryption.AES256" in fixed


class TestFixCodeImports:
    """Tests for import handling in fix_code."""

    def test_groups_imports_by_module(self):
        """Should group multiple imports from the same module."""
        code = '''
sse_algorithm = "AES256"
status = "Enabled"
'''
        fixed = fix_code(code, add_imports=True, rules=[StringShouldBeEnum()])
        # Should have combined import
        assert "cloudformation_dataclasses.aws.s3" in fixed

    def test_preserves_existing_imports(self):
        """Should not duplicate existing imports."""
        code = '''from cloudformation_dataclasses.aws.s3 import ServerSideEncryption

sse_algorithm = "AES256"
'''
        fixed = fix_code(code, add_imports=True, rules=[StringShouldBeEnum()])
        # Should not have duplicate import
        import_count = fixed.count("from cloudformation_dataclasses.aws.s3 import")
        assert import_count == 1

    def test_handles_syntax_errors_gracefully(self):
        """Should return original code for syntax errors."""
        code = '''this is not valid python'''
        issues = lint_code(code)
        assert len(issues) == 0

        fixed = fix_code(code)
        # Should return unchanged since we can't fix invalid code
        assert "this is not valid python" in fixed
