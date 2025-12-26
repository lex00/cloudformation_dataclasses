# Sqsstandardqueue

Migrated from [SQSStandardQueue.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m sqsstandardqueue
```

### Validate Template

```bash
python -m sqsstandardqueue --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `SQSQueue` | AWS::SQS::Queue |
| `MyDeadLetterQueue` | AWS::SQS::Queue |
