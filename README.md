# CloudFormation Dataclasses

**Readable infrastructure code for AWS.**

Infrastructure code should be readable at every stage—by the ops people who write it, the dev people who rely on it, and the AI agents that now help maintain it.

[Read the philosophy →](https://github.com/lex00/cloudformation_dataclasses/blob/main/docs/PHILOSOPHY.md)

## Quick Start

```bash
pip install cloudformation-dataclasses
cfn-dataclasses init -o my_stack/
```

[Full Quick Start →](https://github.com/lex00/cloudformation_dataclasses/blob/main/docs/QUICK_START.md)

## What This Is

Type-safe Python dataclasses that generate CloudFormation JSON:

```python
@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    bucket_name = "data"
    bucket_encryption = MyEncryption  # Reference another class
```

No Node.js. No state files. Minimal dependencies (just PyYAML).

## Documentation

| Guide | Description |
|-------|-------------|
| [Quick Start](https://github.com/lex00/cloudformation_dataclasses/blob/main/docs/QUICK_START.md) | Create your first project |
| [API Reference](https://lex00.github.io/cloudformation_dataclasses/) | Generated from docstrings |
| [CLI Reference](https://github.com/lex00/cloudformation_dataclasses/blob/main/docs/CLI.md) | init, import, lint commands |
| [Examples](https://github.com/lex00/cloudformation_dataclasses/tree/main/examples) | Real-world templates |
| [Comparison](https://github.com/lex00/cloudformation_dataclasses/blob/main/docs/COMPARISON.md) | vs CDK, Terraform |

### More

| Guide | Description |
|-------|-------------|
| [Developer Guide](https://github.com/lex00/cloudformation_dataclasses/blob/main/docs/DEVELOPERS.md) | Building, testing, contributing |
| [Internals](https://github.com/lex00/cloudformation_dataclasses/blob/main/docs/INTERNALS.md) | Registry, code generation, importer |
| [Changelog](https://github.com/lex00/cloudformation_dataclasses/blob/main/CHANGELOG.md) | Version history |

## License

MIT License - see [LICENSE](https://github.com/lex00/cloudformation_dataclasses/blob/main/LICENSE)
