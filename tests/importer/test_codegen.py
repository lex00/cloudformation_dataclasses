"""Tests for the code generator."""

from pathlib import Path

import pytest

from cloudformation_dataclasses.importer.codegen import generate_code
from cloudformation_dataclasses.importer.parser import parse_template

TEMPLATES_DIR = Path(__file__).parent / "templates"


class TestGenerateSimpleBucket:
    """Tests for generating code from simple_bucket.yaml."""

    @pytest.fixture
    def code(self):
        template = parse_template(TEMPLATES_DIR / "simple_bucket.yaml")
        return generate_code(template)

    def test_has_docstring(self, code):
        assert '"""' in code
        assert "Simple S3 bucket" in code

    def test_has_imports(self, code):
        assert "from cloudformation_dataclasses" in code

    def test_has_resource_class(self, code):
        assert "@cloudformation_dataclass" in code
        assert "class MyBucket:" in code
        assert "resource: Bucket" in code
        assert "bucket_name = 'my-test-bucket'" in code

    def test_has_output_class(self, code):
        assert "class BucketNameOutput:" in code
        assert "resource: Output" in code
        assert "ref(MyBucket)" in code

    def test_has_template_class(self, code):
        assert "class SimpleBucketTemplate:" in code
        assert "resource: Template" in code

    def test_has_build_function(self, code):
        assert "def build_template()" in code

    def test_has_main_block(self, code):
        assert 'if __name__ == "__main__":' in code

    def test_generated_code_is_valid_python(self, code):
        # This will raise SyntaxError if invalid
        compile(code, "<test>", "exec")


class TestGenerateBucketWithRef:
    """Tests for generating code from bucket_with_ref.yaml."""

    @pytest.fixture
    def code(self):
        template = parse_template(TEMPLATES_DIR / "bucket_with_ref.yaml")
        return generate_code(template)

    def test_has_parameter_class(self, code):
        assert "class BucketNameParam:" in code
        assert "resource: Parameter" in code
        assert "type = STRING" in code  # Uses constant instead of string
        assert "default = 'my-default-bucket'" in code

    def test_has_ref_to_parameter(self, code):
        assert "ref(BucketNameParam)" in code

    def test_has_getatt(self, code):
        assert 'get_att(MyBucket, "Arn")' in code

    def test_generated_code_is_valid_python(self, code):
        compile(code, "<test>", "exec")


class TestGenerateIntrinsics:
    """Tests for generating code with intrinsic functions."""

    @pytest.fixture
    def code(self):
        template = parse_template(TEMPLATES_DIR / "intrinsics.yaml")
        return generate_code(template)

    def test_has_sub(self, code):
        assert "Sub(" in code
        assert "${AWS::StackName}" in code

    def test_has_join(self, code):
        assert "Join(" in code

    def test_uses_pseudo_parameter_constant(self, code):
        # !Ref AWS::StackName should become AWS_STACK_NAME constant
        assert "AWS_STACK_NAME" in code

    def test_has_if(self, code):
        assert "If(" in code
        assert "IsProd" in code

    def test_has_condition_class(self, code):
        assert "class IsProdCondition:" in code
        assert "Equals(" in code

    def test_generated_code_is_valid_python(self, code):
        compile(code, "<test>", "exec")


class TestGenerateNoMain:
    """Tests for generating code without main block."""

    def test_no_main_block(self):
        template = parse_template(TEMPLATES_DIR / "simple_bucket.yaml")
        code = generate_code(template, include_main=False)
        assert 'if __name__ == "__main__":' not in code


class TestGenerateFromJSON:
    """Tests for generating code from JSON templates."""

    @pytest.fixture
    def code(self):
        template = parse_template(TEMPLATES_DIR / "simple_bucket.json")
        return generate_code(template)

    def test_has_resource(self, code):
        assert "class MyBucket:" in code

    def test_generated_code_is_valid_python(self, code):
        compile(code, "<test>", "exec")


class TestBriefMode:
    """Tests for brief mode (imperative) code generation."""

    @pytest.fixture
    def code(self):
        template = parse_template(TEMPLATES_DIR / "simple_bucket.yaml")
        return generate_code(template, mode="brief")

    def test_no_cloudformation_dataclass_decorator(self, code):
        assert "@cloudformation_dataclass" not in code

    def test_has_variable_assignment(self, code):
        assert "my_bucket = Bucket(" in code

    def test_has_output_variable(self, code):
        assert "bucket_name_output = Output(" in code

    def test_has_template_variable(self, code):
        assert "template = Template(" in code

    def test_no_build_template_function(self, code):
        assert "def build_template()" not in code

    def test_generated_code_is_valid_python(self, code):
        compile(code, "<test>", "exec")


class TestBriefModeWithRef:
    """Tests for brief mode with references."""

    @pytest.fixture
    def code(self):
        template = parse_template(TEMPLATES_DIR / "bucket_with_ref.yaml")
        return generate_code(template, mode="brief")

    def test_has_parameter_variable(self, code):
        assert "bucket_name_param = Parameter(" in code

    def test_has_resource_variable(self, code):
        assert "my_bucket = Bucket(" in code

    def test_generated_code_is_valid_python(self, code):
        compile(code, "<test>", "exec")


class TestMixedMode:
    """Tests for mixed mode code generation."""

    @pytest.fixture
    def code(self):
        template = parse_template(TEMPLATES_DIR / "simple_bucket.yaml")
        return generate_code(template, mode="mixed")

    def test_has_wrapper_classes(self, code):
        # Mixed mode uses classes for resources
        assert "@cloudformation_dataclass" in code
        assert "class MyBucket:" in code

    def test_has_build_function(self, code):
        assert "def build_template()" in code

    def test_generated_code_is_valid_python(self, code):
        compile(code, "<test>", "exec")


class TestMixedModeWithTags:
    """Tests for mixed mode with tag reuse detection."""

    @pytest.fixture
    def code(self):
        template = parse_template(TEMPLATES_DIR / "bucket_with_tags.yaml")
        return generate_code(template, mode="mixed")

    def test_reused_tag_has_class(self, code):
        # Team:Platform is used twice, should have a class
        assert "class TeamPlatformTag:" in code

    def test_unique_tag_is_inlined(self, code):
        # Environment:Development is used once, should be inlined
        assert "Tag(key='Environment', value='Development')" in code

    def test_reused_tag_is_referenced(self, code):
        # Team:Platform should be referenced by class name, not inlined
        assert "TeamPlatformTag" in code
        # Should not have inlined Tag for Platform
        assert "Tag(key='Team', value='Platform')" not in code

    def test_all_resources_present(self, code):
        assert "class ProdBucket:" in code
        assert "class StagingBucket:" in code
        assert "class DevBucket:" in code

    def test_generated_code_is_valid_python(self, code):
        compile(code, "<test>", "exec")


class TestMixedModeVsBlockMode:
    """Tests comparing mixed mode to block mode."""

    def test_block_mode_does_not_inline_tags(self):
        template = parse_template(TEMPLATES_DIR / "bucket_with_tags.yaml")
        code = generate_code(template, mode="block")
        # Block mode should NOT have Tag() inlined
        assert "Tag(key=" not in code
        # But should have the tag as dict value in properties
        compile(code, "<test>", "exec")


class TestMixedModeWithPolicies:
    """Tests for mixed mode with IAM policies."""

    @pytest.fixture
    def code(self):
        template = parse_template(TEMPLATES_DIR / "bucket_with_policy.yaml")
        return generate_code(template, mode="mixed")

    def test_uses_policy_document_class(self, code):
        assert "PolicyDocument(statement=" in code

    def test_uses_policy_statement_class(self, code):
        assert "PolicyStatement(" in code

    def test_statement_has_sid(self, code):
        assert "sid='PublicRead'" in code
        assert "sid='DenyInsecure'" in code

    def test_statement_has_effect_for_deny(self, code):
        # Allow is default, so should not appear
        # Deny should be explicit
        assert "effect='Deny'" in code

    def test_statement_has_resource_arn(self, code):
        assert "resource_arn=" in code

    def test_statement_has_condition(self, code):
        assert "condition={" in code

    def test_condition_uses_constant(self, code):
        # Should use BOOL constant instead of "Bool" string
        assert "BOOL:" in code
        assert '"Bool"' not in code

    def test_imports_policy_classes(self, code):
        assert "PolicyDocument" in code
        assert "PolicyStatement" in code

    def test_imports_condition_operator(self, code):
        assert "BOOL" in code

    def test_generated_code_is_valid_python(self, code):
        compile(code, "<test>", "exec")


class TestBlockModeWithPolicies:
    """Tests for block mode with IAM policies (should use raw dicts)."""

    @pytest.fixture
    def code(self):
        template = parse_template(TEMPLATES_DIR / "bucket_with_policy.yaml")
        return generate_code(template, mode="block")

    def test_does_not_use_policy_document_class(self, code):
        # Block mode should keep policies as raw dicts
        assert "PolicyDocument(" not in code

    def test_does_not_use_policy_statement_class(self, code):
        assert "PolicyStatement(" not in code

    def test_generated_code_is_valid_python(self, code):
        compile(code, "<test>", "exec")
