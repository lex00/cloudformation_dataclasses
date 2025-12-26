"""Watch framework for file monitoring with debouncing.

This module provides a reusable file watching framework used by CLI commands
like `stubs --watch` and `lint --watch`. It handles cross-platform file
monitoring with debouncing to prevent redundant operations during rapid edits.

Example:
    Basic usage with a callback::

        from cloudformation_dataclasses.watch import WatchConfig, DebouncedWatcher

        config = WatchConfig(
            paths=[Path("my_stack/")],
            patterns=["*.py"],
            ignored_patterns=["*.pyi", "__pycache__/*"],
        )

        def on_change(path: Path) -> None:
            print(f"File changed: {path}")

        watcher = DebouncedWatcher(config, on_change)
        watcher.start()  # Blocks until Ctrl+C

    With error handling::

        def on_error(path: Path, error: Exception) -> None:
            print(f"Error processing {path}: {error}")

        watcher = DebouncedWatcher(
            config,
            callback=on_change,
            error_handler=on_error,
        )
"""

from cloudformation_dataclasses.watch.config import WatchConfig
from cloudformation_dataclasses.watch.watcher import DebouncedWatcher

__all__ = ["WatchConfig", "DebouncedWatcher"]
