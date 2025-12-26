# Implementation TODO

**Date**: 2025-12-25
**Status**: Phase 2 In Progress (Core utility consolidation complete)

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

## Phase 2: Consolidation (In Progress)

### 3. LINTER_IMPORTER_UNIFICATION (Phases 1-2) - Priority: P1 🔄 IN PROGRESS

Share utilities between linter and importer systems.

| Task | Status | Notes |
|------|--------|-------|
| Create `core/naming.py` | [x] | `to_snake_case`, `to_pascal_case`, `sanitize_python_name`, `sanitize_class_name` |
| Create `core/ast_helpers.py` | [x] | `is_cloudformation_dataclass`, `find_last_import_line`, `extract_resource_annotation`, etc. |
| Update importer to use shared utilities | [x] | `parser.py` re-exports from `core/naming.py` |
| Update linter to use shared utilities | [x] | `split.py`, `__init__.py`, `rules.py` updated |
| Consolidate `KNOWN_ENUMS` into `constants.py` | [ ] | Single source of truth |
| Document canonical code style | [ ] | Style guide for both systems |

**Implementation Date**: 2025-12-25 (Phase 1 started)
**Status**: Core utility consolidation complete. Remaining items are lower priority.

**Why here**: Package structure simplified, shared utilities are clearer.

---

## Phase 3: Polish

### 4. WATCHDOG_IMPROVEMENTS - Priority: P2

Improve file watching for better development feedback.

| Task | Status | Notes |
|------|--------|-------|
| Add debouncing to `stubs --watch` | [ ] | 500ms default, configurable |
| Handle `on_created` and `on_moved` events | [ ] | Currently only `on_modified` |
| Better error handling in watch mode | [ ] | Catch SyntaxError, continue watching |
| Add `--quiet` flag | [ ] | Minimal output mode |
| Add `lint --watch` command | [ ] | New feature |

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

**Implementation Date**: 2025-12-25

---

## Risk Summary

| Draft | Risk Level | Status |
|-------|------------|--------|
| Package Restructuring | Medium | ✅ Complete |
| CLI Improvements (P0) | Low | ✅ Complete |
| Linter/Importer Unification | Medium | 🔄 In Progress (core done) |
| Watchdog Improvements | Low | Pending |
| Agent Testing | Low | Pending |

---

## Effort Estimates

| Phase | Effort | Status |
|-------|--------|--------|
| 1. Foundation | 3-5 days | ✅ Complete |
| 2. Consolidation | 2-3 days | 🔄 In Progress |
| 3. Polish | 2-3 days | Pending |
| 4. Testing | 3-5 days | Pending |
