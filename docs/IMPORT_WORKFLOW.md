# Third-Party CloudFormation Template Import Workflow

A reusable, agentic workflow for importing third-party CloudFormation templates into the `cloudformation_dataclasses` project. This workflow uses the linter to discover missing types/enums, improves the generator/linter/docs in real-time, and produces well-documented examples with tests.

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
- Default: `examples/generated/{source_name}/`
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
1. **Import** with linter: `cfn-import template.yaml --lint -o example.py`
2. **Analyze** linter output for improvement opportunities
3. **Improve** tools if needed (generator, linter, docs)
4. **Create** folder structure with README and tests
5. **Verify** tests pass, fix errors

## Detailed Steps Per Template

### Step 1: Create Folder Structure
```
{target_location}/{Service}/
├── {example_name}/
│   ├── __init__.py       # Exports, common imports
│   ├── main.py           # Generated code (linted)
│   ├── README.md         # Credits, features, usage
│   └── tests/
│       ├── __init__.py
│       └── test_{example_name}.py
```

For multi-example service folders, create subfolders per example.

### Step 2: Import with Linter
```bash
cfn-import {source_path}/{Service}/template.yaml \
  --lint -o {target_location}/{Service}/{example}/main.py
```

### Step 3: Analyze Linter Output
Check the generated code for patterns the linter should have caught but didn't:

| Rule | Pattern | Action if Missing |
|------|---------|-------------------|
| CFD001 | `{"Bool": ...}` instead of `{BOOL: ...}` | Add to `CONDITION_OPERATOR_MAP` |
| CFD002 | `type = "String"` instead of `type = STRING` | Add to `PARAMETER_TYPE_MAP` |
| CFD003 | `Ref("AWS::Region")` instead of `AWS_REGION` | Add to `PSEUDO_PARAMETER_MAP` |
| CFD004 | String literal for enum field | Add to `KNOWN_ENUMS` in linter rules |
| CFD005 | Dict literal for PropertyType | Add to `KNOWN_PROPERTY_TYPES` in linter rules |

### Step 4: Improve Tools (Interactive Mode)
When the linter doesn't catch a pattern that should be caught:

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
```

### Step 6: Create Tests
Follow the established test pattern:
- `test_template_structure()` - Verify AWSTemplateFormatVersion, sections present
- `test_template_resources()` - Verify resource types and logical IDs
- `test_template_validation()` - `template.validate() == []`
- Service-specific property tests as appropriate

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
- `{target}/{Service}/{example}/main.py`
- `{target}/{Service}/{example}/README.md`
- `{target}/{Service}/{example}/__init__.py`
- `{target}/{Service}/{example}/tests/test_{example}.py`
- `{target}/{Service}/{example}/tests/__init__.py`

### Index Updates
- `{target}/README.md` - Update example list
- `docs/AI_PROMPTING_GUIDE.md` - Add new patterns discovered

## Success Criteria Per Template
1. Template imports without errors
2. Linter applies all applicable type-safe constant fixes
3. All tests pass
4. README properly credits original source
5. `template.validate() == []`

## Session Example

```
[User]: Import templates from ../third-party-cfn-templates

[Claude]: I'll help import CloudFormation templates. First, some questions:

1. Source path: ../third-party-cfn-templates - confirmed
2. Attribution: What's the source for README credits?
3. Target: Use default examples/generated/third_party_cfn/ ?
4. Scope: All templates or specific services?
5. Mode: Interactive (prompt before changes) or unattended?

[User]: Source is Apache-2.0 from ExampleOrg, use defaults, start with S3, interactive mode

[Claude]: Starting with S3 templates...

> Importing: S3/simple-bucket.yaml
  ├─ Created: examples/generated/third_party_cfn/S3/simple_bucket/
  ├─ Running cfn-import with linter...
  ├─ Linter applied 2 fixes:
  │   - "AES256" → ServerSideEncryption.AES256
  │   - "Enabled" → BucketVersioningStatus.ENABLED
  ├─ Creating README.md
  ├─ Creating tests...
  └─ Tests: PASS (5 tests)

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

## Notes
- Source folder should be treated as read-only
- Each imported example should be self-contained
- Tests should not require AWS credentials (local validation only)
- Prefer YAML templates over JSON when both exist (easier to read originals)
- If a template uses unsupported features, document the limitation and skip or partially import

## See Also

- [LINTER.md](LINTER.md) - Linter rules and usage
- [IMPORTER.md](IMPORTER.md) - Template importer documentation
- [AI_PROMPTING_GUIDE.md](AI_PROMPTING_GUIDE.md) - Guide for AI assistants
