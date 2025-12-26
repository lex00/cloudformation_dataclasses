"""Debounced file watcher implementation.

This module provides the DebouncedWatcher class for watching files with
debouncing to prevent redundant operations during rapid edits.
"""

from __future__ import annotations

import threading
import time
from pathlib import Path
from typing import Callable, Optional

from cloudformation_dataclasses.watch.config import WatchConfig


class DebouncedWatcher:
    """File watcher with debouncing support.

    Watches directories for file changes and triggers a callback after a
    configurable debounce delay. This prevents redundant operations when
    editors save files multiple times in quick succession.

    Attributes:
        config: Watch configuration specifying paths, patterns, and debounce delay.
        callback: Function called when a matching file changes.
        error_handler: Optional function called when callback raises an exception.
        quiet: If True, suppress success messages (errors still shown).

    Example:
        Basic usage::

            config = WatchConfig(
                paths=[Path("my_stack/")],
                patterns=["*.py"],
            )

            def regenerate(path: Path) -> None:
                print(f"Regenerating for {path}")

            watcher = DebouncedWatcher(config, regenerate)
            watcher.start()  # Blocks until Ctrl+C
    """

    def __init__(
        self,
        config: WatchConfig,
        callback: Callable[[Path], None],
        error_handler: Optional[Callable[[Path, Exception], None]] = None,
        quiet: bool = False,
    ):
        """Initialize the watcher.

        Args:
            config: Watch configuration.
            callback: Function to call when a file changes.
            error_handler: Optional function to handle callback errors.
            quiet: If True, suppress non-error output.
        """
        self.config = config
        self.callback = callback
        self.error_handler = error_handler
        self.quiet = quiet
        self._timers: dict[str, threading.Timer] = {}
        self._last_errors: dict[str, str] = {}
        self._observer: Optional[object] = None

    def _should_process(self, path: str, is_directory: bool) -> bool:
        """Check if an event should be processed.

        Args:
            path: The file path from the event.
            is_directory: Whether the event is for a directory.

        Returns:
            True if the event should trigger the callback.
        """
        if is_directory:
            return False
        return self.config.matches(Path(path))

    def _trigger_callback(self, file_path: Path) -> None:
        """Trigger the callback with debouncing.

        Args:
            file_path: The file that changed.
        """
        key = str(file_path)

        # Cancel existing timer for this path
        if key in self._timers:
            self._timers[key].cancel()

        # Start new timer
        delay = self.config.debounce_ms / 1000.0
        timer = threading.Timer(delay, lambda: self._execute_callback(file_path))
        self._timers[key] = timer
        timer.start()

    def _execute_callback(self, file_path: Path) -> None:
        """Execute the callback with error handling.

        Args:
            file_path: The file that changed.
        """
        key = str(file_path)

        try:
            self.callback(file_path)
            # Clear previous error for this path
            if key in self._last_errors:
                del self._last_errors[key]
        except SyntaxError as e:
            error_msg = f"Syntax error: {e}"
            # Only report if error changed
            if self._last_errors.get(key) != error_msg:
                self._last_errors[key] = error_msg
                if self.error_handler:
                    self.error_handler(file_path, e)
        except Exception as e:
            error_msg = str(e)
            if self._last_errors.get(key) != error_msg:
                self._last_errors[key] = error_msg
                if self.error_handler:
                    self.error_handler(file_path, e)

    def start(self) -> None:
        """Start watching for file changes.

        This method blocks until interrupted with Ctrl+C (KeyboardInterrupt).

        Raises:
            ImportError: If watchdog is not installed.
        """
        try:
            from watchdog.events import FileSystemEvent, FileSystemEventHandler
            from watchdog.observers import Observer
        except ImportError:
            raise ImportError(
                "Watch mode requires the watchdog package. "
                "Install it with: pip install cloudformation_dataclasses[stubs]"
            )

        watcher = self

        class Handler(FileSystemEventHandler):
            """Event handler that delegates to the watcher."""

            def on_modified(self, event: FileSystemEvent) -> None:
                if watcher._should_process(str(event.src_path), event.is_directory):
                    watcher._trigger_callback(Path(str(event.src_path)))

            def on_created(self, event: FileSystemEvent) -> None:
                if watcher._should_process(str(event.src_path), event.is_directory):
                    watcher._trigger_callback(Path(str(event.src_path)))

            def on_moved(self, event: FileSystemEvent) -> None:
                # For moved events, process the destination path
                dest_path = getattr(event, "dest_path", None)
                if dest_path and watcher._should_process(str(dest_path), event.is_directory):
                    watcher._trigger_callback(Path(str(dest_path)))

        observer = Observer()
        handler = Handler()
        self._observer = observer

        # Watch each unique directory
        watched_dirs: set[Path] = set()
        for path in self.config.paths:
            if path.is_file():
                path = path.parent
            if path not in watched_dirs:
                observer.schedule(handler, str(path), recursive=self.config.recursive)
                watched_dirs.add(path)

        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    def stop(self) -> None:
        """Stop watching for file changes."""
        if self._observer is not None:
            self._observer.stop()  # type: ignore[union-attr]
