# Ec2WithWaitconditionTemplate

Migrated from [ec2_with_waitcondition_template.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

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
uv run python -m ec2_with_waitcondition_template
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `KWOSInstance` | AWS::EC2::Instance |
| `KWOSWaitHandle` | AWS::CloudFormation::WaitConditionHandle |
| `KWOSWaitCondition` | AWS::CloudFormation::WaitCondition |
| `KWOSSecurityGroup` | AWS::EC2::SecurityGroup |
