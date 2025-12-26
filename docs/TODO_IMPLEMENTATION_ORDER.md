# Implementation TODO

**Date**: 2025-12-25
**Status**: Phase 2 Complete (Linter/Importer core unification done)

---

## Overview

Implementation order for the 6 draft documents, based on dependencies and priorities.

---

## Phase 1: Foundation (Do First)

### 1. PACKAGE_RESTRUCTURING - Priority: P0 ✅ COMPLETE

Flatten generated package structure by eliminating `stack/` subdirectory.

| Task | Status | Notes |
|------|--------|-------|
| Update `cfn-dataclasses init` template | [x] | Remove `stack/`, single `__init__.py` |
| Update `cfn-dataclasses import` codegen | [x] | Generate flat structure |
| Implement `run_package_cli()` | [x] | Auto-build from registry, `--yaml`, `--validate` |
| Update `setup_resources()` for package level | [x] | Exclude `__main__.py`, `main.py` |
| Update `cfn-dataclasses stubs` | [x] | Single stub file per package |
| Add `cfn-dataclasses migrate --flatten` | [ ] | Optional migration command (future) |

**Implementation Date**: 2025-12-25
**Status**: All core tasks completed. Migration command deferred.

---

### 2. CLI_IMPROVEMENTS (P0 items) - Priority: P0 ✅ COMPLETE

Quick wins for better developer experience.

| Task | Status | Notes |
|------|--------|-------|
| ~~Lazy import PyYAML~~ Make PyYAML required | [x] | Simpler than lazy imports; pyyaml has no transitive deps |
| Lazy import watchdog in stubs watch mode | [x] | Already implemented in cli.py |
| Add `CLIError` class with suggestions | [x] | User-friendly error messages |

**Implementation Date**: 2025-12-25
**Decision**: Made PyYAML a required dependency instead of lazy import for simplicity.

---

## Phase 2: Consolidation ✅ COMPLETE

### 3. LINTER_IMPORTER_UNIFICATION (Phases 1-2) - Priority: P1 ✅ COMPLETE

Share utilities between linter and importer systems.

| Task | Status | Notes |
|------|--------|-------|
| Create `core/naming.py` | [x] | `to_snake_case`, `to_pascal_case`, `sanitize_python_name`, `sanitize_class_name` |
| Create `core/ast_helpers.py` | [x] | `is_cloudformation_dataclass`, `find_last_import_line`, `extract_resource_annotation`, etc. |
| Update importer to use shared utilities | [x] | `parser.py` re-exports from `core/naming.py` |
| Update linter to use shared utilities | [x] | `split.py`, `__init__.py`, `rules.py` updated |
| Document shared utilities in INTERNALS.md | [x] | `core/naming.py`, `core/ast_helpers.py` sections |
| Update CLI.md with all commands | [x] | Added `split`, `stubs`, CFD006-CFD012 |
| Consolidate `KNOWN_ENUMS` into `constants.py` | [ ] | Single source of truth (future) |
| Document canonical code style | [ ] | Style guide for both systems (future) |

**Implementation Date**: 2025-12-25
**Status**: Complete. Core utility consolidation and documentation done.

---

## Phase 3: Polish ✅ COMPLETE

### 4. WATCHDOG_IMPROVEMENTS - Priority: P2 ✅ COMPLETE

Improve file watching for better development feedback.

| Task | Status | Notes |
|------|--------|-------|
| Create reusable watch framework | [x] | `watch/` module with WatchConfig, DebouncedWatcher |
| Add debouncing to `stubs --watch` | [x] | 500ms default, `--debounce` flag |
| Handle `on_created` and `on_moved` events | [x] | Full event support in DebouncedWatcher |
| Better error handling in watch mode | [x] | Catch SyntaxError, duplicate suppression |
| Add `--quiet` flag | [x] | Both stubs and lint support `--quiet` |
| Add `lint --watch` command | [x] | With `--fix`, `--debounce`, `--quiet` options |
| Add tests for watch framework | [x] | 16 tests in `tests/test_watch.py` |
| Document watch framework | [x] | CLI.md, INTERNALS.md updated |

**Implementation Date**: 2025-12-25
**Status**: Complete. Full watch framework with debouncing, multi-event support, and `lint --watch`.

---

### 5. CLI_IMPROVEMENTS (remaining) - Priority: P2-P3

Additional CLI enhancements.

| Task | Status | Priority | Notes |
|------|--------|----------|-------|
| Dry run mode (`--dry-run`) | [ ] | P1 | Preview changes before modifying |
| Progress indicators | [ ] | P2 | Show progress for long operations |
| Modular entry points | [ ] | P2 | `cfn-init`, `cfn-lint`, etc. |
| Configuration file support | [ ] | P3 | `pyproject.toml` section |
| Startup time optimization | [ ] | P3 | Defer AWS imports |
| Shell completion | [ ] | P3 | argcomplete integration |
| Plugin architecture | [ ] | Future | Entry points for commands |

---

## Phase 4: Testing Infrastructure

### 6. AGENT_TESTING_PATTERN - Priority: P3

Two-Claude testing framework for automated framework validation.

| Task | Status | Notes |
|------|--------|-------|
| Implement orchestrator script | [ ] | Coordinates Developer and Runner |
| Add persona system prompts | [ ] | 5 personas: Beginner, Intermediate, Expert, Terse, Verbose |
| Implement conversation logging | [ ] | session.json, conversation.md, JSONL files |
| Create prompt library | [ ] | Simple, Medium, Complex, Adversarial |
| Implement scoring rubric | [ ] | Completeness, Lint Quality, Code Quality, etc. |
| Add validation pipeline | [ ] | cfn-lint, AWS validate-template |

**Why last**: Tests the framework - needs stable framework first.

---

## Already Complete

### 7. SCC_RELEVANCE - Documentation Only ✅ COMPLETE

| Task | Status | Notes |
|------|--------|-------|
| Add summary to INTERNALS.md | [x] | Explain SCCs are for Python imports, not CloudFormation |
| Add note to CLI.md | [x] | Note circular deps go to main.py in import section |

**Implementation Date**: 2025-12-25

---

## Risk Summary

| Draft | Risk Level | Status |
|-------|------------|--------|
| Package Restructuring | Medium | ✅ Complete |
| CLI Improvements (P0) | Low | ✅ Complete |
| Linter/Importer Unification | Medium | ✅ Complete |
| Watchdog Improvements | Low | ✅ Complete |
| Agent Testing | Low | Pending |

---

## Effort Estimates

| Phase | Effort | Status |
|-------|--------|--------|
| 1. Foundation | 3-5 days | ✅ Complete |
| 2. Consolidation | 2-3 days | ✅ Complete |
| 3. Polish | 2-3 days | ✅ Complete |
| 4. Testing | 3-5 days | Pending |
