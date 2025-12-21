# CloudFormation Dataclasses

**Type-safe Python dataclasses for AWS CloudFormation templates**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Write CloudFormation templates as Python dataclasses. Get full IDE autocomplete, type checking, and zero runtime dependencies.

## Quick Example

```python
from cloudformation_dataclasses.core import *
from cloudformation_dataclasses.aws.s3 import *
from cloudformation_dataclasses.intrinsics import Sub

# S3 bucket with AES-256 encryption
@cloudformation_dataclass
class MyEncryption:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256

@cloudformation_dataclass
class MyEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = MyEncryption

@cloudformation_dataclass
class MyBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [MyEncryptionRule]

@cloudformation_dataclass
class MyData:
    resource: Bucket
    bucket_encryption = MyBucketEncryption

# Policy that denies unencrypted uploads
@cloudformation_dataclass
class DenyUnencryptedStatement:
    resource: DenyStatement
    principal = "*"
    action = "s3:PutObject"
    resource_arn = Sub("${MyData.Arn}/*")
    condition = {STRING_NOT_EQUALS: {"s3:x-amz-server-side-encryption": "AES256"}}

@cloudformation_dataclass
class MyDataPolicyDocument:
    resource: PolicyDocument
    statement = [DenyUnencryptedStatement]

@cloudformation_dataclass
class MyDataPolicy:
    resource: BucketPolicy
    bucket: Ref[MyData] = ref()
    policy_document = MyDataPolicyDocument
```

See [examples/with_context/s3_bucket/](examples/with_context/s3_bucket/) for a complete example with deployment context and naming.

## Installation

```bash
pip install cloudformation-dataclasses
```

## Documentation

| Guide | Description |
|-------|-------------|
| **[Quick Start](docs/QUICK_START.md)** | Create new projects with `cfn-dataclasses-init` |
| **[Template Importer](docs/IMPORTER.md)** | Convert existing YAML/JSON templates to Python |
| **[Linter](docs/LINTER.md)** | Detect and auto-fix common mistakes |
| **[Forward References](docs/FORWARD_REFERENCES.md)** | Cross-module resource references with `Ref[T]` |
| **[Resource Registry](docs/REGISTRY.md)** | Auto-registration and multi-file organization |
| **[Agent Guide](docs/AGENT_GUIDE.md)** | Workflows for AI assistants |
| **[Code Generator](docs/GENERATOR.md)** | Regenerate AWS resources from CloudFormation specs |
| **[Developer Guide](docs/DEVELOPERS.md)** | Building, testing, and contributing |
| **[Changelog](CHANGELOG.md)** | Version history |

## Features

- **Type-Safe** - Full Python type hints, IDE autocomplete, mypy/pyright support
- **Zero Dependencies** - Core package requires nothing (pyyaml optional for YAML output)
- **All AWS Services** - 262 services, 1,502 resource types auto-generated from CloudFormation specs
- **Pure Python** - No Node.js required (unlike AWS CDK)
- **Import Existing Templates** - Convert YAML/JSON to Python with `cfn-dataclasses-import`
- **Linter** - Auto-fix string literals to type-safe constants

## Tools

```bash
# Create a new project
cfn-dataclasses-init default -o my_stack/

# Import existing template
cfn-dataclasses-import template.yaml -o my_stack.py
```

## License

MIT License - see [LICENSE](LICENSE)
