# AI Prompting Guide for cloudformation_dataclasses

AI coding assistants often generate code using raw strings instead of this library's type-safe constants and patterns. This guide provides prompts to prevent that.

## Quick Start

Copy this prompt at the **start of your AI session**:

```
I'm using the cloudformation_dataclasses library. Follow these rules:

1. WRAPPER PATTERN - Never instantiate resources directly:
   @cloudformation_dataclass
   class MyBucket:
       resource: Bucket
       bucket_name = "my-bucket"

2. SERVICE ENUMS - Import from aws.<service>, not strings:
   from cloudformation_dataclasses.aws.s3 import BucketVersioningStatus
   status = BucketVersioningStatus.ENABLED  # NOT "Enabled"

3. PSEUDO-PARAMETERS - Never hardcode region/account:
   from cloudformation_dataclasses.intrinsics import AWS_REGION, AWS_ACCOUNT_ID

4. INTRINSICS for dynamic values:
   from cloudformation_dataclasses.intrinsics import Sub, Ref, GetAtt, Join

5. CONDITION OPERATORS for IAM policies:
   from cloudformation_dataclasses.core import STRING_EQUALS, IP_ADDRESS, ARN_LIKE

6. REFERENCES between resources:
   from cloudformation_dataclasses.core import ref, get_att
   vpc_id = ref(MyVPC)
```

---

## Generic Task Prompt Template

Use this template for any AWS resource:

```
Create [RESOURCE TYPE] using cloudformation_dataclasses.

Required patterns:
- Use @cloudformation_dataclass decorator with `resource: [Type]` field
- Import resource classes and enums from cloudformation_dataclasses.aws.[service]
- Use enum constants, NOT strings (e.g., Status.ENABLED not "Enabled")
- Use ref() for references between resources
- Use Sub/AWS_REGION/AWS_ACCOUNT_ID for dynamic values
- Use STRING_EQUALS/IP_ADDRESS/etc for policy conditions, not string keys

Core imports: cloudformation_dataclass, ref, get_att, STRING, NUMBER, STRING_EQUALS, PolicyStatement, DenyStatement
Intrinsics: Sub, Ref, GetAtt, Join, If, AWS_REGION, AWS_ACCOUNT_ID, AWS_PARTITION
```

### Example filled in:

```
Create an S3 bucket with versioning and encryption using cloudformation_dataclasses.

Required patterns:
- Use @cloudformation_dataclass decorator with `resource: Bucket` field
- Import from cloudformation_dataclasses.aws.s3: Bucket, BucketEncryption, VersioningConfiguration, BucketVersioningStatus
- Use BucketVersioningStatus.ENABLED not "Enabled"
- Use ref() for references between resources

Core imports: cloudformation_dataclass, ref
```

---

## Post-Generation Validation

After the AI generates code, paste this to catch mistakes:

```
Review the code for these common errors:

1. String literals that should be enums:
   - "Enabled" -> BucketVersioningStatus.ENABLED
   - "AES256" -> ServerSideEncryption.AES256
   - "String" -> STRING
   - "StringEquals" -> STRING_EQUALS
   - "Bool" -> BOOL

2. Hardcoded AWS values:
   - "us-east-1" -> AWS_REGION (when dynamic)
   - Account IDs -> AWS_ACCOUNT_ID

3. Direct instantiation:
   - Bucket(...) -> @cloudformation_dataclass wrapper

4. Missing imports from service modules

5. Policy conditions using string keys instead of constants:
   - {"Bool": {...}} -> {BOOL: {...}}
   - {"StringEquals": {...}} -> {STRING_EQUALS: {...}}
```

---

## Providing File Context

If your AI tool supports adding files as context, use these **small** files:

| Purpose | File |
|---------|------|
| Import patterns | `examples/s3_bucket/__init__.py` |
| Complete example | `examples/s3_bucket/bucket_policy.py` |
| Pseudo-parameters | `cloudformation_dataclasses/intrinsics/pseudo.py` |
| Condition operators | `cloudformation_dataclasses/core/constants.py` |

**Do NOT** provide full `aws/<service>.py` files - they're very large. Instead, tell the AI which specific enums exist.

---

## Import Quick Reference

| Need | Import From | Examples |
|------|-------------|----------|
| Decorator & helpers | `core` | `cloudformation_dataclass`, `ref`, `get_att` |
| Parameter types | `core` | `STRING`, `NUMBER`, `ParameterType.AWS_EC2_VPC_ID` |
| Condition operators | `core` | `STRING_EQUALS`, `IP_ADDRESS`, `ARN_LIKE`, `BOOL` |
| Policy classes | `core` | `PolicyStatement`, `DenyStatement`, `PolicyDocument` |
| Intrinsic functions | `intrinsics` | `Sub`, `Ref`, `GetAtt`, `Join`, `If`, `Select` |
| Pseudo-parameters | `intrinsics` | `AWS_REGION`, `AWS_ACCOUNT_ID`, `AWS_PARTITION` |
| Service resources | `aws.<service>` | `Bucket`, `Instance`, `Function` |
| Service enums | `aws.<service>` | `BucketVersioningStatus`, `InstanceType` |

---

## Common Service Enums

When the AI doesn't know what enums exist, include these hints:

### S3
```
from cloudformation_dataclasses.aws.s3 import:
- BucketVersioningStatus.ENABLED / .SUSPENDED
- ServerSideEncryption.AES256 / .AWS_KMS  (for sse_algorithm)
- BucketCannedACL.PRIVATE / .PUBLIC_READ
- ServerSideEncryptionByDefault, ServerSideEncryptionRule, BucketEncryption
```

### IAM
```
from cloudformation_dataclasses.core import:
- STRING_EQUALS, STRING_NOT_EQUALS, STRING_LIKE
- IP_ADDRESS, ARN_LIKE, ARN_EQUALS
- BOOL (for boolean conditions)
- FOR_ALL_VALUES_STRING_EQUALS, FOR_ANY_VALUE_STRING_LIKE
```

### EC2
```
from cloudformation_dataclasses.aws.ec2 import:
- InstanceType (e.g., InstanceType.T3_MICRO)
- Tenancy.DEFAULT / .DEDICATED / .HOST
```

### Lambda
```
from cloudformation_dataclasses.aws.lambda_ import:
- Runtime.PYTHON3_12 / .NODEJS20_X / etc.
- Architecture.X86_64 / .ARM64
```

---

## Importing Third-Party Templates

When importing CloudFormation templates from external sources (AWS examples, GitHub repos, etc.), use the [Import Workflow](IMPORT_WORKFLOW.md) for a structured approach that:

1. Uses the linter to detect and fix type-safe constant opportunities
2. Discovers missing enums/constants and improves the tools
3. Creates proper test coverage and documentation

---

## See Also

- [LINTER.md](LINTER.md) - Linter rules and auto-fix capabilities
- [IMPORTER.md](IMPORTER.md) - cfn-import command usage
- [IMPORT_WORKFLOW.md](IMPORT_WORKFLOW.md) - Full workflow for third-party templates
