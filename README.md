# CloudFormation Dataclasses

**Type-safe Python dataclasses for AWS CloudFormation templates**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Write CloudFormation templates as Python dataclasses. Get full IDE autocomplete, type checking, and zero runtime dependencies.

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
| **[Resource Registry](docs/REGISTRY.md)** | Auto-registration and multi-file organization |
| **[Agent Guide](docs/AGENT_GUIDE.md)** | Workflows for AI assistants |
| **[Code Generator](docs/GENERATOR.md)** | Regenerate AWS resources from CloudFormation specs |
| **[Developer Guide](docs/DEVELOPERS.md)** | Building, testing, and contributing |
| **[Changelog](CHANGELOG.md)** | Version history |

## Key Features

### 1. Declarative Syntax

Infrastructure as **data**, not code. No constructors, no method calls, no execution order:

```python
# cloudformation_dataclasses: Infrastructure as DATA
@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    bucket_name = "data"
    bucket_encryption = MyEncryption  # Just reference another class

# CDK: Imperative with construct tree
bucket = Bucket(self, "MyBucket", bucket_name="data")
bucket.add_encryption(...)  # Execute methods to mutate

# Troposphere: Imperative with manual registration
bucket = Bucket("MyBucket", BucketName="data")
template.add_resource(bucket)  # Don't forget this!
```

### 2. Type-Safe Cross-Resource References

Use **class references** instead of error-prone strings. Your IDE catches typos immediately:

```python
role = get_att(MyRol, "Arn")  # ❌ IDE error: "MyRol" undefined
role = get_att(MyRole, "Arn")  # ✅ IDE validates, autocompletes, refactors
```

### 3. Flexible File Organization

One import pattern. Reference resources from **any file** without explicit imports:

```python
# Every file in your stack uses the same import
from .. import *

# Reference resources from ANY file - no explicit imports needed
bucket = ref(DataBucket)  # DataBucket could be in storage.py, main.py, anywhere
```

Move resources between files → **zero import changes**.

### 4. Pure Python

No Node.js required (unlike CDK). No transitive dependencies.

---

See **[Feature Comparison](docs/comparisons/FEATURES.md)** for the full matrix, or compare with **[CDK](docs/comparisons/CDK.md)** and **[Troposphere](docs/comparisons/TROPOSPHERE.md)** directly.

## Also

- **All AWS Services** - 262 services, 1,502 resource types auto-generated from CloudFormation specs
- **Import Existing Templates** - Convert YAML/JSON to Python with `cfn-dataclasses import`
- **Clean Output** - Readable logical IDs, no CDK metadata or hashes
- **Linter** - Auto-fix string literals to type-safe constants

## Tools

```bash
# Create a new project
cfn-dataclasses init -o my_stack/

# Import existing template
cfn-dataclasses import template.yaml -o my_stack.py

# Lint your code
cfn-dataclasses lint my_stack/
```

## License

MIT License - see [LICENSE](LICENSE)
