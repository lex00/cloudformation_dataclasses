# Third-Party CloudFormation Template Import Workflow

A reusable, agentic workflow for importing third-party CloudFormation templates into the `cloudformation_dataclasses` project. This workflow produces well-documented examples with tests.

## Setup Questions

Before starting, gather the following information:

### 1. Source Location
**Question**: Where are the CloudFormation templates located?
- Path (absolute or relative to project root)
- Is it a git repository? (for attribution links)
- Repository URL (if applicable, for README credits)

**Example**: `/path/to/templates` or `https://github.com/org/repo`

### 2. Target Location
**Question**: Where should the imported examples be placed?
- Default: `examples/3rd_party/{source_name}/`
- Custom path if preferred

### 3. Attribution
**Question**: How should we credit the original source?
- Organization/author name
- License type (if known)
- Link format for READMEs

### 4. Scope
**Question**: Which templates should be imported?
- All templates in the source
- Specific services (e.g., S3, Lambda, VPC)
- Specific templates by name/path

### 5. Interaction Mode
**Question**: How should the workflow handle decisions?
- **Interactive** (default): Prompt before adding new enums, constants, or making tool changes
- **Unattended**: Auto-approve all improvements, continue on errors, generate summary

## Workflow Overview

### For Each Template
1. **Import** template: `cfn-import template.yaml -o example/`
2. **Analyze** generated code for improvement opportunities
3. **Improve** tools if needed (generator, linter, docs)
4. **Create** README and tests in the folder structure
5. **Verify** tests pass, fix errors

The importer automatically:
- Detects implicit refs from matching Sub patterns
- Replaces ARN constructions with `get_att(Resource, ARN)`
- Uses `Join()` for ARN wildcards (cleaner than `Sub()`)
- Adds proper cross-resource imports

## Detailed Steps Per Template

### Step 1: Create Folder Structure

Each template is generated as a package with wrapper classes:

```
{target_location}/{Service}/{example}/
├── __init__.py
├── config.py
├── resources/
│   ├── __init__.py
│   └── {resource}.py      # One file per resource
├── outputs.py             # If template has outputs
├── main.py
├── README.md
├── tests/
│   ├── __init__.py
│   └── test_{example}.py
├── pyproject.toml
├── py.typed
├── mypy.ini
├── CLAUDE.md
└── .vscode/
    └── settings.json
```

### Step 2: Import Template

```bash
# From within {target_location}/{Service}/{example}/
cfn-import {source_path}/template.yaml -o .
```

**Note**: The importer automatically detects and improves patterns:
- Implicit refs: `Sub('${AppName}-bucket')` → `ref(MyBucket)` when patterns match
- ARN patterns: `Sub('arn:...')` → `get_att(MyBucket, ARN)`
- ARN wildcards: Uses `Join('', [get_att(..., ARN), '/*'])` instead of verbose Sub

### Step 3: Analyze Generated Code
Check the generated code for patterns that could be improved:

| Pattern | Action |
|---------|--------|
| String literal that should be an enum | Add to `KNOWN_ENUMS` in linter rules |
| Dict literal that should be a PropertyType | Add to `KNOWN_PROPERTY_TYPES` in linter rules |

### Step 4: Improve Tools (Interactive Mode)
When you discover a pattern that should be handled better:

**Prompt example**:
```
Found string literal "Enabled" for field "status" in VersioningConfiguration.
This looks like a BucketVersioningStatus enum value.
Options:
1. Add to linter KNOWN_ENUMS (recommended)
2. Skip for now
3. Investigate further
```

**Files to potentially update**:
- `src/cloudformation_dataclasses/linter/rules.py` - Add to `KNOWN_ENUMS` or `KNOWN_PROPERTY_TYPES`
- `src/cloudformation_dataclasses/constants/__init__.py` - Add new constant maps
- `src/cloudformation_dataclasses/core/constants.py` - Add new constant classes (like `IpProtocol`)
- `docs/LINTER.md` - Document significant new patterns

After updates, re-run linter to apply fixes.

### Step 5: Create README
Template:
```markdown
# {Example Name}

Migrated from [{Original Filename}]({source_repo_url}/path/to/original).

**Original Author/Source**: {attribution}

{Brief description of what the template does.}

## Features Demonstrated
- {List cloudformation_dataclasses features used}

## Run Tests
\`\`\`bash
uv run pytest {target_location}/{Service}/{example}/tests/ -v
\`\`\`

## Generate Template
\`\`\`bash
uv run python -m {target_module_path}.main
\`\`\`

## Resources

| Logical ID | Type | Description |
|------------|------|-------------|
| `{LogicalId}` | `{Type}` | {Description} |
```

### Step 6: Create Tests

```python
import pytest
from ..main import build_template

class TestTemplate:
    def test_template_validates(self):
        """Template should pass validation."""
        assert build_template().validate() == []

    def test_template_structure(self):
        """Verify AWSTemplateFormatVersion, sections present."""
        template = build_template().to_dict()
        assert "AWSTemplateFormatVersion" in template
        assert "Resources" in template

    def test_template_resources(self):
        """Verify resource types and logical IDs."""
        template = build_template().to_dict()
        # Add service-specific resource checks
```

### Step 7: Verify
```bash
uv run pytest {target_location}/{Service}/{example}/tests/ -v
```

If tests fail:
1. Check if PropertyType class needs adjustment in generator
2. Check if enum mapping is incorrect
3. Update docs if error reveals documentation gap
4. In interactive mode: prompt user for guidance

## Priority Order

Start with simpler templates to build confidence:

### Tier 1: Simple (1-3 resources)
- Basic service configurations (single S3 bucket, SNS topic, SQS queue)
- Good for validating the workflow

### Tier 2: Medium (3-6 resources)
- Service with nested properties (DynamoDB with GSIs, Lambda with role)
- Tests more PropertyType mappings

### Tier 3: Complex (6+ resources)
- Full infrastructure stacks (VPC, ECS, EKS)
- Tests cross-resource references extensively

### Skip Criteria
- Non-standard template formats (Rain modules, SAM-only features)
- Templates requiring transform macros not supported
- Templates with external file references (unless handling separately)

## Files Modified During Workflow

### Core Improvements (as discovered)
- `src/cloudformation_dataclasses/linter/rules.py` - Enum/property mappings
- `src/cloudformation_dataclasses/constants/__init__.py` - Constant maps
- `src/cloudformation_dataclasses/core/constants.py` - Constant classes
- `docs/LINTER.md` - Pattern documentation

### Per Example Created
- `{target}/{Service}/{example}/` - Full package
- `{target}/{Service}/{example}/README.md` - Documentation
- `{target}/{Service}/{example}/tests/test_{example}.py` - Tests
- `{target}/{Service}/{example}/tests/__init__.py`

### Index Updates
- `{target}/README.md` - Update example list
- `docs/AGENT_GUIDE.md` - Add new patterns discovered

## Success Criteria Per Template
1. Template imports without errors
2. All tests pass
3. README properly credits original source
4. `template.validate() == []`

## Session Example

```
[User]: Import templates from ../third-party-cfn-templates

[Claude]: I'll help import CloudFormation templates. First, some questions:

1. Source path: ../third-party-cfn-templates - confirmed
2. Attribution: What's the source for README credits?
3. Target: Use default examples/3rd_party/third_party_cfn/ ?
4. Scope: All templates or specific services?
5. Mode: Interactive (prompt before changes) or unattended?

[User]: Source is Apache-2.0 from ExampleOrg, use defaults, start with S3, interactive mode

[Claude]: Starting with S3 templates...

> Importing: S3/simple-bucket.yaml
  ├─ Created: examples/3rd_party/third_party_cfn/S3/simple_bucket/
  ├─ Auto-detected patterns:
  │   - Implicit ref: bucket policy → ObjectStorageBucket
  │   - ARN pattern: get_att(ObjectStorageBucket, ARN)
  │   - ARN wildcard: Join('', [get_att(..., ARN), '/*'])
  ├─ Creating README.md
  ├─ Creating tests...
  └─ Tests: PASS (3 tests)

> Continue to next template? [Y/n]
```

## Unattended Mode

For batch processing:
- Auto-approve all tool improvements
- Continue on test failures (log for review)
- Generate summary report at end with:
  - Templates successfully imported
  - Templates with failures (and errors)
  - Tool improvements made
  - New patterns added to linter

## Lessons Learned

### Parameter-Only Sub Patterns

When a `!Sub` expression references **only parameters** (not resource properties), the importer preserves `Sub()` instead of converting to `get_att()`.

**Example**: If a bucket's name comes from a parameter:
```yaml
BucketName: !Sub '${BucketNameParam}'
```

Then another resource referencing that bucket's ARN:
```yaml
SourceArn: !Sub 'arn:${AWS::Partition}:s3:::${BucketNameParam}'
```

Will generate `Sub(...)` instead of `get_att(Bucket, ARN)` because `BucketNameParam` is a parameter, not a resource-derived value.

### DependsOn Class References

Resources in `depends_on` are now properly imported with class references instead of strings:

```python
from .lambda_invoke_permission import LambdaInvokePermission

@cloudformation_dataclass
class S3BucketNotification:
    resource: Bucket
    depends_on = [LambdaInvokePermission]  # Class reference, resolved at serialization
```

This enables proper IDE navigation and refactoring support.

## Notes
- Source folder should be treated as read-only
- Each imported example should be self-contained
- Tests should not require AWS credentials (local validation only)
- Prefer YAML templates over JSON when both exist (easier to read originals)
- If a template uses unsupported features, document the limitation and skip or partially import

## See Also

- [LINTER.md](LINTER.md) - Linter rules and usage
- [IMPORTER.md](IMPORTER.md) - Template importer documentation
- [AGENT_GUIDE.md](AGENT_GUIDE.md) - Workflows for AI assistants
