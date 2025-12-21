"""Tests for skeleton CLI."""

from pathlib import Path

import pytest

from cloudformation_dataclasses.skeleton.cli import main


class TestCLI:
    """Tests for cfn-init CLI."""

    def test_list_skeletons(self, capsys: pytest.CaptureFixture[str]) -> None:
        """--list shows available skeletons."""
        exit_code = main(["--list"])

        assert exit_code == 0
        captured = capsys.readouterr()
        assert "s3_bucket" in captured.out
        assert "Available skeletons" in captured.out

    def test_requires_skeleton_name(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Error when skeleton name not provided."""
        with pytest.raises(SystemExit):
            main(["-o", "output/"])

    def test_requires_output(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Error when -o not provided."""
        with pytest.raises(SystemExit):
            main(["s3-bucket"])

    def test_generates_skeleton(self, tmp_path: Path) -> None:
        """CLI generates skeleton files."""
        output_dir = tmp_path / "my_project"

        exit_code = main(["s3-bucket", "-o", str(output_dir)])

        assert exit_code == 0
        assert (output_dir / "__init__.py").exists()
        assert (output_dir / "context.py").exists()
        assert (output_dir / "bucket.py").exists()
        assert (output_dir / "main.py").exists()

    def test_custom_variables(self, tmp_path: Path) -> None:
        """CLI passes custom variables to generator."""
        output_dir = tmp_path / "analytics"

        exit_code = main([
            "s3-bucket",
            "-o", str(output_dir),
            "--project-name", "analytics",
            "--component", "storage",
            "--stage", "prod",
            "--region", "eu-west-1",
        ])

        assert exit_code == 0

        context_content = (output_dir / "context.py").read_text()
        assert 'project_name = "analytics"' in context_content
        assert 'component = "storage"' in context_content
        assert 'stage = "prod"' in context_content
        assert 'region = "eu-west-1"' in context_content

    def test_error_on_nonempty_directory(
        self, tmp_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Error when output directory is not empty."""
        output_dir = tmp_path / "existing"
        output_dir.mkdir()
        (output_dir / "file.txt").write_text("existing file")

        exit_code = main(["s3-bucket", "-o", str(output_dir)])

        assert exit_code == 1
        captured = capsys.readouterr()
        assert "not empty" in captured.err

    def test_error_on_unknown_skeleton(
        self, tmp_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Error when skeleton doesn't exist."""
        exit_code = main(["nonexistent", "-o", str(tmp_path / "output")])

        assert exit_code == 1
        captured = capsys.readouterr()
        assert "Unknown skeleton" in captured.err

    def test_output_includes_next_steps(
        self, tmp_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Success message includes helpful next steps."""
        output_dir = tmp_path / "my_project"

        main(["s3-bucket", "-o", str(output_dir)])

        captured = capsys.readouterr()
        assert "Next steps:" in captured.out
        assert "context.py" in captured.out
