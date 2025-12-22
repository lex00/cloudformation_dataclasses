# Versioning

This document explains the versioning system for cloudformation_dataclasses.

## Version Types

The project maintains **three independent version streams**:

| Version | Format | Purpose |
|---------|--------|---------|
| **Package Version** | Semantic (X.Y.Z) | PyPI releases, API changes |
| **CloudFormation Spec Date** | Date (YYYY.MM.DD) | Track AWS spec updates |
| **Generator Version** | Semantic (X.Y.Z) | Track code generator changes |

### Package Version

The main version for PyPI releases. Follows [Semantic Versioning](https://semver.org/):

- **MAJOR** (X): Breaking API changes
- **MINOR** (Y): New features, backwards compatible
- **PATCH** (Z): Bug fixes, backwards compatible

**Locations:**
- `pyproject.toml` - Line 3
- `src/cloudformation_dataclasses/__version__.py` - Line 17

### CloudFormation Spec Date

Tracks which AWS CloudFormation spec was used to generate resource classes.

**Format:** `YYYY.MM.DD` from the AWS `Last-Modified` header.

**Location:** `src/cloudformation_dataclasses/codegen/config.py`

### Generator Version

Tracks changes to the code generation logic itself.

**Location:** `src/cloudformation_dataclasses/codegen/config.py`

---

## Bumping the Package Version

Use the bump script:

```bash
./scripts/bump_version.sh 0.6.0
```

This automatically updates:
1. `pyproject.toml`
2. `src/cloudformation_dataclasses/__version__.py`
3. `src/cloudformation_dataclasses/__init__.py` (docstring)
4. `CHANGELOG.md` (adds placeholder section)

### Manual Steps After Bumping

1. **Edit CHANGELOG.md** - Fill in the changes for the new version
2. **Run tests** - `./scripts/test.sh`
3. **Commit** - `git commit -am "Bump version to X.Y.Z"`
4. **Tag** - `git tag vX.Y.Z`
5. **Push** - `git push && git push --tags`

---

## Bumping the CloudFormation Spec

When AWS releases a new CloudFormation spec:

1. Run the regeneration script:
   ```bash
   ./scripts/regenerate.sh --all
   ```

2. Update the spec date in `src/cloudformation_dataclasses/codegen/config.py`:
   ```python
   CLOUDFORMATION_SPEC_DATE = "YYYY.MM.DD"
   ```

3. Run tests to verify generated code works

4. Bump the package version (usually minor bump)

---

## Bumping the Generator Version

When changing the code generator logic:

1. Update `GENERATOR_VERSION` in `src/cloudformation_dataclasses/codegen/config.py`

2. Regenerate all services:
   ```bash
   ./scripts/regenerate.sh --all
   ```

3. Run tests

4. Bump the package version

---

## Viewing Current Versions

### From Python

```python
from cloudformation_dataclasses import print_version_info
print_version_info()
```

### From CLI

```bash
cfn-dataclasses-import --version
```

### Programmatically

```python
from cloudformation_dataclasses import (
    __version__,
    __cf_spec_date__,
    __generator_version__,
    __combined_version__,
    get_version_info,
)

print(__version__)        # "0.5.2"
print(__cf_spec_date__)   # "2025.12.11"
print(get_version_info()) # {"package": "0.5.2", ...}
```

---

## Version in Generated Code

All generated AWS resource files include version metadata in their headers:

```python
"""
AWS S3 CloudFormation resources.

Version Information:
  CloudFormation Spec: 2025.12.11
  Generator Version: 1.0.0
  Combined: spec-2025.12.11_gen-1.0.0
  Generated: 2025-12-21 00:10:06
"""
```

---

## See Also

- [CHANGELOG.md](../CHANGELOG.md) - Version history
- [DEVELOPERS.md](DEVELOPERS.md) - Full development guide
