"""Configuration for file watching.

This module provides the WatchConfig dataclass for configuring file watchers.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fnmatch import fnmatch
from pathlib import Path


@dataclass
class WatchConfig:
    """Configuration for file watching.

    Attributes:
        paths: Directories to watch for changes.
        patterns: Glob patterns for files to include (e.g., ["*.py"]).
        ignored_patterns: Glob patterns for files to exclude (e.g., ["*.pyi"]).
        recursive: Whether to watch subdirectories recursively.
        debounce_ms: Delay in milliseconds before triggering callback after last event.

    Example:
        Watch Python files but ignore stubs and cache::

            config = WatchConfig(
                paths=[Path("src/")],
                patterns=["*.py"],
                ignored_patterns=["*.pyi", "__pycache__/*", "*.pyc"],
                debounce_ms=500,
            )
    """

    paths: list[Path]
    patterns: list[str] = field(default_factory=lambda: ["*.py"])
    ignored_patterns: list[str] = field(default_factory=lambda: ["*.pyi", "__pycache__/*"])
    recursive: bool = True
    debounce_ms: int = 500

    def matches(self, path: Path) -> bool:
        """Check if a path matches the watch configuration.

        Args:
            path: The file path to check.

        Returns:
            True if the path matches patterns and is not ignored.
        """
        path_str = str(path)
        name = path.name

        # Check if matches any include pattern
        matched = False
        for pattern in self.patterns:
            if fnmatch(name, pattern) or fnmatch(path_str, pattern):
                matched = True
                break

        if not matched:
            return False

        # Check if matches any ignore pattern
        for pattern in self.ignored_patterns:
            if fnmatch(name, pattern) or fnmatch(path_str, pattern):
                return False

        return True
