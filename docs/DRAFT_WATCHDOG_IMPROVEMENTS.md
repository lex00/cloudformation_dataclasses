# Watchdog Integration: Analysis and Improvement Recommendations

**Date**: 2025-12-25
**Status**: DRAFT
**Author**: Research Analysis

---

## Executive Summary

The `cfn-dataclasses stubs --watch` command currently provides basic file watching capabilities for auto-regenerating `.pyi` stub files. This document analyzes the current implementation, explores broader use cases for watch mode across other CLI commands, and provides concrete recommendations for improvements.

**Key Findings**:
- Current watch mode is functional but basic (no debouncing, limited error handling)
- High-value opportunities exist for `lint --watch` and potential `build --watch`
- Modern Python tools use sophisticated watch patterns that we can learn from
- Improvements should focus on developer experience and incremental feedback

---

## Current Watchdog Implementation Analysis

### Location and Structure

**Primary Implementation**: `/Users/alex/Documents/checkouts/cloudformation_dataclasses/src/cloudformation_dataclasses/importer/cli.py` (lines 709-776)

### Current Capabilities

The `stubs --watch` implementation provides:

1. **Auto-discovery of stack packages**: Finds all `stack/` directories with `setup_resources` imports
2. **Initial stub generation**: Generates stubs before entering watch mode
3. **File monitoring**: Watches for `.py` file modifications (excludes `.pyi` files)
4. **Incremental regeneration**: Only regenerates stubs for the affected stack package
5. **Graceful shutdown**: Handles Ctrl+C to stop watching

### Implementation Details

```python
class StubHandler(FileSystemEventHandler):
    """Regenerate stubs when .py files change."""

    def on_modified(self, event: FileModifiedEvent) -> None:
        if event.is_directory:
            return
        if not str(event.src_path).endswith(".py"):
            return
        # Skip .pyi files
        if str(event.src_path).endswith(".pyi"):
            return

        # Find which stack this file belongs to
        file_path = Path(str(event.src_path))
        for stack in stacks:
            if stack in file_path.parents or file_path.parent == stack:
                from cloudformation_dataclasses.stubs import generate_stub_file
                if generate_stub_file(stack):
                    print(f"Regenerated stubs for {stack.parent.name}")
                break
```

**Observer Setup**:
- Uses `watchdog.observers.Observer` for cross-platform file watching
- Watches each stack's parent directory recursively
- Deduplicates watched directories to avoid redundant observers

### Current Limitations

1. **No Debouncing**: Rapid file saves (especially from editors with autosave) trigger multiple regenerations
2. **Limited Event Handling**: Only handles `on_modified`, missing `on_created` and `on_moved`
3. **No Error Recovery**: If stub generation fails, watch continues but error handling is minimal
4. **Verbose Output**: Every regeneration prints to console, can be noisy during rapid edits
5. **No Incremental Optimization**: Always regenerates entire stub files, even for single-class changes
6. **No Build System Integration**: Doesn't integrate with external build tools or IDEs

### Strengths

1. **Correct Scope Detection**: Accurately identifies which stack package to regenerate
2. **Minimal Resource Usage**: Only watches relevant directories
3. **Simple User Experience**: Easy to start/stop with Ctrl+C
4. **Cross-platform**: Uses `watchdog` which supports macOS, Linux, Windows

---

## Potential Expanded Use Cases

### 1. `lint --watch` (High Value)

**Rationale**: Linting during development provides immediate feedback on code quality issues.

**Current State**: The linter (`cloudformation_dataclasses.linter`) supports:
- `lint_file()` - Check files for issues
- `fix_file()` - Auto-fix issues with `--fix` flag
- Multiple rules (enum usage, pseudo-parameters, dict-to-PropertyType conversions)

**Proposed Behavior**:

```bash
# Watch mode for continuous linting
cfn-dataclasses lint path/to/stack --watch

# Watch mode with auto-fix
cfn-dataclasses lint path/to/stack --watch --fix
```

**Benefits**:
- Immediate feedback loop during development
- Catches common mistakes before commit
- Reduces need for manual linting passes
- Pairs well with IDE integration

**Implementation Considerations**:
- Should debounce to avoid running lint on every keystroke
- Display summary of issues found (not full lint output each time)
- Optional: Integrate with system notifications for critical issues
- Should track file additions/deletions in stack/ directory

### 2. `build --watch` (Medium Value)

**Rationale**: Auto-rebuild CloudFormation templates during development for rapid iteration.

**Current State**: No dedicated build command exists. Users run:
```bash
python -m <package_name>  # Runs main.py to build template
```

**Proposed Behavior**:

```bash
# Watch mode that rebuilds template on changes
cfn-dataclasses build path/to/stack --watch --output template.json

# Alternative: Validate on each build
cfn-dataclasses build path/to/stack --watch --validate
```

**Benefits**:
- Immediate template feedback during development
- Catches CloudFormation syntax errors early
- Enables rapid iteration on resource definitions
- Could integrate with local CloudFormation deployment tools

**Implementation Considerations**:
- Requires adding a new `build` subcommand (doesn't currently exist)
- Should run template validation after build
- Debouncing critical (template building can be slow for large stacks)
- Error handling important (partial code during edits)
- Could watch entire package (not just stack/ directory)

### 3. `stubs --watch` Improvements (Current Feature)

**Enhancements** (see Recommendations section below):
- Add debouncing
- Handle `on_created` and `on_moved` events
- Better error messages when stub generation fails
- Quieter output mode (--quiet flag)
- Integration with IDE language servers

---

## Design Considerations for Watch Mode

### 1. Debouncing Strategy

**Problem**: Editors save files multiple times during edits, triggering redundant operations.

**Solutions**:

**A. Time-based Debouncing** (Recommended)
```python
class DebouncedHandler(FileSystemEventHandler):
    def __init__(self, callback, delay=0.5):
        self.callback = callback
        self.delay = delay
        self.timers = {}

    def on_modified(self, event):
        path = event.src_path

        # Cancel existing timer for this path
        if path in self.timers:
            self.timers[path].cancel()

        # Start new timer
        timer = threading.Timer(self.delay, lambda: self.callback(path))
        self.timers[path] = timer
        timer.start()
```

**B. Coalescing Events** (Alternative)
- Collect events in a queue
- Process queue every N seconds
- Deduplicate events for same file

**Recommendation**: Time-based debouncing with configurable delay (default 500ms).

### 2. Incremental Updates

**Problem**: Regenerating entire stub files for single-class changes is inefficient.

**Solutions**:

**A. Smart Diffing** (Complex)
- Parse existing stub file
- Compare with newly generated content
- Only write if changed (already done via `_write_stub_if_changed`)

**B. Module-level Tracking** (Simpler)
- Track which module files changed
- Only re-scan those modules
- Update stub file incrementally

**C. Full Regeneration** (Current - Simplest)
- Always regenerate entire stub file
- Fast enough for typical projects (<100ms)

**Recommendation**: Keep current full regeneration approach. It's simple and fast enough. Optimize only if performance issues arise in large projects.

### 3. Error Handling

**Problem**: Syntax errors during editing can break watch mode.

**Current State**: Stub generation fails silently if code has syntax errors.

**Improvements**:

```python
def on_modified(self, event):
    try:
        if generate_stub_file(stack):
            print(f"✓ Regenerated stubs for {stack.parent.name}")
    except SyntaxError as e:
        print(f"⚠ Syntax error in {event.src_path}: {e}")
    except Exception as e:
        print(f"✗ Failed to regenerate stubs: {e}")
```

**Additional Considerations**:
- Suppress repeated errors for same file
- Clear error state when file is fixed
- Optional: Desktop notifications for errors

### 4. Output and Logging

**Problem**: Current output can be verbose during active development.

**Improvements**:

```bash
# Quiet mode - only show errors
cfn-dataclasses stubs --watch --quiet

# Verbose mode - show all regenerations
cfn-dataclasses stubs --watch --verbose

# Default - balanced output
cfn-dataclasses stubs --watch
```

**Output Patterns**:
```
# Initial
Generated stubs for 3 stack(s)
Watching for changes... (Ctrl+C to stop)

# On change (default)
✓ fargate

# On change (verbose)
✓ Regenerated stubs for fargate (127ms)

# On error
✗ fargate: SyntaxError on line 45
```

### 5. Cross-Command Watch Architecture

**Problem**: Duplicating watch logic across commands leads to inconsistency.

**Solution**: Create a reusable watch framework.

```python
# cloudformation_dataclasses/watch.py

from dataclasses import dataclass
from typing import Callable, Optional
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading

@dataclass
class WatchConfig:
    """Configuration for file watching."""
    paths: list[Path]
    patterns: list[str]  # e.g., ["*.py", "*.yaml"]
    ignored_patterns: list[str]  # e.g., ["*.pyi", "__pycache__/*"]
    recursive: bool = True
    debounce_ms: int = 500

class DebouncedWatcher:
    """Reusable file watcher with debouncing."""

    def __init__(
        self,
        config: WatchConfig,
        callback: Callable[[Path], None],
        error_handler: Optional[Callable[[Exception], None]] = None,
    ):
        self.config = config
        self.callback = callback
        self.error_handler = error_handler
        self.timers: dict[str, threading.Timer] = {}

    def start(self):
        """Start watching files."""
        observer = Observer()
        handler = self._create_handler()

        for path in self.config.paths:
            observer.schedule(handler, str(path), recursive=self.config.recursive)

        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    def _create_handler(self) -> FileSystemEventHandler:
        # Implementation with debouncing
        ...
```

**Usage**:
```python
# In cli.py for stubs --watch
config = WatchConfig(
    paths=[stack.parent for stack in stacks],
    patterns=["*.py"],
    ignored_patterns=["*.pyi"],
    debounce_ms=500,
)

watcher = DebouncedWatcher(
    config=config,
    callback=lambda path: regenerate_stubs(path),
    error_handler=lambda e: print(f"Error: {e}"),
)
watcher.start()
```

---

## Comparison with Similar Tools

### pytest-watch

**Implementation**: Uses `watchdog` with custom event handling.

**Key Features**:
- Debouncing (200ms default)
- Clears terminal before each run
- Shows summary (tests passed/failed)
- Colorized output
- Configurable via `.pytest-watch.cfg`

**Lessons**:
- Clear terminal between runs improves readability
- Summary output > verbose logs
- Configuration files enable per-project settings

### mypy --watch (via dmypy)

**Implementation**: Uses daemon process with file watching.

**Key Features**:
- Incremental type checking
- Caches module state between runs
- Fast feedback (<100ms for single file)
- JSON output mode for IDE integration

**Lessons**:
- Daemon approach enables caching
- Incremental analysis critical for large codebases
- IDE integration requires structured output

### jest --watch (JavaScript)

**Implementation**: Custom file watcher with intelligent filtering.

**Key Features**:
- Interactive mode (press 'a' to run all, 'f' for failed)
- Pattern filtering
- Dependency graph tracking
- Only reruns affected tests

**Lessons**:
- Interactive controls enhance developer experience
- Dependency tracking enables smart re-execution
- Pattern filtering helps focus on specific files

### nodemon (Node.js)

**Implementation**: Standalone file watcher for any command.

**Key Features**:
- Configurable file patterns
- Delay/debounce settings
- Execute arbitrary commands on changes
- JSON config file (`nodemon.json`)

**Lessons**:
- Generic watch framework can power multiple use cases
- Configuration files enable reusable setups
- Arbitrary command execution adds flexibility

---

## Concrete Recommendations

### Priority 1: Improve Current `stubs --watch`

**Timeline**: Can be implemented incrementally

**Changes**:

1. **Add Debouncing** (500ms default)
   - Prevents redundant regenerations
   - Configurable via `--debounce` flag

2. **Handle Additional Events**
   - `on_created`: New files in stack/ directory
   - `on_moved`: Renamed files
   - `on_deleted`: Clean up stale stub entries

3. **Better Error Handling**
   - Catch `SyntaxError` during partial edits
   - Show clear error messages
   - Continue watching after errors

4. **Improved Output**
   - Add `--quiet` flag for minimal output
   - Show emoji indicators (✓ success, ⚠ warning, ✗ error)
   - Optional: Desktop notifications via `pync` (macOS) or similar

5. **Configuration File Support** (Optional)
   ```toml
   # .cfn-watch.toml
   [stubs]
   debounce_ms = 500
   quiet = false
   notify = true
   ```

**Implementation Example**:

```python
def _run_stubs_command(args: argparse.Namespace) -> int:
    if args.watch:
        try:
            from watchdog.observers import Observer
            from watchdog.events import FileSystemEventHandler, FileSystemEvent
        except ImportError:
            print("Error: Watch mode requires watchdog...", file=sys.stderr)
            return 1

        stacks = find_stack_packages(path)
        if not stacks:
            print(f"No stack packages found in {path}", file=sys.stderr)
            return 1

        # Initial generation
        count = generate_stubs_for_path(path)
        print(f"Generated stubs for {count} stack(s)")
        print(f"Watching for changes... (Ctrl+C to stop)")

        class DebouncedStubHandler(FileSystemEventHandler):
            def __init__(self, stacks: list[Path], debounce_ms: int = 500):
                self.stacks = stacks
                self.debounce_delay = debounce_ms / 1000.0
                self.timers: dict[str, threading.Timer] = {}
                self.last_errors: dict[str, str] = {}

            def _should_process(self, event: FileSystemEvent) -> bool:
                if event.is_directory:
                    return False
                path = str(event.src_path)
                if not path.endswith(".py"):
                    return False
                if path.endswith(".pyi"):
                    return False
                return True

            def _debounced_regenerate(self, file_path: Path):
                """Regenerate stubs after debounce delay."""
                for stack in self.stacks:
                    if stack in file_path.parents or file_path.parent == stack:
                        try:
                            if generate_stub_file(stack):
                                stack_name = stack.parent.name
                                # Clear previous error for this stack
                                if stack_name in self.last_errors:
                                    del self.last_errors[stack_name]

                                if not args.quiet:
                                    print(f"✓ {stack_name}")
                        except SyntaxError as e:
                            stack_name = stack.parent.name
                            error_msg = f"Syntax error: {e}"
                            # Only print if error changed
                            if self.last_errors.get(stack_name) != error_msg:
                                print(f"⚠ {stack_name}: {error_msg}")
                                self.last_errors[stack_name] = error_msg
                        except Exception as e:
                            stack_name = stack.parent.name
                            error_msg = str(e)
                            if self.last_errors.get(stack_name) != error_msg:
                                print(f"✗ {stack_name}: {error_msg}")
                                self.last_errors[stack_name] = error_msg
                        break

            def _trigger_regenerate(self, file_path: Path):
                """Trigger regeneration with debouncing."""
                key = str(file_path)

                # Cancel existing timer
                if key in self.timers:
                    self.timers[key].cancel()

                # Start new timer
                timer = threading.Timer(
                    self.debounce_delay,
                    lambda: self._debounced_regenerate(file_path)
                )
                self.timers[key] = timer
                timer.start()

            def on_modified(self, event: FileSystemEvent) -> None:
                if self._should_process(event):
                    self._trigger_regenerate(Path(str(event.src_path)))

            def on_created(self, event: FileSystemEvent) -> None:
                if self._should_process(event):
                    self._trigger_regenerate(Path(str(event.src_path)))

            def on_moved(self, event: FileSystemEvent) -> None:
                # Treat rename as creation of new file
                if self._should_process(event):
                    self._trigger_regenerate(Path(str(event.dest_path)))

        observer = Observer()
        handler = DebouncedStubHandler(
            stacks,
            debounce_ms=getattr(args, 'debounce', 500)
        )

        # Watch each stack's parent directory
        watched_dirs: set[Path] = set()
        for stack in stacks:
            parent = stack.parent
            if parent not in watched_dirs:
                observer.schedule(handler, str(parent), recursive=True)
                watched_dirs.add(parent)

        observer.start()
        try:
            import time
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            print("\nStopped watching.")
        observer.join()
        return 0
```

### Priority 2: Add `lint --watch`

**Timeline**: After stubs improvements stabilize

**Benefits**:
- High developer value (immediate linting feedback)
- Leverages existing linter infrastructure
- Natural pairing with `--fix` for auto-correction

**Implementation**:

```python
def _run_lint_command(args: argparse.Namespace) -> int:
    path = Path(args.path)

    if args.watch:
        # Similar structure to stubs --watch
        # Use DebouncedWatcher with lint_file callback
        print(f"Watching {path} for changes...")

        def on_file_change(file_path: Path):
            if args.fix:
                original = file_path.read_text()
                fixed = fix_file(file_path, write=True)
                if fixed != original:
                    print(f"✓ Fixed {file_path.name}")
            else:
                issues = lint_file(file_path)
                if issues:
                    print(f"⚠ {file_path.name}: {len(issues)} issue(s)")
                    for issue in issues[:5]:  # Show first 5
                        print(f"  {issue.line}:{issue.column} {issue.rule_id}")
                else:
                    print(f"✓ {file_path.name}")

        config = WatchConfig(
            paths=[path],
            patterns=["*.py"],
            ignored_patterns=["*.pyi", "__pycache__/*"],
            debounce_ms=500,
        )

        watcher = DebouncedWatcher(config, on_file_change)
        watcher.start()
        return 0
```

**CLI Additions**:

```python
lint_parser.add_argument(
    "--watch", "-w",
    action="store_true",
    help="Watch for changes and re-lint automatically",
)
lint_parser.add_argument(
    "--debounce",
    type=int,
    default=500,
    help="Debounce delay in milliseconds (default: 500)",
)
lint_parser.add_argument(
    "--quiet", "-q",
    action="store_true",
    help="Only show errors, not successful lints",
)
```

### Priority 3: Create Reusable Watch Framework

**Timeline**: After implementing both stubs and lint watch modes

**Purpose**:
- Consolidate watch logic
- Enable future watch commands (build, test, etc.)
- Consistent behavior across all watch modes

**Module Structure**:

```
src/cloudformation_dataclasses/watch/
├── __init__.py          # Public API
├── config.py            # WatchConfig, file patterns
├── debouncer.py         # Debouncing logic
├── handler.py           # DebouncedHandler, event filtering
└── watcher.py           # Main Watcher class
```

### Priority 4: IDE Integration

**Timeline**: Future enhancement

**Features**:
- Language Server Protocol (LSP) integration
- Watch mode triggers IDE refresh
- JSON output mode for programmatic consumption

**Example**:

```bash
# JSON output for IDE consumption
cfn-dataclasses lint --watch --format json
```

---

## Testing Strategy

### Unit Tests

```python
# tests/watch/test_debouncer.py
def test_debouncer_coalesces_rapid_events():
    """Multiple rapid events should trigger single callback."""
    calls = []
    debouncer = Debouncer(lambda x: calls.append(x), delay=0.1)

    debouncer.trigger("file.py")
    debouncer.trigger("file.py")
    debouncer.trigger("file.py")

    time.sleep(0.2)
    assert len(calls) == 1
```

### Integration Tests

```python
# tests/watch/test_stubs_watch.py
def test_stubs_watch_regenerates_on_file_change(tmp_path):
    """Watch mode should regenerate stubs when .py files change."""
    # Setup stack structure
    stack_dir = tmp_path / "mystack" / "stack"
    stack_dir.mkdir(parents=True)

    # Create initial file
    (stack_dir / "resources.py").write_text("class MyBucket: pass")

    # Start watch mode in background
    process = subprocess.Popen([
        "cfn-dataclasses", "stubs", "--watch", str(tmp_path)
    ])

    time.sleep(1)  # Wait for initial generation

    # Modify file
    (stack_dir / "resources.py").write_text("class MyBucket2: pass")

    time.sleep(1)  # Wait for regeneration

    # Check stub updated
    stub_content = (tmp_path / "mystack" / "__init__.pyi").read_text()
    assert "MyBucket2" in stub_content

    process.terminate()
```

---

## Migration Path

### Phase 1: Improve `stubs --watch` (Weeks 1-2)
- Add debouncing
- Handle additional events (created, moved)
- Better error handling
- Output improvements (quiet mode, emojis)

### Phase 2: Add `lint --watch` (Weeks 3-4)
- Implement watch mode for linter
- Add `--watch`, `--debounce`, `--quiet` flags
- Test with real-world projects

### Phase 3: Extract Common Framework (Weeks 5-6)
- Create `cloudformation_dataclasses.watch` module
- Refactor stubs and lint to use framework
- Add configuration file support

### Phase 4: Polish and Document (Week 7)
- Update documentation
- Add examples to README
- Create tutorial for watch modes

---

## Configuration File Format

**File**: `.cfn-watch.toml` (in project root)

```toml
[watch]
# Global watch settings
debounce_ms = 500
notify = false  # Desktop notifications

[stubs]
enabled = true
quiet = false
patterns = ["*.py"]
ignored_patterns = ["*.pyi", "*.pyc", "__pycache__/*"]

[lint]
enabled = true
auto_fix = true
quiet = false
patterns = ["stack/*.py"]
ignored_patterns = ["tests/*"]

[build]
enabled = false
output = "template.json"
validate = true
patterns = ["**/*.py"]
```

---

## Risks and Mitigations

### Risk 1: Performance on Large Projects

**Risk**: Watching hundreds of files could impact performance.

**Mitigation**:
- Only watch relevant directories (stack/, not entire project)
- Use debouncing to limit execution frequency
- Add `--max-watch-files` limit with warning

### Risk 2: Cross-Platform Compatibility

**Risk**: File watching behavior differs between macOS/Linux/Windows.

**Mitigation**:
- `watchdog` library handles platform differences
- Test on all three platforms
- Document known platform-specific issues

### Risk 3: Editor Conflicts

**Risk**: Some editors create temporary files that trigger false events.

**Mitigation**:
- Ignore common temp file patterns (`.swp`, `.tmp`, `~`)
- Add `ignored_patterns` configuration
- Document known editor issues

### Risk 4: Circular Dependencies

**Risk**: Watch mode triggers changes that trigger more watches.

**Mitigation**:
- Ignore self-generated files (`.pyi` already ignored)
- Track recently processed files to prevent loops
- Add max-recursion depth protection

---

## Success Metrics

### Developer Experience
- Time from file save to feedback < 1 second (95th percentile)
- Zero false positives from temp files
- Graceful degradation on errors (watch continues)

### Adoption
- 30% of users enable watch mode in local development
- Positive feedback in user surveys
- Reduced "I forgot to regenerate stubs" issues

### Performance
- < 100ms overhead for debouncing logic
- < 10MB memory footprint for watch process
- Works reliably with 100+ file projects

---

## Future Enhancements

### 1. Multi-Command Watch

```bash
# Watch for changes and run multiple commands
cfn-dataclasses watch --stubs --lint --build
```

### 2. Smart Filtering

```bash
# Only watch specific modules
cfn-dataclasses stubs --watch --include "stack/network.py,stack/compute.py"
```

### 3. Custom Commands

```bash
# Run arbitrary command on changes
cfn-dataclasses watch --exec "pytest tests/test_stack.py"
```

### 4. IDE Plugin

- VSCode extension that auto-starts watch mode
- Real-time linting in editor gutter
- Stub regeneration on file save

### 5. Cloud Integration

- Watch mode triggers CDK deploy (with confirmation)
- Integrate with AWS SAM local development
- Real-time CloudFormation validation via AWS API

---

## Conclusion

The current `stubs --watch` implementation provides a solid foundation, but has significant room for improvement. By adding debouncing, better error handling, and expanding watch mode to other commands (especially `lint --watch`), we can dramatically improve the developer experience.

The proposed reusable watch framework will enable consistent behavior across all watch modes and make it easy to add watch support to future commands. This aligns with modern Python tool patterns seen in pytest-watch, mypy, and similar tools.

**Recommended Next Steps**:
1. Implement debouncing and improved error handling for `stubs --watch`
2. Add `lint --watch` as a high-value enhancement
3. Extract common watch logic into reusable framework
4. Gather user feedback and iterate

**Estimated Effort**: 2-3 weeks for Priority 1-2, additional 1-2 weeks for framework extraction.
