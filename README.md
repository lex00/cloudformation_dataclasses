# CloudFormation Dataclasses

**Readable infrastructure code for AWS.**

Infrastructure code should be readable at every stage—by the ops people who write it, the dev people who rely on it, and the AI agents that now help maintain it.

[Read the philosophy →](docs/PHILOSOPHY.md)

## Quick Start

```bash
pip install cloudformation-dataclasses
cfn-dataclasses init -o my_stack/
```

[Full Quick Start →](docs/QUICK_START.md)

## What This Is

Type-safe Python dataclasses that generate CloudFormation JSON:

```python
@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    bucket_name = "data"
    bucket_encryption = MyEncryption  # Reference another class
```

No Node.js. No state files. No runtime dependencies.

## Documentation

| Guide | Description |
|-------|-------------|
| [Quick Start](docs/QUICK_START.md) | Create your first project |
| [CLI Reference](docs/CLI.md) | init, import, lint commands |
| [Examples](examples/) | Real-world templates |
| [Comparison](docs/COMPARISON.md) | vs CDK, Terraform |

### More

| Guide | Description |
|-------|-------------|
| [Developer Guide](docs/DEVELOPERS.md) | Building, testing, contributing |
| [Internals](docs/INTERNALS.md) | Registry, code generation, importer |
| [Changelog](CHANGELOG.md) | Version history |

## License

MIT License - see [LICENSE](LICENSE)
