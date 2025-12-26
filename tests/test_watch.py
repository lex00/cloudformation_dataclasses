"""Tests for the watch framework module.

Tests for WatchConfig and DebouncedWatcher functionality.
"""

from pathlib import Path
import threading
import time

import pytest

from cloudformation_dataclasses.watch import WatchConfig, DebouncedWatcher


class TestWatchConfig:
    """Tests for WatchConfig."""

    def test_default_patterns(self) -> None:
        """Test default configuration values."""
        config = WatchConfig(paths=[Path(".")])
        assert config.patterns == ["*.py"]
        assert config.ignored_patterns == ["*.pyi", "__pycache__/*"]
        assert config.recursive is True
        assert config.debounce_ms == 500

    def test_custom_patterns(self) -> None:
        """Test custom pattern configuration."""
        config = WatchConfig(
            paths=[Path("src/")],
            patterns=["*.py", "*.yaml"],
            ignored_patterns=["test_*.py"],
            debounce_ms=1000,
        )
        assert config.patterns == ["*.py", "*.yaml"]
        assert config.ignored_patterns == ["test_*.py"]
        assert config.debounce_ms == 1000

    def test_matches_include_pattern(self) -> None:
        """Test that paths matching include patterns are matched."""
        config = WatchConfig(
            paths=[Path(".")],
            patterns=["*.py"],
            ignored_patterns=[],
        )
        assert config.matches(Path("test.py")) is True
        assert config.matches(Path("src/module.py")) is True
        assert config.matches(Path("test.txt")) is False
        assert config.matches(Path("test.yaml")) is False

    def test_matches_excludes_ignored(self) -> None:
        """Test that ignored patterns are excluded."""
        config = WatchConfig(
            paths=[Path(".")],
            patterns=["*.py"],
            ignored_patterns=["*.pyi", "test_*.py"],
        )
        assert config.matches(Path("module.py")) is True
        assert config.matches(Path("module.pyi")) is False
        assert config.matches(Path("test_module.py")) is False

    def test_matches_default_ignores_pyi(self) -> None:
        """Test default configuration ignores .pyi files."""
        config = WatchConfig(paths=[Path(".")])
        assert config.matches(Path("module.py")) is True
        assert config.matches(Path("module.pyi")) is False

    def test_matches_multiple_patterns(self) -> None:
        """Test matching against multiple patterns."""
        config = WatchConfig(
            paths=[Path(".")],
            patterns=["*.py", "*.yaml", "*.json"],
            ignored_patterns=[],
        )
        assert config.matches(Path("file.py")) is True
        assert config.matches(Path("config.yaml")) is True
        assert config.matches(Path("data.json")) is True
        assert config.matches(Path("readme.md")) is False


class TestDebouncedWatcher:
    """Tests for DebouncedWatcher."""

    def test_init_with_config(self) -> None:
        """Test watcher initialization."""
        config = WatchConfig(paths=[Path(".")])
        callback_called = []

        def callback(path: Path) -> None:
            callback_called.append(path)

        watcher = DebouncedWatcher(config, callback)
        assert watcher.config == config
        assert watcher.callback == callback
        assert watcher.error_handler is None
        assert watcher.quiet is False

    def test_init_with_error_handler(self) -> None:
        """Test watcher initialization with error handler."""
        config = WatchConfig(paths=[Path(".")])
        errors = []

        def callback(path: Path) -> None:
            pass

        def error_handler(path: Path, error: Exception) -> None:
            errors.append((path, error))

        watcher = DebouncedWatcher(
            config,
            callback,
            error_handler=error_handler,
            quiet=True,
        )
        assert watcher.error_handler == error_handler
        assert watcher.quiet is True

    def test_should_process_filters_directories(self) -> None:
        """Test that directories are filtered out."""
        config = WatchConfig(paths=[Path(".")])
        watcher = DebouncedWatcher(config, lambda p: None)
        assert watcher._should_process("test.py", is_directory=True) is False
        assert watcher._should_process("test.py", is_directory=False) is True

    def test_should_process_uses_config_patterns(self) -> None:
        """Test that config patterns are applied."""
        config = WatchConfig(
            paths=[Path(".")],
            patterns=["*.py"],
            ignored_patterns=["*.pyi"],
        )
        watcher = DebouncedWatcher(config, lambda p: None)
        assert watcher._should_process("module.py", is_directory=False) is True
        assert watcher._should_process("module.pyi", is_directory=False) is False
        assert watcher._should_process("module.txt", is_directory=False) is False

    def test_trigger_callback_debounces(self) -> None:
        """Test that rapid calls are debounced."""
        config = WatchConfig(paths=[Path(".")], debounce_ms=100)
        callback_calls: list[Path] = []

        def callback(path: Path) -> None:
            callback_calls.append(path)

        watcher = DebouncedWatcher(config, callback)

        # Trigger multiple times rapidly
        test_path = Path("test.py")
        watcher._trigger_callback(test_path)
        watcher._trigger_callback(test_path)
        watcher._trigger_callback(test_path)

        # Wait for debounce
        time.sleep(0.2)

        # Should only have been called once
        assert len(callback_calls) == 1
        assert callback_calls[0] == test_path

    def test_execute_callback_handles_errors(self) -> None:
        """Test that callback errors are handled."""
        config = WatchConfig(paths=[Path(".")])
        errors: list[tuple[Path, Exception]] = []

        def callback(path: Path) -> None:
            raise ValueError("Test error")

        def error_handler(path: Path, error: Exception) -> None:
            errors.append((path, error))

        watcher = DebouncedWatcher(config, callback, error_handler=error_handler)

        test_path = Path("test.py")
        watcher._execute_callback(test_path)

        assert len(errors) == 1
        assert errors[0][0] == test_path
        assert isinstance(errors[0][1], ValueError)

    def test_execute_callback_handles_syntax_errors(self) -> None:
        """Test that syntax errors are handled specially."""
        config = WatchConfig(paths=[Path(".")])
        errors: list[tuple[Path, Exception]] = []

        def callback(path: Path) -> None:
            raise SyntaxError("invalid syntax")

        def error_handler(path: Path, error: Exception) -> None:
            errors.append((path, error))

        watcher = DebouncedWatcher(config, callback, error_handler=error_handler)

        test_path = Path("test.py")
        watcher._execute_callback(test_path)

        assert len(errors) == 1
        assert isinstance(errors[0][1], SyntaxError)

    def test_execute_callback_clears_previous_errors(self) -> None:
        """Test that successful callback clears previous errors."""
        config = WatchConfig(paths=[Path(".")])
        call_count = [0]

        def callback(path: Path) -> None:
            call_count[0] += 1
            if call_count[0] == 1:
                raise ValueError("First call fails")
            # Second call succeeds

        def error_handler(path: Path, error: Exception) -> None:
            pass

        watcher = DebouncedWatcher(config, callback, error_handler=error_handler)

        test_path = Path("test.py")

        # First call - fails and records error
        watcher._execute_callback(test_path)
        assert str(test_path) in watcher._last_errors

        # Second call - succeeds and clears error
        watcher._execute_callback(test_path)
        assert str(test_path) not in watcher._last_errors

    def test_duplicate_errors_not_reported(self) -> None:
        """Test that same error isn't reported multiple times."""
        config = WatchConfig(paths=[Path(".")])
        error_reports: list[tuple[Path, Exception]] = []

        def callback(path: Path) -> None:
            raise ValueError("Same error")

        def error_handler(path: Path, error: Exception) -> None:
            error_reports.append((path, error))

        watcher = DebouncedWatcher(config, callback, error_handler=error_handler)

        test_path = Path("test.py")

        # Multiple calls with same error
        watcher._execute_callback(test_path)
        watcher._execute_callback(test_path)
        watcher._execute_callback(test_path)

        # Error should only be reported once
        assert len(error_reports) == 1

    def test_start_raises_without_watchdog(self) -> None:
        """Test that start raises ImportError without watchdog.

        Note: This test may pass or fail depending on whether watchdog
        is installed. We skip if watchdog is available.
        """
        try:
            import watchdog
            pytest.skip("watchdog is installed")
        except ImportError:
            config = WatchConfig(paths=[Path(".")])
            watcher = DebouncedWatcher(config, lambda p: None)
            with pytest.raises(ImportError):
                watcher.start()
