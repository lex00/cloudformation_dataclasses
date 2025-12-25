# Example1

Migrated from [example_1.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m example_1
```

### Validate Template

```bash
python -m example_1 --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `Repo` | AWS::CodeCommit::Repository |
| `AddReadme` | Boto3::CodeCommit.put_file |
