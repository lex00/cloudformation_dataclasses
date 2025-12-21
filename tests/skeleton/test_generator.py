"""Tests for skeleton generator."""

import sys
from pathlib import Path

import pytest

from cloudformation_dataclasses.skeleton import generate_skeleton, list_skeletons


class TestListSkeletons:
    """Tests for list_skeletons()."""

    def test_returns_available_skeletons(self) -> None:
        """list_skeletons() returns available skeleton templates."""
        skeletons = list_skeletons()

        assert len(skeletons) >= 1
        names = [s.name for s in skeletons]
        assert "s3_bucket" in names

    def test_skeletons_have_descriptions(self) -> None:
        """Each skeleton has a description."""
        skeletons = list_skeletons()

        for skeleton in skeletons:
            assert skeleton.description
            assert skeleton.description != "No description"


class TestGenerateSkeleton:
    """Tests for generate_skeleton()."""

    def test_generates_s3_bucket_skeleton(self, tmp_path: Path) -> None:
        """generate_skeleton() creates files for s3_bucket skeleton."""
        output_dir = tmp_path / "my_project"

        created = generate_skeleton("s3_bucket", output_dir)

        # Check files were created
        assert len(created) >= 5
        file_names = {f.name for f in created}
        assert "__init__.py" in file_names
        assert "context.py" in file_names
        assert "bucket.py" in file_names
        assert "bucket_policy.py" in file_names
        assert "main.py" in file_names
        assert "README.md" in file_names

    def test_accepts_hyphenated_name(self, tmp_path: Path) -> None:
        """Skeleton names can use hyphens instead of underscores."""
        output_dir = tmp_path / "my_project"

        created = generate_skeleton("s3-bucket", output_dir)

        assert len(created) >= 5

    def test_substitutes_project_name(self, tmp_path: Path) -> None:
        """Variable substitution replaces {{project_name}}."""
        output_dir = tmp_path / "analytics"

        generate_skeleton("s3_bucket", output_dir, project_name="analytics")

        context_content = (output_dir / "context.py").read_text()
        assert 'project_name = "analytics"' in context_content
        assert "{{project_name}}" not in context_content

    def test_substitutes_pascal_case_name(self, tmp_path: Path) -> None:
        """Variable substitution converts to PascalCase for {{ProjectName}}."""
        output_dir = tmp_path / "my_analytics"

        generate_skeleton("s3_bucket", output_dir, project_name="my_analytics")

        context_content = (output_dir / "context.py").read_text()
        assert "class MyAnalyticsContext:" in context_content
        assert "{{ProjectName}}" not in context_content

    def test_substitutes_all_variables(self, tmp_path: Path) -> None:
        """All template variables are substituted."""
        output_dir = tmp_path / "test_project"

        generate_skeleton(
            "s3_bucket",
            output_dir,
            project_name="analytics",
            component="storage",
            stage="prod",
            region="us-west-2",
        )

        context_content = (output_dir / "context.py").read_text()
        assert 'project_name = "analytics"' in context_content
        assert 'component = "storage"' in context_content
        assert 'stage = "prod"' in context_content
        assert 'region = "us-west-2"' in context_content

    def test_raises_for_unknown_skeleton(self, tmp_path: Path) -> None:
        """ValueError raised for unknown skeleton names."""
        with pytest.raises(ValueError, match="Unknown skeleton"):
            generate_skeleton("nonexistent", tmp_path / "output")

    def test_creates_output_directory(self, tmp_path: Path) -> None:
        """Output directory is created if it doesn't exist."""
        output_dir = tmp_path / "nested" / "deep" / "project"

        generate_skeleton("s3_bucket", output_dir)

        assert output_dir.exists()

    def test_generated_code_is_valid_python(self, tmp_path: Path) -> None:
        """Generated Python files can be compiled."""
        output_dir = tmp_path / "test_project"

        generate_skeleton("s3_bucket", output_dir)

        for py_file in output_dir.glob("*.py"):
            content = py_file.read_text()
            # Should not raise SyntaxError
            compile(content, py_file.name, "exec")


class TestGeneratedSkeletonImports:
    """Tests that generated skeletons can be imported and used."""

    def test_generated_skeleton_imports(self, tmp_path: Path) -> None:
        """Generated skeleton can be imported as a Python package."""
        output_dir = tmp_path / "test_project"
        generate_skeleton("s3_bucket", output_dir, project_name="test_project")

        # Add to sys.path temporarily
        sys.path.insert(0, str(tmp_path))
        try:
            # Import the generated package
            import test_project.main as main_module
            import test_project.bucket as bucket_module
            import test_project.context as context_module

            # Check key exports exist
            assert hasattr(main_module, "build_template")
            assert hasattr(bucket_module, "DataBucket")
            assert hasattr(context_module, "ctx")
        finally:
            sys.path.remove(str(tmp_path))
            # Clean up imported modules
            for mod_name in list(sys.modules.keys()):
                if mod_name.startswith("test_project"):
                    del sys.modules[mod_name]

    def test_generated_skeleton_builds_template(self, tmp_path: Path) -> None:
        """Generated skeleton can build a valid CloudFormation template."""
        output_dir = tmp_path / "test_project"
        generate_skeleton("s3_bucket", output_dir, project_name="test_project")

        sys.path.insert(0, str(tmp_path))
        try:
            from test_project.main import build_template
            from test_project.bucket import DataBucket
            from test_project.bucket_policy import DataBucketPolicy

            # Instantiate resources
            bucket = DataBucket()
            policy = DataBucketPolicy()

            # Build template
            template = build_template()

            # Validate
            assert template.validate() == []

            # Check structure
            cf_dict = template.to_dict()
            assert "AWSTemplateFormatVersion" in cf_dict
            assert "Resources" in cf_dict
            assert "DataBucket" in cf_dict["Resources"]
            assert "DataBucketPolicy" in cf_dict["Resources"]
        finally:
            sys.path.remove(str(tmp_path))
            for mod_name in list(sys.modules.keys()):
                if mod_name.startswith("test_project"):
                    del sys.modules[mod_name]

    def test_generated_skeleton_uses_context_naming(self, tmp_path: Path) -> None:
        """Resources get names from the deployment context."""
        output_dir = tmp_path / "test_project"
        generate_skeleton(
            "s3_bucket",
            output_dir,
            project_name="analytics",
            component="storage",
            stage="prod",
            region="us-west-2",
        )

        sys.path.insert(0, str(tmp_path))
        try:
            from test_project.bucket import DataBucket

            bucket = DataBucket()
            # Includes deployment_name="001" and deployment_group="blue" from skeleton defaults
            expected_name = "analytics-storage-DataBucket-prod-001-blue-us-west-2"
            assert bucket.resource.resource_name == expected_name
        finally:
            sys.path.remove(str(tmp_path))
            for mod_name in list(sys.modules.keys()):
                if mod_name.startswith("test_project"):
                    del sys.modules[mod_name]
