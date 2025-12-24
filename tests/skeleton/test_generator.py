"""Tests for skeleton generator."""

import subprocess
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
        assert "default" in names

    def test_skeletons_have_descriptions(self) -> None:
        """Each skeleton has a description."""
        skeletons = list_skeletons()

        for skeleton in skeletons:
            assert skeleton.description
            assert skeleton.description != "No description"


class TestGenerateSkeleton:
    """Tests for generate_skeleton()."""

    def test_generates_default_skeleton(self, tmp_path: Path) -> None:
        """generate_skeleton() creates files for default skeleton."""
        output_dir = tmp_path / "my_project"

        created = generate_skeleton("default", output_dir)

        # Check core files were created
        file_names = {f.name for f in created}
        assert "__init__.py" in file_names
        assert "main.py" in file_names
        assert "README.md" in file_names
        # IDE support files from package_templates
        assert "pyproject.toml" in file_names
        assert "py.typed" in file_names
        assert "mypy.ini" in file_names
        assert "CLAUDE.md" in file_names

    def test_substitutes_project_name(self, tmp_path: Path) -> None:
        """Variable substitution replaces {{project_name}}."""
        output_dir = tmp_path / "analytics"

        generate_skeleton("default", output_dir, project_name="analytics")

        readme_content = (output_dir / "README.md").read_text()
        assert "analytics" in readme_content.lower()
        assert "{{project_name}}" not in readme_content

    def test_substitutes_pascal_case_name(self, tmp_path: Path) -> None:
        """Variable substitution converts to PascalCase for {{ProjectName}}."""
        output_dir = tmp_path / "my_analytics"

        generate_skeleton("default", output_dir, project_name="my_analytics")

        readme_content = (output_dir / "README.md").read_text()
        assert "MyAnalytics" in readme_content
        assert "{{ProjectName}}" not in readme_content

    def test_substitutes_all_variables(self, tmp_path: Path) -> None:
        """All template variables are substituted."""
        output_dir = tmp_path / "test_project"

        generate_skeleton(
            "default",
            output_dir,
            project_name="analytics",
            component="storage",
            stage="prod",
            region="us-west-2",
        )

        readme_content = (output_dir / "README.md").read_text()
        # Verify no unsubstituted placeholders remain
        assert "{{" not in readme_content

    def test_raises_for_unknown_skeleton(self, tmp_path: Path) -> None:
        """ValueError raised for unknown skeleton names."""
        with pytest.raises(ValueError, match="Unknown skeleton"):
            generate_skeleton("nonexistent", tmp_path / "output")

    def test_creates_output_directory(self, tmp_path: Path) -> None:
        """Output directory is created if it doesn't exist."""
        output_dir = tmp_path / "nested" / "deep" / "project"

        generate_skeleton("default", output_dir)

        assert output_dir.exists()

    def test_generated_code_is_valid_python(self, tmp_path: Path) -> None:
        """Generated Python files can be compiled."""
        output_dir = tmp_path / "test_project"

        generate_skeleton("default", output_dir)

        for py_file in output_dir.glob("*.py"):
            content = py_file.read_text()
            # Should not raise SyntaxError
            compile(content, py_file.name, "exec")


class TestGeneratedSkeletonImports:
    """Tests that generated skeletons can be imported and used."""

    def test_generated_skeleton_imports(self, tmp_path: Path) -> None:
        """Generated skeleton can be imported as a Python package."""
        output_dir = tmp_path / "test_project"
        generate_skeleton("default", output_dir, project_name="test_project")

        # Add to sys.path temporarily
        sys.path.insert(0, str(tmp_path))
        try:
            # Import the generated package
            import test_project.main as main_module

            # Check key exports exist
            assert hasattr(main_module, "build_template")
        finally:
            sys.path.remove(str(tmp_path))
            # Clean up imported modules
            for mod_name in list(sys.modules.keys()):
                if mod_name.startswith("test_project"):
                    del sys.modules[mod_name]

    def test_generated_skeleton_builds_template(self, tmp_path: Path) -> None:
        """Generated skeleton can build a CloudFormation template structure."""
        output_dir = tmp_path / "test_project"
        generate_skeleton("default", output_dir, project_name="test_project")

        sys.path.insert(0, str(tmp_path))
        try:
            from test_project.main import build_template

            # Build template (no resources in default skeleton)
            template = build_template()

            # Check structure (empty template won't validate, but structure is correct)
            cf_dict = template.to_dict()
            assert "AWSTemplateFormatVersion" in cf_dict
            assert "Description" in cf_dict
        finally:
            sys.path.remove(str(tmp_path))
            for mod_name in list(sys.modules.keys()):
                if mod_name.startswith("test_project"):
                    del sys.modules[mod_name]


class TestGeneratedIDESupport:
    """Tests for IDE support files generated by skeleton."""

    def test_generates_pyproject_toml(self, tmp_path: Path) -> None:
        """generate_skeleton() creates pyproject.toml with dependencies."""
        output_dir = tmp_path / "my_project"

        generate_skeleton("default", output_dir, project_name="my_project")

        pyproject = output_dir / "pyproject.toml"
        assert pyproject.exists()
        content = pyproject.read_text()
        assert 'name = "my_project"' in content
        assert "cloudformation_dataclasses" in content

    def test_generates_py_typed(self, tmp_path: Path) -> None:
        """generate_skeleton() creates py.typed marker file."""
        output_dir = tmp_path / "my_project"

        generate_skeleton("default", output_dir)

        py_typed = output_dir / "py.typed"
        assert py_typed.exists()

    def test_generates_mypy_ini(self, tmp_path: Path) -> None:
        """generate_skeleton() creates mypy.ini config."""
        output_dir = tmp_path / "my_project"

        generate_skeleton("default", output_dir)

        mypy_ini = output_dir / "mypy.ini"
        assert mypy_ini.exists()
        content = mypy_ini.read_text()
        assert "[mypy]" in content
        assert "python_version" in content

    def test_generates_vscode_settings(self, tmp_path: Path) -> None:
        """generate_skeleton() creates .vscode/settings.json."""
        output_dir = tmp_path / "my_project"

        generate_skeleton("default", output_dir)

        settings = output_dir / ".vscode" / "settings.json"
        assert settings.exists()
        content = settings.read_text()
        assert "python.analysis.typeCheckingMode" in content

    def test_generates_claude_md(self, tmp_path: Path) -> None:
        """generate_skeleton() creates CLAUDE.md with project name."""
        output_dir = tmp_path / "my_project"

        generate_skeleton("default", output_dir, project_name="analytics")

        claude_md = output_dir / "CLAUDE.md"
        assert claude_md.exists()
        content = claude_md.read_text()
        assert "# Analytics" in content
        assert "cloudformation_dataclasses" in content

    def test_generated_skeleton_passes_mypy(self, tmp_path: Path) -> None:
        """Generated skeleton passes mypy type checking."""
        output_dir = tmp_path / "test_project"
        generate_skeleton("default", output_dir, project_name="test_project")

        result = subprocess.run(
            ["mypy", str(output_dir), "--ignore-missing-imports"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"mypy errors:\n{result.stdout}\n{result.stderr}"
