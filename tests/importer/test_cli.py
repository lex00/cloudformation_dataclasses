"""Tests for CLI helper functions."""

from pathlib import Path

import pytest

from cloudformation_dataclasses.importer.cli import (
    _get_git_remote_url,
    detect_attribution,
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
