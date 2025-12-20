# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planning
- Extended examples (Lambda, API Gateway, etc.)
- API documentation site (auto-generated from docstrings)
- Best practices guide and tutorials
- Contributing guidelines and code of conduct

---

## [0.4.0] - 2025-12-18

### Added
- **CloudFormation Template Importer** (`cfn-import` CLI tool)
  - Convert existing YAML/JSON CloudFormation templates to Python code
  - Three output modes:
    - **Block mode** (default): Declarative wrapper classes with `@cloudformation_dataclass`
    - **Brief mode**: Imperative style with direct variable assignments
    - **Mixed mode**: Hybrid approach with intelligent inlining
  - Mixed mode features:
    - Tag reuse detection: tags used 2+ times become wrapper classes, unique tags are inlined as `Tag()`
    - Policy document handling: converts to `PolicyDocument` and `PolicyStatement` classes
  - Supports all CloudFormation intrinsic functions (!Ref, !GetAtt, !Sub, !Join, !If, etc.)
  - Topological sorting ensures resources are defined before their dependencies
  - Supports stdin/stdout for pipeline usage
- Comprehensive importer documentation ([docs/IMPORTER.md](docs/IMPORTER.md))
- Importer test suite (71 tests)

### Changed
- Updated README.md with Tools section for importer and generator
- Documentation now clarifies `uv run cfn-import` usage for development from source

---

## [0.3.4] - 2025-12-17

### Changed
- **Generated code size reduced by 62%**: 720K → 274K lines (31 MB → 10 MB)
  - Phase 1: Data-driven resource serialization with `_property_mappings`
  - Phase 2: `PropertyType` base class for nested structures
  - Phase 3: Removed truncated documentation URL comments
  - Removed property type class docstrings
- Examples now use declarative Tag wrapper classes instead of inline `Tag()` calls:
  - VPC `vpc_with_nat.py`: Reusable `ApplicationTag`, `PublicNetworkTag`, `PrivateNetworkTag` classes
  - EC2 `ec2_with_wait_condition.py`: `WebInstanceNameTag` wrapper class

### Added
- `PropertyType` base class in `core/base.py` for CloudFormation property types
- `Tag` export in generated AWS modules for use in wrapper classes

---

## [0.3.3] - 2025-12-17

### Added
- EC2 examples (4 templates with tests):
  - `ec2_instance_with_security_group.py` - EC2 instance with SSH security group
  - `eip_with_association.py` - Elastic IP with EIPAssociation
  - `instance_with_cfn_init.py` - EC2 with cfn-init metadata
  - `ec2_with_wait_condition.py` - EC2 with WaitCondition signaling
- VPC examples (5 templates with tests):
  - `vpc_single_instance_in_subnet.py` - VPC with single EC2 instance
  - `vpc_with_public_and_private_subnets.py` - Multi-tier VPC
  - `multi_az_vpc.py` - Multi-AZ VPC with NAT gateways
  - `vpc_with_vpn_gateway.py` - VPC with VPN connectivity
  - `four_subnets.py` - VPC with 4 subnets across 2 AZs
- S3 examples:
  - `cross_account_access.py` - S3 bucket with cross-account policy
- List parameter types in `ParameterType` constants:
  - `LIST_AWS_EC2_AVAILABILITY_ZONE_NAME`
  - `LIST_AWS_EC2_IMAGE_ID`
  - `LIST_AWS_EC2_INSTANCE_ID`
  - `LIST_AWS_EC2_SECURITY_GROUP_GROUP_NAME`
  - `LIST_AWS_EC2_SECURITY_GROUP_ID`
  - `LIST_AWS_EC2_SUBNET_ID`
  - `LIST_AWS_EC2_VOLUME_ID`
  - `LIST_AWS_EC2_VPC_ID`
  - `LIST_AWS_ROUTE53_HOSTED_ZONE_ID`
- SSM parameter types:
  - `AWS_SSM_PARAMETER_NAME`
  - `AWS_SSM_PARAMETER_VALUE_STRING`
  - `AWS_SSM_PARAMETER_VALUE_LIST_STRING`
  - `AWS_SSM_PARAMETER_VALUE_COMMA_DELIMITED_LIST`

### Fixed
- `WaitConditionHandle` missing `_get_properties()` method
- `PolicyStatement._serialize_value()` now recursively serializes nested dicts and lists
- `Select` intrinsic now accepts intrinsic functions as the list argument
- Ruff configuration to allow star imports in examples for brevity

---

## [0.3.2] - 2025-12-16
- Fix use of ref() and sub()
- use date based versioning for CF spec file
- internalize CF spec file to repo
- use context project_name in resource names
- add aws constants
- add DynamoDB examples (simple_table, secondary_indexes)
- add DeploymentContext to DynamoDB examples

---

## [0.2.1] - 2025-12-15

- Fix build version

---

## [0.2.0] - 2025-12-15

### Added

**Complete AWS Service Coverage**
- Generated all 262 AWS services from CloudFormation spec
- 1,502 resource types now available
- 8,117 property types across all services
- Full support for: EC2, Lambda, IAM, DynamoDB, RDS, ECS, EKS, SageMaker, and 254 more services

**Comprehensive Test Suite**
- 128 total tests (up from 19 in v0.1.0)
- **Framework tests** (114 tests):
  - 47 tests for intrinsic functions (Ref, GetAtt, Sub, Join, If, Select, Split, etc.)
  - 41 tests for core base classes (CloudFormationResource, Tag, DeploymentContext, PolicyDocument)
  - 26 tests for wrapper decorator and DeferredRef/DeferredGetAtt patterns
- **Integration tests** (14 tests):
  - S3 resource integration tests
  - Template generation and serialization
  - Cross-resource references
  - Context-driven naming and tag merging
- Test coverage: ~36% (focused on framework functionality)
- All tests resource-agnostic for fast execution

**Documentation**
- Comprehensive test suite documentation ([tests/README.md](tests/README.md))
- Test philosophy and organization guide
- Framework vs integration test strategy

### Changed
- Updated README to reflect complete AWS service coverage
- Improved project status section with accurate completion status

### Technical Details

**Versions**
- Package version: 0.2.0
- CloudFormation spec date: 2025.12.11
- Generator version: 1.0.0
- Combined: spec-2025.12.11_gen-1.0.0

**Generated Code Statistics**
- AWS Services: 262 (up from 1 in v0.1.0)
- Resource Types: 1,502 (up from 10)
- Property Types: 8,117 (up from 56)
- Top services by resource count:
  - EC2: 110 resources
  - SageMaker: 34 resources
  - Connect: 31 resources
  - IoT: 30 resources
  - Glue: 24 resources

**Test Coverage**
- Total tests: 128 (up from 19)
- Framework tests: 114
- Integration tests: 14
- Coverage: ~36% (focused on tested paths)
- Execution time: ~0.2 seconds for all tests

**Build Artifacts**
- Package size: 1.9 MB (wheel)
- Source distribution: 1.7 MB (tar.gz)

### Fixed
- macOS compatibility in regenerate.sh script (replaced `readarray` with bash 3.2-compatible loop)

---

## [0.1.0] - 2025-12-15

### Added

**Core Foundation**
- `CloudFormationResource` base class with resource serialization
- `Tag` class with automatic snake_case to PascalCase conversion
- `DeploymentContext` base class for environment configuration
- `PolicyDocument` and `PolicyStatement` classes for IAM policies
- Template system (`Template`, `Parameter`, `Output`, `Condition`, `Mapping`)
- Complete intrinsic functions (Ref, GetAtt, Sub, Join, If, Select, Split, etc.)
- `@cloudformation_dataclass` decorator for declarative resource definitions

**Deployment Context Features**
- Automatic resource naming with configurable patterns
- Context parameter support (component, stage, deployment_name, deployment_group, region)
- Blue/green deployment support via `deployment_group` parameter
- Automatic tag merging (context tags + resource-specific tags)
- Custom naming patterns per context and per resource

**Code Generation**
- CloudFormation spec parser and downloader
- Automatic Python class generation from CloudFormation specs
- Type mapping (CloudFormation types → Python types)
- Snake_case property conversion (PascalCase → snake_case)
- Complete S3 service generation (10 resources, 56 property types)

**AWS Services**
- **S3**: Complete service with all resources and property types
  - Bucket with encryption, versioning, lifecycle, etc.
  - BucketPolicy with policy document integration
  - All S3-related property types

**Build & Distribution**
- Package configuration with hatchling build system
- Version management system (dual-version: spec + generator)
- Build automation scripts (build.sh, test.sh, regenerate.sh)
- GitHub Actions CI/CD workflows
- Automated PyPI publishing on releases

**Testing**
- Framework validation test suite (14 tests)
- Example-focused test suite (5 tests)
- Test coverage reporting
- Test automation scripts

**Documentation**
- Comprehensive README with examples
- Developer guide (docs/DEVELOPERS.md)
- Project checklist (docs/CHECKLIST.md)
- S3 bucket example with encryption and policies

**Repository Management**
- GitHub issue templates (bug report, feature request)
- Pull request template
- .gitignore and .gitattributes configuration

### Technical Details

**Versions**
- Package version: 0.1.0
- CloudFormation spec date: 2025.12.11
- Generator version: 1.0.0
- Combined: spec-2025.12.11_gen-1.0.0

**Generated Code Statistics**
- AWS Services: 1 (S3)
- Resource Types: 10
- Property Types: 56
- Total Lines: 2,969

**Test Coverage**
- Total tests: 19
- Framework tests: 14
- Example tests: 5
- Coverage: ~35% (focused on tested paths)

### Design Decisions

1. **Declarative Block Syntax**: Use `@cloudformation_dataclass` decorator with typed fields
2. **Zero Runtime Dependencies**: Core package has no dependencies (pyyaml optional)
3. **Type Safety**: Full Python type hints for IDE support and static analysis
4. **Generated Code**: All AWS resources auto-generated from official CloudFormation specs
5. **Version Pinning**: Explicit version tracking for reproducible builds
6. **Pythonic Naming**: snake_case properties mapping to CloudFormation PascalCase

### Known Limitations

- Only S3 service is generated (by design for v0.1.0)
- No runtime validation (relies on static type checking + CloudFormation validation)
- No higher-level constructs or patterns library
- No deployment integration (boto3 integration planned for future)

---

## Version History Legend

### Types of Changes
- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security vulnerability fixes

### Version Numbering

This project uses three independent versions:

1. **Package Version** (0.4.0) - Semantic versioning for the package
   - MAJOR: Breaking API changes
   - MINOR: New features, backward compatible
   - PATCH: Bug fixes, backward compatible

2. **CloudFormation Spec Date** (2025.12.11) - Date from AWS Last-Modified header
   - Format: YYYY.MM.DD
   - Updated when AWS releases new CloudFormation spec
      - Always triggers regeneration of affected services
   - Spec file committed to `specs/` for reproducibility

3. **Generator Version** (1.0.0) - Code generator version
   - MAJOR: Breaking changes to generated code structure
   - MINOR: New generator features or optimizations
   - PATCH: Bug fixes in generator

Combined version format: `spec-{SPEC_DATE}_gen-{GEN_VERSION}`

---

## Release Process

### For Package Updates (Bug Fixes, New Features)

1. Update version in `pyproject.toml`
2. Update version in `src/cloudformation_dataclasses/__version__.py`
3. Update version in `src/cloudformation_dataclasses/__init__.py` docstring
4. Add entry to this CHANGELOG under "Unreleased"
5. Run tests: `./scripts/test.sh`
6. Build package: `./scripts/build.sh`
7. Create git tag: `git tag v0.x.x`
8. Push tag: `git push origin v0.x.x`
9. Create GitHub release (triggers PyPI publish)
10. Move CHANGELOG entry from "Unreleased" to new version section

### For CloudFormation Spec Updates

1. Check for updates: `uv run python -m cloudformation_dataclasses.codegen.spec_parser check`
2. Download new spec: `uv run python -m cloudformation_dataclasses.codegen.spec_parser update`
3. Update `CLOUDFORMATION_SPEC_DATE` and `CLOUDFORMATION_SPEC_AWS_VERSION` in `config.py`
4. Regenerate services: `./scripts/regenerate.sh S3` (or other services)
5. Add entry to CHANGELOG under "Changed" section
6. Commit spec file along with generated code: `git add specs/CloudFormationResourceSpecification.json`
7. Follow package update process above

### For Generator Bug Fixes

1. Fix generator code in `src/cloudformation_dataclasses/codegen/generator.py`
2. Update only `GENERATOR_VERSION` in `config.py` (patch bump)
3. Regenerate affected services: `./scripts/regenerate.sh S3`
4. Add entry to CHANGELOG under "Fixed" section
5. Follow package update process above

---

**Links**
- [PyPI](https://pypi.org/project/cloudformation-dataclasses/)
- [GitHub](https://github.com/lex00/cloudformation_dataclasses)
- [Documentation](README.md)
- [Developer Guide](docs/DEVELOPERS.md)

---

*This changelog is maintained according to [Keep a Changelog](https://keepachangelog.com/).*
