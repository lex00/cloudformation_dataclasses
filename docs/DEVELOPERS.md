# Developer Guide

This guide provides comprehensive information for developers working on `cloudformation_dataclasses`.

## Table of Contents

- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Building the Project](#building-the-project)
- [Running Tests](#running-tests)
- [Code Generation](#code-generation)
- [Version Management](#version-management)
- [Publishing Releases](#publishing-releases)
- [CI/CD Pipeline](#cicd-pipeline)
- [Contributing Guidelines](#contributing-guidelines)

---

## Development Setup

### Prerequisites

- **Python 3.13+** (required)
- **uv** (recommended package manager)
- **git** (version control)

### Installing uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Clone and Setup

```bash
# Clone repository
git clone https://github.com/lex00/cloudformation_dataclasses.git
cd cloudformation_dataclasses

# Install dependencies (creates .venv automatically)
uv sync --all-extras

# Activate virtual environment (optional - uv run handles this)
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate  # Windows
```

### Verify Installation

```bash
# Check package version
uv run python -c "from cloudformation_dataclasses import __version__; print(__version__)"

# Run tests
uv run pytest tests/ examples/ -v
```

---

## Project Structure

```
cloudformation_dataclasses/
├── src/cloudformation_dataclasses/     # Source code
│   ├── core/                           # Core base classes
│   │   ├── base.py                     # CloudFormationResource, DeploymentContext, Tag
│   │   ├── constants.py                # CloudFormation parameter type constants
│   │   ├── template.py                 # Template, Parameter, Output, Condition
│   │   └── wrapper.py                  # @cloudformation_dataclass decorator
│   ├── intrinsics/                     # Intrinsic functions
│   │   └── functions.py                # Ref, GetAtt, Sub, Join, etc.
│   ├── codegen/                        # Code generation tools (dev-time only)
│   │   ├── config.py                   # Version configuration
│   │   ├── spec_parser.py              # CloudFormation spec parser
│   │   ├── botocore_enums.py           # Botocore enum extraction
│   │   └── generator.py                # AWS resource generator
│   ├── linter/                         # Linter for detecting/fixing common mistakes
│   │   ├── __init__.py                 # Public API: lint_code(), fix_code()
│   │   ├── rules.py                    # Lint rules (CFD001-CFD005)
│   │   └── introspection.py            # Type introspection utilities
│   ├── constants/                      # Shared constant mappings
│   │   └── __init__.py                 # Condition operators, pseudo-params, etc.
│   ├── aws/                            # Generated AWS resources (262 services)
│   │   ├── s3.py                       # S3 resources
│   │   ├── dynamodb.py                 # DynamoDB resources
│   │   ├── lambda_.py                  # Lambda resources
│   │   └── ...                         # All other AWS services
│   ├── __init__.py                     # Package entry point
│   └── __version__.py                  # Version information
├── specs/                              # CloudFormation spec (committed)
│   └── CloudFormationResourceSpecification.json
├── tests/                              # Framework validation tests
├── examples/                           # Usage examples
│   ├── s3_bucket/                      # S3 bucket example
│   └── aws_cloudformation_templates/   # DynamoDB examples
├── scripts/                            # Automation scripts
│   ├── build.sh                        # Build automation
│   ├── test.sh                         # Test automation
│   └── regenerate.sh                   # Code regeneration
├── .github/                            # GitHub configuration
│   ├── workflows/                      # CI/CD workflows
│   │   ├── ci.yml                      # Continuous Integration
│   │   └── release.yml                 # Release automation
│   ├── ISSUE_TEMPLATE/                 # Issue templates
│   └── PULL_REQUEST_TEMPLATE.md        # PR template
├── pyproject.toml                      # Package configuration
├── README.md                           # User documentation
├── GENERATOR.md                        # Code generator architecture docs
├── DEVELOPERS.md                       # This file
└── CHANGELOG.md                        # Version history
```

---

## Building the Project

### Quick Build

```bash
# Full build with tests
./scripts/build.sh

# Build without tests (faster)
./scripts/build.sh --skip-tests

# Clean build artifacts only
./scripts/build.sh --clean-only
```

### Manual Build Steps

```bash
# 1. Clean previous builds
rm -rf dist/ build/ *.egg-info

# 2. Run tests
uv run pytest tests/ examples/ -v

# 3. Build package
uv build

# 4. Verify artifacts
ls -lh dist/
# Should see:
#   cloudformation_dataclasses-0.1.0-py3-none-any.whl
#   cloudformation_dataclasses-0.1.0.tar.gz
```

### Build Outputs

- **Wheel** (`.whl`) - Binary distribution, fast installation
- **Source Distribution** (`.tar.gz`) - Source code archive

### Testing the Build

```bash
# Install locally from wheel
uv pip install dist/*.whl

# Test the installation
python -c "from cloudformation_dataclasses import __version__; print(__version__)"

# Uninstall
uv pip uninstall cloudformation_dataclasses
```

---

## Running Tests

### Test Scripts

```bash
# Run all tests with coverage
./scripts/test.sh

# Run tests without coverage (faster)
./scripts/test.sh --fast

# Run only framework tests
./scripts/test.sh --framework-only

# Run only example tests
./scripts/test.sh --examples-only

# Verbose output
./scripts/test.sh -v
```

### Manual Test Execution

```bash
# All tests
uv run pytest tests/ examples/ -v

# Specific test file
uv run pytest tests/test_s3_resources.py -v

# Specific test
uv run pytest tests/test_s3_resources.py::test_bucket_creation -v

# With coverage
uv run pytest tests/ examples/ --cov=cloudformation_dataclasses --cov-report=term-missing

# Watch mode (requires pytest-watch)
uv run ptw tests/ examples/
```

### Test Structure

- **tests/** - Framework validation (129 tests)
  - Core functionality tests
  - Resource creation and serialization
  - Template generation
  - Intrinsic functions
  - Tag merging and context-driven naming

- **examples/*/tests/** - Example tests (24 tests)
  - User-focused demonstrations
  - Real-world usage patterns
  - DynamoDB examples with secondary indexes

---

## Code Generation

The generator combines two data sources to produce type-safe Python modules:

1. **CloudFormation Resource Specification** - Defines resource types, properties, and structure
2. **Botocore Service Models** - Provides enum values and property-to-enum mappings

For detailed architecture documentation, see [GENERATOR.md](./GENERATOR.md).

### CloudFormation Spec Version

The project uses **pinned versions** for reproducible builds:

```python
# src/cloudformation_dataclasses/codegen/config.py
CLOUDFORMATION_SPEC_DATE = "2025.12.11"  # Date from AWS Last-Modified header
GENERATOR_VERSION = "1.0.0"              # Our generator version
COMBINED_VERSION = "spec-2025.12.11_gen-1.0.0"
```

The CloudFormation spec file is **committed to the repository** in `specs/CloudFormationResourceSpecification.json` for reproducibility.

### Regenerating Services

```bash
# List available AWS services
./scripts/regenerate.sh --list

# Check for spec updates from AWS
uv run python -m cloudformation_dataclasses.codegen.spec_parser check

# Regenerate S3 service
./scripts/regenerate.sh S3

# Regenerate multiple services
./scripts/regenerate.sh S3 EC2 Lambda

# Regenerate all services (takes time!)
./scripts/regenerate.sh --all

# Skip tests after regeneration
./scripts/regenerate.sh S3 --skip-tests
```

### Manual Code Generation

```bash
# Download/verify CloudFormation spec
uv run python -m cloudformation_dataclasses.codegen.spec_parser download

# List available services
uv run python -m cloudformation_dataclasses.codegen.spec_parser list-services

# Generate specific service
uv run python -m cloudformation_dataclasses.codegen.generator --service S3

# Generated code location
# → src/cloudformation_dataclasses/aws/s3.py
```

### Generated Code Metadata

All generated files include version metadata:

```python
"""
AWS CloudFormation S3 Resources

⚠️  AUTO-GENERATED FILE - DO NOT EDIT MANUALLY ⚠️

Version Information:
  CloudFormation Spec: 2025.12.11
  Generator Version: 1.0.0
  Combined: spec-2025.12.11_gen-1.0.0
  Generated: 2024-12-15 13:18:57
"""
```

---

## Version Management

### Version Components

The project uses **three independent versions**:

1. **Package Version** (`pyproject.toml`)
   ```toml
   [project]
   version = "0.4.0"
   ```

2. **CloudFormation Spec Date** (`config.py`)
   ```python
   CLOUDFORMATION_SPEC_DATE = "2025.12.11"  # Date from AWS Last-Modified header
   ```

3. **Generator Version** (`config.py`)
   ```python
   GENERATOR_VERSION = "1.0.0"
   ```

### When to Bump Versions

**Package Version** (semantic versioning):
- **MAJOR** (1.0.0): Breaking API changes
- **MINOR** (0.2.0): New features, backward compatible
- **PATCH** (0.1.1): Bug fixes, backward compatible

**CloudFormation Spec Date** (YYYY.MM.DD format):
- Update when AWS releases new CloudFormation spec
- Date is derived from AWS's Last-Modified header
- Always triggers regeneration of all services

**Generator Version** (semantic versioning):
- **MAJOR**: Breaking changes to generated code structure
- **MINOR**: New generator features or optimizations
- **PATCH**: Bug fixes in generator

### Version Update Workflow

#### Updating CloudFormation Spec

```bash
# 1. Check for updates from AWS
uv run python -m cloudformation_dataclasses.codegen.spec_parser check

# 2. Download and save new spec
uv run python -m cloudformation_dataclasses.codegen.spec_parser update

# 3. Update config.py with new date (shown in update output)
# CLOUDFORMATION_SPEC_DATE = "2025.12.15"  # New date from AWS

# 4. Regenerate services
./scripts/regenerate.sh S3

# 5. Test
./scripts/test.sh

# 6. Commit (including the updated spec file)
git add specs/CloudFormationResourceSpecification.json
git add src/cloudformation_dataclasses/codegen/config.py
git add src/cloudformation_dataclasses/aws/
git commit -m "Update to CloudFormation spec 2025.12.15"
```

#### Patching Generator

```bash
# 1. Fix generator code
vim src/cloudformation_dataclasses/codegen/generator.py

# 2. Update only generator version in config.py
# CLOUDFORMATION_SPEC_DATE = "2025.12.11"  # Unchanged
# GENERATOR_VERSION = "1.0.1"              # Patch bump

# 3. Regenerate affected service
./scripts/regenerate.sh S3

# 4. Test
./scripts/test.sh

# 5. Commit
git commit -m "Fix S3 property serialization (generator v1.0.1)"
```

#### Updating Package Version

When bumping the package version, update these files:

| File | What to Update |
|------|----------------|
| `pyproject.toml` | `version = "X.Y.Z"` |
| `src/cloudformation_dataclasses/__version__.py` | `__version__ = "X.Y.Z"` |
| `README.md` | Version references in "Check Installed Version" and "Current Release" sections |
| `CHANGELOG.md` | Add new version section, update version in "Version Numbering" |

```bash
# 1. Update pyproject.toml
# [project]
# version = "0.4.0"

# 2. Update __version__.py
# __version__ = "0.4.0"

# 3. Update README.md version references
# - print(__version__)  # Package version: 0.4.0
# - **Current Release: v0.4.0**
# - Package: `0.4.0`

# 4. Update CHANGELOG.md
# - Add new ## [0.4.0] - YYYY-MM-DD section
# - Update Package Version example in Version Numbering section

# 5. Build and test
./scripts/build.sh

# 6. Verify version is correct
uv run python -c "from cloudformation_dataclasses import __version__; print(__version__)"

# 7. Commit
git commit -m "Bump version to 0.4.0"
```

**Note**: The `cfn-import` CLI automatically uses the version from `__version__.py`, so no separate update is needed there.

---

## Publishing Releases

### Pre-Release Checklist

- [ ] All tests passing (`./scripts/test.sh`)
- [ ] Package builds successfully (`./scripts/build.sh`)
- [ ] Version numbers updated (package, __version__.py, __init__.py)
- [ ] CHANGELOG.md updated with release notes
- [ ] Documentation up to date (README.md, DEVELOPERS.md)
- [ ] Examples tested manually
- [ ] No pending TODO items for this release

### Release Methods

#### Method 1: Automated (GitHub Release)

**Recommended for production releases**

```bash
# 1. Create and push git tag
git tag v0.1.0
git push origin v0.1.0

# 2. Create GitHub release
# Go to: https://github.com/lex00/cloudformation_dataclasses/releases/new
# - Select tag: v0.1.0
# - Title: "v0.1.0 - Initial Release"
# - Description: Copy from CHANGELOG.md
# - Click "Publish release"

# 3. GitHub Actions will automatically:
#    - Run tests
#    - Build package
#    - Upload artifacts to release
#    - Publish to PyPI (via trusted publishing)
```

#### Method 2: Manual Publishing

**For testing or one-off releases**

```bash
# 1. Build package
./scripts/build.sh

# 2. Publish to TestPyPI (test first!)
uv publish --repository testpypi dist/*

# 3. Test installation from TestPyPI
uv pip install --index-url https://test.pypi.org/simple/ cloudformation_dataclasses

# 4. Publish to PyPI (production)
uv publish dist/*
```

### PyPI Trusted Publishing Setup

**One-time setup for automated publishing:**

1. Go to https://pypi.org/manage/account/publishing/
2. Add a new publisher:
   - **PyPI Project Name**: `cloudformation_dataclasses`
   - **Owner**: `lex00`
   - **Repository**: `cloudformation_dataclasses`
   - **Workflow**: `release.yml`
   - **Environment**: (leave empty)

This allows GitHub Actions to publish without API tokens.

### Post-Release Tasks

```bash
# 1. Verify package on PyPI
# https://pypi.org/project/cloudformation_dataclasses/

# 2. Test installation
uv pip install cloudformation_dataclasses

# 3. Update documentation
# - Add release notes to CHANGELOG.md
# - Update README.md if needed

# 4. Announce release
# - GitHub Discussions
# - Social media
# - Community channels
```

---

## CI/CD Pipeline

### Continuous Integration (.github/workflows/ci.yml)

**Triggers**: Push to main/develop, Pull Requests

**Jobs**:
1. **Test** - Run test suite with coverage
   - Python 3.13 on Ubuntu
   - Upload coverage to Codecov

2. **Lint** - Code quality checks
   - ruff (linter)
   - black (formatter)
   - mypy (type checker)

3. **Build** - Build package
   - Create wheel and sdist
   - Verify artifacts
   - Upload for download

4. **Verify Spec** - Validate CloudFormation spec version

### Release Automation (.github/workflows/release.yml)

**Triggers**: GitHub Release published

**Steps**:
1. Run full test suite
2. Build package distributions
3. Upload artifacts to GitHub release
4. Publish to PyPI (via trusted publishing)

### Local CI Simulation

```bash
# Run what CI runs
./scripts/test.sh                    # Tests
uv run ruff check src/ tests/        # Linting
uv run black --check src/ tests/     # Formatting
uv run mypy src/cloudformation_dataclasses/  # Type checking
./scripts/build.sh                   # Build
```

---

## Contributing Guidelines

### Code Style

- **Formatting**: Use `black` (line length 100)
- **Linting**: Use `ruff`
- **Type Hints**: Required for all public APIs
- **Docstrings**: Google style for public functions/classes

**Note**: The generated `aws/` directory is excluded from linting/formatting since it's auto-generated.

```bash
# Format code (excludes generated aws/ directory)
uv run black src/ tests/ examples/

# Check linting (excludes generated aws/ directory)
uv run ruff check src/ tests/ examples/

# Auto-fix linting issues
uv run ruff check src/ --fix

# Type check
uv run mypy src/cloudformation_dataclasses/
```

### Commit Messages

Follow conventional commits:

```
feat: Add support for EC2 resources
fix: Correct S3 bucket serialization
docs: Update installation instructions
test: Add tests for context-driven naming
chore: Update dependencies
```

### Pull Request Process

1. **Fork and clone** the repository
2. **Create feature branch**: `git checkout -b feature/my-feature`
3. **Make changes** with tests
4. **Run tests**: `./scripts/test.sh`
5. **Commit changes** with clear messages
6. **Push to fork**: `git push origin feature/my-feature`
7. **Open Pull Request** with description
8. **Wait for CI** to pass
9. **Address review comments**
10. **Merge** when approved

### Development Workflow

```bash
# 1. Create feature branch
git checkout -b feature/add-lambda-support

# 2. Make changes
vim src/cloudformation_dataclasses/aws/lambda.py

# 3. Regenerate if needed
./scripts/regenerate.sh Lambda

# 4. Add tests
vim tests/test_lambda_resources.py

# 5. Run tests
./scripts/test.sh

# 6. Format and lint
uv run black src/ tests/
uv run ruff check src/ tests/

# 7. Commit
git add .
git commit -m "feat: Add Lambda resource support"

# 8. Push
git push origin feature/add-lambda-support

# 9. Open PR on GitHub
```

---

## Troubleshooting

### Common Issues

**Import Errors**
```bash
# Ensure dependencies are installed
uv sync --all-extras
```

**Test Failures**
```bash
# Run tests with verbose output
./scripts/test.sh -v

# Run specific test
uv run pytest tests/test_s3_resources.py::test_bucket_creation -vv
```

**Build Failures**
```bash
# Clean and rebuild
./scripts/build.sh --clean-only
./scripts/build.sh
```

**Version Mismatch**
```bash
# Verify CloudFormation spec version
uv run python -m cloudformation_dataclasses.codegen.spec_parser version
```

### Getting Help

- **Issues**: https://github.com/lex00/cloudformation_dataclasses/issues
- **Discussions**: https://github.com/lex00/cloudformation_dataclasses/discussions
- **Documentation**: See README.md and CLAUDE.md

---

## Additional Resources

- **User Guide**: [README.md](../README.md) - End-user documentation
- **Template Importer**: [IMPORTER.md](./IMPORTER.md) - Convert CloudFormation templates to Python
- **Linter**: [LINTER.md](./LINTER.md) - Detect and fix common mistakes
- **AI Prompting Guide**: [AI_PROMPTING_GUIDE.md](./AI_PROMPTING_GUIDE.md) - Tips for AI assistants
- **Generator Docs**: [GENERATOR.md](./GENERATOR.md) - Code generator architecture
- **Changelog**: [CHANGELOG.md](../CHANGELOG.md) - Version history and release notes
- **CloudFormation Docs**: https://docs.aws.amazon.com/AWSCloudFormation/

---

**Last Updated**: 2025-12-18
**For**: v0.4.0 (spec-2025.12.11_gen-1.0.0)
