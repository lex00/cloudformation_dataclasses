# CloudFormation Template Importer

## Overview

A tool to convert existing CloudFormation templates (YAML/JSON) into Python code using `cloudformation_dataclasses`.

**Status**: Planning (not yet implemented)

---

## Dependencies & Prerequisites

### Python Version
- Python 3.10+ (matches main package requirement)

### Required Dependencies

```toml
[project.optional-dependencies]
importer = [
    "pyyaml>=6.0",           # YAML parsing with tag support
]
importer-live = [
    "pyyaml>=6.0",
    "boto3>=1.26",           # AWS API access
]
```

### Development Setup

```bash
# Clone and install with importer dependencies
git clone https://github.com/lex00/cloudformation_dataclasses
cd cloudformation_dataclasses
uv pip install -e ".[importer,dev]"

# Or for live import development
uv pip install -e ".[importer-live,dev]"
```

### Runtime Requirements

- **File import**: No AWS credentials needed
- **Live import**: Valid AWS credentials with CloudFormation read permissions:
  - `cloudformation:GetTemplate`
  - `cloudformation:DescribeStacks`
  - `cloudformation:ListStackResources`
  - `s3:GetObject` (for nested stack templates in S3)

---

## Package Placement

The importer will be part of this package as an optional extra:

```bash
pip install cloudformation-dataclasses              # Runtime only
pip install cloudformation-dataclasses[codegen]     # + spec generator
pip install cloudformation-dataclasses[importer]    # + template importer
pip install cloudformation-dataclasses[dev]         # all tools
```

### Rationale

- **Single package**: Unified versioning and maintenance
- **Optional dependencies**: Runtime stays lean (zero dependencies)
- **Shared internals**: Importer uses same property mappings, naming conventions
- **Parallel tools**: `codegen/` and `importer/` are conceptually similar
  - `codegen/` = CloudFormation Spec → Python classes
  - `importer/` = CloudFormation Template → Python wrapper code

---

## Package Structure

```
src/cloudformation_dataclasses/
├── core/                   # Runtime (always installed)
├── intrinsics/             # Runtime (always installed)
├── aws/                    # Runtime (pre-generated)
├── codegen/                # Optional [codegen] extra
│   ├── generator.py
│   ├── spec_parser.py
│   └── botocore_enums.py
└── importer/               # Optional [importer] extra
    ├── __init__.py
    ├── parser.py           # YAML/JSON → intermediate representation
    ├── intrinsics.py       # Intrinsic function parsing
    ├── resolver.py         # Property type resolution
    ├── codegen.py          # IR → Python code generation
    └── cli.py              # cfn-import command
```

### pyproject.toml

```toml
[project.optional-dependencies]
codegen = ["botocore"]
importer = ["pyyaml"]
dev = ["botocore", "pyyaml", "pytest", "ruff"]

[project.scripts]
cfn-generate = "cloudformation_dataclasses.codegen.cli:main"
cfn-import = "cloudformation_dataclasses.importer.cli:main"
```

---

## Output Modes

The importer supports three output modes to match different coding preferences:

### Block Mode (`--mode block`)

Maximize declarative wrapper classes. Every construct becomes a separate `@cloudformation_dataclass`:

```python
# Input CloudFormation:
# Resources:
#   MyBucket:
#     Type: AWS::S3::Bucket
#     Properties:
#       BucketName: my-bucket
#       Tags:
#         - Key: Environment
#           Value: Production

# Block Mode Output:
@cloudformation_dataclass
class EnvironmentTag:
    resource: Tag
    key = "Environment"
    value = "Production"

@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    bucket_name = "my-bucket"
    tags = [EnvironmentTag]
```

**Characteristics:**
- Every tag, nested property type, and parameter becomes a class
- Maximum reusability - classes can be imported/composed
- Verbose but highly readable and self-documenting
- Best for: large templates, team collaboration, reusable components

---

### Brief Mode (`--mode brief`)

Maximize imperative output. Direct instantiation, minimal class definitions:

```python
# Brief Mode Output:
my_bucket = Bucket(
    logical_id="MyBucket",
    bucket_name="my-bucket",
    tags=[Tag(key="Environment", value="Production")],
)

template = Template(
    resources=[my_bucket],
)
```

**Characteristics:**
- No wrapper classes - direct object construction
- Compact, script-like feel
- Resources stored in variables, referenced by variable name
- Best for: quick conversions, small templates, prototyping

---

### Mixed Mode (`--mode mixed`)

Balanced approach. Resources as wrappers, inline simple constructs:

```python
# Mixed Mode Output:
@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    bucket_name = "my-bucket"
    tags = [Tag(key="Environment", value="Production")]  # inline

@cloudformation_dataclass
class MyBucketPolicy:
    resource: BucketPolicy
    bucket = ref(MyBucket)
    policy_document = PolicyDocument(  # inline nested structure
        statement=[
            PolicyStatement(
                effect="Allow",
                principal="*",
                action="s3:GetObject",
                resource_arn=Sub("${MyBucket.Arn}/*"),
            )
        ]
    )
```

**Heuristics for mixed mode:**

| Construct | Block (wrapper class) | Inline (imperative) |
|-----------|----------------------|---------------------|
| Resources | Always | Never |
| Parameters | Always | Never |
| Outputs | Always | Never |
| Tags | If reused ≥2 times | If used once |
| Policy statements | If complex/reused | If simple, single use |
| Nested property types | If >3 fields | If ≤3 fields |
| Ingress/Egress rules | If >2 rules | If ≤2 simple rules |

---

## Implementation Approach

### Option 1: Full Code Generator (Recommended)

Generate complete Python modules with proper imports, type hints, and structure.

**Components:**

1. **Parser** (`parser.py`)
   - Load YAML/JSON templates
   - Build intermediate representation (IR)
   - Handle CloudFormation intrinsic functions

2. **Intrinsic Parser** (`intrinsics.py`)
   - Convert `!Ref`, `!GetAtt`, `!Sub` → Python objects
   - Handle both short form (`!Ref Foo`) and long form (`Fn::Ref: Foo`)
   - Support nested intrinsics

3. **Property Resolver** (`resolver.py`)
   - Map CloudFormation property names to Python snake_case
   - Resolve nested property types using CloudFormation spec
   - Determine appropriate Python types

4. **Code Generator** (`codegen.py`)
   - Generate Python source code from IR
   - Apply output mode (block/brief/mixed)
   - Handle imports, ordering, and formatting

5. **CLI** (`cli.py`)
   - Entry point: `cfn-import template.yaml --mode mixed -o output.py`
   - Support stdin/stdout for piping

### Key Challenges

1. **Intrinsic function parsing**: Multiple syntaxes (YAML tags, Fn:: prefix)
2. **Property name mapping**: PascalCase → snake_case with edge cases
3. **Nested type resolution**: Match property types to generated classes
4. **Cross-references**: Track `!Ref` and `!GetAtt` to generate proper `ref()` calls
5. **Reuse detection**: For mixed mode, count usage to decide block vs inline

---

## Intermediate Representation (IR)

The IR is the parsed template structure before code generation. Defined in `importer/ir.py`:

```python
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional


class IntrinsicType(Enum):
    """CloudFormation intrinsic function types."""
    REF = "Ref"
    GET_ATT = "GetAtt"
    SUB = "Sub"
    JOIN = "Join"
    SELECT = "Select"
    GET_AZS = "GetAZs"
    IF = "If"
    EQUALS = "Equals"
    AND = "And"
    OR = "Or"
    NOT = "Not"
    CONDITION = "Condition"
    FIND_IN_MAP = "FindInMap"
    BASE64 = "Base64"
    CIDR = "Cidr"
    IMPORT_VALUE = "ImportValue"
    SPLIT = "Split"
    TRANSFORM = "Transform"


@dataclass
class IRIntrinsic:
    """Parsed intrinsic function."""
    type: IntrinsicType
    args: Any  # Type varies by intrinsic
    # For Ref: str (logical_id)
    # For GetAtt: tuple[str, str] (logical_id, attribute)
    # For Sub: tuple[str, dict[str, Any]] (template, variables)
    # For Join: tuple[str, list[Any]] (delimiter, values)
    # etc.


@dataclass
class IRProperty:
    """A single property value (may contain intrinsics)."""
    cf_name: str           # Original CloudFormation name (PascalCase)
    python_name: str       # Converted name (snake_case)
    value: Any             # Literal, IRIntrinsic, or nested IRProperty
    is_intrinsic: bool = False


@dataclass
class IRParameter:
    """Parsed CloudFormation parameter."""
    logical_id: str
    type: str
    description: Optional[str] = None
    default: Optional[Any] = None
    allowed_values: Optional[list[Any]] = None
    allowed_pattern: Optional[str] = None
    min_length: Optional[int] = None
    max_length: Optional[int] = None
    min_value: Optional[int] = None
    max_value: Optional[int] = None
    constraint_description: Optional[str] = None
    no_echo: bool = False


@dataclass
class IRResource:
    """Parsed CloudFormation resource."""
    logical_id: str
    resource_type: str     # e.g., "AWS::S3::Bucket"
    service: str           # e.g., "S3"
    type_name: str         # e.g., "Bucket"
    properties: dict[str, IRProperty] = field(default_factory=dict)
    depends_on: list[str] = field(default_factory=list)
    condition: Optional[str] = None
    deletion_policy: Optional[str] = None
    update_replace_policy: Optional[str] = None
    metadata: Optional[dict[str, Any]] = None
    # Tracking for code generation
    referenced_by: list[str] = field(default_factory=list)  # Resources that !Ref this


@dataclass
class IROutput:
    """Parsed CloudFormation output."""
    logical_id: str
    value: Any             # Literal or IRIntrinsic
    description: Optional[str] = None
    export_name: Optional[Any] = None  # Can be intrinsic
    condition: Optional[str] = None


@dataclass
class IRMapping:
    """Parsed CloudFormation mapping."""
    logical_id: str
    map_data: dict[str, dict[str, Any]]


@dataclass
class IRCondition:
    """Parsed CloudFormation condition."""
    logical_id: str
    expression: Any  # IRIntrinsic (Fn::Equals, Fn::And, etc.)


@dataclass
class IRTemplate:
    """Complete parsed template - the main IR structure."""
    description: Optional[str] = None
    aws_template_format_version: str = "2010-09-09"

    parameters: dict[str, IRParameter] = field(default_factory=dict)
    mappings: dict[str, IRMapping] = field(default_factory=dict)
    conditions: dict[str, IRCondition] = field(default_factory=dict)
    resources: dict[str, IRResource] = field(default_factory=dict)
    outputs: dict[str, IROutput] = field(default_factory=dict)

    # Metadata for code generation
    source_file: Optional[str] = None
    nested_stacks: dict[str, "IRTemplate"] = field(default_factory=dict)

    # Analysis results (populated by resolver)
    reference_graph: dict[str, list[str]] = field(default_factory=dict)  # logical_id -> [referenced_ids]
    reuse_counts: dict[str, int] = field(default_factory=dict)  # For mixed mode decisions
```

### IR Flow

```
CloudFormation YAML/JSON
        ↓
    parser.py (parse_template)
        ↓
    IRTemplate (raw parse)
        ↓
    intrinsics.py (resolve_intrinsics)
        ↓
    IRTemplate (intrinsics resolved)
        ↓
    resolver.py (analyze_references, count_reuse)
        ↓
    IRTemplate (fully analyzed)
        ↓
    codegen.py (generate_code)
        ↓
    Python source code
```

---

## Algorithm Details

### Intrinsic Function Detection (`intrinsics.py`)

CloudFormation intrinsics have two syntaxes:

```yaml
# Short form (YAML tags)
BucketName: !Ref BucketParam
Arn: !GetAtt MyBucket.Arn

# Long form (Fn:: prefix)
BucketName:
  Fn::Ref: BucketParam
Arn:
  Fn::GetAtt:
    - MyBucket
    - Arn
```

**Detection Algorithm:**

```python
def parse_value(value: Any) -> Any:
    """Recursively parse a value, detecting intrinsics."""

    # Long form: dict with single Fn:: or Ref key
    if isinstance(value, dict) and len(value) == 1:
        key = next(iter(value))
        if key == "Ref":
            return IRIntrinsic(IntrinsicType.REF, value[key])
        if key.startswith("Fn::"):
            intrinsic_name = key[4:]  # Remove "Fn::" prefix
            return parse_intrinsic(intrinsic_name, value[key])

    # YAML tags are converted by PyYAML custom constructors
    # (registered during YAML loading)

    # Recurse into dicts and lists
    if isinstance(value, dict):
        return {k: parse_value(v) for k, v in value.items()}
    if isinstance(value, list):
        return [parse_value(item) for item in value]

    return value
```

**PyYAML Custom Constructors:**

```python
import yaml

def ref_constructor(loader, node):
    """Handle !Ref tag."""
    value = loader.construct_scalar(node)
    return IRIntrinsic(IntrinsicType.REF, value)

def getatt_constructor(loader, node):
    """Handle !GetAtt tag (scalar or sequence)."""
    if isinstance(node, yaml.ScalarNode):
        # !GetAtt MyBucket.Arn
        parts = loader.construct_scalar(node).split(".", 1)
        return IRIntrinsic(IntrinsicType.GET_ATT, tuple(parts))
    else:
        # !GetAtt [MyBucket, Arn]
        parts = loader.construct_sequence(node)
        return IRIntrinsic(IntrinsicType.GET_ATT, tuple(parts))

# Register all constructors
yaml.SafeLoader.add_constructor("!Ref", ref_constructor)
yaml.SafeLoader.add_constructor("!GetAtt", getatt_constructor)
yaml.SafeLoader.add_constructor("!Sub", sub_constructor)
# ... etc for all intrinsics
```

### Property Name Mapping (`resolver.py`)

Uses same algorithm as `codegen/generator.py`:

```python
import re

def to_snake_case(name: str) -> str:
    """Convert PascalCase to snake_case."""
    # BucketName -> bucket_name
    # VPCId -> vpc_id
    # IPv6CidrBlock -> ipv6_cidr_block
    result = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    result = re.sub("([a-z0-9])([A-Z])", r"\1_\2", result)
    return result.lower()

def sanitize_python_name(name: str) -> str:
    """Handle Python keyword conflicts."""
    PYTHON_KEYWORDS = {"type", "class", "import", "from", ...}
    if name in PYTHON_KEYWORDS:
        return f"{name}_"
    return name
```

### Reference Analysis (`resolver.py`)

Build a graph of resource references for ordering and mode decisions:

```python
def analyze_references(template: IRTemplate) -> None:
    """Populate reference_graph and referenced_by fields."""

    def find_refs(value: Any, source_id: str) -> None:
        """Recursively find all Ref/GetAtt in a value."""
        if isinstance(value, IRIntrinsic):
            if value.type == IntrinsicType.REF:
                target_id = value.args
                template.reference_graph.setdefault(source_id, []).append(target_id)
                if target_id in template.resources:
                    template.resources[target_id].referenced_by.append(source_id)
            elif value.type == IntrinsicType.GET_ATT:
                target_id = value.args[0]
                template.reference_graph.setdefault(source_id, []).append(target_id)
                if target_id in template.resources:
                    template.resources[target_id].referenced_by.append(source_id)
        elif isinstance(value, dict):
            for v in value.values():
                find_refs(v, source_id)
        elif isinstance(value, list):
            for item in value:
                find_refs(item, source_id)

    for resource_id, resource in template.resources.items():
        for prop in resource.properties.values():
            find_refs(prop.value, resource_id)
```

### Reuse Detection for Mixed Mode (`resolver.py`)

Count how many times each construct is used to decide block vs inline:

```python
def count_reuse(template: IRTemplate) -> None:
    """Count usage of tags, property types, etc. for mixed mode."""

    # Count identical tags
    tag_signatures: dict[str, int] = {}
    for resource in template.resources.values():
        if "tags" in resource.properties:
            for tag in resource.properties["tags"].value:
                sig = f"{tag.get('Key')}:{tag.get('Value')}"
                tag_signatures[sig] = tag_signatures.get(sig, 0) + 1

    template.reuse_counts["tags"] = tag_signatures

    # Count identical policy statements, ingress rules, etc.
    # ...
```

### Code Generation Order (`codegen.py`)

Generate classes in dependency order:

```python
def topological_sort(template: IRTemplate) -> list[str]:
    """Sort resources so dependencies come first."""
    visited = set()
    result = []

    def visit(resource_id: str):
        if resource_id in visited:
            return
        visited.add(resource_id)

        # Visit dependencies first
        for dep_id in template.reference_graph.get(resource_id, []):
            if dep_id in template.resources:
                visit(dep_id)

        result.append(resource_id)

    for resource_id in template.resources:
        visit(resource_id)

    return result
```

### Mixed Mode Decision Algorithm

```python
def should_inline(construct_type: str, value: Any, template: IRTemplate) -> bool:
    """Decide if a construct should be inlined (imperative) or wrapped (block)."""

    # Resources, parameters, outputs are always wrapped
    if construct_type in ("resource", "parameter", "output"):
        return False

    # Tags: inline if used once, wrap if reused
    if construct_type == "tag":
        sig = f"{value.get('Key')}:{value.get('Value')}"
        return template.reuse_counts["tags"].get(sig, 1) < 2

    # Property types: inline if ≤3 fields
    if construct_type == "property_type":
        return len(value) <= 3

    # Policy statements: inline if simple
    if construct_type == "policy_statement":
        return (
            value.get("Condition") is None and
            not isinstance(value.get("Action"), list) or len(value.get("Action", [])) <= 2
        )

    return True  # Default to inline
```

---

## CLI Usage

```bash
# Basic usage
cfn-import template.yaml -o my_stack.py

# Specify output mode
cfn-import template.yaml --mode block -o my_stack.py  # default
cfn-import template.yaml --mode brief -o my_stack.py
cfn-import template.yaml --mode mixed -o my_stack.py

# Read from stdin, write to stdout
cat template.yaml | cfn-import - --mode brief

# JSON input
cfn-import template.json -o my_stack.py
```

### Full CLI Options

```
cfn-import [OPTIONS] INPUT

Arguments:
  INPUT                      Template file path, or "-" for stdin
                            For live import: omit INPUT and use --stack-name

Options:
  -o, --output PATH          Output file path (default: stdout)
  -m, --mode MODE            Output mode: block, brief, mixed (default: block)

  # Live import options
  --stack-name NAME          Import from deployed CloudFormation stack
  --profile PROFILE          AWS profile name
  --region REGION            AWS region

  # Nested stack options
  --flatten                  Merge nested stacks into single module
  --preserve-nesting         Generate separate modules per stack
  --nested-dir PATH          Directory for nested stack modules (with --preserve-nesting)

  # Code generation options
  --class-prefix PREFIX      Prefix for generated class names
  --template-class NAME      Name for the template wrapper class
  --no-docstrings            Omit docstrings from generated code
  --no-main-block            Omit if __name__ == "__main__" block

  # Formatting options
  --format / --no-format     Run ruff format on output (default: --format)
  --line-length N            Line length for formatting (default: 100)

  # Debugging
  --dump-ir                  Dump intermediate representation and exit
  --verbose                  Verbose output

  --help                     Show this message and exit
  --version                  Show version and exit
```

### Examples

```bash
# Import with custom class prefix
cfn-import template.yaml -o stack.py --class-prefix MyApp

# Live import from production
cfn-import --stack-name ProdVPC --profile prod --region us-east-1 -o vpc.py

# Flatten nested stacks
cfn-import parent.yaml --flatten -o unified.py

# Preserve nesting with custom output directory
cfn-import parent.yaml --preserve-nesting --nested-dir ./infrastructure/

# Debug: see the IR without generating code
cfn-import template.yaml --dump-ir

# Pipe through for quick viewing
cat template.yaml | cfn-import - --mode brief | less
```

---

## Error Handling Strategy

### Error Types

```python
class ImporterError(Exception):
    """Base exception for importer errors."""
    pass

class ParseError(ImporterError):
    """Template parsing failed."""
    def __init__(self, message: str, line: int | None = None, column: int | None = None):
        self.line = line
        self.column = column
        location = f" at line {line}" if line else ""
        super().__init__(f"{message}{location}")

class UnsupportedResourceError(ImporterError):
    """Resource type not supported."""
    def __init__(self, resource_type: str, logical_id: str):
        self.resource_type = resource_type
        self.logical_id = logical_id
        super().__init__(f"Unsupported resource type '{resource_type}' for '{logical_id}'")

class IntrinsicError(ImporterError):
    """Intrinsic function parsing failed."""
    def __init__(self, intrinsic_name: str, message: str):
        self.intrinsic_name = intrinsic_name
        super().__init__(f"Error parsing {intrinsic_name}: {message}")

class NestedStackError(ImporterError):
    """Nested stack resolution failed."""
    def __init__(self, logical_id: str, template_url: str, cause: str):
        self.logical_id = logical_id
        self.template_url = template_url
        super().__init__(f"Failed to fetch nested stack '{logical_id}' from {template_url}: {cause}")

class LiveImportError(ImporterError):
    """AWS API call failed."""
    def __init__(self, operation: str, stack_name: str, cause: str):
        self.operation = operation
        self.stack_name = stack_name
        super().__init__(f"Failed to {operation} for stack '{stack_name}': {cause}")
```

### Error Handling Behavior

| Scenario | Behavior | Exit Code |
|----------|----------|-----------|
| YAML/JSON syntax error | Fail with ParseError, show line number | 1 |
| Unsupported resource type | Warn and skip resource, continue | 0 (with warnings) |
| Unknown intrinsic function | Warn and emit as comment | 0 (with warnings) |
| Nested stack URL inaccessible | Fail if --flatten/--preserve-nesting, else warn | 1 or 0 |
| AWS credentials missing (live) | Fail with clear message | 1 |
| Stack not found (live) | Fail with LiveImportError | 1 |
| Circular DependsOn detected | Warn but continue | 0 (with warnings) |
| Generated Python has syntax errors | Fail (internal error) | 2 |

### Warning vs Error Philosophy

- **Errors** (stop processing): Invalid syntax, inaccessible required resources, AWS auth failures
- **Warnings** (continue with degraded output): Unsupported features that can be skipped

### Output with Warnings

When warnings occur, the generated code includes comments:

```python
# WARNING: Resource 'MyCustomResource' has unsupported type 'Custom::MyLambda'
# Original properties preserved as comment:
# {
#   "ServiceToken": "arn:aws:lambda:...",
#   "CustomProperty": "value"
# }
```

---

## Module Interfaces

### parser.py

```python
"""Template parser - YAML/JSON to IR."""

def parse_template(
    source: str | Path | TextIO,
    source_name: str | None = None,
) -> IRTemplate:
    """
    Parse a CloudFormation template into IR.

    Args:
        source: File path, string content, or file-like object
        source_name: Name for error messages (default: file path or "<stdin>")

    Returns:
        Parsed IRTemplate

    Raises:
        ParseError: If template syntax is invalid
    """
    ...

def parse_yaml(content: str) -> dict[str, Any]:
    """Parse YAML with CloudFormation intrinsic support."""
    ...

def parse_json(content: str) -> dict[str, Any]:
    """Parse JSON (intrinsics are in long form)."""
    ...
```

### intrinsics.py

```python
"""Intrinsic function handling."""

def resolve_intrinsics(template: IRTemplate) -> IRTemplate:
    """
    Walk template and convert intrinsic dicts to IRIntrinsic objects.

    Handles both YAML tag form (already IRIntrinsic from parser)
    and JSON/long form (dicts with Fn:: keys).
    """
    ...

def intrinsic_to_python(intrinsic: IRIntrinsic, context: CodegenContext) -> str:
    """
    Convert an IRIntrinsic to Python code string.

    Args:
        intrinsic: The intrinsic to convert
        context: Code generation context (for resolving references)

    Returns:
        Python code string, e.g., "ref(MyBucket)" or "Sub('${MyBucket.Arn}')"
    """
    ...
```

### resolver.py

```python
"""Property resolution and analysis."""

def analyze_template(template: IRTemplate) -> IRTemplate:
    """
    Perform all analysis passes on a template.

    - Analyze references (populate reference_graph)
    - Count reuse (for mixed mode decisions)
    - Resolve property types
    - Validate resource types exist

    Returns:
        Analyzed template (mutated in place and returned)
    """
    ...

def resolve_resource_type(resource_type: str) -> tuple[str, str, type] | None:
    """
    Resolve a CloudFormation resource type to Python class info.

    Args:
        resource_type: e.g., "AWS::S3::Bucket"

    Returns:
        Tuple of (service, class_name, class) or None if unknown
        e.g., ("s3", "Bucket", cloudformation_dataclasses.aws.s3.Bucket)
    """
    ...
```

### codegen.py

```python
"""Python code generation from IR."""

@dataclass
class CodegenContext:
    """Context for code generation."""
    mode: Literal["block", "brief", "mixed"]
    template: IRTemplate
    class_prefix: str = ""
    template_class_name: str | None = None
    include_docstrings: bool = True
    include_main_block: bool = True

    # Tracking during generation
    generated_classes: set[str] = field(default_factory=set)
    imports: set[str] = field(default_factory=set)


def generate_code(template: IRTemplate, context: CodegenContext) -> str:
    """
    Generate Python code from analyzed IR.

    Args:
        template: Analyzed IRTemplate
        context: Code generation options

    Returns:
        Complete Python module source code
    """
    ...

def generate_resource_class(resource: IRResource, context: CodegenContext) -> str:
    """Generate a single resource wrapper class."""
    ...

def generate_parameter_class(param: IRParameter, context: CodegenContext) -> str:
    """Generate a parameter wrapper class."""
    ...

def generate_output_class(output: IROutput, context: CodegenContext) -> str:
    """Generate an output wrapper class."""
    ...

def generate_imports(context: CodegenContext) -> str:
    """Generate import statements based on what's used."""
    ...
```

### cli.py

```python
"""Command-line interface."""

def main(argv: list[str] | None = None) -> int:
    """
    Main entry point for cfn-import command.

    Args:
        argv: Command line arguments (default: sys.argv[1:])

    Returns:
        Exit code (0 for success)
    """
    ...
```

### live.py

```python
"""Live import from AWS."""

def fetch_stack_template(
    stack_name: str,
    profile: str | None = None,
    region: str | None = None,
) -> tuple[str, dict[str, Any]]:
    """
    Fetch template and metadata from a deployed stack.

    Args:
        stack_name: CloudFormation stack name or ARN
        profile: AWS profile name
        region: AWS region

    Returns:
        Tuple of (template_body, stack_info)

    Raises:
        LiveImportError: If stack not found or access denied
    """
    ...

def fetch_nested_stacks(
    stack_name: str,
    profile: str | None = None,
    region: str | None = None,
) -> dict[str, IRTemplate]:
    """
    Recursively fetch all nested stack templates.

    Returns:
        Dict mapping logical ID to parsed IRTemplate
    """
    ...
```

---

## Known Limitations / Out of Scope (v1)

### Not Supported in v1

| Feature | Reason | Workaround |
|---------|--------|------------|
| `AWS::CloudFormation::CustomResource` | Arbitrary Lambda behavior | Emitted as comment |
| `Custom::*` resource types | Same as above | Emitted as comment |
| `AWS::CloudFormation::Macro` | Template transforms | Run transform first, import result |
| `Fn::Transform` | Same as above | Run transform first |
| SAM resources (`AWS::Serverless::*`) | Different spec, different tooling | Use `sam build` first |
| CloudFormation Modules | Not widely adopted | Expand manually |
| StackSets | Multi-account orchestration | Import individual templates |
| Drift detection | Requires live state comparison | Future consideration |
| Template validation | Focus is conversion, not linting | Use `cfn-lint` separately |

### Partial Support

| Feature | Limitation |
|---------|------------|
| `Fn::Transform` | Recognized but emitted as warning |
| Nested intrinsics | Depth limit of 10 (configurable) |
| Large templates (>500 resources) | May be slow, no streaming |
| Binary data in UserData | Base64 encoded, not decoded |

### Known Edge Cases

1. **Duplicate logical IDs after snake_case**: `MyVPC` and `MyVpc` both become `my_vpc`
   - Solution: Append numeric suffix (`my_vpc`, `my_vpc_2`)

2. **Circular references**: Template has `A -> B -> A`
   - Solution: Warn and break cycle at arbitrary point

3. **Resource type not in spec**: Third-party or new resource types
   - Solution: Emit as generic `CloudFormationResource` with dict properties

4. **Ambiguous !GetAtt**: `!GetAtt Foo.Bar.Baz` (is it `Foo` with attr `Bar.Baz` or `Foo.Bar` with attr `Baz`?)
   - Solution: Follow CloudFormation rules (first `.` splits logical ID from attribute)

---

## Example Conversion

### Input (CloudFormation YAML)

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: Simple S3 bucket with policy

Parameters:
  BucketNameParam:
    Type: String
    Description: Name of the bucket

Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Ref BucketNameParam
      Tags:
        - Key: Environment
          Value: Production

  MyBucketPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref MyBucket
      PolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal: "*"
            Action: s3:GetObject
            Resource: !Sub "${MyBucket.Arn}/*"

Outputs:
  BucketArn:
    Value: !GetAtt MyBucket.Arn
    Description: ARN of the bucket
```

### Output (Mixed Mode)

```python
"""
Simple S3 bucket with policy

Imported from: template.yaml
"""

from cloudformation_dataclasses import (
    cloudformation_dataclass,
    ref,
    get_att,
)
from cloudformation_dataclasses.core.template import (
    Template,
    Parameter,
    Output,
)
from cloudformation_dataclasses.core.base import (
    Tag,
    PolicyDocument,
    PolicyStatement,
)
from cloudformation_dataclasses.aws.s3 import Bucket, BucketPolicy
from cloudformation_dataclasses.intrinsics.functions import Sub


@cloudformation_dataclass
class BucketNameParam:
    """Name of the bucket"""
    resource: Parameter
    type = "String"
    description = "Name of the bucket"


@cloudformation_dataclass
class EnvironmentTag:
    resource: Tag
    key = "Environment"
    value = "Production"


@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    bucket_name = ref(BucketNameParam)
    tags = [EnvironmentTag]


@cloudformation_dataclass
class MyBucketPolicy:
    resource: BucketPolicy
    bucket = ref(MyBucket)
    policy_document = PolicyDocument(
        statement=[
            PolicyStatement(
                effect="Allow",
                principal="*",
                action="s3:GetObject",
                resource_arn=Sub("${MyBucket.Arn}/*"),
            )
        ]
    )


@cloudformation_dataclass
class BucketArnOutput:
    """ARN of the bucket"""
    resource: Output
    value = get_att(MyBucket, "Arn")
    description = "ARN of the bucket"


@cloudformation_dataclass
class SimpleS3Template:
    """Simple S3 bucket with policy"""
    resource: Template
    description = "Simple S3 bucket with policy"
    parameters = [BucketNameParam]
    resources = [MyBucket, MyBucketPolicy]
    outputs = [BucketArnOutput]


def build_template() -> Template:
    return SimpleS3Template().resource


if __name__ == "__main__":
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))
```

---

## Implementation Phases

### Phase 1: Core Parser
- YAML/JSON loading
- Basic resource extraction
- Simple property mapping

### Phase 2: Intrinsic Functions
- `!Ref` / `Fn::Ref`
- `!GetAtt` / `Fn::GetAtt`
- `!Sub` / `Fn::Sub`
- `!Join`, `!If`, `!Select`, etc.

### Phase 3: Code Generation
- Brief mode (simplest)
- Block mode
- Mixed mode with reuse detection

### Phase 4: Polish
- Import optimization
- Code formatting (black/ruff)
- Error handling and validation
- Edge cases

---

## Live Import via Boto3

Beyond file-based import, the importer can also import live stacks directly from AWS:

```bash
# Import from deployed stack
cfn-import --stack-name MyProductionStack -o my_stack.py

# Import with specific profile/region
cfn-import --stack-name MyStack --profile prod --region us-west-2 -o output.py
```

### How It Works

1. **Get Template**: `cloudformation.get_template(StackName=stack_name)`
   - Returns the original template used to create the stack
   - Includes all resources, parameters, outputs

2. **Get Stack Info**: `cloudformation.describe_stacks(StackName=stack_name)`
   - Returns current parameter values
   - Returns current output values
   - Stack status and metadata

3. **Get Physical Resources**: `cloudformation.list_stack_resources(StackName=stack_name)`
   - Maps logical IDs to physical resource IDs
   - Enables `# Physical: bucket-name-abc123` comments in generated code

### Live Import Benefits

- **Resolved parameters**: See actual values used in production
- **Physical resource IDs**: Comments showing real AWS resource names
- **Drift context**: Compare template vs actual state

### Package Structure Addition

```
src/cloudformation_dataclasses/importer/
├── ...
├── live.py              # boto3-based live import
└── cli.py               # Extended with --stack-name option
```

### pyproject.toml Update

```toml
[project.optional-dependencies]
importer = ["pyyaml"]
importer-live = ["pyyaml", "boto3"]  # For live import feature
```

---

## Nested Stack Support

Nested stacks are a key differentiator. CDK migrate does NOT fully support nested stacks, but we can:

### Challenge

Nested stacks reference other templates via `AWS::CloudFormation::Stack`:

```yaml
Resources:
  VPCStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://s3.amazonaws.com/bucket/vpc-template.yaml
      Parameters:
        VPCCidr: 10.0.0.0/16
```

The child template is a separate file, potentially with its own nested stacks.

### Import Modes

#### 1. Flatten Mode (`--flatten`)

Merge all nested stacks into a single Python module:

```bash
cfn-import parent-stack.yaml --flatten -o unified_stack.py
```

- Automatically fetches nested templates (from S3 or local paths)
- Resolves cross-stack references
- Generates one cohesive module with all resources
- Best for: understanding full infrastructure, smaller nested hierarchies

#### 2. Preserve Nesting (`--preserve-nesting`)

Generate separate modules matching the stack hierarchy:

```bash
cfn-import parent-stack.yaml --preserve-nesting -o ./stacks/
```

Output structure:
```
stacks/
├── parent_stack.py
├── vpc_stack.py         # From VPCStack nested template
├── database_stack.py    # From DatabaseStack nested template
└── __init__.py          # Exports all stack builders
```

- Maintains original architecture
- Each module is independently usable
- Cross-stack references become explicit imports
- Best for: large infrastructures, maintaining modularity

### Live Import with Nested Stacks

```bash
cfn-import --stack-name ParentStack --flatten -o unified.py
cfn-import --stack-name ParentStack --preserve-nesting -o ./stacks/
```

For live import:
1. Identify nested stack resources via `list_stack_resources()`
2. Recursively call `get_template()` on each nested stack
3. Build complete template tree
4. Apply flatten or preserve-nesting strategy

### Cross-Stack References

When preserving nesting, cross-stack references become explicit:

```python
# vpc_stack.py
@cloudformation_dataclass
class VPCIdOutput:
    resource: Output
    value = ref(MainVPC)
    export_name = "${AWS::StackName}-VPCId"

# database_stack.py
from .vpc_stack import VPCStack

@cloudformation_dataclass
class DatabaseSubnet:
    resource: Subnet
    vpc_id = ImportValue(Sub("${VPCStackName}-VPCId"))
```

---

## Test Templates

Test templates for validating the importer are located in:

```
tests/importer/templates/
├── simple/
│   ├── s3_bucket.yaml           # Single resource
│   ├── s3_bucket.json           # JSON format
│   ├── ec2_instance.yaml        # Basic EC2
│   └── parameters_only.yaml     # Just parameters
│
├── intrinsics/
│   ├── ref_basic.yaml           # !Ref usage
│   ├── getatt_basic.yaml        # !GetAtt usage
│   ├── sub_basic.yaml           # !Sub with variables
│   ├── sub_mapping.yaml         # !Sub with mapping syntax
│   ├── join.yaml                # !Join
│   ├── select_getazs.yaml       # !Select + !GetAZs
│   ├── if_condition.yaml        # !If conditional
│   ├── nested_intrinsics.yaml   # Intrinsics within intrinsics
│   └── fn_prefix.yaml           # Fn::Ref style (not YAML tags)
│
├── complex/
│   ├── vpc_full.yaml            # VPC with subnets, routes, NAT
│   ├── ec2_userdata.yaml        # EC2 with UserData scripts
│   ├── iam_policies.yaml        # IAM roles and policies
│   ├── lambda_function.yaml     # Lambda with inline code
│   ├── api_gateway.yaml         # API Gateway setup
│   └── dynamodb_tables.yaml     # DynamoDB with GSIs
│
├── nested/
│   ├── parent_stack.yaml        # Parent with nested stack refs
│   ├── child_vpc.yaml           # Child VPC template
│   ├── child_database.yaml      # Child database template
│   ├── three_level_deep/        # Grandchild nesting
│   │   ├── root.yaml
│   │   ├── level1.yaml
│   │   └── level2.yaml
│   └── cross_stack_refs.yaml    # Export/ImportValue patterns
│
├── edge_cases/
│   ├── empty_properties.yaml    # Resource with no properties
│   ├── all_intrinsics.yaml      # Every intrinsic function
│   ├── special_chars.yaml       # Names with special characters
│   ├── large_template.yaml      # 50+ resources
│   ├── circular_depends.yaml    # DependsOn cycles (should warn)
│   └── custom_resource.yaml     # AWS::CloudFormation::CustomResource
│
└── real_world/
    ├── wordpress.yaml           # Classic WordPress stack
    ├── eks_cluster.yaml         # EKS with node groups
    └── serverless_api.yaml      # API Gateway + Lambda + DynamoDB
```

### Test Template Sources

1. **AWS Sample Templates**: Adapted from [aws-cloudformation-templates](https://github.com/awslabs/aws-cloudformation-templates)
2. **Custom edge cases**: Hand-crafted to test specific parsing scenarios
3. **Real-world examples**: Anonymized production patterns

### Test Validation

Each template has expected output in:

```
tests/importer/expected/
├── simple/
│   ├── s3_bucket_block.py       # Expected block mode output
│   ├── s3_bucket_brief.py       # Expected brief mode output
│   └── s3_bucket_mixed.py       # Expected mixed mode output
...
```

Tests verify:
1. **Round-trip**: Generated Python produces identical CloudFormation JSON
2. **Mode correctness**: Each mode generates expected style
3. **Import validity**: Generated code is syntactically correct Python
4. **Type correctness**: All resource types resolve properly

---

## Comparison with Existing Tools

### CDK Migrate

AWS's `cdk migrate` converts CloudFormation to CDK code.

| Feature | CDK Migrate | cfn-import |
|---------|-------------|------------|
| Output style | Imperative (CDK constructs) | Declarative (dataclasses) |
| Nested stacks | Limited/No full support | Full support (flatten/preserve) |
| Live import | Yes | Yes (with boto3) |
| Round-trip fidelity | Best effort | Exact match goal |
| Multiple modes | No | Yes (block/brief/mixed) |

### Former2

Browser-based tool that generates IaC from existing AWS resources.

| Feature | Former2 | cfn-import |
|---------|---------|------------|
| Input | Live AWS resources | Templates or live stacks |
| Output formats | Many (CFN, Terraform, CDK) | Python dataclasses only |
| Nested stacks | No | Yes |
| Offline | No (browser-based) | Yes (file mode) |

### IaC Generator (AWS Console)

AWS Console feature to generate templates from resources.

| Feature | IaC Generator | cfn-import |
|---------|---------------|------------|
| Scope | Selected resources → template | Template → Python code |
| Purpose | Create new templates | Convert existing templates |

---

## Future Considerations

- **Round-trip fidelity**: Generated Python should produce identical CloudFormation output
- **Comments preservation**: Extract and preserve YAML comments as docstrings
- **Drift detection**: Compare imported Python with source template
- **Watch mode**: Re-import on file changes
- **IDE integration**: VSCode extension for import-on-paste
- **Partial import**: Import specific resources from a template

---

## Migration Strategies

Teams with existing CloudFormation infrastructure have several paths to adopt `cloudformation_dataclasses`. The right approach depends on codebase size, team expertise, and risk tolerance.

### Strategy 1: Automated Import (Recommended Starting Point)

Use the `cfn-import` tool to convert existing templates to Python:

```bash
# Convert a single template
cfn-import template.yaml -o infra/vpc.py

# Convert a directory of templates
cfn-import templates/ -o infra/ --recursive

# Import from a deployed stack
cfn-import --stack prod-vpc -o infra/vpc.py --profile production
```

**Workflow:**

```
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│   Existing YAML     │────▶│    cfn-import       │────▶│   Python Code       │
│   template.yaml     │     │    (automated)      │     │   template.py       │
└─────────────────────┘     └─────────────────────┘     └─────────────────────┘
                                      │
                                      ▼
                            ┌─────────────────────┐
                            │   Verify round-trip │
                            │   (JSON matches)    │
                            └─────────────────────┘
```

**Pros:**
- Fast initial conversion
- Preserves exact CloudFormation structure
- Round-trip verification ensures correctness
- Low risk - generated code produces identical output

**Cons:**
- Generated code may not be idiomatic Python
- May need cleanup for readability
- Nested stacks need decisions (flatten vs preserve)

**Best for:** Large templates, legacy infrastructure, rapid adoption

### Strategy 2: Gradual Migration

Convert templates piece by piece, starting with simpler resources:

**Phase 1: Low-Risk Resources**
```python
# Start with stateless resources
@cloudformation_dataclass
class AppSecurityGroup:
    resource: SecurityGroup
    group_description: str = "Application servers"
    vpc_id = Ref("VpcId")
```

**Phase 2: Stateful Resources**
```python
# Then move to data stores (more carefully)
@cloudformation_dataclass
class AppDatabase:
    resource: DBInstance
    deletion_policy: str = "Retain"  # Safety first!
    db_instance_class: str = "db.t3.medium"
```

**Phase 3: Complex Resources**
```python
# Finally tackle IAM, Lambda, etc.
@cloudformation_dataclass
class AppFunction:
    resource: Function
    # ... complex configuration
```

**Migration Checklist:**
- [ ] Identify template dependencies
- [ ] Start with leaf resources (no dependencies on other templates)
- [ ] Test in non-production first
- [ ] Verify outputs match original
- [ ] Update CI/CD pipelines
- [ ] Document any behavioral changes

**Pros:**
- Lower risk - small changes
- Team learns incrementally
- Easy rollback per resource
- Can prioritize high-churn resources

**Cons:**
- Slower overall migration
- Two code styles during transition
- More coordination needed

**Best for:** Critical production systems, risk-averse teams, learning phase

### Strategy 3: Side-by-Side Hybrid

Keep existing YAML for stable infrastructure, use Python for new development:

```
infrastructure/
├── legacy/                    # Existing YAML (read-only)
│   ├── vpc.yaml
│   ├── database.yaml
│   └── iam.yaml
├── python/                    # New Python code
│   ├── api_gateway.py         # New features in Python
│   ├── lambda_functions.py
│   └── monitoring.py
└── deploy.sh                  # Orchestrates both
```

**Deployment Script:**
```bash
#!/bin/bash
# Deploy legacy YAML templates
aws cloudformation deploy --template-file legacy/vpc.yaml --stack-name prod-vpc
aws cloudformation deploy --template-file legacy/database.yaml --stack-name prod-db

# Deploy new Python-generated templates
python python/api_gateway.py > /tmp/api.yaml
aws cloudformation deploy --template-file /tmp/api.yaml --stack-name prod-api
```

**Or with Rain:**
```bash
# Rain can handle both in one config
rain deploy legacy/vpc.yaml prod-vpc
rain deploy legacy/database.yaml prod-db

python python/api_gateway.py | rain deploy - prod-api
```

**Pros:**
- Zero risk to existing infrastructure
- Immediate benefits for new code
- No migration pressure
- Can migrate legacy opportunistically

**Cons:**
- Two systems to maintain
- Context switching for developers
- Cross-references need care

**Best for:** Large organizations, stable legacy systems, new feature focus

### Strategy Comparison

| Factor | Automated Import | Gradual Migration | Side-by-Side |
|--------|-----------------|-------------------|--------------|
| Initial effort | Low | Medium | Low |
| Risk | Low | Low | None |
| Speed | Fast | Slow | N/A |
| Code quality | Needs cleanup | High from start | High for new |
| Team learning | After migration | During migration | Gradual |
| Rollback | Full template | Per resource | N/A |

### Enterprise Considerations

For large-scale migrations, additional tooling may be needed:

**1. Template Discovery**
```bash
# Find all CloudFormation templates in a repo
cfn-import scan ./infrastructure --report templates.json
```

**2. Dependency Analysis**
```bash
# Understand cross-stack references
cfn-import analyze templates/ --deps-graph deps.dot
dot -Tpng deps.dot -o deps.png
```

**3. Bulk Conversion with Validation**
```bash
# Convert all, verify each
cfn-import batch templates/ \
    --output python/ \
    --verify \
    --report migration-report.json
```

**4. CI/CD Integration**
```yaml
# GitHub Actions example
- name: Verify round-trip fidelity
  run: |
    python infra/vpc.py > /tmp/generated.yaml
    cfn-diff legacy/vpc.yaml /tmp/generated.yaml
```

### Migration Blockers & Solutions

| Blocker | Solution |
|---------|----------|
| Custom resources | Import as-is, refactor later |
| Macros | Expand before import, or preserve |
| Nested stacks | Flatten or preserve as modules |
| Dynamic references | Keep as strings initially |
| SSM parameters | Use `Ref` or `Sub` |
| Secrets Manager | Use dynamic references |

### Recommended Migration Path

1. **Start small**: Pick one non-critical template
2. **Use automated import**: `cfn-import template.yaml -o infra.py`
3. **Verify round-trip**: Ensure generated code produces identical JSON
4. **Refactor for clarity**: Clean up naming, add type hints
5. **Deploy to staging**: Test thoroughly
6. **Expand gradually**: Move to more templates
7. **Establish patterns**: Create team conventions
8. **Migrate critical systems last**: After building confidence
