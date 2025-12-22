# S3 Bucket Example

**Original Source**: Based on S3 bucket patterns from [aws-cloudformation-templates](https://github.com/aws-cloudformation/aws-cloudformation-templates/tree/main/S3)

This example demonstrates creating an AWS S3 bucket with encryption and bucket policy using **declarative wrapper classes**.

## Key Concepts

### Declarative Wrapper Pattern

Shows how to use wrapper classes for clean, reusable infrastructure code:

```python
@cloudformation_dataclass
class MyData:
    resource: Bucket
    context = ctx
    tags = [{"Key": "DataClassification", "Value": "sensitive"}]
    bucket_encryption = MyBucketEncryption
    versioning_configuration = {"Status": "Enabled"}

@cloudformation_dataclass
class DenyUnencryptedUploadsStatement:
    resource: DenyStatement
    sid = "DenyUnencryptedObjectUploads"
    principal = "*"
    action = "s3:PutObject"
    resource_arn = Sub("${MyData.Arn}/*")

# Zero boilerplate instantiation!
bucket = MyData()
```

### What This Example Demonstrates

1. **Smart Resource Naming** - Context-driven resource naming with configurable patterns
2. **Deployment Context** - Environment defaults (prod, us-east-1), custom naming patterns, and 3 base tags applied to all resources
3. **Tag Merging** - Context's 3 base tags (Environment, Project, ManagedBy) + resource-specific tag (DataClassification) = 4 total tags in CloudFormation template
4. **Declarative Wrapper Classes** - Reusable configuration components for encryption, versioning, and IAM policies
5. **Cross-Resource References** - Using `ref()` to reference other resources (bucket policy → bucket)
6. **CloudFormation Intrinsic Functions** - Using `Sub()` for string substitution with resource ARN references
7. **Zero Boilerplate** - All config in class declarations, instantiation with `MyData()` requires no parameters

## Running the Example

### Basic Usage

```bash
cd /Users/alex/Documents/checkouts/cf-dataclasses
uv run python -m examples.s3_bucket.main
```

This will generate and display:
- Resource summary with context-driven naming
- Tag merging demonstration
- CloudFormation template in JSON format
- CloudFormation template in YAML format (if pyyaml installed)

### Expected Output

**Resources:**
```
Bucket:        DataPlatform-MyData-prod-001-blue-us-east-1
  Class name:  MyData
  Pattern:     {component}-{resource_name}-{stage}-{deployment_name}-{deployment_group}-{region}

Bucket Policy: DataPlatform-MyDataPolicy-prod-001-blue-us-east-1
Environment:   prod (us-east-1)

Bucket Tags: 4 total (3 from context + 1 resource-specific)
  • Environment: Production
  • Project: MyApplication
  • ManagedBy: cloudformation-dataclasses
  • DataClassification: sensitive
```

**CloudFormation Template:**
```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "S3 bucket with encryption-required policy",
  "Resources": {
    "MyData": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "BucketEncryption": {
          "ServerSideEncryptionConfiguration": [
            {
              "ServerSideEncryptionByDefault": {
                "SSEAlgorithm": "AES256"
              }
            }
          ]
        },
        "VersioningConfiguration": {
          "Status": "Enabled"
        },
        "Tags": [
          {
            "Key": "Environment",
            "Value": "Production"
          },
          {
            "Key": "Project",
            "Value": "MyApplication"
          },
          {
            "Key": "ManagedBy",
            "Value": "cloudformation-dataclasses"
          },
          {
            "Key": "DataClassification",
            "Value": "sensitive"
          }
        ]
      }
    },
    "MyDataPolicy": {
      "Type": "AWS::S3::BucketPolicy",
      "Properties": {
        "Bucket": {
          "Ref": "MyData"
        },
        "PolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Deny",
              "Sid": "DenyUnencryptedObjectUploads",
              "Principal": "*",
              "Action": "s3:PutObject",
              "Resource": {
                "Fn::Sub": "${MyData.Arn}/*"
              },
              "Condition": {
                "StringNotEquals": {
                  "s3:x-amz-server-side-encryption": "AES256"
                }
              }
            }
          ]
        }
      }
    }
  }
}
```

## Running Tests

```bash
# Run example tests (user-focused)
cd /Users/alex/Documents/checkouts/cf-dataclasses
uv run pytest examples/with_context/s3_bucket/tests/ -v

# Run framework validation tests (comprehensive)
uv run pytest tests/test_s3_resources.py -v
```

### Example Tests

The example tests demonstrate typical usage patterns and verify the example works correctly:
- ✅ Template generation and validation
- ✅ Bucket encryption and versioning configuration
- ✅ Tag merging (context + resource-specific tags)
- ✅ Cross-resource references (bucket policy → bucket)
- ✅ Context-driven naming

## Code Structure

```
examples/with_context/s3_bucket/
├── __init__.py        # Package imports
├── context.py         # Deployment context for production environment
├── bucket.py          # S3 bucket with encryption and versioning
├── bucket_policy.py   # Bucket policy requiring encrypted uploads
├── main.py            # Main entry point - creates and displays template
├── tests/
│   ├── __init__.py
│   └── test.py          # User-focused example tests
└── README.md          # This file
```

## Key Pattern Details

### 1. Deployment Context

Provides environment defaults and automatic resource naming:

```python
@cloudformation_dataclass
class ProdDeploymentContext:
    context: DeploymentContext
    component = "DataPlatform"          # Application/service component
    stage = "prod"                       # Environment stage (dev, staging, prod)
    deployment_name = "001"              # Deployment identifier
    deployment_group = "blue"            # For blue/green deployments
    region = "us-east-1"                 # AWS region
    # Default pattern: {component}-{resource_name}-{stage}-{deployment_name}-{deployment_group}-{region}
    tags = [
        {"Key": "Environment", "Value": "Production"},
        {"Key": "Project", "Value": "MyApplication"},
        {"Key": "ManagedBy", "Value": "cloudformation-dataclasses"},
    ]

ctx = ProdDeploymentContext()
```

**Context Parameters**:
- `component`: Application or service component name (e.g., "DataPlatform", "APIGateway")
- `stage`: Deployment stage/environment (e.g., "dev", "staging", "prod")
- `deployment_name`: Unique deployment identifier (e.g., "001", "v2")
- `deployment_group`: For blue/green deployments - enables zero-downtime deployments (e.g., "blue", "green")
- `region`: AWS region for deployment

**Resource Naming**:
- Class name: `MyData` becomes `resource_name` in pattern
- Pattern: `{component}-{resource_name}-{stage}-{deployment_name}-{deployment_group}-{region}`
- Result: `DataPlatform-MyData-prod-001-blue-us-east-1`

**Blue/Green Deployment Example**:
```python
# Blue deployment (current production)
ctx_blue = ProdDeploymentContext(deployment_group="blue")
# Resource names: DataPlatform-MyData-prod-001-blue-us-east-1

# Green deployment (new version)
ctx_green = ProdDeploymentContext(deployment_group="green")
# Resource names: DataPlatform-MyData-prod-001-green-us-east-1

# Deploy green alongside blue, test, then switch traffic
# Both stacks can coexist for zero-downtime deployments
```

**Custom Pattern per Context**:
```python
@cloudformation_dataclass
class SimpleContext:
    context: DeploymentContext
    component = "MyApp"
    naming_pattern = "{component}-{resource_name}"  # Custom pattern

# Result: MyApp-MyData
```

**Override Pattern per Resource**:
```python
@cloudformation_dataclass
class MyData:
    resource: Bucket
    context = ctx
    naming_pattern = "{resource_name}-{stage}"  # Override context pattern

# Result: MyData-prod
```

### 2. Nested Configuration

Encryption config uses nested wrapper classes:

```python
@cloudformation_dataclass
class MyServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = "AES256"

@cloudformation_dataclass
class MyServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = MyServerSideEncryptionByDefault

@cloudformation_dataclass
class MyBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [MyServerSideEncryptionRule]
```

**Alternative**: Simple properties can use inline dicts:
```python
versioning_configuration = {"Status": "Enabled"}
```

### 3. IAM Policy Documents

Type-safe policy statements using base classes:

```python
@cloudformation_dataclass
class DenyUnencryptedUploadsStatement:
    resource: DenyStatement  # Pre-configured with effect="Deny"
    sid = "DenyUnencryptedObjectUploads"
    principal = "*"
    action = "s3:PutObject"
    resource_arn = Sub("${MyData.Arn}/*")  # Use Sub() with GetAtt shorthand
    condition = {"StringNotEquals": {"s3:x-amz-server-side-encryption": "AES256"}}

@cloudformation_dataclass
class EncryptionRequiredPolicyDocument:
    resource: PolicyDocument
    statement = [DenyUnencryptedUploadsStatement]
```

**Notes**:
- Uses `resource_arn` instead of `resource` to avoid naming conflict with wrapper pattern's `resource:` field
- `Sub("${MyData.Arn}/*")` uses CloudFormation's Sub shorthand for GetAtt: `${LogicalId.Attribute}`

### 4. Cross-Resource References

Use `ref()` to create CloudFormation `{"Ref": "..."}` intrinsic functions. There are three patterns:

```python
# Pattern 1: String reference (simple, no IDE support)
bucket = ref("MyData")  # Creates {"Ref": "MyData"}

# Pattern 2: Direct class reference (when class is imported)
from .bucket import MyData
bucket = ref(MyData)  # Creates {"Ref": "MyData"}

# Pattern 3: Annotation-based (cross-module with IDE support)
from __future__ import annotations
bucket: Ref[MyData] = ref()  # Creates {"Ref": "MyData"}
```

**Which pattern to use?**
- **String refs** - Simple cases, no IDE navigation needed
- **Direct refs** - Same-file or already-imported classes
- **Class-based refs** - Cross-module with full IDE support (autocomplete, go-to-definition)

For cross-module references, import the target class and use `ref(ClassName)` or `get_att(ClassName, "Attr")`.

### 5. Tag Merging

Context tags and resource-specific tags are merged automatically:

```python
# Context provides 3 tags
ctx = ProdDeploymentContext()  # Environment, Project, ManagedBy

# Resource adds 1 tag
@cloudformation_dataclass
class MyData:
    resource: Bucket
    context = ctx
    tags = [{"Key": "DataClassification", "Value": "sensitive"}]

# Result: 4 tags total (3 from context + 1 resource-specific)
bucket = MyData()
print(len(bucket.resource.all_tags))  # 4
```

## Important Notes

### Auto-Naming vs Explicit Naming

**With context** (recommended for production):
```python
@cloudformation_dataclass
class MyData:
    resource: Bucket
    context = ctx  # Auto-names as "DataPlatform-MyData-prod-001-A-us-east-1"
```

**Without context** (simple use cases):
```python
@cloudformation_dataclass
class MyData:
    resource: Bucket
    # Resource name will be "MyData" (class name)
```

**Explicit override** (rarely needed):
```python
@cloudformation_dataclass
class MyData:
    resource: Bucket
    bucket_name = "my-explicit-bucket-name"  # Overrides auto-naming
```

### Inline Dicts vs Wrapper Classes

**Use inline dicts for**:
- Simple key-value configs
- Tags: `[{"Key": "Name", "Value": "value"}]`
- Simple properties: `{"Status": "Enabled"}`

**Use wrapper classes for**:
- Complex nested structures (3+ levels deep)
- Reusable configuration patterns
- When you want type safety and IDE autocomplete

## Next Steps

- Explore deployment contexts for multi-environment setups
- Add lifecycle policies, CORS configuration, replication
- Combine multiple resources into complete infrastructure stacks
- Generate other AWS services (EC2, Lambda, RDS, DynamoDB)

## Documentation

For more information, see:
- [Main Project README](../../README.md)
- [CLAUDE.md](../../CLAUDE.md) - Development guide
