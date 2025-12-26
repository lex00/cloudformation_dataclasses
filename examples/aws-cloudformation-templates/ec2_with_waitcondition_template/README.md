# Ec2WithWaitconditionTemplate

Migrated from [ec2_with_waitcondition_template.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m ec2_with_waitcondition_template
```

### Validate Template

```bash
python -m ec2_with_waitcondition_template --validate
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
