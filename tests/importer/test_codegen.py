"""Tests for the code generator."""

from pathlib import Path

import pytest

from cloudformation_dataclasses.importer.codegen import generate_code, generate_package
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
        assert 'ref("MyBucket")' in code

    def test_uses_template_from_registry(self, code):
        # Template class is no longer generated - resources auto-register
        # and we use Template.from_registry() to build the template
        assert "Template.from_registry(" in code
        assert "class SimpleBucketTemplate:" not in code

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
        # Output values use string refs (inline mode), not class refs
        assert 'get_att("MyBucket", "Arn")' in code

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


class TestBlockModeWithTags:
    """Tests for code generation with tags."""

    @pytest.fixture
    def code(self):
        template = parse_template(TEMPLATES_DIR / "bucket_with_tags.yaml")
        return generate_code(template)

    def test_has_wrapper_classes(self, code):
        # Block mode uses wrapper classes for PropertyTypes
        assert "@cloudformation_dataclass" in code
        assert "class ProdBucket:" in code

    def test_does_not_inline_tags(self, code):
        # Block mode should NOT have Tag() inlined
        assert "Tag(key=" not in code
        # But should have the tag referenced via wrapper classes
        compile(code, "<test>", "exec")

    def test_all_resources_present(self, code):
        assert "class ProdBucket:" in code
        assert "class StagingBucket:" in code
        assert "class DevBucket:" in code

    def test_generated_code_is_valid_python(self, code):
        compile(code, "<test>", "exec")


class TestBlockModeWithPolicies:
    """Tests for code generation with IAM policies."""

    @pytest.fixture
    def code(self):
        template = parse_template(TEMPLATES_DIR / "bucket_with_policy.yaml")
        return generate_code(template)

    def test_does_not_use_inline_policy_document(self, code):
        # Block mode should use wrapper classes, not PolicyDocument()
        assert "PolicyDocument(" not in code

    def test_does_not_use_inline_policy_statement(self, code):
        assert "PolicyStatement(" not in code

    def test_has_wrapper_classes_for_policy(self, code):
        # Should have wrapper classes for policy structures
        assert "@cloudformation_dataclass" in code

    def test_generated_code_is_valid_python(self, code):
        compile(code, "<test>", "exec")


class TestGeneratePackage:
    """Tests for generate_package with nested structure."""

    @pytest.fixture
    def files(self):
        template = parse_template(TEMPLATES_DIR / "simple_bucket.yaml")
        return generate_package(template, package_name="my_stack")

    def test_files_have_package_prefix(self, files):
        """All files should be prefixed with package_name/."""
        for filename in files:
            assert filename.startswith("my_stack/"), f"{filename} missing prefix"

    def test_has_init_py(self, files):
        assert "my_stack/__init__.py" in files

    def test_has_main_py(self, files):
        assert "my_stack/main.py" in files

    def test_has_dunder_main(self, files):
        """Should have __main__.py for python -m support."""
        assert "my_stack/__main__.py" in files
        content = files["my_stack/__main__.py"]
        assert "from .main import main" in content
        assert "main()" in content

    def test_has_config_py(self, files):
        assert "my_stack/config.py" in files

    def test_has_resources_package(self, files):
        assert "my_stack/resources/__init__.py" in files

    def test_main_has_build_template(self, files):
        content = files["my_stack/main.py"]
        assert "def build_template()" in content
        assert "Template.from_registry(" in content

    def test_all_files_are_valid_python(self, files):
        for filename, content in files.items():
            if filename.endswith(".py"):
                compile(content, filename, "exec")
