# Linter-Importer Unification Analysis

**Date:** 2025-12-25
**Status:** Draft Research Document

## Executive Summary

This document analyzes opportunities to unify the **linter** and **importer** features in the cloudformation_dataclasses codebase. Both systems operate on Python source code and CloudFormation concepts, but currently have distinct architectures and minimal shared code. This research identifies overlaps, shared concerns, and concrete proposals for deeper integration.

**Key Finding:** While the systems have distinct purposes, there are significant opportunities to share infrastructure, particularly around:
- Python AST manipulation and code generation
- Name conversion (PascalCase ↔ snake_case)
- Enum and PropertyType detection
- Import management
- CloudFormation constant mappings

---

## Current Architecture

### Importer System

**Purpose:** Convert CloudFormation YAML/JSON templates to Python dataclasses

**Pipeline:**
```
CloudFormation Template (YAML/JSON)
    ↓ parse_template()
Intermediate Representation (IR)
    ↓ generate_code() / generate_package()
Python Source Code (dataclasses)
```

**Key Components:**

1. **Parser** (`importer/parser.py`)
   - YAML/JSON parsing with CloudFormation intrinsic support
   - Converts to IR (IRTemplate, IRResource, IRProperty, IRIntrinsic)
   - Reference graph analysis for dependency tracking
   - Name conversion: `to_snake_case()`, `sanitize_python_name()`

2. **IR** (`importer/ir.py`)
   - Normalized data structures decoupled from CloudFormation format
   - IntrinsicType enum for all CloudFormation functions
   - Resource, Parameter, Output, Condition, Mapping representations

3. **Code Generation** (`importer/codegen/`)
   - `package.py`: Orchestrates multi-file package generation
   - `blocks.py`: PropertyType wrapper class generation
   - `values.py`: Value serialization (literals, enums, intrinsics)
   - `classes.py`: Resource/Parameter/Output class generation
   - `imports.py`: Import statement consolidation
   - `helpers.py`: Enum detection, PropertyType resolution
   - `context.py`: Tracks imports, generated classes, forward references

4. **Integration Point with Linter:**
   - `_lint_generated_files()` in package.py (line 275)
   - Calls `linter.fix_code()` on stack files after generation
   - Only lints stack files, not __init__.py

**Code Generation Strategy:**
- Block mode (declarative) generates wrapper classes for all PropertyTypes
- Uses `ref(ClassName)` and `get_att(ClassName, "Attr")` helpers
- Detects forward references in SCCs (strongly connected components)
- Generates qualified imports (e.g., `s3.Bucket`) to avoid name collisions
- Pattern matching in Sub() intrinsics to convert to ref()/get_att() calls

### Linter System

**Purpose:** Check and auto-fix style issues in generated/user-written code

**Pipeline:**
```
Python Source Code
    ↓ lint_code() / fix_code()
AST Analysis
    ↓ Apply Rules
LintIssues (with fixes)
    ↓ Apply fixes + add imports
Fixed Python Source Code
```

**Key Components:**

1. **Core** (`linter/__init__.py`)
   - `lint_code()`: Detect issues
   - `fix_code()`: Apply auto-fixes
   - `_add_imports()`: Insert missing import statements

2. **Rules** (`linter/rules.py`)
   - 11 rule classes (CFD001-CFD012)
   - Each rule has: `check()` method, suggestions, fix imports
   - Pattern matching on AST nodes

3. **Introspection** (`linter/introspection.py`)
   - Runtime type analysis for enum/PropertyType detection
   - `get_enum_for_field()`, `get_property_type_for_field()`
   - Uses Python's `typing.get_type_hints()` for runtime introspection

4. **Split Utility** (`linter/split.py`)
   - Analyzes resource files to categorize by AWS service
   - Breaks large files into network.py, compute.py, etc.
   - Dependency detection via ref()/get_att() calls

**Rule Categories:**
- **Constants:** CFD001 (condition operators), CFD002 (parameter types), CFD003 (pseudo-parameters)
- **Enums:** CFD004 (string literals → enum constants)
- **PropertyTypes:** CFD005 (dict → PropertyType), CFD009 (inline constructors)
- **Intrinsics:** CFD006 (dict → intrinsic functions), CFD007 (unnecessary .to_dict())
- **Imports:** CFD008 (explicit imports), CFD011 (missing imports)
- **References:** CFD010 (Ref string → ref(Class))
- **Organization:** CFD012 (file splitting)

---

## Identified Overlaps and Shared Concerns

### 1. Name Conversion and Sanitization

**Importer:**
- `to_snake_case()` in parser.py (lines 48-67)
- `sanitize_python_name()` in parser.py (lines 70-126)
- Converts CloudFormation property names to Python identifiers
- Handles Python keywords, acronyms (VPCId → vpc_id)

**Linter:**
- Uses `to_snake_case()` from parser module (indirect import)
- `linter/split.py` line 180: imports from `cloudformation_dataclasses.importer.parser`
- Rules need to convert between PascalCase and snake_case for pattern matching

**Overlap:** Both systems perform identical name transformations. The linter currently imports from the importer for this functionality.

**Opportunity:** Extract to shared utility module (`core/naming.py`) to avoid circular dependency and improve modularity.

### 2. Enum Detection and Mapping

**Importer:**
- `KNOWN_ENUMS` dictionary in `codegen/helpers.py` (maps module + class + value → constant)
- `try_convert_to_enum()` in `values.py` (converts string values to enum references)
- `extract_enum_from_type_hint()` in `helpers.py` (extracts enum class from type hints)

**Linter:**
- `KNOWN_ENUMS` in `rules.py` (CFD004) - **DUPLICATE DATA**
- Pattern matching on snake_case field names and dict keys
- Runtime introspection via `introspection.py`

**Overlap:**
- Both maintain enum mappings for S3, DynamoDB, Lambda, EC2
- Both need to identify when a string value should be an enum constant
- **Critical Duplication:** The KNOWN_ENUMS data is maintained in two places

**Opportunity:** Consolidate enum metadata in `constants.py` and share between both systems.

### 3. PropertyType Resolution

**Importer:**
- `resolve_property_type()` in `codegen/helpers.py`
- Uses `constants.get_property_type_info()` to find PropertyType classes
- Matches CloudFormation keys to PropertyType classes
- `find_property_type_for_cf_keys()` in constants

**Linter:**
- `KNOWN_PROPERTY_TYPES` in `rules.py` (CFD005) - partial duplication
- Runtime introspection in `introspection.py` using `PropertyType` base class
- `get_property_type_for_field()` for runtime type checking

**Overlap:**
- Both systems identify when a dict should be a PropertyType
- Both need PropertyType field mappings (cf_name → python_name)
- Importer uses static analysis, linter uses runtime introspection

**Opportunity:**
- Enhance constants.py with more comprehensive PropertyType metadata
- Linter could use static analysis from importer instead of runtime introspection
- Share field mapping logic

### 4. Import Management

**Importer:**
- `CodegenContext.imports` tracks needed imports
- `generate_imports()` in `imports.py` creates import statements
- Detects name collisions across AWS modules
- Groups imports by module for cleaner output

**Linter:**
- `_add_imports()` in `linter/__init__.py` (lines 252-335)
- Inserts imports after existing imports
- Filters out duplicates
- Groups imports by module

**Overlap:**
- Both parse AST to find existing imports
- Both group imports by module
- Both handle import deduplication
- **Similar logic, different implementations**

**Opportunity:** Extract shared import utilities (`core/imports.py`) with functions like:
- `find_last_import_line(ast.Module) → int`
- `parse_existing_imports(ast.Module) → set[str]`
- `group_imports_by_module(set[str]) → dict[str, list[str]]`
- `format_import_block(dict) → str`

### 5. CloudFormation Constants

**Shared Resource:**
- Both use `constants.py` for:
  - `CONDITION_OPERATOR_MAP`
  - `PARAMETER_TYPE_MAP`
  - `PSEUDO_PARAMETER_MAP`
  - `resolve_resource_type()`
  - `get_property_type_info()`

**Current State:** This is the primary shared infrastructure between the systems.

**Opportunity:** Expand constants.py to include:
- Comprehensive enum mappings (consolidate from both systems)
- PropertyType constructor mappings
- Common intrinsic function patterns

### 6. Python AST Manipulation

**Importer:**
- Generates AST-like structures programmatically
- Uses string templates for class generation
- Indentation management via `indent_str = "    " * indent`

**Linter:**
- Parses existing code to AST
- Walks AST to find patterns
- Applies fixes by string replacement

**Overlap:**
- Both work with Python syntax
- Both need to understand class structure, decorators, field assignments

**Opportunity:**
- Share AST utilities for common patterns:
  - `is_cloudformation_dataclass(ast.ClassDef) → bool`
  - `extract_resource_type(ast.ClassDef) → tuple[str, str]`
  - `find_decorator(ast.ClassDef, str) → ast.expr | None`

### 7. Reference Detection

**Importer:**
- `_analyze_references()` in parser.py
- Builds reference graph from Ref, GetAtt, Sub intrinsics
- Pattern matching in Sub() to detect resource references

**Linter:**
- `_find_dependencies()` in `split.py` (line 176)
- Detects ref() and get_att() calls in AST
- CFD010 rule suggests converting Ref("Name") → ref(Class)

**Overlap:**
- Both analyze dependencies between resources
- Both understand ref/get_att semantics

**Opportunity:** Share reference analysis utilities, especially Sub() pattern matching logic.

### 8. Code Style Patterns

**Importer Generates:**
- `from .. import *` in stack files
- Annotation-based refs: `bucket: Ref[Bucket] = ref()`
- PropertyType wrapper classes
- Qualified imports for name collisions

**Linter Enforces:**
- CFD008: Use `from .. import *` in stack files
- CFD010: Use `ref(Class)` not `Ref("string")`
- CFD005/CFD009: Use PropertyType wrappers
- CFD011: Ensure required imports present

**Observation:** The linter enforces the patterns that the importer generates. This is by design, but shows tight coupling.

**Opportunity:** Document the "canonical style" that both systems target, making it explicit rather than implicit.

---

## Concrete Proposals for Unification

### Proposal 1: Extract Shared Utilities to `core/` (Low-Hanging Fruit)

**What:** Create new modules in `core/` for common functionality:

```python
# core/naming.py
def to_snake_case(name: str) -> str: ...
def to_pascal_case(name: str) -> str: ...
def sanitize_python_name(name: str) -> str: ...
def is_valid_python_identifier(name: str) -> bool: ...

# core/ast_helpers.py
def is_cloudformation_dataclass(node: ast.ClassDef) -> bool: ...
def extract_resource_type(node: ast.ClassDef) -> tuple[str, str] | None: ...
def find_decorator(node: ast.ClassDef, name: str) -> ast.expr | None: ...
def find_last_import_line(tree: ast.Module) -> int: ...
def parse_existing_imports(tree: ast.Module) -> dict[str, set[str]]: ...

# core/import_manager.py
class ImportManager:
    def add_import(self, module: str, name: str) -> None: ...
    def get_import_block(self) -> str: ...
    def merge_with_existing(self, tree: ast.Module) -> str: ...
```

**Impact:**
- Eliminates duplication
- Reduces coupling between importer and linter
- Makes utilities testable independently
- Both systems can evolve without breaking the other

**Migration Effort:** LOW (2-4 hours)
- Move functions to new modules
- Update imports in importer and linter
- No behavioral changes

**Benefits:**
- Improved modularity
- Single source of truth for name conversions
- Easier to test
- Reduces risk of divergence

**Tradeoffs:**
- Adds another module layer
- Requires coordination between systems

---

### Proposal 2: Consolidate Enum and PropertyType Metadata (Medium Impact)

**What:** Enhance `constants.py` to be the single source of truth for all CloudFormation metadata:

```python
# constants.py - expanded

# Comprehensive enum metadata (consolidate from both systems)
ENUM_METADATA: dict[tuple[str, str], dict[str, str]] = {
    # (module, enum_class) -> {cf_value: const_name}
    ("s3", "ServerSideEncryption"): {
        "AES256": "AES256",
        "aws:kms": "AWS_KMS",
        "aws:kms:dsse": "AWS_KMS_DSSE",
    },
    ("dynamodb", "KeyType"): {
        "HASH": "HASH",
        "RANGE": "RANGE",
    },
    # ... all enums from both importer and linter
}

# Field name -> enum lookup
FIELD_TO_ENUM: dict[str, tuple[str, str]] = {
    # python_field_name -> (module, enum_class)
    "sse_algorithm": ("s3", "ServerSideEncryption"),
    "key_type": ("dynamodb", "KeyType"),
    # ...
}

# CloudFormation property name -> enum lookup
CF_PROPERTY_TO_ENUM: dict[str, tuple[str, str]] = {
    # CF_PropertyName -> (module, enum_class)
    "SSEAlgorithm": ("s3", "ServerSideEncryption"),
    "KeyType": ("dynamodb", "KeyType"),
    # ...
}

# Helper functions
def find_enum_for_value(value: str, field_name: str = None, cf_name: str = None) -> tuple[str, str, str] | None:
    """Find enum (module, class, const_name) for a string value."""
    ...

def get_enum_constant_name(module: str, enum_class: str, value: str) -> str | None:
    """Get the constant name for an enum value."""
    ...
```

**Importer Changes:**
- Remove `KNOWN_ENUMS` from `codegen/helpers.py`
- Use `constants.find_enum_for_value()` in `try_convert_to_enum()`
- Simplify enum detection logic

**Linter Changes:**
- Remove `KNOWN_ENUMS` from `rules.py`
- Use `constants.find_enum_for_value()` in CFD004 rule
- Keep runtime introspection as fallback for user-defined enums

**Impact:**
- Eliminates duplicate enum data (currently ~200 lines duplicated)
- Easier to add new enums (one place instead of two)
- Linter can detect more enums automatically
- Importer generates better code

**Migration Effort:** MEDIUM (1-2 days)
- Build comprehensive enum metadata
- Update both systems to use new constants
- Add tests for enum resolution
- Verify backward compatibility

**Benefits:**
- Single source of truth
- No divergence risk
- Easier maintenance
- Better coverage

**Tradeoffs:**
- constants.py becomes larger (but more organized)
- Requires one-time migration of all enum data
- Need to keep metadata in sync with AWS CloudFormation spec updates

---

### Proposal 3: Linter-Aware Code Generation (Medium-High Impact)

**What:** Make the importer generate code that already passes all linter rules, eliminating the need for post-generation linting.

**Current State:**
```python
# In package.py:
files = _generate_stack_package(...)
if lint:
    files = _lint_generated_files(files)  # Post-processing
```

**Proposed State:**
```python
# In package.py:
ctx = CodegenContext(lint_aware=True)  # Linting integrated
files = _generate_stack_package(pkg_ctx, template)
# No post-processing needed - code is already compliant
```

**Implementation:**
1. **Generate compliant imports from the start:**
   - Always emit `from .. import *` in stack files
   - Always emit `from . import *` in params.py
   - Context tracks required imports, emits them correctly

2. **Generate annotation-based refs directly:**
   - `ref(ClassName)` when target is defined before
   - `ref("ClassName")` for forward references (same file)
   - Annotation-based refs for top-level properties

3. **Use enum constants during value generation:**
   - `try_convert_to_enum()` already does this
   - Extend to cover all cases linter checks

4. **Generate PropertyType wrappers by default:**
   - Block mode already does this
   - Ensure consistency with linter expectations

**Impact:**
- Faster code generation (no post-processing step)
- Generated code is cleaner and more consistent
- Linter becomes validation-only for generated code
- Reduces complexity in package.py

**Migration Effort:** MEDIUM-HIGH (2-3 days)
- Audit all linter rules to see which apply to generated code
- Update code generation to satisfy rules
- Add tests to verify generated code passes linter
- Make post-processing optional (for backward compatibility)

**Benefits:**
- Cleaner architecture (generate right the first time)
- Faster import workflow
- Generated code serves as canonical examples
- Linter focuses on user-written code

**Tradeoffs:**
- Code generation becomes more complex
- Tight coupling between generation rules and linter rules
- Need to update generator when linter rules change

---

### Proposal 4: Shared Reference Analysis (High Impact)

**What:** Create a unified reference analysis system used by both importer and linter:

```python
# core/reference_analysis.py

@dataclass
class ResourceReference:
    """A reference from one resource to another."""
    source: str  # Source resource logical ID
    target: str  # Target resource/parameter logical ID
    reference_type: Literal["ref", "get_att", "sub_pattern"]
    attribute: str | None  # For get_att
    location: tuple[int, int] | None  # Line, column in source

class ReferenceAnalyzer:
    """Analyze resource dependencies from IR or AST."""

    def analyze_from_ir(self, template: IRTemplate) -> dict[str, list[ResourceReference]]:
        """Analyze references from IR (importer use case)."""
        ...

    def analyze_from_ast(self, tree: ast.Module) -> dict[str, list[ResourceReference]]:
        """Analyze references from AST (linter use case)."""
        ...

    def build_dependency_graph(self, refs: dict) -> dict[str, set[str]]:
        """Build simplified dependency graph."""
        ...

    def find_cycles(self, graph: dict) -> list[list[str]]:
        """Find strongly connected components (cycles)."""
        ...

    def topological_sort(self, graph: dict) -> list[str]:
        """Sort resources by dependency order."""
        ...
```

**Importer Changes:**
- Use `ReferenceAnalyzer.analyze_from_ir()` in place of `_analyze_references()`
- Use shared topological sort
- Use shared SCC detection

**Linter Changes:**
- Use `ReferenceAnalyzer.analyze_from_ast()` in split.py
- Use shared dependency graph building
- CFD010 rule uses reference analysis to suggest fixes

**Impact:**
- Consistent reference detection across systems
- Improved accuracy (one implementation to maintain)
- Better cycle detection
- Enables new features (e.g., detect missing dependencies)

**Migration Effort:** HIGH (3-5 days)
- Design unified reference model
- Implement IR and AST analyzers
- Migrate importer to use new analyzer
- Migrate linter to use new analyzer
- Extensive testing for correctness

**Benefits:**
- Single source of truth for dependency logic
- Enables advanced dependency analysis
- Better error messages
- Foundation for future tooling (dependency visualizer, etc.)

**Tradeoffs:**
- Large architectural change
- Risk of introducing bugs
- Need to handle edge cases from both systems
- Performance considerations (AST analysis can be slow)

---

### Proposal 5: Unified Code Style Specification (Documentation)

**What:** Create a formal specification document that defines the canonical code style both systems target.

**Document Structure:**
```markdown
# CloudFormation Dataclasses Code Style Guide

## 1. Wrapper Class Pattern
## 2. Resource References (ref/get_att)
## 3. PropertyType Wrappers
## 4. Import Patterns
## 5. Enum Usage
## 6. File Organization
## 7. Naming Conventions
## 8. Forward References
```

**Integration:**
- Importer generates code following the spec
- Linter enforces the spec
- Users can reference the spec for manual coding
- CI can validate compliance

**Impact:**
- Makes implicit knowledge explicit
- Easier onboarding for contributors
- Clearer expectations for users
- Foundation for future style evolution

**Migration Effort:** LOW (4-8 hours)
- Document existing patterns
- Add examples
- Link from README and documentation

**Benefits:**
- Improved documentation
- Alignment between systems
- User guidance
- Reduces style debates

**Tradeoffs:**
- Maintenance burden (keep spec updated)
- May constrain future changes

---

## Benefits and Tradeoffs Analysis

### Overall Benefits of Unification

1. **Reduced Code Duplication**
   - Eliminate 200+ lines of duplicated enum/PropertyType data
   - Share name conversion logic
   - Share import management

2. **Improved Consistency**
   - Same enum mappings across systems
   - Same naming conventions
   - Same reference analysis

3. **Easier Maintenance**
   - Update shared code once, both systems benefit
   - Fewer places to fix bugs
   - Centralized metadata

4. **Better Quality**
   - Importer generates linter-compliant code from the start
   - Shared utilities are better tested
   - Fewer edge cases

5. **Future Extensibility**
   - Shared infrastructure enables new tools
   - Dependency visualizer could use reference analyzer
   - Style formatter could use shared AST utilities

### Overall Tradeoffs

1. **Increased Coupling**
   - Systems become more interdependent
   - Changes to shared code affect both
   - Need coordination for breaking changes

2. **Migration Risk**
   - Refactoring introduces bugs
   - Need comprehensive testing
   - Backward compatibility concerns

3. **Complexity Trade-off**
   - Adds new abstraction layers
   - More modules to understand
   - Higher cognitive load for contributors

4. **Performance Considerations**
   - Shared code may be less optimized for specific use cases
   - Runtime introspection (linter) vs static analysis (importer) have different performance profiles

5. **Testing Burden**
   - Shared code needs testing for both use cases
   - Integration tests become more important
   - More test fixtures needed

---

## Migration Path

If proceeding with unification, recommended phased approach:

### Phase 1: Extract Utilities (Low Risk)
**Timeline:** 1 week
**Proposals:** #1 (Shared Utilities)

1. Create `core/naming.py` and `core/ast_helpers.py`
2. Move existing functions from importer and linter
3. Update imports in both systems
4. Add unit tests for shared utilities
5. Verify integration tests pass

**Success Criteria:** No behavioral changes, all tests pass

### Phase 2: Consolidate Metadata (Medium Risk)
**Timeline:** 1-2 weeks
**Proposals:** #2 (Enum/PropertyType Metadata), #5 (Style Spec)

1. Audit all enum and PropertyType data in both systems
2. Build comprehensive metadata in constants.py
3. Write migration scripts to update both systems
4. Add tests for metadata lookup functions
5. Update both systems to use new constants
6. Document canonical code style

**Success Criteria:** Both systems use shared metadata, generated code unchanged

### Phase 3: Optimize Generation (Medium-High Risk)
**Timeline:** 2-3 weeks
**Proposals:** #3 (Linter-Aware Generation)

1. Analyze which linter rules apply to generated code
2. Update code generation to satisfy rules natively
3. Make post-processing optional (feature flag)
4. Add tests to verify generated code passes linter
5. Migrate existing templates to verify compatibility

**Success Criteria:** Generated code passes linter without post-processing

### Phase 4: Unified Reference Analysis (High Risk - Optional)
**Timeline:** 3-5 weeks
**Proposals:** #4 (Reference Analysis)

1. Design unified reference model
2. Implement reference analyzer with IR and AST frontends
3. Migrate importer to use new analyzer
4. Migrate linter to use new analyzer
5. Extensive testing and validation
6. Performance benchmarking

**Success Criteria:** Both systems use shared reference analysis, no regressions

---

## Recommendations

### High Priority (Do First)

1. **Proposal #1: Extract Shared Utilities**
   - Low risk, high value
   - Eliminates immediate duplication
   - Improves modularity
   - Foundation for other proposals

2. **Proposal #2: Consolidate Metadata**
   - Addresses critical duplication
   - Improves maintainability
   - Relatively low risk if done carefully

3. **Proposal #5: Style Specification**
   - Low effort, high value
   - Makes implicit knowledge explicit
   - Helps users and contributors

### Medium Priority (Consider)

4. **Proposal #3: Linter-Aware Generation**
   - Good architectural improvement
   - Reduces complexity
   - Requires careful coordination

### Low Priority (Optional)

5. **Proposal #4: Unified Reference Analysis**
   - Significant effort
   - Unclear immediate benefit
   - Consider if building more dependency-aware tools

### Do NOT Recommend

- **Merging the systems entirely**: They have distinct purposes and user-facing APIs
- **Forcing uniform implementation**: Different performance characteristics (static vs runtime analysis) are appropriate
- **Over-abstracting**: Keep shared code focused on concrete, reusable utilities

---

## Conclusion

The linter and importer systems have significant opportunities for sharing infrastructure while maintaining their distinct purposes. The highest-value opportunities are:

1. **Shared utilities** for naming, AST manipulation, and import management
2. **Consolidated metadata** for enums and PropertyTypes
3. **Linter-aware code generation** to eliminate post-processing

These changes would reduce duplication, improve consistency, and make both systems easier to maintain. A phased migration approach minimizes risk while delivering incremental value.

The systems should remain architecturally distinct (importer = YAML→Python, linter = Python→Python), but share the foundational utilities and metadata that both need. This achieves the benefits of unification without the risks of over-coupling.

---

## Appendix: Code Volume Analysis

### Current Code Distribution

**Importer:**
- Parser: ~900 lines
- IR: ~350 lines
- Codegen (all): ~2,400 lines
  - package.py: ~940 lines
  - blocks.py: ~445 lines
  - values.py: ~640 lines
  - classes.py: ~300 lines
  - helpers.py: ~200 lines
- **Total: ~3,650 lines**

**Linter:**
- Core: ~340 lines
- Rules: ~1,130 lines
- Introspection: ~250 lines
- Split: ~335 lines
- **Total: ~2,055 lines**

**Shared Infrastructure (constants.py):**
- ~1,500 lines (already shared)

**Duplication Estimate:**
- Enum data: ~200 lines
- PropertyType patterns: ~100 lines
- Name conversion: ~80 lines
- Import management: ~150 lines
- AST utilities: ~100 lines
- **Total duplication: ~630 lines (11% of combined codebase)**

### Projected Savings from Proposals

**Proposal #1 (Shared Utilities):**
- Remove ~230 duplicate lines
- Add ~150 lines in core/

**Proposal #2 (Consolidated Metadata):**
- Remove ~300 duplicate lines
- Add ~200 lines in constants.py

**Proposal #3 (Linter-Aware Generation):**
- Remove ~150 lines from package.py (post-processing)
- Add ~100 lines in codegen (smarter generation)

**Total Impact:**
- Remove ~680 duplicate/unnecessary lines
- Add ~450 lines of shared infrastructure
- **Net reduction: ~230 lines (~4%)**
- **Maintainability improvement: Much larger (single source of truth)**
