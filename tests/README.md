# Test Suite Documentation

This directory contains the comprehensive test suite for the cloudformation_dataclasses framework.

## Test Organization

The test suite is organized into **framework tests** (resource-agnostic) and **integration tests** (service-specific).

### Framework Tests (Resource-Agnostic)

These tests validate core framework functionality without depending on any specific AWS service:

#### [test_intrinsics.py](test_intrinsics.py) - 47 tests
Tests all CloudFormation intrinsic functions to ensure correct serialization to CloudFormation JSON format.

**Coverage:**
- **Basic functions**: `Ref`, `GetAtt`, `Sub`, `Join`, `Select`, `Split`
- **Conditionals**: `If`, `Equals`, `And`, `Or`, `Not`
- **Utility functions**: `Base64`, `GetAZs`, `ImportValue`, `FindInMap`, `Cidr`
- **Complex combinations**: Nested intrinsics, deeply nested structures

**Example:**
```python
def test_ref_basic():
    ref = Ref(logical_id="MyVPC")
    assert ref.to_dict() == {"Ref": "MyVPC"}

def test_sub_with_variables():
    sub = Sub(
        template_string="My ${Key1} is ${Key2}",
        variables={"Key1": "value1", "Key2": Ref("Parameter")}
    )
    # Verifies nested intrinsic serialization
```

**Why these tests are valuable:**
- Fast execution (pure Python, no AWS resources)
- Test intrinsic function logic in isolation
- Validate CloudFormation JSON output format
- Cover edge cases and complex nesting scenarios

#### [test_core.py](test_core.py) - 41 tests
Tests core base classes that all resources inherit from.

**Coverage:**
- **Tag**: Creation and CloudFormation serialization
- **PolicyStatement & DenyStatement**: IAM policy statements with principals, actions, resources, and conditions
- **PolicyDocument**: IAM policy documents with statement lists
- **DeploymentContext**:
  - Resource naming patterns (`{component}-{resource_name}-{stage}-...`)
  - Blue/green deployments via `deployment_group`
  - Tag merging (context tags + resource-specific tags)
  - Custom naming pattern overrides
- **CloudFormationResource**:
  - Logical ID management
  - Context-driven resource naming
  - Tag merging from context
  - `ref()` and `get_att()` helper methods
  - CloudFormation attributes (`DependsOn`, `Condition`, `DeletionPolicy`, `UpdateReplacePolicy`, `Metadata`)

**Example:**
```python
def test_deployment_context_resource_naming():
    ctx = TestContext(
        component="DataPlatform",
        stage="prod",
        deployment_name="001",
        deployment_group="blue",
        region="us-east-1"
    )
    name = ctx.resource_name("MyData")
    assert name == "DataPlatform-MyData-prod-001-blue-us-east-1"
```

**Why these tests are valuable:**
- Validate core abstractions all resources depend on
- Test resource naming logic crucial for blue/green deployments
- Ensure tag merging works correctly
- Verify CloudFormation attribute handling

#### [test_wrapper.py](test_wrapper.py) - 26 tests
Tests the `@cloudformation_dataclass` decorator and wrapper pattern.

**Coverage:**
- **Wrapper detection**: `is_wrapper_dataclass()`, `get_wrapped_resource_type()`
- **DeferredRef & DeferredGetAtt**: Cross-resource references with `ref()` and `get_att()` helpers
- **Decorator functionality**:
  - Auto-instantiation (no constructor parameters needed)
  - Automatic logical ID setting from class name
  - Context field support
  - Mutable default handling
  - Nested wrapper classes
  - Post-init preservation
- **Resource creation**: `create_wrapped_resource()` with tags, deferred refs, lists of wrappers
- **Integration tests**: Full workflows with deployment context, tag merging, cross-resource references

**Example:**
```python
def test_decorator_basic():
    @cloudformation_dataclass
    class MyResource:
        resource: TestResource
        test_prop: str = "custom"

    # No parameters needed!
    instance = MyResource()
    assert instance.resource.test_prop == "custom"
    assert instance.resource.logical_id == "MyResource"
```

**Why these tests are valuable:**
- Validate the declarative block syntax pattern
- Test the "magic" that makes zero-boilerplate instantiation work
- Ensure cross-resource references work correctly
- Verify context integration

### Integration Tests (Service-Specific)

#### [test_s3_resources.py](test_s3_resources.py) - 14 tests
Integration tests using actual generated S3 resources.

**Coverage:**
- S3 Bucket creation with wrapper pattern
- Bucket encryption configuration (nested property types)
- Bucket policies with IAM policy documents
- Cross-resource references (`ref()` between bucket and policy)
- Context-driven naming with S3 resources
- Tag merging with real S3 resources
- Template generation and validation
- Complete CloudFormation JSON serialization

**Example:**
```python
def test_bucket_with_encryption():
    @cloudformation_dataclass
    class MyBucket:
        resource: Bucket
        bucket_encryption = MyBucketEncryption

    bucket = MyBucket()
    # Verifies nested property type serialization
    cf_dict = bucket.resource.to_dict()
    assert "BucketEncryption" in cf_dict["Properties"]
```

**Why these tests are valuable:**
- **Smoke test**: Verify code generation produces usable resources
- **Integration test**: Validate framework + generated code work together
- **Regression safety**: Catch breaking changes in generator
- **Real-world validation**: Test actual AWS resource patterns
- **Documentation**: Demonstrate how generated resources work

**Note**: These tests have lower priority now that comprehensive framework tests exist. They primarily serve as integration/smoke tests rather than validating unique functionality.

## Test Statistics

### Overall Coverage
- **Total tests**: 128
- **Framework tests**: 114 (resource-agnostic)
- **Integration tests**: 14 (S3-specific)
- **Example tests**: 5 (in `examples/with_context/s3_bucket/tests/`)

### Code Coverage
- `intrinsics/functions.py`: 100%
- `core/base.py`: 100%
- `core/wrapper.py`: 87%
- `core/template.py`: 60%
- Overall project: ~36%

### Execution Speed
- All 128 tests run in ~0.2 seconds
- Framework tests are extremely fast (no AWS resource instantiation)
- Integration tests are still fast due to mock resources

## Test Philosophy

### Why Resource-Agnostic Tests?

The framework tests are intentionally **resource-agnostic** - they don't depend on any generated AWS service code (S3, EC2, Lambda, etc.). This design has several advantages:

1. **Fast execution**: No heavy resource instantiation
2. **Focused testing**: Each test validates one specific capability
3. **Portable**: Work even if you change/remove generated services
4. **Independence**: Framework tests don't break when generator changes
5. **Early validation**: Test core logic before code generation

### Test Mock Pattern

Framework tests use simple mock resources:

```python
@dataclass
class TestResource(CloudFormationResource):
    resource_type = "AWS::Test::Resource"
    test_property: str = "default"

    def _get_properties(self):
        return {"TestProperty": self.test_property}
```

This allows testing framework behavior without coupling to AWS CloudFormation specifications.

### Integration Test Strategy

**S3 tests serve as integration tests** to verify:
- Code generator produces valid resource classes
- Generated resources work with the framework
- Real-world AWS patterns serialize correctly

**We don't need extensive resource-specific tests** for each AWS service because:
- Framework tests already validate all patterns
- Code generator uses the same logic for all services
- One service (S3) is sufficient for integration testing

**Recommendation**: When adding new AWS services, include 1-2 smoke tests max, not comprehensive test suites.

## Running Tests

### Run All Tests
```bash
# All tests (framework + integration + examples)
uv run pytest tests/ examples/ -v

# With coverage
uv run pytest tests/ examples/ --cov=src/cloudformation_dataclasses
```

### Run Specific Test Files
```bash
# Framework tests only
uv run pytest tests/test_intrinsics.py tests/test_core.py tests/test_wrapper.py -v

# Integration tests only
uv run pytest tests/test_s3_resources.py -v

# Example tests only
uv run pytest examples/ -v
```

### Run Specific Test Classes or Functions
```bash
# Single test class
uv run pytest tests/test_intrinsics.py::TestRef -v

# Single test function
uv run pytest tests/test_core.py::TestDeploymentContext::test_deployment_context_blue_green -v
```

### Test Options
```bash
# Verbose output
uv run pytest -v

# Show print statements
uv run pytest -s

# Stop on first failure
uv run pytest -x

# Run only failed tests from last run
uv run pytest --lf

# Run tests matching pattern
uv run pytest -k "test_ref" -v
```

## Writing New Tests

### For Framework Features

When adding new framework features, write **resource-agnostic tests**:

```python
# tests/test_new_feature.py
from dataclasses import dataclass
from cloudformation_dataclasses.core.base import CloudFormationResource

class TestNewFeature:
    """Tests for new framework feature."""

    def test_feature_basic(self):
        """Test basic usage of new feature."""
        @dataclass
        class TestResource(CloudFormationResource):
            resource_type = "AWS::Test::Resource"
            def _get_properties(self):
                return {}

        # Test your feature here
        assert something
```

### For Generated Resources

When adding new AWS services, write **minimal smoke tests**:

```python
# tests/test_ec2_resources.py (if needed)
def test_ec2_instance_basic_creation():
    """Smoke test: Can we create and serialize an EC2 instance?"""
    @cloudformation_dataclass
    class MyInstance:
        resource: Instance
        instance_type: str = "t3.micro"

    instance = MyInstance()
    cf_dict = instance.resource.to_dict()
    assert cf_dict["Type"] == "AWS::EC2::Instance"
    assert cf_dict["Properties"]["InstanceType"] == "t3.micro"
```

**Don't write extensive resource-specific tests** - framework tests already cover all the patterns.

### For Code Generator

When modifying the code generator, test **the generator itself**:

```python
# tests/test_codegen.py (future)
def test_generator_creates_valid_resource_class():
    """Test generator produces valid CloudFormationResource subclass."""
    # Mock CloudFormation spec data
    spec_data = {...}

    # Run generator
    generated_code = generate_resource(spec_data)

    # Verify output structure
    assert "class Bucket(CloudFormationResource):" in generated_code
    assert "resource_type = 'AWS::S3::Bucket'" in generated_code
```

This tests code generation logic directly rather than indirectly through generated resources.

## Test Maintenance

### When Framework Changes
- Update `test_core.py`, `test_intrinsics.py`, or `test_wrapper.py`
- Ensure all framework tests still pass
- Integration tests (S3) should automatically work if framework is correct

### When Generator Changes
- Run S3 integration tests to verify generated code still works
- Consider adding generator-specific tests if logic changes significantly
- Don't add more resource-specific tests for each service

### When Adding AWS Services
- **Don't write comprehensive tests** for each service
- Add 1-2 smoke tests max to verify basic functionality
- Framework tests already validate all patterns the service will use

## Future Test Additions

Potential areas for expansion:

1. **Template system tests**: More coverage for `Parameter`, `Output`, `Condition`, `Mapping` (currently at 60%)
2. **Code generator tests**: Test the generator logic itself rather than generated output
3. **Error handling tests**: Validate error messages and validation logic
4. **Edge case tests**: Unusual CloudFormation patterns or corner cases
5. **Performance tests**: Ensure template generation scales for large templates

## Questions?

For questions about the test suite:
- Check this README for test philosophy and organization
- Look at existing tests for patterns and examples
- See [DEVELOPERS.md](../DEVELOPERS.md) for build and development workflows
- See main [README.md](../README.md) for framework usage examples
