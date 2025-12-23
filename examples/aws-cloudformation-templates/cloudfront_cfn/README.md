# CloudfrontCfn

Imported from `EC2-Domain-Join.yaml`.

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Run Tests

```bash
uv run pytest tests/ -v
```

### Generate Template

```bash
uv run python -m cloudfront_cfn
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `myssmdocument` | AWS::SSM::Document |
| `myEC2InstanceSSM` | AWS::EC2::Instance |
| `myInstanceProfile` | AWS::IAM::InstanceProfile |
| `myEC2SSMRole` | AWS::IAM::Role |
| `InstanceSecurityGroup` | AWS::EC2::SecurityGroup |
