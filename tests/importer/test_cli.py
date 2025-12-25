"""Tests for CLI helper functions."""

from pathlib import Path

import pytest

from cloudformation_dataclasses.importer.cli import (
    _get_git_remote_url,
    detect_attribution,
    main,
)


class TestGetGitRemoteUrl:
    """Tests for _get_git_remote_url helper."""

    def test_https_url(self, tmp_path):
        """Should extract HTTPS URL from git config."""
        git_dir = tmp_path / ".git"
        git_dir.mkdir()
        (git_dir / "config").write_text("""
[core]
    repositoryformatversion = 0
[remote "origin"]
    url = https://github.com/user/repo.git
    fetch = +refs/heads/*:refs/remotes/origin/*
""")
        url = _get_git_remote_url(git_dir)
        assert url == "https://github.com/user/repo"

    def test_ssh_url_github(self, tmp_path):
        """Should convert git@github.com URLs to HTTPS."""
        git_dir = tmp_path / ".git"
        git_dir.mkdir()
        (git_dir / "config").write_text("""
[remote "origin"]
    url = git@github.com:user/repo.git
""")
        url = _get_git_remote_url(git_dir)
        assert url == "https://github.com/user/repo"

    def test_ssh_url_gitlab(self, tmp_path):
        """Should convert git@gitlab.com URLs to HTTPS."""
        git_dir = tmp_path / ".git"
        git_dir.mkdir()
        (git_dir / "config").write_text("""
[remote "origin"]
    url = git@gitlab.com:group/project.git
""")
        url = _get_git_remote_url(git_dir)
        assert url == "https://gitlab.com/group/project"

    def test_no_origin(self, tmp_path):
        """Should return None if no origin remote."""
        git_dir = tmp_path / ".git"
        git_dir.mkdir()
        (git_dir / "config").write_text("""
[remote "upstream"]
    url = https://github.com/other/repo.git
""")
        url = _get_git_remote_url(git_dir)
        assert url is None

    def test_no_config_file(self, tmp_path):
        """Should return None if no config file."""
        git_dir = tmp_path / ".git"
        git_dir.mkdir()
        url = _get_git_remote_url(git_dir)
        assert url is None


class TestDetectAttribution:
    """Tests for detect_attribution function."""

    def test_git_remote_takes_priority(self, tmp_path):
        """Git remote URL should take priority over README links."""
        # Create .git/config with origin
        git_dir = tmp_path / ".git"
        git_dir.mkdir()
        (git_dir / "config").write_text("""
[remote "origin"]
    url = https://github.com/correct/repo.git
""")
        # Create README with different URL
        (tmp_path / "README.md").write_text("""
# My Project
Check out https://github.com/wrong/link for more info.
""")
        attr = detect_attribution(tmp_path)
        assert attr.source_url == "https://github.com/correct/repo"
        assert attr.project_name == "My Project"

    def test_readme_url_fallback(self, tmp_path):
        """Should use README URL if no git remote."""
        (tmp_path / "README.md").write_text("""
# My Project
Visit https://github.com/user/project for docs.
""")
        attr = detect_attribution(tmp_path)
        assert attr.source_url == "https://github.com/user/project"
        assert attr.project_name == "My Project"

    def test_license_txt(self, tmp_path):
        """Should detect LICENSE.txt files."""
        (tmp_path / "LICENSE.txt").write_text("""
Apache License
Version 2.0, January 2004
""")
        attr = detect_attribution(tmp_path)
        assert attr.license_type == "Apache-2.0"

    def test_license_md(self, tmp_path):
        """Should detect LICENSE.md files."""
        (tmp_path / "LICENSE.md").write_text("""
MIT License

Permission is hereby granted, free of charge...
""")
        attr = detect_attribution(tmp_path)
        assert attr.license_type == "MIT"

    def test_walks_up_directory_tree(self, tmp_path):
        """Should find attribution in parent directories."""
        # Create attribution in parent
        (tmp_path / "README.md").write_text("# Parent Project")
        (tmp_path / "LICENSE").write_text("MIT License\nPermission is hereby granted")

        # Create subdirectory
        subdir = tmp_path / "subdir" / "nested"
        subdir.mkdir(parents=True)

        attr = detect_attribution(subdir)
        assert attr.project_name == "Parent Project"
        assert attr.license_type == "MIT"

    def test_no_attribution(self, tmp_path):
        """Should return empty Attribution if nothing found."""
        attr = detect_attribution(tmp_path)
        assert attr.source_url is None
        assert attr.project_name is None
        assert attr.license_type is None


class TestInitSubcommand:
    """Tests for init subcommand (skeleton generation)."""

    def test_init_creates_package(self, tmp_path: Path) -> None:
        """init creates a complete package structure."""
        output_dir = tmp_path / "my_project"

        exit_code = main(["init", "-o", str(output_dir)])

        assert exit_code == 0
        assert (output_dir / "my_project" / "__init__.py").exists()
        assert (output_dir / "my_project" / "main.py").exists()
        assert (output_dir / "my_project" / "__main__.py").exists()
        assert (output_dir / "my_project" / "stack" / "__init__.py").exists()
        assert (output_dir / "README.md").exists()
        assert (output_dir / "pyproject.toml").exists()

    def test_init_with_project_name(self, tmp_path: Path) -> None:
        """--project-name overrides package name."""
        output_dir = tmp_path / "output"

        exit_code = main(["init", "-o", str(output_dir), "--project-name", "analytics"])

        assert exit_code == 0
        # Package directory uses project name
        assert (output_dir / "analytics" / "__init__.py").exists()
        assert (output_dir / "analytics" / "main.py").exists()
        # README uses project name
        readme = (output_dir / "README.md").read_text()
        assert "Analytics" in readme

    def test_init_adds_aws_imports(self, tmp_path: Path) -> None:
        """init adds real AWS imports (not commented hints)."""
        output_dir = tmp_path / "my_project"

        main(["init", "-o", str(output_dir)])

        init_content = (output_dir / "my_project" / "__init__.py").read_text()
        # Should have real imports, not commented hints
        assert "from cloudformation_dataclasses.aws import" in init_content
        assert "# from cloudformation_dataclasses.aws import" not in init_content
        # Should include common AWS modules
        assert "ec2" in init_content
        assert "iam" in init_content
        assert "lambda_" in init_content
        assert "s3" in init_content
        # AWS modules should be in __all__
        assert '"ec2"' in init_content
        assert '"s3"' in init_content

    def test_init_requires_output(self) -> None:
        """init requires -o flag."""
        with pytest.raises(SystemExit):
            main(["init"])

    def test_init_no_original_folder(self, tmp_path: Path) -> None:
        """init doesn't create original/ folder."""
        output_dir = tmp_path / "my_project"

        main(["init", "-o", str(output_dir)])

        assert not (output_dir / "original").exists()

    def test_init_readme_content(self, tmp_path: Path) -> None:
        """init generates appropriate README."""
        output_dir = tmp_path / "my_project"

        main(["init", "-o", str(output_dir)])

        readme = (output_dir / "README.md").read_text()
        assert "CloudFormation infrastructure as Python code" in readme
        assert "Imported from" not in readme

    def test_generated_skeleton_imports(self, tmp_path: Path) -> None:
        """Generated skeleton can be imported."""
        import sys

        output_dir = tmp_path / "test_project"
        main(["init", "-o", str(output_dir), "--project-name", "test_project"])

        sys.path.insert(0, str(output_dir))
        try:
            from test_project.main import build_template

            template = build_template()
            cf_dict = template.to_dict()
            assert "AWSTemplateFormatVersion" in cf_dict
        finally:
            sys.path.remove(str(output_dir))
            for mod_name in list(sys.modules.keys()):
                if mod_name.startswith("test_project"):
                    del sys.modules[mod_name]


class TestLintSubcommand:
    """Tests for lint subcommand."""

    def test_lint_no_issues(self, tmp_path: Path) -> None:
        """lint returns 0 when no issues found."""
        # Create a clean file
        test_file = tmp_path / "clean.py"
        test_file.write_text('"""Clean code."""\nx = 1\n')

        exit_code = main(["lint", str(test_file)])

        assert exit_code == 0

    def test_lint_file_not_found(self, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
        """lint returns error for missing file."""
        exit_code = main(["lint", str(tmp_path / "nonexistent.py")])

        assert exit_code == 1
        captured = capsys.readouterr()
        assert "Path not found" in captured.err

    def test_lint_directory(self, tmp_path: Path) -> None:
        """lint scans all Python files in directory."""
        # Create multiple files
        (tmp_path / "a.py").write_text('"""A."""\n')
        (tmp_path / "b.py").write_text('"""B."""\n')
        (tmp_path / "sub").mkdir()
        (tmp_path / "sub" / "c.py").write_text('"""C."""\n')

        exit_code = main(["lint", str(tmp_path)])

        assert exit_code == 0

    def test_lint_package_structure(self, tmp_path: Path) -> None:
        """lint detects package structure and lints stack/."""
        # Create package structure
        output_dir = tmp_path / "my_project"
        main(["init", "-o", str(output_dir)])

        exit_code = main(["lint", str(output_dir)])

        assert exit_code == 0

    def test_lint_with_fix(self, tmp_path: Path) -> None:
        """lint --fix modifies files in place."""
        # Create a file with a fixable issue (string that should be enum)
        test_file = tmp_path / "fixable.py"
        test_file.write_text('"""Test."""\nsse_algorithm = "AES256"\n')

        exit_code = main(["lint", str(test_file), "--fix"])

        assert exit_code == 0
