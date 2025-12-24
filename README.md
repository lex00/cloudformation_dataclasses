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

## Why cloudformation_dataclasses?

| Feature | cloudformation_dataclasses | AWS CDK | Troposphere |
|---------|:--------------------------:|:-------:|:-----------:|
| **Declarative syntax** | ✅ | ❌ | ❌ |
| **Pure Python (no Node.js)** | ✅ | ❌ | ✅ |
| **No transitive dependencies** | ✅ | ❌ | ❌ |
| **Type-safe cross-resource refs** | ✅ | ✅ | ❌ |
| **Move resources without import changes** | ✅ | ❌ | ❌ |
| **Clean output (no metadata/hashes)** | ✅ | ❌ | ✅ |
| **Import existing templates** | ✅ | ⚠️ | ❌ |

**Declarative means simpler code:**

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

**Type-safe references catch errors in your IDE:**

```python
role = get_att(MyRol, "Arn")  # ❌ IDE error: "MyRol" undefined

# vs Troposphere strings - typo caught at deploy time
Role=GetAtt("MyRol", "Arn")  # ⚠️ No error until AWS rejects it
```

**Simplified imports - move resources between files freely:**

```python
# Every file in your stack uses the same import
from .. import *

# Reference resources from ANY file - no explicit imports needed
bucket = ref(DataBucket)  # DataBucket could be in storage.py, main.py, anywhere
```

See **[Feature Comparison](docs/comparisons/FEATURES.md)** for the full matrix, or compare with **[CDK](docs/comparisons/CDK.md)** and **[Troposphere](docs/comparisons/TROPOSPHERE.md)** directly.

## Features

- **Declarative** - Infrastructure as data, not code. No constructors, no method calls
- **Type-Safe** - Full Python type hints, IDE autocomplete, mypy/pyright support
- **No Dependencies** - No transitive packages (pyyaml optional for YAML output)
- **All AWS Services** - 262 services, 1,502 resource types auto-generated from CloudFormation specs
- **Pure Python** - No Node.js required (unlike AWS CDK)
- **Import Existing Templates** - Convert YAML/JSON to Python with `cfn-dataclasses-import`
- **Flexible Organization** - Move resources between files without updating imports
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
